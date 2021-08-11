import json
import typing

import napari_features
import pkg_resources
import qtpy.QtWidgets
import qtpy.QtCore

from napari_features._tree_widget_item import TreeWidgetItem

resource_filename = pkg_resources.resource_filename(napari_features.__name__, "./data/translations/en.json")

with open(resource_filename, "r") as fp:
    FEATURES = json.load(fp)


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

            if item.checked:
                grandparent = item.parent().parent().text(0)

                parent = item.parent().text(0)

                self.features = self.features.union(FEATURES[grandparent][parent][item.text(0)])

                print(self.features)
