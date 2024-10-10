import argparse
from typing import Any
from datetime import date
from logging import getLogger


logger = getLogger()


def validate_date(iso_date: str) -> None | date:
    if not iso_date:
        return

    try:
        date_arg = date.fromisoformat(iso_date)
        return date_arg
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"Date '{iso_date}' must be specified in ISO format 'YYYY-MM-DD'."
        )
    except Exception as e:
        logger.exception(e)
        raise


def parse_args_to_validate() -> None | dict[str, Any]:
    parser = argparse.ArgumentParser()
    parser.add_argument("--company_name", type=str, required=False)
    parser.add_argument("--date", type=validate_date, required=False)
    args = parser.parse_args().__dict__

    if not any(args.values()):
        logger.warning("Can't find targets to validate. Nothing to validate.")
        return

    logger.debug(f"Got args: {args}")
    return args
