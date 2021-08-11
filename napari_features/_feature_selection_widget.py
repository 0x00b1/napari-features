import typing

import qtpy.QtWidgets
import qtpy.QtCore

from napari_features._tree_widget_item import TreeWidgetItem

FEATURES = {
    "Color": {
        "Image": {
            "Integrated intensity": [
                "_feature_color_image_integrated_intensity",
            ],
            "Maximum": [
                "_feature_color_image_maximum_intensity",
            ],
            "Mean": [
                "_feature_color_image_mean_intensity",
            ],
            "Median absolute deviation (MAD)": [
                "_feature_color_image_median_absolute_deviation_intensity",
            ],
            "Median": [
                "_feature_color_image_median_intensity",
            ],
            "Minimum": [
                "_feature_color_image_minimum_intensity",
            ],
            "Quartile, first": [
                "_feature_color_image_quantile_1_intensity",
            ],
            "Quartile, third": [
                "_feature_color_image_quantile_3_intensity",
            ],
            "Standard deviation": [
                "_feature_color_image_standard_deviation_intensity",
            ],
        },
        "Object distribution": {
            "Coefficient of variation": [],
            "Integrated intensity": [],
            "Mean": [],
        },
        "Object": {
            "Center mass": [
                "_feature_color_object_center_mass_intensity_x",
                "_feature_color_object_center_mass_intensity_y",
            ],
            "Integrated intensity": [
                "_feature_color_object_integrated_intensity",

            ],
            "Mass displacement": [
                "_feature_color_object_mass_displacement",

            ],
            "Maximum intensity": [
                "_feature_color_object_maximum_intensity_x",
                "_feature_color_object_maximum_intensity_y",
                "_feature_color_object_maximum_intensity",
            ],
            "Mean": [
                "_feature_color_object_mean_intensity",
            ],
            "Median absolute deviation (MAD)": [
                "_feature_color_object_median_absolute_deviation_intensity",
            ],
            "Median": [
                "_feature_color_object_median_intensity",
            ],
            "Minimum": [
                "_feature_color_object_minimum_intensity",
            ],
            "Quartile, first": [
                "_feature_color_object_quantile_1_intensity",
            ],
            "Quartile, third": [
                "_feature_color_object_quantile_3_intensity",
            ],
            "Standard deviation": [
                "_feature_color_object_standard_deviation_intensity",
            ],
        },
        "Object edge": {
            "Integrated intensity": [
                "_feature_color_object_edge_integrated_intensity",
            ],
            "Maximum": [
                "_feature_color_object_edge_maximum_intensity",
            ],
            "Mean": [
                "_feature_color_object_edge_mean_intensity",
            ],
            "Median": [
                "_feature_color_object_edge_median_intensity",
            ],
            "Minimum": [
                "_feature_color_object_edge_minimum_intensity",
            ],
            "Quartile, first": [
                "_feature_color_object_edge_quantile_1_intensity",
            ],
            "Quartile, third": [
                "_feature_color_object_edge_quantile_3_intensity",
            ],
            "Standard deviation": [
                "_feature_color_object_edge_standard_deviation_intensity",
            ],
        }
    },
    "Location": {
        "Object neighborhood": {
            "1-closest": [
                "_feature_location_object_neighborhood_closest_0_distance",
                "_feature_location_object_neighborhood_closest_0_object_index",
            ],
            "2-closest": [
                "_feature_location_object_neighborhood_closest_1_distance",
                "_feature_location_object_neighborhood_closest_1_object_index",
            ],
            "3-closest": [
                "_feature_location_object_neighborhood_closest_2_distance",
                "_feature_location_object_neighborhood_closest_2_object_index",
            ],
            "Angle": [
                "_feature_location_object_neighborhood_angle",
            ],
            "Neighbors": [
                "_feature_location_object_neighborhood_neighbors",
            ],
            "Touching": [
                "_feature_location_object_neighborhood_touching",
            ],
        }
    },
    "Shape": {
        "Image": {
            "Area": {
                "_feature_shape_image_area",
            },
        },
        "Image skeleton": {
            "Branches": [
                "_feature_shape_image_skeleton_branches",
            ],
            "Endpoints": [
                "_feature_shape_image_skeleton_endpoints",
            ],
            "Length": [
                "_feature_shape_image_skeleton_length",
            ],
            "Trunks": [
                "_feature_shape_image_skeleton_trunks",
            ],
        },
        "Object": {
            "Area": [
                "_feature_shape_object_area",
            ],
            "Bounding box area": [
                "_feature_shape_object_bounding_box_area",
            ],
            "Bounding box": [
                "_feature_shape_object_bounding_box_maximum_x",
                "_feature_shape_object_bounding_box_maximum_y",
                "_feature_shape_object_bounding_box_maximum_z",
                "_feature_shape_object_bounding_box_minimum_x",
                "_feature_shape_object_bounding_box_minimum_y",
                "_feature_shape_object_bounding_box_minimum_z",
            ],
            "Central moment": [
                "_feature_shape_object_central_moment_0_0_0",
                "_feature_shape_object_central_moment_0_0_1",
                "_feature_shape_object_central_moment_0_0_2",
                "_feature_shape_object_central_moment_0_0_3",
                "_feature_shape_object_central_moment_0_1_0",
                "_feature_shape_object_central_moment_0_1_1",
                "_feature_shape_object_central_moment_0_1_2",
                "_feature_shape_object_central_moment_0_1_3",
                "_feature_shape_object_central_moment_0_2_0",
                "_feature_shape_object_central_moment_0_2_1",
                "_feature_shape_object_central_moment_0_2_2",
                "_feature_shape_object_central_moment_0_2_3",
                "_feature_shape_object_central_moment_0_3_0",
                "_feature_shape_object_central_moment_0_3_1",
                "_feature_shape_object_central_moment_0_3_2",
                "_feature_shape_object_central_moment_0_3_3",
                "_feature_shape_object_central_moment_1_0_0",
                "_feature_shape_object_central_moment_1_0_1",
                "_feature_shape_object_central_moment_1_0_2",
                "_feature_shape_object_central_moment_1_0_3",
                "_feature_shape_object_central_moment_1_1_0",
                "_feature_shape_object_central_moment_1_1_1",
                "_feature_shape_object_central_moment_1_1_2",
                "_feature_shape_object_central_moment_1_1_3",
                "_feature_shape_object_central_moment_1_2_0",
                "_feature_shape_object_central_moment_1_2_1",
                "_feature_shape_object_central_moment_1_2_2",
                "_feature_shape_object_central_moment_1_2_3",
                "_feature_shape_object_central_moment_1_3_0",
                "_feature_shape_object_central_moment_1_3_1",
                "_feature_shape_object_central_moment_1_3_2",
                "_feature_shape_object_central_moment_1_3_3",
                "_feature_shape_object_central_moment_2_0_0",
                "_feature_shape_object_central_moment_2_0_1",
                "_feature_shape_object_central_moment_2_0_2",
                "_feature_shape_object_central_moment_2_0_3",
                "_feature_shape_object_central_moment_2_1_0",
                "_feature_shape_object_central_moment_2_1_1",
                "_feature_shape_object_central_moment_2_1_2",
                "_feature_shape_object_central_moment_2_1_3",
                "_feature_shape_object_central_moment_2_2_0",
                "_feature_shape_object_central_moment_2_2_1",
                "_feature_shape_object_central_moment_2_2_2",
                "_feature_shape_object_central_moment_2_2_3",
                "_feature_shape_object_central_moment_2_3_0",
                "_feature_shape_object_central_moment_2_3_1",
                "_feature_shape_object_central_moment_2_3_2",
                "_feature_shape_object_central_moment_2_3_3",
                "_feature_shape_object_central_moment_3_0_0",
                "_feature_shape_object_central_moment_3_0_1",
                "_feature_shape_object_central_moment_3_0_2",
                "_feature_shape_object_central_moment_3_0_3",
                "_feature_shape_object_central_moment_3_1_0",
                "_feature_shape_object_central_moment_3_1_1",
                "_feature_shape_object_central_moment_3_1_2",
                "_feature_shape_object_central_moment_3_1_3",
                "_feature_shape_object_central_moment_3_2_0",
                "_feature_shape_object_central_moment_3_2_1",
                "_feature_shape_object_central_moment_3_2_2",
                "_feature_shape_object_central_moment_3_2_3",
                "_feature_shape_object_central_moment_3_3_0",
                "_feature_shape_object_central_moment_3_3_1",
                "_feature_shape_object_central_moment_3_3_2",
                "_feature_shape_object_central_moment_3_3_3",
            ],
            "Centroid": [
                "_feature_shape_object_centroid_x",
                "_feature_shape_object_centroid_y",
                "_feature_shape_object_centroid_z",
            ],
            "Compactness": [
                "_feature_shape_object_compactness",
            ],
            "Eccentricity": [
                "_feature_shape_object_eccentricity",
            ],
            "Elongation": [
                "_feature_shape_object_elongation",
            ],
            "Equivalent diameter": [
                "_feature_shape_object_equivalent_diameter",
            ],
            "Euler number": [
                "_feature_shape_object_euler_number",
            ],
            "Extent": [
                "_feature_shape_object_extent",
            ],
            "Form factor": [
                "_feature_shape_object_form_factor",
            ],
            "Hu moment": [
                "_feature_shape_object_hu_moment_0",
                "_feature_shape_object_hu_moment_1",
                "_feature_shape_object_hu_moment_2",
                "_feature_shape_object_hu_moment_3",
                "_feature_shape_object_hu_moment_4",
                "_feature_shape_object_hu_moment_5",
                "_feature_shape_object_hu_moment_6",
            ],
            "Inertia tensor": [
                "_feature_shape_object_inertia_tensor_x_x",
                "_feature_shape_object_inertia_tensor_x_y",
                "_feature_shape_object_inertia_tensor_x_z",
                "_feature_shape_object_inertia_tensor_y_x",
                "_feature_shape_object_inertia_tensor_y_y",
                "_feature_shape_object_inertia_tensor_y_z",
                "_feature_shape_object_inertia_tensor_z_x",
                "_feature_shape_object_inertia_tensor_z_y",
                "_feature_shape_object_inertia_tensor_z_z",
            ],
            "Inertia tensor eigenvalues": [
                "_feature_shape_object_inertia_tensor_eigenvalues_x",
                "_feature_shape_object_inertia_tensor_eigenvalues_y",
                "_feature_shape_object_inertia_tensor_eigenvalues_z",
            ],
            "Major axis length": [
                "_feature_shape_object_major_axis_length",
            ],
            "Maximum feret diameter": [
                "_feature_shape_object_maximum_feret_diameter",
            ],
            "Maximum radius": [
                "_feature_shape_object_maximum_radius",
            ],
            "Mean radius": [
                "_feature_shape_object_mean_radius",
            ],
            "Median radius": [
                "_feature_shape_object_median_radius",
            ],
            "Minimum feret diameter": [
                "_feature_shape_object_minimum_feret_diameter",
            ],
            "Minor axis length": [
                "_feature_shape_object_minor_axis_length",
            ],
            "Normalized moment": [
                "_feature_shape_object_normalized_moment_x_y",
            ],
            "Orientation": [
                "_feature_shape_object_orientation",
            ],
            "Perimeter": [
                "_feature_shape_object_perimeter",
            ],
            "Solidity": [
                "_feature_shape_object_solidity",
            ],
            "Spatial moment": [
                "_feature_shape_object_spatial_moment_0_0_0",
                "_feature_shape_object_spatial_moment_0_0_1",
                "_feature_shape_object_spatial_moment_0_0_2",
                "_feature_shape_object_spatial_moment_0_0_3",
                "_feature_shape_object_spatial_moment_0_1_0",
                "_feature_shape_object_spatial_moment_0_1_1",
                "_feature_shape_object_spatial_moment_0_1_2",
                "_feature_shape_object_spatial_moment_0_1_3",
                "_feature_shape_object_spatial_moment_0_2_0",
                "_feature_shape_object_spatial_moment_0_2_1",
                "_feature_shape_object_spatial_moment_0_2_2",
                "_feature_shape_object_spatial_moment_0_2_3",
                "_feature_shape_object_spatial_moment_0_3_0",
                "_feature_shape_object_spatial_moment_0_3_1",
                "_feature_shape_object_spatial_moment_0_3_2",
                "_feature_shape_object_spatial_moment_0_3_3",
                "_feature_shape_object_spatial_moment_1_0_0",
                "_feature_shape_object_spatial_moment_1_0_1",
                "_feature_shape_object_spatial_moment_1_0_2",
                "_feature_shape_object_spatial_moment_1_0_3",
                "_feature_shape_object_spatial_moment_1_1_0",
                "_feature_shape_object_spatial_moment_1_1_1",
                "_feature_shape_object_spatial_moment_1_1_2",
                "_feature_shape_object_spatial_moment_1_1_3",
                "_feature_shape_object_spatial_moment_1_2_0",
                "_feature_shape_object_spatial_moment_1_2_1",
                "_feature_shape_object_spatial_moment_1_2_2",
                "_feature_shape_object_spatial_moment_1_2_3",
                "_feature_shape_object_spatial_moment_1_3_0",
                "_feature_shape_object_spatial_moment_1_3_1",
                "_feature_shape_object_spatial_moment_1_3_2",
                "_feature_shape_object_spatial_moment_1_3_3",
                "_feature_shape_object_spatial_moment_2_0_0",
                "_feature_shape_object_spatial_moment_2_0_1",
                "_feature_shape_object_spatial_moment_2_0_2",
                "_feature_shape_object_spatial_moment_2_0_3",
                "_feature_shape_object_spatial_moment_2_1_0",
                "_feature_shape_object_spatial_moment_2_1_1",
                "_feature_shape_object_spatial_moment_2_1_2",
                "_feature_shape_object_spatial_moment_2_1_3",
                "_feature_shape_object_spatial_moment_2_2_0",
                "_feature_shape_object_spatial_moment_2_2_1",
                "_feature_shape_object_spatial_moment_2_2_2",
                "_feature_shape_object_spatial_moment_2_2_3",
                "_feature_shape_object_spatial_moment_2_3_0",
                "_feature_shape_object_spatial_moment_2_3_1",
                "_feature_shape_object_spatial_moment_2_3_2",
                "_feature_shape_object_spatial_moment_2_3_3",
                "_feature_shape_object_spatial_moment_3_0_0",
                "_feature_shape_object_spatial_moment_3_0_1",
                "_feature_shape_object_spatial_moment_3_0_2",
                "_feature_shape_object_spatial_moment_3_0_3",
                "_feature_shape_object_spatial_moment_3_1_0",
                "_feature_shape_object_spatial_moment_3_1_1",
                "_feature_shape_object_spatial_moment_3_1_2",
                "_feature_shape_object_spatial_moment_3_1_3",
                "_feature_shape_object_spatial_moment_3_2_0",
                "_feature_shape_object_spatial_moment_3_2_1",
                "_feature_shape_object_spatial_moment_3_2_2",
                "_feature_shape_object_spatial_moment_3_2_3",
                "_feature_shape_object_spatial_moment_3_3_0",
                "_feature_shape_object_spatial_moment_3_3_1",
                "_feature_shape_object_spatial_moment_3_3_2",
                "_feature_shape_object_spatial_moment_3_3_3",
            ],
            "Surface area": [
                "_feature_shape_object_surface_area",
            ],
        },
        "Object skeleton": {
            "Branches": [
                "_feature_shape_object_skeleton_branches",
            ],
            "Endpoints": [
                "_feature_shape_object_skeleton_endpoints",
            ],
            "Length": [
                "_feature_shape_object_skeleton_length",
            ],
            "Trunks": [
                "_feature_shape_object_skeleton_trunks",
            ],
        }
    },
    "Texture": {
        "Object": {
            "Haralick": [
                "_feature_texture_object_haralick_angular_second_moment",
                "_feature_texture_object_haralick_contrast",
                "_feature_texture_object_haralick_coorelation",
                "_feature_texture_object_haralick_difference_variance",
                "_feature_texture_object_haralick_entropy",
                "_feature_texture_object_haralick_inverse_difference_moment",
                "_feature_texture_object_haralick_maximum_correlation_coefficient",
                "_feature_texture_object_haralick_measure_of_correlation_0",
                "_feature_texture_object_haralick_measure_of_correlation_1",
                "_feature_texture_object_haralick_sum_average",
                "_feature_texture_object_haralick_sum_entropy",
                "_feature_texture_object_haralick_sum_of_squares_variance",
                "_feature_texture_object_haralick_sum_variance",
            ],
        }
    }
}


