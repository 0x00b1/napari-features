import typing

import magicgui
import qtpy.QtWidgets
import qtpy.QtCore


class DockWidget(qtpy.QtWidgets.QWidget):
    def __init__(
        self,
        flags: typing.Union[qtpy.QtCore.Qt.WindowFlags, qtpy.QtCore.Qt.WindowType] = qtpy.QtCore.Qt.WindowFlags(),
    ):
        super(DockWidget, self).__init__(flags=flags)

        self.setWindowTitle("Features")

        self.table = magicgui.widgets.Table()

        self.setLayout(qtpy.QtWidgets.QGridLayout())

        self.layout().addWidget(self.table.native)
