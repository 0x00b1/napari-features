import typing

import napari.layers


def generate(image: napari.layers.Image) -> typing.Dict:
    features = {}

    if image.source.path:
        features["path"] = image.source.path

    return features
