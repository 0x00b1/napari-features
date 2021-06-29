import magicgui.widgets
import napari.layers
import napari.types
import napari.utils.events
import napari_plugin_engine
import qtpy.QtWidgets

from ._generator import Generator


def features(viewer: napari.Viewer):
    generator = Generator()

    @viewer.layers.events.connect
    def generate(event: napari.utils.events.event.Event):
        if event.type not in {"changed", "inserted", "removed"}:
            return

        source = event.source[0]

        if isinstance(source, napari.layers.Image):
            generator.images[source.source] = source.data

        if isinstance(source, napari.layers.Labels):
            generator.objects[source.source] = source.data

    dock_widget = qtpy.QtWidgets.QWidget()

    dock_widget.setWindowTitle("Features")

    table = magicgui.widgets.Table([[0.0] * 16, [0.0] * 16])

    dock_widget.setLayout(qtpy.QtWidgets.QGridLayout())

    dock_widget.layout().addWidget(table.native)

    viewer.window.add_dock_widget(dock_widget, area="bottom")


@napari_plugin_engine.napari_hook_implementation
def napari_experimental_provide_function():
    return [features]
