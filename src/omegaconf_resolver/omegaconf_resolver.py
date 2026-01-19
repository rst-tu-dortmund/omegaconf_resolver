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
        # skip none args
        args = [a for a in args if a is not None]
        
        if len(args) == 0:
            return ""
        
        if len(args) == 1:
            return args[0]
        
        return self.joinmethod(*args)
