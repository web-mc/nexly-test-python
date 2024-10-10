from logging import getLogger

from .abstract_validator import BaseValidator


logger = getLogger()


class CompanyNameValidator(BaseValidator):
    name: str = "Company name"

    def __init__(self, name_from_source: str) -> None:
        self.name_from_source = name_from_source

    def validate(self, name_to_check: str) -> None:
        if self.name_from_source.lower() == name_to_check.strip().lower():
            logger.info(f"{self.name} validation passed.")
        else:
            msg = (
                f'{self.name} validation failed: expected "{name_to_check}", '
                f'found "{self.name_from_source}".'
            )
            logger.info(msg)
