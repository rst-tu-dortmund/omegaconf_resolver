# To be filled
# Install
run `pip install -e .` inside top-level directory of omega_conf_resolver. \
or run `pip install git+https://git.rst.e-technik.tu-dortmund.de/osterburg/omega_conf_resolver.git` \
To add a resolver, just add a class that inherits from OmegaConfResolver class in src/omega_conf_resolver/omega_conf_resolver.py \
To use the costum resolvers run:
`import omega_conf_resolver \
omega_conf_resolver.register()` \
before usage of hydra or omega conf.
