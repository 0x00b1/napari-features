import magicgui.widgets
import napari.types
import napari_plugin_engine
import numpy
import pandas
import qtpy.QtWidgets
import skimage.color

from .generator import Generator


def featurize(x: napari.types.ImageData, y: napari.types.LabelsData, napari_viewer: napari.Viewer):
    if x.shape[-1] == 4:
        x = skimage.color.rgba2rgb(x)
        x = skimage.color.rgb2gray(x)

    generator = Generator(numpy.asarray(y).astype(int), numpy.asarray(x))

    data = pandas.DataFrame([generated for generated in generator], columns=generator.names)

    dock_widget = qtpy.QtWidgets.QWidget()

    dock_widget.setWindowTitle("Features")

    table = magicgui.widgets.Table(value=data.to_dict("list"))

    dock_widget.setLayout(qtpy.QtWidgets.QGridLayout())

    dock_widget.layout().addWidget(table.native)

    napari_viewer.window.add_dock_widget(dock_widget, area="bottom")


@napari_plugin_engine.napari_hook_implementation
def napari_experimental_provide_function():
    return [featurize]
