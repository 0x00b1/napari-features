import magicgui.widgets
import napari_plugin_engine
import qtpy.QtWidgets


class Table(qtpy.QtWidgets.QWidget):
    def __init__(self, napari_viewer):
        super(Table, self).__init__()

        self.data = {
            "col1": ["1", "2", "3", "4"],
            "col2": ["1", "2", "1", "3"],
            "col3": ["1", "1", "2", "1"]
        }

        table = magicgui.widgets.Table(value=self.data)

        self.setWindowTitle("Features")

        self.setLayout(qtpy.QtWidgets.QGridLayout())

        self.layout().addWidget(table.native)


@napari_plugin_engine.napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return Table
