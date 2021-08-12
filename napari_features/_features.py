import napari.layers
import napari.utils.events
import napari_plugin_engine
import pandas

from ._dock_widget import DockWidget
from .generator import Generator
from ._feature_selection_widget import FeatureSelectionWidget


def features(
        image: napari.layers.Image,
        masks: napari.layers.Labels,
        viewer: napari.Viewer
):
    dock_widget = DockWidget()

    viewer.window.add_dock_widget(dock_widget, area="bottom")

    viewer.window.add_dock_widget(dock_widget)

    feature_selection_widget = FeatureSelectionWidget()

    viewer.window.add_dock_widget(feature_selection_widget)

    generator = Generator(masks.data, image.data, feature_selection_widget.selected)

    data = pandas.DataFrame([feature for feature in generator], columns=generator.columns)

    data["_feature_metadata_image_filename"] = image.source.path

    data["_feature_metadata_layer_name"] = masks.name

    masks.properties["features"] = data.to_dict()

    dock_widget.table.value = masks.properties["features"]


@napari_plugin_engine.napari_hook_implementation
def napari_experimental_provide_function():
    return [features]
