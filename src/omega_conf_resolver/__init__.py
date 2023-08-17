import inspect
import sys
import importlib
from omegaconf import OmegaConf
from .omega_conf_resolver import OmegaConfResolver

for name, obj in inspect.getmembers(
    sys.modules["omega_conf_resolver.omega_conf_resolver"]
):
    if (
        inspect.isclass(obj)
        and issubclass(obj, OmegaConfResolver)
        and not inspect.isabstract(obj)
    ):
        OmegaConf.register_new_resolver(name, obj())

        # importlib.import_module(name, package="omega_conf_resolver.omega_conf_resolver")
