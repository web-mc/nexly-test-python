from datetime import date
from logging import getLogger

from .abstract_validator import BaseValidator


logger = getLogger()


class DateValidator(BaseValidator):
    name: str = "Date"

    def __init__(self, date_from_source) -> None:
        self.date_from_source = date_from_source

    def validate(self, date_to_check: date) -> None:
        if date_to_check == self.date_from_source:
            logger.info(f"{self.name} validation passed.")
            return
        else:
            msg = (
                f'{self.name} validation failed: expected "{date_to_check}", '
                f'found "{self.date_from_source}".'
            )
            logger.info(msg)
