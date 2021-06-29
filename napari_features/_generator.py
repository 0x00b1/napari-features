import collections.abc
import functools
import typing

import numpy

V = typing.TypeVar("V")


def cache(wrapped):
    @functools.wraps(wrapped)
    def function(generator: "Generator"):
        name = wrapped.__name__

        if not (name in generator.cache):
            generator.cache[name] = wrapped(generator)

        return generator.cache[name]

    return function


class Generator(collections.abc.Iterator[V]):
    cache: dict[str, object] = {}

    images: dict[str, numpy.array] = {}

    objects: dict[str, numpy.array] = {}

    def __next__(self) -> V:
        pass
