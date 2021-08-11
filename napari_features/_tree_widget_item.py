import qtpy.QtCore
import qtpy.QtWidgets


class TreeWidgetItem(qtpy.QtWidgets.QTreeWidgetItem):
    def __init__(self, tree_widget_item: qtpy.QtWidgets.QTreeWidgetItem):
        super().__init__(tree_widget_item)

        self.check_state: qtpy.QtCore.Qt.CheckState = self.checkState(0)

    @property
    def checked(self):
        return self.check_state == qtpy.QtCore.Qt.Checked

    def setCheckState(self, column: int, state: qtpy.QtCore.Qt.CheckState) -> None:
        if column == 0:
            self.check_state = state

        return super().setCheckState(column, state)
