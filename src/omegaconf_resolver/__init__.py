import inspect
import sys
import importlib
from omegaconf import OmegaConf
from omegaconf_resolver.omegaconf_resolver import OmegaConfResolver


def register():
    for name, obj in inspect.getmembers(
        sys.modules["omegaconf_resolver.omegaconf_resolver"]
    ):
        if (
            inspect.isclass(obj)
            and issubclass(obj, OmegaConfResolver)
            and not inspect.isabstract(obj)
        ):
            OmegaConf.register_new_resolver(name, obj())

            # importlib.import_module(name, package="omega_conf_resolver.omega_conf_resolver")
