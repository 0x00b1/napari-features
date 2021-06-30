import collections.abc
import typing

import numpy

V = typing.TypeVar("V")


class Generator(collections.abc.Iterator[V]):
    cache: dict[str, object] = {}

    images: dict[str, numpy.array] = {}

    objects: dict[str, numpy.array] = {}

    def __next__(self) -> V:
        pass
