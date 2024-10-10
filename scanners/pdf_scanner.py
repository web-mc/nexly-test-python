from validators import VALIDATORS
from exctractors import PdfExctarctor
from exctractors.utils import get_pdf_file_to_scan


def scan_pdf(args: dict) -> None:
    """
    Main function to scan PDF files.
    """
    pdf_file = get_pdf_file_to_scan()
    if not pdf_file:
        return

    pdf = PdfExctarctor(pdf_file)
    for validator_name, value_to_check in args.items():
        if not value_to_check:
            continue

        match validator_name:
            case "company_name":
                company_name = pdf.get_company_name()
                validator = VALIDATORS[validator_name](company_name)
                validator.validate(value_to_check)

            case "date":
                report_date = pdf.get_report_date()
                validator = VALIDATORS[validator_name](report_date)
                validator.validate(value_to_check)
