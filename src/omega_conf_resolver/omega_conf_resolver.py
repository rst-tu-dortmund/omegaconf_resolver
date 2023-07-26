from omegaconf import OmegaConf
from abc import ABC, abstractmethod


class OmegaConfResolver(ABC):
    @abstractmethod
    def __str__(self):
        return "OmegaConfResolver"

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass


class mult(OmegaConfResolver):
    def __str__(self):
        return "mult"

    def __call__(self, x, y, *, _parent_, _root_):
        if isinstance(x, str):
            x_loc = OmegaConf.select(_parent_, x)
            if x_loc is None:
                x = OmegaConf.select(_root_, x)
            else:
                x = x_loc

        if isinstance(y, str):
            y_loc = OmegaConf.select(_parent_, y)
            if y_loc is None:
                y = OmegaConf.select(_root_, y)
            else:
                y = y_loc

        return x * y


class div(OmegaConfResolver):
    def __str__(self):
        return "div"

    def __call__(self, x, y, *, _parent_, _root_):
        if isinstance(x, str):
            x_loc = OmegaConf.select(_parent_, x)
            if x_loc is None:
                x = OmegaConf.select(_root_, x)
            else:
                x = x_loc

        if isinstance(y, str):
            y_loc = OmegaConf.select(_parent_, y)
            if y_loc is None:
                y = OmegaConf.select(_root_, y)
            else:
                y = y_loc

        return x / y


class intdiv(OmegaConfResolver):
    def __str__(self):
        return "intdiv"

    def __call__(self, x, y, *, _parent_, _root_):
        if isinstance(x, str):
            x_loc = OmegaConf.select(_parent_, x)
            if x_loc is None:
                x = OmegaConf.select(_root_, x)
            else:
                x = x_loc

        if isinstance(y, str):
            y_loc = OmegaConf.select(_parent_, y)
            if y_loc is None:
                y = OmegaConf.select(_root_, y)
            else:
                y = y_loc

        return x // y


class add(OmegaConfResolver):
    def __str__(self):
        return "add"

    def __call__(self, x, y, *, _parent_, _root_):
        if isinstance(x, str):
            x_loc = OmegaConf.select(_parent_, x)
            if x_loc is None:
                x = OmegaConf.select(_root_, x)
            else:
                x = x_loc

        if isinstance(y, str):
            y_loc = OmegaConf.select(_parent_, y)
            if y_loc is None:
                y = OmegaConf.select(_root_, y)
            else:
                y = y_loc

        return x + y