import re
from logging import getLogger
from datetime import date, datetime

from pypdf import PdfReader

from config import app_config


logger = getLogger()


class PdfExctarctor:
    def __init__(self) -> None:
        self.pdf = self._get_pdf_file_to_scan()

    def get_company_name(self) -> str:
        page = self.pdf.pages[0]
        page_text = page.extract_text()
        return page_text.split("\n")[0].strip()

    def get_report_date(self) -> date:
        page = self.pdf.pages[0]
        page_text = page.extract_text()

        # регулярка привязана к тексту в шаблоне "for the year ended {month} {day}, {year}"
        # Можно добавить вариантов регулярок
        # и искать совпадения в цикле пока не найдём первое совпадение
        pattern = r"(\w+)\s+(\d{1,2}),\s+(\d+)"
        regex_res = re.search(pattern, page_text)
        if not regex_res:
            raise ValueError("Can't find the date. Check regex pattern.")

        month, day, year = regex_res.groups()
        result_date = datetime.strptime(f"{year}-{month}-{day}", "%Y-%B-%d")
        return result_date.date()

    def _get_pdf_file_to_scan(self) -> PdfReader:
        """
        Checks the folder, file and its format.
        If everything is OK, returns the path to the file.
        """

        scan_dir = app_config.app_dir / "report_to_scan"
        if not scan_dir.exists():
            raise FileNotFoundError(f"Dir '{scan_dir}' doesn't exists.")

        file_to_scan = scan_dir / "report.pdf"
        if not file_to_scan.exists():
            raise FileNotFoundError(f"File '{file_to_scan}' doesn't exists.")

        logger.debug("Found PDF to scan.")
        return PdfReader(file_to_scan)
