import napari.layers
import napari.types
import napari.utils.events
import napari_plugin_engine
import pandas

from ._dock_widget import DockWidget


def features(viewer: napari.Viewer):
    data = pandas.DataFrame(columns=["image", "masks"])

    dock_widget = DockWidget()

    @viewer.layers.events.connect
    def generate(event: napari.utils.events.event.Event):
        if event.type not in {"changed", "inserted", "removed"}:
            return

        source = event.source[0]

        if isinstance(source, napari.layers.Image):
            data.loc[len(data.index)] = ["image.png", "masks.png"]

        if isinstance(source, napari.layers.Labels):
            data.loc[len(data.index)] = ["image.png", "masks.png"]

        dock_widget.table.value = data

    viewer.window.add_dock_widget(dock_widget, area="bottom")


@napari_plugin_engine.napari_hook_implementation
def napari_experimental_provide_function():
    return [features]
