from omegaconf import OmegaConf, ListConfig, DictConfig
from abc import ABC, abstractmethod


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
        if isinstance(x, str):
            x_loc = OmegaConf.select(_parent_, x)
            if x_loc is None:
                x = OmegaConf.select(_root_, x)
            else:
                x = x_loc
        if isinstance(x, (list, tuple, dict, ListConfig, DictConfig)):
            return len(x)
        raise TypeError(f"len() not supported for type {type(x)}")

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


class if_cond(OmegaConfResolver):
    def __str__(self):
        return "if"
    
    def __call__(self, cond, x, y, *, _parent_, _root_):
        if isinstance(cond, str):
            cond_loc = OmegaConf.select(_parent_, cond)
            if cond_loc is None:
                cond = OmegaConf.select(_root_, cond)
            else:
                cond = cond_loc

        if cond:
            if isinstance(x, str):
                x_loc = OmegaConf.select(_parent_, x)
                if x_loc is None:
                    x = OmegaConf.select(_root_, x)
                else:
                    x = x_loc
            return x
        else:
            if isinstance(y, str):
                y_loc = OmegaConf.select(_parent_, y)
                if y_loc is None:
                    y = OmegaConf.select(_root_, y)
                else:
                    y = y_loc
            return y


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


class sub(OmegaConfResolver):
    def __str__(self):
        return "sub"

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

        return x - y