from abc import ABC
from typing import Any

from exctractors import PdfExctarctor


class BaseValidator(ABC):
    """
    name: Name of validator.
    page_number: The page from which need to get data for validation.
    """

    name: str

    def validate(self, value: Any) -> None:
        raise NotImplementedError
