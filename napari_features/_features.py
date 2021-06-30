import napari.layers
import napari.types
import napari.utils.events
import napari_plugin_engine
import pandas

from ._dock_widget import DockWidget

COLUMNS = [
    "id",
    "name",
    "path",
]


def features(viewer: napari.Viewer):
    dock_widget = DockWidget()

    viewer.window.add_dock_widget(dock_widget, area="bottom")

    data = pandas.DataFrame(columns=COLUMNS)

    data.set_index("id", inplace=True)

    @viewer.layers.events.connect
    def insert(event: napari.utils.events.event.Event):
        if event.type != "inserted":
            return

        for layer in viewer.layers:
            if isinstance(layer, napari.layers.Image):
                data.loc[id(layer)] = [layer.name, layer.source.path]

        dock_widget.table.value = data

    @viewer.layers.events.connect
    def remove(event: napari.utils.events.event.Event):
        if event.type != "removing":
            return

        source = event.source[0]

        if isinstance(source, napari.layers.Image):
            data.drop(id(source), inplace=True)

        dock_widget.table.value = data


@napari_plugin_engine.napari_hook_implementation
def napari_experimental_provide_function():
    return [features]
