import hydra
from omegaconf import OmegaConf

import omega_conf_resolver

@hydra.main(config_path="config", config_name="config")
def main(cfg):
    cfg = OmegaConf.to_object(cfg)
    print(cfg)


if __name__ == '__main__':
    main()