import functools

from .generator import Generator


def cache(wrapped):
    @functools.wraps(wrapped)
    def function(generator: Generator):
        name = wrapped.__name__

        if not (name in generator.cache):
            generator.cache[name] = wrapped(generator)

        return generator.cache[name]

    return function
