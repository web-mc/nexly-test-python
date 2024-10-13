from validators import VALIDATORS
from exctractors import PdfExctarctor


def scan_pdf(args: dict) -> None:
    """
    Main function to scan PDF files.
    """

    pdf_file = PdfExctarctor()

    for validator_name, value_to_check in args.items():
        if not value_to_check:
            continue

        match validator_name:
            case "company_name":
                name_from_pdf = pdf_file.get_company_name()
                validator = VALIDATORS[validator_name](name_from_pdf)
                validator.validate(value_to_check)

            case "date":
                date_from_pdf = pdf_file.get_report_date()
                validator = VALIDATORS[validator_name](date_from_pdf)
                validator.validate(value_to_check)
