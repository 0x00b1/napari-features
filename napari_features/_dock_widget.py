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

        # store data
        self.table = magicgui.widgets.Table()

        self.copy_button = qtpy.QtWidgets.QPushButton("Copy to clipboard")

        # operations on data
        @self.copy_button.clicked.connect
        def copy_trigger():
            self.table.to_dataframe().to_clipboard()

        self.save_button = qtpy.QtWidgets.QPushButton("Save as csv...")

        @self.save_button.clicked.connect
        def save_trigger():
            filename, _ = qtpy.QtWidgets.QFileDialog.getSaveFileName(self.save_button, "Save as csv...", ".", "*.csv")
            self.table.to_dataframe().to_csv(filename)

        # build GUI
        self.setLayout(qtpy.QtWidgets.QGridLayout())

        self.layout().addWidget(self.copy_button)
        self.layout().addWidget(self.save_button)
        self.layout().addWidget(self.table.native)

