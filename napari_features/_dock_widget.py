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

        grid_layout = qtpy.QtWidgets.QGridLayout()

        self.setLayout(grid_layout)

        self.copy_button = qtpy.QtWidgets.QPushButton("Copy to clipboard")

        @self.copy_button.clicked.connect
        def on_copy():
            self.table.to_dataframe().to_clipboard()

        self.save_button = qtpy.QtWidgets.QPushButton("Save as csv...")

        self.layout().addWidget(self.copy_button)

        @self.save_button.clicked.connect
        def on_save():
            filename, _ = qtpy.QtWidgets.QFileDialog.getSaveFileName(self.save_button, "Save as csv...", ".", "*.csv")

            self.table.to_dataframe().to_csv(filename)

        self.layout().addWidget(self.save_button)

        self.table = magicgui.widgets.Table()

        self.layout().addWidget(self.table.native)
