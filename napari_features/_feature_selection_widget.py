import typing

import qtpy.QtWidgets
import qtpy.QtCore

FEATURES = {
    "Color": {
        "Image": {
            "Integrated intensity": [],
            "Maximum": [],
            "Mean": [],
            "Median absolute deviation (MAD)": [],
            "Median": [],
            "Minimum": [],
            "Quartile, first": [],
            "Quartile, third": [],
            "Standard deviation": [],
        },
        "Object distribution": {
            "Coefficient of variation": [],
            "Integrated intensity": [],
            "Mean": [],
        },
        "Object": {
            "Center mass": [],
            "Integrated intensity": [],
            "Mass displacement": [],
            "Maximum intensity": [],
            "Mean": [],
            "Median absolute deviation (MAD)": [],
            "Median": [],
            "Minimum": [],
            "Quartile, first": [],
            "Quartile, third": [],
            "Standard deviation": [],
        },
        "Object edge": {
            "Integrated intensity": [],
            "Maximum": [],
            "Mean": [],
            "Median": [],
            "Minimum": [],
            "Quartile, first": [],
            "Quartile, third": [],
            "Standard deviation": [],
        }
    },
    "Location": {
        "Object neighborhood": {
            "1-closest": [],
            "2-closest": [],
            "3-closest": [],
            "Neighbors": [],
            "Touching": [],
        }
    },
    "Shape": {
        "Image": {
            "Area": [],
        },
        "Image skeleton": {
            "Branches": [],
            "Endpoints": [],
            "Length": [],
            "Trunks": [],
        },
        "Object": {
            "Area": [],
            "Bounding box area": [],
            "Bounding box": [],
            "Central_moment": [],
            "Centroid": [],
            "Compactness": [],
            "Eccentricity": [],
            "Equivalent diameter": [],
            "Euler number": [],
            "Extent": [],
            "Form factor": [],
            "Hu moment": [],
            "Inertia tensor": [],
            "Inertia tensor eigenvalues": [],
            "Major axis length": [],
            "Maximum feret diameter": [],
            "Maximum radius": [],
            "Mean radius": [],
            "Median radius": [],
            "Minimum feret diameter": [],
            "Minor axis length": [],
            "Normalized moment": [],
            "Orientation": [],
            "Perimeter": [],
            "Solidity": [],
            "Spatial moment": [],
            "Surface area": [],
        },
        "Object skeleton": {
            "Branches": [],
            "Endpoints": [],
            "Length": [],
            "Trunks": [],
        }
    },
    "Texture": {
        "Object": {
            "Haralick": [],
        }
    }
}


class FeatureSelectionWidget(qtpy.QtWidgets.QWidget):
    def __init__(
            self,
            flags: typing.Union[qtpy.QtCore.Qt.WindowFlags, qtpy.QtCore.Qt.WindowType] = qtpy.QtCore.Qt.WindowFlags(),
    ):
        super(FeatureSelectionWidget, self).__init__(flags=flags)

        grid_layout = qtpy.QtWidgets.QGridLayout()

        self.setLayout(grid_layout)

        tree_widget = qtpy.QtWidgets.QTreeWidget()

        for descriptor in FEATURES.keys():
            parent = qtpy.QtWidgets.QTreeWidgetItem(tree_widget)

            parent.setText(0, descriptor)

            parent.setFlags(parent.flags() | qtpy.QtCore.Qt.ItemIsTristate | qtpy.QtCore.Qt.ItemIsUserCheckable)

            for name in FEATURES[descriptor]:
                child = qtpy.QtWidgets.QTreeWidgetItem(parent)

                child.setText(0, name)

                child.setFlags(child.flags() | qtpy.QtCore.Qt.ItemIsTristate | qtpy.QtCore.Qt.ItemIsUserCheckable)

                for feature in FEATURES[descriptor][name].keys():
                    grandchild = qtpy.QtWidgets.QTreeWidgetItem(child)

                    grandchild.setFlags(grandchild.flags() | qtpy.QtCore.Qt.ItemIsUserCheckable)

                    grandchild.setText(0, feature)

                    grandchild.setCheckState(0, qtpy.QtCore.Qt.Unchecked)

        self.layout().addWidget(tree_widget)
