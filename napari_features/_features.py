import napari.layers
import napari.types
import napari.utils.events
import napari_plugin_engine
import pandas

from ._dock_widget import DockWidget

COLUMNS = [
    "name",
    "path",
]


def features(viewer: napari.Viewer):
    dock_widget = DockWidget()

    viewer.window.add_dock_widget(dock_widget, area="bottom")

    data = pandas.DataFrame(columns=COLUMNS)

    data.set_index("name", inplace=True)

    for layer in viewer.layers:
        if isinstance(layer, napari.layers.Image):
            data.loc[layer.name] = [layer.source.path]

            dock_widget.table.value = data

    @viewer.layers.events.connect
    def insert(event: napari.utils.events.event.Event):
        if event.type != "inserted":
            return

        event_source = event.source[-1]

        if isinstance(event_source, napari.layers.Image):
            data.loc[event_source.name] = [event_source.source.path]

            dock_widget.table.value = data

    @viewer.layers.events.connect
    def remove(event: napari.utils.events.event.Event):
        if event.type != "removing":
            return

        event_source = event.source[-1]

        if isinstance(event_source, napari.layers.Image):
            try:
                data.drop(event_source.name, inplace=True)

                dock_widget.table.value = data
            except KeyError:
                pass


@napari_plugin_engine.napari_hook_implementation
def napari_experimental_provide_function():
    return [features]
