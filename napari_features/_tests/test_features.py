import pytest
import napari_features.features


@pytest.fixture
def image():
    return []


@pytest.fixture
def objects(image):
    return []


@pytest.fixture
def features(objects, image):
    napari_features.features.Features(0, 0, objects, image)


class TestFeatures:
    def test_color_colocalization_k1_coefficient(self, features):
        assert True

    def test_color_colocalization_k2_coefficient(self, features):
        assert True

    def test_color_colocalization_manders_overlap_coefficient(self, features):
        assert True

    def test_color_colocalization_overlap_coefficient(self, features):
        assert True

    def test_color_colocalization_pearson_correlation_coefficient(self, features):
        assert True

    def test_color_image_integrated_intensity(self, features):
        assert True

    def test_color_image_maximum_intensity(self, features):
        assert True

    def test_color_image_mean_intensity(self, features):
        assert True

    def test_color_image_median_absolute_deviation_intensity(self, features):
        assert True

    def test_color_image_median_intensity(self, features):
        assert True

    def test_color_image_minimum_intensity(self, features):
        assert True

    def test_color_image_quantile_1_intensity(self, features):
        assert True

    def test_color_image_quantile_3_intensity(self, features):
        assert True

    def test_color_image_standard_deviation_intensity(self, features):
        assert True

    def test_color_object_center_mass_intensity_x(self, features):
        assert True

    def test_color_object_center_mass_intensity_y(self, features):
        assert True

    def test_color_object_distribution_coefficient_of_variation_intensity(self, features):
        assert True

    def test_color_object_distribution_integrated_intensity(self, features):
        assert True

    def test_color_object_distribution_mean_intensity(self, features):
        assert True

    def test_color_object_integrated_intensity(self, features):
        assert True

    def test_color_object_integrated_intensity_edge(self, features):
        assert True

    def test_color_object_mass_displacement(self, features):
        assert True

    def test_color_object_maximum_intensity(self, features):
        assert True

    def test_color_object_maximum_intensity_edge(self, features):
        assert True

    def test_color_object_maximum_intensity_x(self, features):
        assert True

    def test_color_object_maximum_intensity_y(self, features):
        assert True

    def test_color_object_mean_intensity(self, features):
        assert True

    def test_color_object_mean_intensity_edge(self, features):
        assert True

    def test_color_object_median_absolute_deviation_intensity(self, features):
        assert True

    def test_color_object_median_intensity(self, features):
        assert True

    def test_color_object_median_intensity_edge(self, features):
        assert True

    def test_color_object_minimum_intensity(self, features):
        assert True

    def test_color_object_minimum_intensity_edge(self, features):
        assert True

    def test_color_object_quantile_1_intensity(self, features):
        assert True

    def test_color_object_quantile_1_intensity_edge(self, features):
        assert True

    def test_color_object_quantile_3_intensity(self, features):
        assert True

    def test_color_object_quantile_3_intensity_edge(self, features):
        assert True

    def test_color_object_standard_deviation_intensity(self, features):
        assert True

    def test_color_object_standard_deviation_intensity_edge(self, features):
        assert True

    def test_location_object_neighborhood_angle(self, features):
        assert True

    def test_location_object_neighborhood_closest_0_distance(self, features):
        assert True

    def test_location_object_neighborhood_closest_0_object_index(self, features):
        assert True

    def test_location_object_neighborhood_closest_1_distance(self, features):
        assert True

    def test_location_object_neighborhood_closest_1_object_index(self, features):
        assert True

    def test_location_object_neighborhood_closest_2_distance(self, features):
        assert True

    def test_location_object_neighborhood_closest_2_object_index(self, features):
        assert True

    def test_location_object_neighborhood_neighbors(self, features):
        assert True

    def test_location_object_neighborhood_touching(self, features):
        assert True

    def test_shape_image_area(self, features):
        assert True

    def test_shape_image_skeleton_branches(self, features):
        assert True

    def test_shape_image_skeleton_endpoints(self, features):
        assert True

    def test_shape_image_skeleton_length(self, features):
        assert True

    def test_shape_image_skeleton_trunks(self, features):
        assert True

    def test_shape_object_area(self, features):
        assert True

    def test_shape_object_bounding_box_area(self, features):
        assert True

    def test_shape_object_bounding_box_maximum_x(self, features):
        assert True

    def test_shape_object_bounding_box_maximum_y(self, features):
        assert True

    def test_shape_object_bounding_box_maximum_z(self, features):
        assert True

    def test_shape_object_bounding_box_minimum_x(self, features):
        assert True

    def test_shape_object_bounding_box_minimum_y(self, features):
        assert True

    def test_shape_object_bounding_box_minimum_z(self, features):
        assert True

    def test_shape_object_bounding_box_volume(self, features):
        assert True

    def test_shape_object_central_moment_0_0_0(self, features):
        assert True

    def test_shape_object_central_moment_0_0_1(self, features):
        assert True

    def test_shape_object_central_moment_0_1_2(self, features):
        assert True

    def test_shape_object_central_moment_0_1_3(self, features):
        assert True

    def test_shape_object_central_moment_1_2_0(self, features):
        assert True

    def test_shape_object_central_moment_1_2_1(self, features):
        assert True

    def test_shape_object_central_moment_1_3_2(self, features):
        assert True

    def test_shape_object_central_moment_1_3_3(self, features):
        assert True

    def test_shape_object_central_moment_2_0_0(self, features):
        assert True

    def test_shape_object_central_moment_2_0_1(self, features):
        assert True

    def test_shape_object_central_moment_2_1_2(self, features):
        assert True

    def test_shape_object_central_moment_2_1_3(self, features):
        assert True

    def test_shape_object_central_moment_3_2_0(self, features):
        assert True

    def test_shape_object_central_moment_3_2_1(self, features):
        assert True

    def test_shape_object_central_moment_3_3_2(self, features):
        assert True

    def test_shape_object_central_moment_3_3_3(self, features):
        assert True

    def test_shape_object_centroid_x(self, features):
        assert True

    def test_shape_object_centroid_y(self, features):
        assert True

    def test_shape_object_centroid_z(self, features):
        assert True

    def test_shape_object_compactness(self, features):
        assert True

    def test_shape_object_eccentricity(self, features):
        assert True

    def test_shape_object_equivalent_diameter(self, features):
        assert True

    def test_shape_object_euler_number(self, features):
        assert True

    def test_shape_object_extent(self, features):
        assert True

    def test_shape_object_form_factor(self, features):
        assert True

    def test_shape_object_hu_moment_0(self, features):
        assert True

    def test_shape_object_hu_moment_1(self, features):
        assert True

    def test_shape_object_hu_moment_2(self, features):
        assert True

    def test_shape_object_hu_moment_3(self, features):
        assert True

    def test_shape_object_hu_moment_4(self, features):
        assert True

    def test_shape_object_hu_moment_5(self, features):
        assert True

    def test_shape_object_hu_moment_6(self, features):
        assert True

    def test_shape_object_inertia_tensor_eigenvalues_x(self, features):
        assert True

    def test_shape_object_inertia_tensor_eigenvalues_y(self, features):
        assert True

    def test_shape_object_inertia_tensor_eigenvalues_z(self, features):
        assert True

    def test_shape_object_inertia_tensor_x_x(self, features):
        assert True

    def test_shape_object_inertia_tensor_x_y(self, features):
        assert True

    def test_shape_object_inertia_tensor_x_z(self, features):
        assert True

    def test_shape_object_inertia_tensor_y_x(self, features):
        assert True

    def test_shape_object_inertia_tensor_y_y(self, features):
        assert True

    def test_shape_object_inertia_tensor_y_z(self, features):
        assert True

    def test_shape_object_inertia_tensor_z_x(self, features):
        assert True

    def test_shape_object_inertia_tensor_z_y(self, features):
        assert True

    def test_shape_object_inertia_tensor_z_z(self, features):
        assert True

    def test_shape_object_major_axis_length(self, features):
        assert True

    def test_shape_object_maximum_feret_diameter(self, features):
        assert True

    def test_shape_object_maximum_radius(self, features):
        assert True

    def test_shape_object_mean_radius(self, features):
        assert True

    def test_shape_object_median_radius(self, features):
        assert True

    def test_shape_object_minimum_feret_diameter(self, features):
        assert True

    def test_shape_object_minor_axis_length(self, features):
        assert True

    def test_shape_object_normalized_moment_x_y(self, features):
        assert True

    def test_shape_object_orientation(self, features):
        assert True

    def test_shape_object_perimeter(self, features):
        assert True

    def test_shape_object_skeleton_branches(self, features):
        assert True

    def test_shape_object_skeleton_endpoints(self, features):
        assert True

    def test_shape_object_skeleton_length(self, features):
        assert True

    def test_shape_object_skeleton_trunks(self, features):
        assert True

    def test_shape_object_solidity(self, features):
        assert True

    def test_shape_object_spatial_moment_0_0_0(self, features):
        assert True

    def test_shape_object_spatial_moment_0_0_1(self, features):
        assert True

    def test_shape_object_spatial_moment_0_1_2(self, features):
        assert True

    def test_shape_object_spatial_moment_0_1_3(self, features):
        assert True

    def test_shape_object_spatial_moment_1_2_0(self, features):
        assert True

    def test_shape_object_spatial_moment_1_2_1(self, features):
        assert True

    def test_shape_object_spatial_moment_1_3_2(self, features):
        assert True

    def test_shape_object_spatial_moment_1_3_3(self, features):
        assert True

    def test_shape_object_spatial_moment_2_0_0(self, features):
        assert True

    def test_shape_object_spatial_moment_2_0_1(self, features):
        assert True

    def test_shape_object_spatial_moment_2_1_2(self, features):
        assert True

    def test_shape_object_spatial_moment_2_1_3(self, features):
        assert True

    def test_shape_object_spatial_moment_3_2_0(self, features):
        assert True

    def test_shape_object_spatial_moment_3_2_1(self, features):
        assert True

    def test_shape_object_spatial_moment_3_3_2(self, features):
        assert True

    def test_shape_object_spatial_moment_3_3_3(self, features):
        assert True

    def test_shape_object_surface_area(self, features):
        assert True

    def test_shape_object_volume(self, features):
        assert True

    def test_texture_object_haralick_angular_second_moment(self, features):
        assert True

    def test_texture_object_haralick_contrast(self, features):
        assert True

    def test_texture_object_haralick_coorelation(self, features):
        assert True

    def test_texture_object_haralick_difference_variance(self, features):
        assert True

    def test_texture_object_haralick_entropy(self, features):
        assert True

    def test_texture_object_haralick_inverse_difference_moment(self, features):
        assert True

    def test_texture_object_haralick_maximum_correlation_coefficient(self, features):
        assert True

    def test_texture_object_haralick_measure_of_correlation_0(self, features):
        assert True

    def test_texture_object_haralick_measure_of_correlation_1(self, features):
        assert True

    def test_texture_object_haralick_sum_average(self, features):
        assert True

    def test_texture_object_haralick_sum_entropy(self, features):
        assert True

    def test_texture_object_haralick_sum_of_squares_variance(self, features):
        assert True

    def test_texture_object_haralick_sum_variance(self, features):
        assert True
