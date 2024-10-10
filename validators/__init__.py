from .company_name import CompanyNameValidator
from .date_validator import DateValidator


VALIDATORS = {
    "company_name": CompanyNameValidator,
    "date": DateValidator,
}
