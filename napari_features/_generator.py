import collections.abc
import itertools
import typing

import numpy

V = typing.TypeVar("V")


class Generator(collections.abc.Iterator):
    cache = {}

    def __init__(
            self,
            images: typing.Optional[typing.Dict[str, numpy.array]] = None,
            masks: typing.Optional[typing.Dict[str, numpy.array]] = None
    ):
        if images is None:
            self.images = {}

        if masks is None:
            self.masks = {}

        self.index = 0

    def __next__(self):
        self.product.__next__()

    @property
    def n(self):
        return len([*self.product])

    @property
    def product(self):
        return itertools.product([*self.images.keys()], [*self.masks.keys()])


if __name__ == '__main__':
    generator = Generator()

    generator.images["a"] = numpy.zeros((224, 224, 3), numpy.uint8)
    generator.images["b"] = numpy.zeros((224, 224, 3), numpy.uint8)
    generator.images["c"] = numpy.zeros((224, 224, 3), numpy.uint8)

    generator.masks["x"] = numpy.zeros((224, 224, 3), numpy.uint8)
    generator.masks["y"] = numpy.zeros((224, 224, 3), numpy.uint8)
    generator.masks["z"] = numpy.zeros((224, 224, 3), numpy.uint8)

    for a, b in generator:
        print(a, b)

