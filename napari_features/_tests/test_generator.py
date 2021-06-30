import pathlib

import numpy.testing
import pytest
import skimage.color
import skimage.data
import skimage.exposure
import skimage.filters
import skimage.io
import skimage.measure
import skimage.morphology
import skimage.segmentation

from ..generator import Generator


@pytest.fixture
def label(request):
    path = pathlib.Path(request.node.fspath.strpath).with_name("label.png")

    return skimage.io.imread(str(path))


@pytest.fixture
def image(request):
    path = pathlib.Path(request.node.fspath.strpath).with_name("image.png")

    return skimage.io.imread(str(path))


@pytest.fixture
def generator(label, image):
    return Generator(label, image)


class TestGenerator:
    # General-purpose features

    # Color

    # Color: Image

    def test__feature_color_image_integrated_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_image_integrated_intensity, 96744.12)

    def test__feature_color_image_maximum_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_image_maximum_intensity, 1.0)

    def test__feature_color_image_mean_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_image_mean_intensity, 0.26651272)

    def test__feature_color_image_median_absolute_deviation_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_image_median_absolute_deviation_intensity, 0.023256469202041625)

    def test__feature_color_image_median_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_image_median_intensity, 0.2627451)

    def test__feature_color_image_minimum_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_image_minimum_intensity, 0.0)

    def test__feature_color_image_quantile_1_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_image_quantile_1_intensity, 0.24705883860588074)

    def test__feature_color_image_quantile_3_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_image_quantile_3_intensity, 0.27843138575553894)

    def test__feature_color_image_standard_deviation_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_image_standard_deviation_intensity, 0.09368451)

    # Color: Object

    def test__feature_color_object_edge_integrated_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_edge_integrated_intensity, 90.29021)

    def test__feature_color_object_edge_maximum_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_edge_maximum_intensity, 0.48235297)

    def test__feature_color_object_edge_mean_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_edge_mean_intensity, 0.00024873335)

    def test__feature_color_object_edge_median_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_edge_median_intensity, 0.0)

    def test__feature_color_object_edge_minimum_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_edge_minimum_intensity, 0.0)

    def test__feature_color_object_edge_quantile_1_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_edge_quantile_1_intensity, 0.0)

    def test__feature_color_object_edge_quantile_3_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_edge_quantile_3_intensity, 0.0)

    def test__feature_color_object_edge_standard_deviation_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_edge_standard_deviation_intensity, 0.008109777)

    def test__feature_color_object_center_mass_intensity_x(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_center_mass_intensity_x, 0.0)

    def test__feature_color_object_center_mass_intensity_y(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_center_mass_intensity_y, 0.0)

    def test__feature_color_object_integrated_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_integrated_intensity, 8798.737)

    def test__feature_color_object_mass_displacement(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_mass_displacement, 0.0)

    def test__feature_color_object_maximum_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_maximum_intensity, 1.0)

    def test__feature_color_object_maximum_intensity_x(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_maximum_intensity_x, 400)

    def test__feature_color_object_maximum_intensity_y(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_maximum_intensity_y, 412)

    def test__feature_color_object_mean_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_mean_intensity, 0.024238946)

    def test__feature_color_object_median_absolute_deviation_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_median_absolute_deviation_intensity, 0.0)

    def test__feature_color_object_median_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_median_intensity, 0.0)

    def test__feature_color_object_minimum_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_minimum_intensity, 0.0)

    def test__feature_color_object_quantile_1_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_quantile_1_intensity, 0.0)

    def test__feature_color_object_quantile_3_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_quantile_3_intensity, 0.0)

    def test__feature_color_object_standard_deviation_intensity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_color_object_standard_deviation_intensity, 0.1279013)

    # Location

    # Location: Object neighborhood

    def test__feature_location_object_neighborhood_angle(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_location_object_neighborhood_angle, 0.0)

    def test__feature_location_object_neighborhood_closest_0_distance(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_location_object_neighborhood_closest_0_distance, 0.0)

    def test__feature_location_object_neighborhood_closest_0_object_index(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_location_object_neighborhood_closest_0_object_index, 0.0)

    def test__feature_location_object_neighborhood_closest_1_distance(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_location_object_neighborhood_closest_1_distance, 0.0)

    def test__feature_location_object_neighborhood_closest_1_object_index(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_location_object_neighborhood_closest_1_object_index, 0.0)

    def test__feature_location_object_neighborhood_closest_2_distance(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_location_object_neighborhood_closest_2_distance, 0.0)

    def test__feature_location_object_neighborhood_closest_2_object_index(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_location_object_neighborhood_closest_2_object_index, 0.0)

    def test__feature_location_object_neighborhood_neighbors(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_location_object_neighborhood_neighbors, 0.0)

    def test__feature_location_object_neighborhood_touching(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_location_object_neighborhood_touching, 0.0)

    # Metadata

    # Metadata: Image

    def test__feature_metadata_image_checksum(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_metadata_image_checksum, 0.0)

    def test__feature_metadata_image_filename(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_metadata_image_filename, 0.0)

    # Metadata: Layer

    def test__feature_metadata_layer_name(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_metadata_layer_name, 0.0)

    def test__feature_metadata_layer_type(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_metadata_layer_type, 0.0)

    # Metadata: Object

    def test__feature_metadata_object_index(self, generator):
        assert generator._feature_metadata_object_index == 1

    # Shape

    # Shape: Image

    def test__feature_shape_image_area(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_image_area, 363000)

    # Shape: Image skeleton

    def test__feature_shape_image_skeleton_branches(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_image_skeleton_branches, 0.0)

    def test__feature_shape_image_skeleton_endpoints(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_image_skeleton_endpoints, 0.0)

    def test__feature_shape_image_skeleton_length(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_image_skeleton_length, 0.0)

    def test__feature_shape_image_skeleton_trunks(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_image_skeleton_trunks, 0.0)

    # Shape: Object

    def test__feature_shape_object_area(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_area, 0.0)

    def test__feature_shape_object_bounding_box_area(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_bounding_box_area, 0.0)

    def test__feature_shape_object_bounding_box_maximum_x(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_bounding_box_maximum_x, 0.0)

    def test__feature_shape_object_bounding_box_maximum_y(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_bounding_box_maximum_y, 0.0)

    def test__feature_shape_object_bounding_box_maximum_z(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_bounding_box_maximum_z, 0.0)

    def test__feature_shape_object_bounding_box_minimum_x(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_bounding_box_minimum_x, 0.0)

    def test__feature_shape_object_bounding_box_minimum_y(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_bounding_box_minimum_y, 0.0)

    def test__feature_shape_object_bounding_box_minimum_z(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_bounding_box_minimum_z, 0.0)

    def test__feature_shape_object_bounding_box_volume(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_bounding_box_volume, 0.0)

    def test__feature_shape_object_central_moment_0_0_0(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_central_moment_0_0_0, 0.0)

    def test__feature_shape_object_central_moment_0_0_1(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_central_moment_0_0_1, 0.0)

    def test__feature_shape_object_central_moment_0_1_2(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_central_moment_0_1_2, 0.0)

    def test__feature_shape_object_central_moment_0_1_3(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_central_moment_0_1_3, 0.0)

    def test__feature_shape_object_central_moment_1_2_0(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_central_moment_1_2_0, 0.0)

    def test__feature_shape_object_central_moment_1_2_1(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_central_moment_1_2_1, 0.0)

    def test__feature_shape_object_central_moment_1_3_2(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_central_moment_1_3_2, 0.0)

    def test__feature_shape_object_central_moment_1_3_3(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_central_moment_1_3_3, 0.0)

    def test__feature_shape_object_central_moment_2_0_0(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_central_moment_2_0_0, 0.0)

    def test__feature_shape_object_central_moment_2_0_1(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_central_moment_2_0_1, 0.0)

    def test__feature_shape_object_central_moment_2_1_2(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_central_moment_2_1_2, 0.0)

    def test__feature_shape_object_central_moment_2_1_3(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_central_moment_2_1_3, 0.0)

    def test__feature_shape_object_central_moment_3_2_0(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_central_moment_3_2_0, 0.0)

    def test__feature_shape_object_central_moment_3_2_1(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_central_moment_3_2_1, 0.0)

    def test__feature_shape_object_central_moment_3_3_2(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_central_moment_3_3_2, 0.0)

    def test__feature_shape_object_central_moment_3_3_3(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_central_moment_3_3_3, 0.0)

    # def test__feature_shape_object_centroid_x(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_centroid_x, 0.0)
    #
    # def test__feature_shape_object_centroid_y(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_centroid_y, 0.0)
    #
    # def test__feature_shape_object_centroid_z(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_centroid_z, 0.0)

    def test__feature_shape_object_compactness(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_compactness, 0.0)

    def test__feature_shape_object_eccentricity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_eccentricity, 0.0)

    # def test__feature_shape_object_equivalent_diameter(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_equivalent_diameter, 0.0)

    # def test__feature_shape_object_euler_number(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_euler_number, 0.0)

    # def test__feature_shape_object_extent(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_extent, 0.0)

    def test__feature_shape_object_form_factor(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_form_factor, 0.0)

    def test__feature_shape_object_hu_moment_0(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_hu_moment_0, 0.0)

    def test__feature_shape_object_hu_moment_1(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_hu_moment_1, 0.0)

    def test__feature_shape_object_hu_moment_2(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_hu_moment_2, 0.0)

    def test__feature_shape_object_hu_moment_3(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_hu_moment_3, 0.0)

    def test__feature_shape_object_hu_moment_4(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_hu_moment_4, 0.0)

    def test__feature_shape_object_hu_moment_5(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_hu_moment_5, 0.0)

    def test__feature_shape_object_hu_moment_6(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_hu_moment_6, 0.0)

    def test__feature_shape_object_inertia_tensor_eigenvalues_x(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_inertia_tensor_eigenvalues_x, 0.0)

    def test__feature_shape_object_inertia_tensor_eigenvalues_y(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_inertia_tensor_eigenvalues_y, 0.0)

    def test__feature_shape_object_inertia_tensor_eigenvalues_z(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_inertia_tensor_eigenvalues_z, 0.0)

    def test__feature_shape_object_inertia_tensor_x_x(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_inertia_tensor_x_x, 0.0)

    def test__feature_shape_object_inertia_tensor_x_y(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_inertia_tensor_x_y, 0.0)

    def test__feature_shape_object_inertia_tensor_x_z(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_inertia_tensor_x_z, 0.0)

    def test__feature_shape_object_inertia_tensor_y_x(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_inertia_tensor_y_x, 0.0)

    def test__feature_shape_object_inertia_tensor_y_y(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_inertia_tensor_y_y, 0.0)

    def test__feature_shape_object_inertia_tensor_y_z(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_inertia_tensor_y_z, 0.0)

    def test__feature_shape_object_inertia_tensor_z_x(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_inertia_tensor_z_x, 0.0)

    def test__feature_shape_object_inertia_tensor_z_y(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_inertia_tensor_z_y, 0.0)

    def test__feature_shape_object_inertia_tensor_z_z(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_inertia_tensor_z_z, 0.0)

    def test__feature_shape_object_major_axis_length(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_major_axis_length, 0.0)

    def test__feature_shape_object_maximum_feret_diameter(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_maximum_feret_diameter, 0.0)

    def test__feature_shape_object_maximum_radius(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_maximum_radius, 0.0)

    def test__feature_shape_object_mean_radius(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_mean_radius, 0.0)

    def test__feature_shape_object_median_radius(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_median_radius, 0.0)

    def test__feature_shape_object_minimum_feret_diameter(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_minimum_feret_diameter, 0.0)

    def test__feature_shape_object_minor_axis_length(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_minor_axis_length, 0.0)

    def test__feature_shape_object_normalized_moment_x_y(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_normalized_moment_x_y, 0.0)

    def test__feature_shape_object_orientation(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_orientation, 0.0)

    def test__feature_shape_object_perimeter(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_perimeter, 0.0)

    def test__feature_shape_object_solidity(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_solidity, 0.0)

    # def test__feature_shape_object_spatial_moment_0_0_0(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_spatial_moment_0_0_0, 0.0)
    #
    # def test__feature_shape_object_spatial_moment_0_0_1(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_spatial_moment_0_0_1, 0.0)
    #
    # def test__feature_shape_object_spatial_moment_0_1_2(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_spatial_moment_0_1_2, 0.0)
    #
    # def test__feature_shape_object_spatial_moment_0_1_3(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_spatial_moment_0_1_3, 0.0)
    #
    # def test__feature_shape_object_spatial_moment_1_2_0(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_spatial_moment_1_2_0, 0.0)
    #
    # def test__feature_shape_object_spatial_moment_1_2_1(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_spatial_moment_1_2_1, 0.0)
    #
    # def test__feature_shape_object_spatial_moment_1_3_2(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_spatial_moment_1_3_2, 0.0)
    #
    # def test__feature_shape_object_spatial_moment_1_3_3(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_spatial_moment_1_3_3, 0.0)
    #
    # def test__feature_shape_object_spatial_moment_2_0_0(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_spatial_moment_2_0_0, 0.0)
    #
    # def test__feature_shape_object_spatial_moment_2_0_1(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_spatial_moment_2_0_1, 0.0)
    #
    # def test__feature_shape_object_spatial_moment_2_1_2(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_spatial_moment_2_1_2, 0.0)
    #
    # def test__feature_shape_object_spatial_moment_2_1_3(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_spatial_moment_2_1_3, 0.0)
    #
    # def test__feature_shape_object_spatial_moment_3_2_0(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_spatial_moment_3_2_0, 0.0)
    #
    # def test__feature_shape_object_spatial_moment_3_2_1(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_spatial_moment_3_2_1, 0.0)
    #
    # def test__feature_shape_object_spatial_moment_3_3_2(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_spatial_moment_3_3_2, 0.0)
    #
    # def test__feature_shape_object_spatial_moment_3_3_3(self, generator):
    #     numpy.testing.assert_approx_equal(generator._feature_shape_object_spatial_moment_3_3_3, 0.0)

    def test__feature_shape_object_surface_area(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_surface_area, 0.0)

    def test__feature_shape_object_volume(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_volume, 0.0)

    # Shape: Object skeleton

    def test__feature_shape_object_skeleton_endpoints(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_skeleton_endpoints, 0.0)

    def test__feature_shape_object_skeleton_branches(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_skeleton_branches, 0.0)

    def test__feature_shape_object_skeleton_length(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_skeleton_length, 0.0)

    def test__feature_shape_object_skeleton_trunks(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_shape_object_skeleton_trunks, 0.0)

    # Texture

    # Texture: Object

    def test__feature_texture_object_haralick_angular_second_moment(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_texture_object_haralick_angular_second_moment, 0.0)

    def test__feature_texture_object_haralick_contrast(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_texture_object_haralick_contrast, 0.0)

    def test__feature_texture_object_haralick_coorelation(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_texture_object_haralick_coorelation, 0.0)

    def test__feature_texture_object_haralick_sum_of_squares_variance(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_texture_object_haralick_sum_of_squares_variance, 0.0)

    def test__feature_texture_object_haralick_inverse_difference_moment(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_texture_object_haralick_inverse_difference_moment, 0.0)

    def test__feature_texture_object_haralick_sum_average(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_texture_object_haralick_sum_average, 0.0)

    def test__feature_texture_object_haralick_sum_variance(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_texture_object_haralick_sum_variance, 0.0)

    def test__feature_texture_object_haralick_sum_entropy(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_texture_object_haralick_sum_entropy, 0.0)

    def test__feature_texture_object_haralick_entropy(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_texture_object_haralick_entropy, 0.0)

    def test__feature_texture_object_haralick_difference_variance(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_texture_object_haralick_difference_variance, 0.0)

    def test__feature_texture_object_haralick_measure_of_correlation_0(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_texture_object_haralick_measure_of_correlation_0, 0.0)

    def test__feature_texture_object_haralick_measure_of_correlation_1(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_texture_object_haralick_measure_of_correlation_1, 0.0)

    def test__feature_texture_object_haralick_maximum_correlation_coefficient(self, generator):
        numpy.testing.assert_approx_equal(generator._feature_texture_object_haralick_maximum_correlation_coefficient, 0.0)
