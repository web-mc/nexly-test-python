from logging import getLogger
from logging.config import dictConfig

from config.log import LOGGERS
from config import app_config
from utils.arg_parser import parse_targets_to_validate

print(app_config)

def main() -> None:
    args = parse_targets_to_validate()
    if not args:
        logger.info("Nothing to validate.")
        return



if __name__ == "__main__":
    dictConfig(LOGGERS)
    logger = getLogger()
    logger.info("etl_pipeline started.")

    main()

    logger.info("etl_pipeline finished.")
