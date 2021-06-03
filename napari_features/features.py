import functools
import inspect
import math

import numpy
import scipy.ndimage
import scipy.spatial.distance
import skimage.morphology
import skimage.measure

PROPS = {
    'Area': 'area',
    'BoundingBox': 'bbox',
    'BoundingBoxArea': 'bbox_area',
    'CentralMoments': 'moments_central',
    'Centroid': 'centroid',
    'ConvexArea': 'convex_area',
    # 'ConvexHull',
    'ConvexImage': 'convex_image',
    'Coordinates': 'coords',
    'Eccentricity': 'eccentricity',
    'EquivDiameter': 'equivalent_diameter',
    'EulerNumber': 'euler_number',
    'Extent': 'extent',
    # 'Extrema',
    'FeretDiameterMax': 'feret_diameter_max',
    'FilledArea': 'filled_area',
    'FilledImage': 'filled_image',
    'HuMoments': 'moments_hu',
    'Image': 'image',
    'InertiaTensor': 'inertia_tensor',
    'InertiaTensorEigvals': 'inertia_tensor_eigvals',
    'IntensityImage': 'intensity_image',
    'Label': 'label',
    'LocalCentroid': 'local_centroid',
    'MajorAxisLength': 'major_axis_length',
    'MaxIntensity': 'max_intensity',
    'MeanIntensity': 'mean_intensity',
    'MinIntensity': 'min_intensity',
    'MinorAxisLength': 'minor_axis_length',
    'Moments': 'moments',
    'NormalizedMoments': 'moments_normalized',
    'Orientation': 'orientation',
    'Perimeter': 'perimeter',
    'CroftonPerimeter': 'perimeter_crofton',
    # 'PixelIdxList',
    # 'PixelList',
    'Slice': 'slice',
    'Solidity': 'solidity',
    # 'SubarrayIdx'
    'WeightedCentralMoments': 'weighted_moments_central',
    'WeightedCentroid': 'weighted_centroid',
    'WeightedHuMoments': 'weighted_moments_hu',
    'WeightedLocalCentroid': 'weighted_local_centroid',
    'WeightedMoments': 'weighted_moments',
    'WeightedNormalizedMoments': 'weighted_moments_normalized'
}

OBJECT_COLUMNS = {
    'image', 'coords', 'convex_image', 'slice',
    'filled_image', 'intensity_image'
}

COL_DTYPES = {
    'area': int,
    'bbox': int,
    'bbox_area': int,
    'moments_central': float,
    'centroid': float,
    'convex_area': int,
    'convex_image': object,
    'coords': object,
    'eccentricity': float,
    'equivalent_diameter': float,
    'euler_number': int,
    'extent': float,
    'feret_diameter_max': float,
    'filled_area': int,
    'filled_image': object,
    'moments_hu': float,
    'image': object,
    'inertia_tensor': float,
    'inertia_tensor_eigvals': float,
    'intensity_image': object,
    'label': int,
    'local_centroid': float,
    'major_axis_length': float,
    'max_intensity': float,
    'mean_intensity': float,
    'min_intensity': float,
    'minor_axis_length': float,
    'moments': float,
    'moments_normalized': float,
    'orientation': float,
    'perimeter': float,
    'perimeter_crofton': float,
    'slice': object,
    'solidity': float,
    'weighted_moments_central': float,
    'weighted_centroid': float,
    'weighted_moments_hu': float,
    'weighted_local_centroid': float,
    'weighted_moments': float,
    'weighted_moments_normalized': float
}

PROP_VALS = set(PROPS.values())


def _infer_number_of_required_args(func):
    """Infer the number of required arguments for a function

    Parameters
    ----------
    func : callable
        The function that is being inspected.

    Returns
    -------
    n_args : int
        The number of required arguments of func.
    """
    argspec = inspect.getfullargspec(func)
    n_args = len(argspec.args)
    if argspec.defaults is not None:
        n_args -= len(argspec.defaults)
    return n_args


def _infer_regionprop_dtype(func, *, intensity, ndim):
    """Infer the dtype of a region property calculated by func.

    If a region property function always returns the same shape and type of
    output regardless of input size, then the dtype is the dtype of the
    returned array. Otherwise, the property has object dtype.

    Parameters
    ----------
    func : callable
        Function to be tested. The signature should be array[bool] -> Any if
        intensity is False, or *(array[bool], array[float]) -> Any otherwise.
    intensity : bool
        Whether the regionprop is calculated on an intensity image.
    ndim : int
        The number of dimensions for which to check func.

    Returns
    -------
    dtype : NumPy data type
        The data type of the returned property.
    """
    labels = [1, 2]
    sample = numpy.zeros((3,) * ndim, dtype=numpy.intp)
    sample[(0,) * ndim] = labels[0]
    sample[(slice(1, None),) * ndim] = labels[1]
    propmasks = [(sample == n) for n in labels]
    if intensity and _infer_number_of_required_args(func) == 2:
        def _func(mask):
            return func(mask, numpy.random.random(sample.shape))
    else:
        _func = func
    props1, props2 = map(_func, propmasks)
    if (numpy.isscalar(props1) and numpy.isscalar(props2)
            or numpy.array(props1).shape == numpy.array(props2).shape):
        dtype = numpy.array(props1).dtype.type
    else:
        dtype = numpy.object_
    return dtype


