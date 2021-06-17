import functools
import inspect

import numpy
import scipy.ndimage
import scipy.stats
import skimage.segmentation


def cache(wrapped):
    @functools.wraps(wrapped)
    def function(generator: "Generator"):
        name = wrapped.__name__

        if not (name in generator.cache):
            generator.cache[name] = wrapped(generator)

        return generator.cache[name]

    return function


class Generator:
    def __init__(self, label, image):
        self.cache = {}

        self.image = skimage.img_as_float32(image)

        self.label = label

        self.multichannel = label.shape < image.shape

        self.object = None

        self.object_index = None

        self.objects = scipy.ndimage.find_objects(label)

        self._cropped = None

        self._spatial_axes = tuple(range(label.ndim))

    def __iter__(self):
        for object_index, _object_slice in enumerate(self.objects):
            self.object_index = object_index + 1

            self.object = _object_slice

            yield [getattr(self, member) for member in self._members]

    @property
    @cache
    def coordinates(self):
        indices = numpy.nonzero(self.image)

        stack = []

        for index in range(self.label.ndim):
            stack += [indices[index] + self.object[index].start]

        return numpy.vstack(stack).T

    @property
    @cache
    def crop(self):
        return self.image[self.object]

    @property
    @cache
    def edge(self):
        boundary = skimage.segmentation.find_boundaries(self.mask, mode="outer")

        return self.crop * boundary

    @property
    def names(self):
        return [member.replace("_feature_", "") for member in self._members]

    @property
    @cache
    def mask(self):
        return self.label[self.object] > 0

    @property
    @cache
    def masked(self):
        return self.image[self.object] * self.mask

    @property
    def _feature_color_object_edge_integrated_intensity(self):
        return numpy.sum(self.edge)

    @property
    def _feature_color_object_edge_maximum_intensity(self):
        return numpy.max(self.edge)

    @property
    def _feature_color_object_edge_mean_intensity(self):
        return numpy.mean(self.edge)

    @property
    def _feature_color_object_edge_median_intensity(self):
        return numpy.median(self.edge)

    @property
    def _feature_color_object_edge_minimum_intensity(self):
        return numpy.min(self.edge)

    @property
    def _feature_color_object_edge_quantile_1_intensity(self):
        return numpy.quantile(self.edge, 0.25)

    @property
    def _feature_color_object_edge_quantile_3_intensity(self):
        return numpy.quantile(self.edge, 0.75)

    @property
    def _feature_color_object_edge_standard_deviation_intensity(self):
        return numpy.std(self.edge)

    @property
    def _feature_color_object_center_mass_intensity_x(self):
        return 0.0

    @property
    def _feature_color_object_center_mass_intensity_y(self):
        return 0.0

    @property
    def _feature_color_object_integrated_intensity(self):
        return numpy.sum(self.masked)

    @property
    def _feature_color_object_mass_displacement(self):
        return 0.0

    @property
    def _feature_color_object_maximum_intensity(self):
        return numpy.max(self.masked)

    @property
    def _feature_color_object_maximum_intensity_x(self):
        xs, _ = numpy.where(self.image == self._feature_color_object_maximum_intensity)

        # If there are multiple matches, first match is returned.
        return xs[0]

    @property
    def _feature_color_object_maximum_intensity_y(self):
        _, ys = numpy.where(self.image == self._feature_color_object_maximum_intensity)

        # If there are multiple matches, first match is returned.
        return ys[0]

    @property
    def _feature_color_object_mean_intensity(self):
        return numpy.mean(self.masked)

    @property
    def _feature_color_object_median_absolute_deviation_intensity(self):
        return 0.0

    @property
    def _feature_color_object_median_intensity(self):
        return numpy.median(self.masked)

    @property
    def _feature_color_object_minimum_intensity(self):
        return numpy.min(self.masked)

    @property
    def _feature_color_object_quantile_1_intensity(self):
        return numpy.quantile(self.masked, 0.25)

    @property
    def _feature_color_object_quantile_3_intensity(self):
        return numpy.quantile(self.masked, 0.75)

    @property
    def _feature_color_object_standard_deviation_intensity(self):
        return numpy.std(self.masked)

    @property
    def _feature_metadata_object_index(self):
        return self.object_index

    @property
    def _members(self):
        members = inspect.getmembers(self.__class__, lambda member: isinstance(member, property))

        return sorted([k for k, _ in members if k.startswith("_feature_")])
