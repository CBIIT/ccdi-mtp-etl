#Custom modules
import logging.config

# Custom modules
import modules.RMTL as rmtl
import modules.cfg as cfg
from modules.YAMLReader import YAMLReader

logger = logging.getLogger(__name__)

def execution(step, config):
    if(step == "rmtl"):
        rmtl.run(config);


def main():
    cfg.setBasicConfigLog()
    cfg.setup_parser()
    args = cfg.get_args()
    yaml = YAMLReader(args.config)
    yaml_dict = yaml.read_yaml()
    for step in yaml_dict.steps:
        logger.info("Execution Steps: %s", step);

        if(yaml_dict[step] is None):
            logger.info()
        else:
            execution(step,yaml_dict[step])


if __name__ == '__main__':
    main()