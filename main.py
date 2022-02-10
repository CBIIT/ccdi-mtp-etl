# Custom modules
import logging.config

# Custom modules
import modules.RMTL as rmtl
import modules.PedCanDataNav as nav
import modules.cfg as cfg
from modules.YAMLReader import YAMLReader

logger = logging.getLogger(__name__)


def execution(step, config):
    if(step == "rmtl"):
        rmtl.run(config)
    if(step == "ped-can-data-nav"):
        nav.run(config)
    else:
        logger.error("Unknown step: %s", step)


def main():
    cfg.setBasicConfigLog()
    cfg.setup_parser()
    args = cfg.get_args()
    yaml = YAMLReader(args.config)
    yaml_dict = yaml.read_yaml()
    for step in yaml_dict.steps:
        logger.info("Request to run step: %s", step)
        if(yaml_dict[step] is None):
            logger.info("No configuration settings for  %s", step)
            execution(step)
        else:
            execution(step, yaml_dict[step])


if __name__ == '__main__':
    main()
