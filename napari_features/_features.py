import napari.layers
import napari.utils.events
import napari_plugin_engine
import pandas

from ._dock_widget import DockWidget
from .generator import Generator


def features(
        image: napari.layers.Image,
        masks: napari.layers.Labels,
        viewer: napari.Viewer
):
    dock_widget = DockWidget()

    viewer.window.add_dock_widget(dock_widget, area="bottom")

    generator = Generator(masks.data, image.data)

    data = pandas.DataFrame([feature for feature in generator], columns=generator.columns)

    data["image_name"] = image.name
    data["image_path"] = image.source.path

    data["masks_name"] = image.name
    data["masks_path"] = image.source.path

    dock_widget.table.value = data


@napari_plugin_engine.napari_hook_implementation
def napari_experimental_provide_function():
    return [features]
