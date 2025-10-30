from omegaconf import OmegaConf, ListConfig, DictConfig
from abc import ABC, abstractmethod

from omegaconf.errors import InterpolationResolutionError


class OmegaConfResolver(ABC):
    @abstractmethod
    def __str__(self):
        return "OmegaConfResolver"

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass


class length(OmegaConfResolver):
    def __str__(self):
        return "length"

    def __call__(self, x, *, _parent_, _root_):
        if isinstance(x, (list, tuple, dict, ListConfig, DictConfig)):
            return len(x)
        raise TypeError(f"len() not supported for type {type(x)}")


class array(OmegaConfResolver):
    def __str__(self):
        return "array"

    def __call__(self, x, *, _parent_, _root_):
        import numpy

        return numpy.asarray(x)


class mult(OmegaConfResolver):
    def __str__(self):
        return "mult"

    def __call__(self, x, y, *, _parent_, _root_):
        return x * y


class div(OmegaConfResolver):
    def __str__(self):
        return "div"

    def __call__(self, x, y, *, _parent_, _root_):
        return x / y


class intdiv(OmegaConfResolver):
    def __str__(self):
        return "intdiv"

    def __call__(self, x, y, *, _parent_, _root_):
        return x // y


class if_cond(OmegaConfResolver):
    def __str__(self):
        return "if_cond"

    def __call__(self, cond, x, y, *, _parent_, _root_):
        if cond:
            return x
        else:
            return y


class add(OmegaConfResolver):
    def __str__(self):
        return "add"

    def __call__(self, x, y, *, _parent_, _root_):
        return x + y


class sub(OmegaConfResolver):
    def __str__(self):
        return "sub"

    def __call__(self, x, y, *, _parent_, _root_):
        return x - y


class path_join(OmegaConfResolver):
    def __init__(self):
        import os

        super().__init__()
        self.joinmethod = os.path.join

    def __str__(self):
        return "path_join"

    def __call__(self, *args, _parent_, _root_):
        return self.joinmethod(*args)


class condition(OmegaConfResolver):
    def __str__(self):
        return "condition"

    def __call__(self, condition, a, b, *, _parent_, _root_):
        if condition == "eq":
            return a == b
        elif condition == "ne":
            return a != b
        elif condition == "lt":
            return a < b
        elif condition == "le":
            return a <= b
        elif condition == "gt":
            return a > b
        elif condition == "ge":
            return a >= b
        else:
            raise ValueError(f"Unknown condition: {condition}")


class math(OmegaConfResolver):
    def __init__(self):
        super().__init__()
        self._known_ops = {
            "pi",
            "sqrt",
            "log",
            "exp",
            "sin",
            "cos",
            "tan",
            "rad2deg",
            "deg2rad",
            "pow",
        }

    def __str__(self):
        return "math"

    def __call__(self, operation, x=None, y=None, *, _parent_, _root_):
        import math

        if operation not in self._known_ops:
            raise InterpolationResolutionError(
                ValueError(f"Unknown math operation: {operation}")
            )
        # constant ops
        if operation == "pi":
            return math.pi
        # unary ops
        if x is None:
            raise InterpolationResolutionError(
                ValueError(f"math op {operation} requires argument x")
            )
        if operation == "sqrt":
            return math.sqrt(x)
        if operation == "log":
            return math.log(x)
        if operation == "exp":
            return math.exp(x)
        if operation == "sin":
            return math.sin(x)
        if operation == "cos":
            return math.cos(x)
        if operation == "tan":
            return math.tan(x)
        if operation == "rad2deg":
            return x * 180.0 / math.pi
        if operation == "deg2rad":
            return x * math.pi / 180.0
        # binary ops
        if y is None:
            raise InterpolationResolutionError(
                ValueError(f"math op {operation} requires argument y")
            )
        if operation == "pow":
            return math.pow(x, y)
        raise InterpolationResolutionError(
            ValueError(f"Unknown math operation: {operation}")
        )
