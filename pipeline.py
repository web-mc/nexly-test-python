from logging import getLogger
from logging.config import dictConfig

from config.log import LOGGERS

from scanners.pdf_scanner import scan_pdf
from utils.arg_parser import parse_args_to_validate


def main() -> None:
    logger.info("Scan pipeline started.")

    args = parse_args_to_validate()
    if not args:
        return

    scan_pdf(args)

    logger.info("Scan pipeline finished successfully.")


if __name__ == "__main__":
    dictConfig(LOGGERS)
    logger = getLogger()

    try:
        main()
    except Exception as e:
        logger.info(f"Scan pipeline finished with error: {e}.")
        logger.exception(e)
