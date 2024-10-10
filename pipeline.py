from logging import getLogger
from logging.config import dictConfig

from config.log import LOGGERS
from utils.arg_parser import parse_targets_to_validate



def main() -> None:
    args = parse_targets_to_validate()
    if not args:
        logger.info("Nothing to validate.")
        return

    logger.info("Scan pipeline started.")


if __name__ == "__main__":
    dictConfig(LOGGERS)
    logger = getLogger()

    try:
        main()
        logger.info("Scan pipeline finished successfully.")
    except Exception as e:
        logger.info(f"Scan pipeline finished with error: {e}.")
