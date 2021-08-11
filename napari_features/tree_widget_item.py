import qtpy.QtCore
import qtpy.QtWidgets


class TreeWidgetItem(qtpy.QtWidgets.QTreeWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.check_state: qtpy.QtCore.Qt.CheckState = self.checkState(0)

    def setCheckState(self, state: qtpy.QtCore.Qt.CheckState, column: int = 0) -> None:
        if column == 0:
            self.check_state = state

        return super().setCheckState(column, state)
