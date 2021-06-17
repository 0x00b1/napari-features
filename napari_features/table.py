import magicgui.widgets
import napari
import napari_plugin_engine
import napari.layers
import pandas
import qtpy.QtWidgets

from .generator import Generator


class Widget(qtpy.QtWidgets.QWidget):
    def __init__(self, napari_viewer: napari.Viewer):
        self.viewer = napari_viewer

        images = []

        for layer in self.viewer.layers:
            if isinstance(layer, napari.layers.Image):
                images.append(layer)

        if images:
            self.image = images[0]
        else:
            return

        labels = []

        for layer in self.viewer.layers:
            if isinstance(layer, napari.layers.Labels):
                labels.append(layer)

        if labels:
            self.labels = labels[0]
        else:
            return

        generator = Generator(self.image.data, self.labels.data)

        data = [generated for generated in generator]

        data = pandas.DataFrame(data, columns=generator.names)

        super().__init__()

        self.setWindowTitle("Features")

        table = magicgui.widgets.Table(value=data.to_dict("list"))

        layout = qtpy.QtWidgets.QGridLayout()

        layout.addWidget(table.native)

        self.setLayout(layout)


@napari_plugin_engine.napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return Widget