def _cached(f):
    @functools.wraps(f)
    def wrapper(obj):
        cache = obj.cache
        prop = f.__name__

        if not ((prop in cache) and obj._cache_active):
            cache[prop] = f(obj)

        return cache[prop]

    return wrapper


def only2d(method):
    @functools.wraps(method)
    def func2d(self, *args, **kwargs):
        if self._ndim > 2:
            raise NotImplementedError('Property %s is not implemented for '
                                      '3D images' % method.__name__)
        return method(self, *args, **kwargs)
    return func2d


class Features:
    def __init__(self, slice, object_index, objects, image: numpy.array, cache_active):
        if image is not None:
            ndim = objects.ndim

            if not (image.shape[:ndim] == objects.shape and image.ndim in [ndim, ndim + 1]):
                raise ValueError("Label and intensity image shapes must match, except for channel (last) axis.")

            self._multichannel = objects.shape < image.shape
        else:
            self._multichannel = False

        self.object_index = object_index

        self._slice = slice
        self.slice = slice
        self._objects = objects
        self._image = image

        self._cache_active = cache_active
        self._cache = {}
        self._ndim = objects.ndim
        self._spatial_axes = tuple(range(self._ndim))

        self._extra_properties = {}

    @property
    @_cached
    def shape_image_area(self):
        return numpy.sum(self.image)

    @property
    @_cached
    def shape_object_bounding_box(self):
        return tuple([self.slice[i].start for i in range(self._ndim)] + [self.slice[i].stop for i in range(self._ndim)])

    @property
    def shape_object_bounding_box_maximum_x(self):
        return self.shape_object_bounding_box[0]

    @property
    def shape_object_bounding_box_maximum_y(self):
        return self.shape_object_bounding_box[1]

    @property
    def shape_object_bounding_box_maximum_z(self):
        if self._ndim > 2:
            return None

        return self.shape_object_bounding_box[2]

    @property
    def shape_object_bounding_box_area(self):
        return self.image.size

    @property
    def centroid(self):
        return tuple(self.coords.mean(axis=0))

    @property
    @_cached
    def convex_area(self):
        return numpy.sum(self.convex_image)

    @property
    @_cached
    def convex_image(self) -> numpy.array:
        return skimage.morphology.convex_hull_image(self.image)

    @property
    def coords(self):
        indices = numpy.nonzero(self.image)
        return numpy.vstack([indices[i] + self.slice[i].start
                             for i in range(self._ndim)]).T

    @property
    @only2d
    def shape_object_eccentricity(self):
        l1, l2 = self.shape_object_inertia_tensor_eigenvalues

        if l1 == 0:
            return 0

        return math.sqrt(1 - l2 / l1)

    @property
    def shape_object_equivalent_diameter(self):
        return (2 * self._ndim * self.shape_image_area / math.pi) ** (1 / self._ndim)

    @property
    def shape_object_euler_number(self):
        return skimage.measure.euler_number(self.image, self._ndim)

    @property
    def shape_object_extent(self):
        return self.shape_image_area / self.image.size

    @property
    def feret_diameter_max(self):
        identity_convex_hull = numpy.pad(self.convex_image,
                                         2, mode='constant', constant_values=0)
        if self._ndim == 2:
            coordinates = numpy.vstack(skimage.measure.find_contours(identity_convex_hull, .5,
                                                                     fully_connected='high'))
        elif self._ndim == 3:
            coordinates, _, _, _ = skimage.measure.marching_cubes(identity_convex_hull, level=.5)
        distances = scipy.spatial.distance.pdist(coordinates, 'sqeuclidean')
        return math.sqrt(numpy.max(distances))

    @property
    def filled_area(self):
        return numpy.sum(self.filled_image)

    @property
    @_cached
    def filled_image(self):
        structure = numpy.ones((3,) * self._ndim)
        return scipy.ndimage.binary_fill_holes(self.image, structure)

    @property
    @_cached
    def image(self):
        return self._objects[self.slice] == self.object_index

    @property
    @_cached
    def shape_object_inertia_tensor(self):
        return skimage.measure.inertia_tensor(self.image, self.shape_object_central_moments)

    @property
    @_cached
    def shape_object_inertia_tensor_eigenvalues(self):
        return skimage.measure.inertia_tensor_eigvals(self.image, T=self.shape_object_inertia_tensor)

    @property
    @_cached
    def intensity_image(self):
        image = (
            self.image
            if not self._multichannel
            else numpy.expand_dims(self.image, self._ndim)
        )

        return self._image[self.slice] * image

    def _intensity_image_double(self):
        return self.intensity_image.astype(numpy.double)

    @property
    def local_centroid(self):
        moments = self.shape_object_spatial_moments

        return tuple(moments[tuple(numpy.eye(self._ndim, dtype=int))] / moments[(0,) * self._ndim])

    @property
    def color_object_maximum_intensity(self):
        return numpy.max(self.intensity_image[self.image], axis=0).astype(numpy.double)

    @property
    def color_object_mean_intensity(self):
        return numpy.mean(self.intensity_image[self.image], axis=0)

    @property
    def color_object_minimum_intensity(self):
        return numpy.min(self.intensity_image[self.image], axis=0).astype(numpy.double)

    @property
    def shape_object_major_axis_length(self):
        return 4 * math.sqrt(self.shape_object_inertia_tensor_eigenvalues[0])

    @property
    def shape_object_minor_axis_length(self):
        return 4 * math.sqrt(self.shape_object_inertia_tensor_eigenvalues[-1])

    @property
    @_cached
    def shape_object_spatial_moments(self):
        return skimage.measure.moments(self.image.astype(numpy.uint8), 3)

    @property
    @_cached
    def shape_object_central_moments(self):
        return skimage.measure.moments_central(self.image.astype(numpy.uint8), self.local_centroid, order=3)

    @property
    @only2d
    def moments_hu(self):
        return skimage.measure.moments_hu(self.moments_normalized)

    @property
    @_cached
    def moments_normalized(self):
        return skimage.measure.moments_normalized(self.shape_object_central_moments, 3)

    @property
    @only2d
    def shape_object_orientation(self):
        a, b, b, c = self.shape_object_inertia_tensor.flat

        if a - c == 0:
            if b < 0:
                return -math.pi / 4.
            else:
                return math.pi / 4.
        else:
            return 0.5 * math.atan2(-2 * b, c - a)

    @property
    @only2d
    def shape_object_perimeter(self):
        return skimage.measure.perimeter(self.image, 4)

    @property
    @only2d
    def perimeter_crofton(self):
        return skimage.measure.perimeter_crofton(self.image, 4)

    @property
    def shape_object_solidity(self):
        return self.shape_image_area / self.convex_area

    @property
    def weighted_centroid(self):
        ctr = self.weighted_local_centroid
        return tuple(idx + slc.start
                     for idx, slc in zip(ctr, self.slice))

    @property
    def weighted_local_centroid(self):
        M = self.weighted_moments
        return (M[tuple(numpy.eye(self._ndim, dtype=int))] /
                M[(0,) * self._ndim])

    @property
    @_cached
    def weighted_moments(self):
        image = self._intensity_image_double()
        if self._multichannel:
            moments = numpy.stack(
                    [skimage.measure.moments(image[..., i], order=3)
                     for i in range(image.shape[-1])],
                    axis=-1,
                    )
        else:
            moments = skimage.measure.moments(image, order=3)
        return moments

    @property
    @_cached
    def weighted_moments_central(self):
        ctr = self.weighted_local_centroid
        image = self._intensity_image_double()
        if self._multichannel:
            moments_list = [
                skimage.measure.moments_central(
                    image[..., i], center=ctr[..., i], order=3
                )
                for i in range(image.shape[-1])
            ]
            moments = numpy.stack(moments_list, axis=-1)
        else:
            moments = skimage.measure.moments_central(image, ctr, order=3)
        return moments

    @property
    @only2d
    def weighted_moments_hu(self):
        nu = self.weighted_moments_normalized
        if self._multichannel:
            nchannels = self._image.shape[-1]
            return numpy.stack(
                [skimage.measure.moments_hu(nu[..., i]) for i in range(nchannels)],
                axis=-1,
            )
        else:
            return skimage.measure.moments_hu(nu)

    @property
    @_cached
    def weighted_moments_normalized(self):
        mu = self.weighted_moments_central

        if self._multichannel:
            nchannels = self._image.shape[-1]
            return numpy.stack(
                [skimage.measure.moments_normalized(mu[..., i], order=3)
                 for i in range(nchannels)],
                axis=-1,
            )
        else:
            return skimage.measure.moments_normalized(mu, order=3)

    def __iter__(self):
        props = PROP_VALS

        if self._image is None:
            unavailable_props = ('intensity_image',
                                 'max_intensity',
                                 'mean_intensity',
                                 'min_intensity',
                                 'weighted_moments',
                                 'weighted_moments_central',
                                 'weighted_centroid',
                                 'weighted_local_centroid',
                                 'weighted_moments_hu',
                                 'weighted_moments_normalized')

            props = props.difference(unavailable_props)

        return iter(sorted(props))

    def __getitem__(self, key):
        value = getattr(self, key, None)
        if value is not None:
            return value
        else:  # backwards compatibility
            return getattr(self, PROPS[key])

    def __eq__(self, other):
        if not isinstance(other, Features):
            return False

        for key in PROP_VALS:
            try:
                # so that NaNs are equal
                numpy.testing.assert_equal(getattr(self, key, None),
                                           getattr(other, key, None))
            except AssertionError:
                return False

        return True