class FeatureSelectionWidget(qtpy.QtWidgets.QWidget):
    features: typing.Set[str] = set()

    def __init__(
            self,
            flags: typing.Union[qtpy.QtCore.Qt.WindowFlags, qtpy.QtCore.Qt.WindowType] = qtpy.QtCore.Qt.WindowFlags(),
    ):
        super(FeatureSelectionWidget, self).__init__(flags=flags)

        grid_layout = qtpy.QtWidgets.QGridLayout()

        self.setLayout(grid_layout)

        self.tree_widget = qtpy.QtWidgets.QTreeWidget()

        for descriptor in FEATURES.keys():
            parent = TreeWidgetItem(self.tree_widget)

            parent.setText(0, descriptor)

            parent.setFlags(parent.flags() | qtpy.QtCore.Qt.ItemIsTristate | qtpy.QtCore.Qt.ItemIsUserCheckable)

            for name in FEATURES[descriptor]:
                child = TreeWidgetItem(parent)

                child.setText(0, name)

                child.setFlags(child.flags() | qtpy.QtCore.Qt.ItemIsTristate | qtpy.QtCore.Qt.ItemIsUserCheckable)

                for feature in FEATURES[descriptor][name].keys():
                    grandchild = TreeWidgetItem(child)

                    grandchild.setFlags(grandchild.flags() | qtpy.QtCore.Qt.ItemIsUserCheckable)

                    grandchild.setText(0, feature)

                    grandchild.setCheckState(0, qtpy.QtCore.Qt.Unchecked)

        self.tree_widget.itemChanged.connect(self._on_change)

        self.layout().addWidget(self.tree_widget)

    def _on_change(self, item: TreeWidgetItem, column: int) -> None:
        if column == 0 and (item.check_state != item.checkState(0)):
            item.check_state = item.checkState(0)
