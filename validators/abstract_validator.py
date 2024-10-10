from abc import ABC
from typing import Any


class BaseValidator(ABC):
    name: str

    def validate(self, value: Any) -> None:
        raise NotImplementedError
