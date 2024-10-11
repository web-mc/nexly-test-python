import re
from datetime import date
from logging import getLogger

from pypdf import PdfReader

from config import app_config
from .utils import MONTH_MAPPING


logger = getLogger()


class PdfExctarctor:
    def __init__(self) -> None:
        self.pdf = self._get_pdf_file_to_scan()

    def get_company_name(self) -> str:
        page = self.pdf.pages[0]
        page_text = page.extract_text()
        return page_text.split("\n")[0].strip()

    def get_report_date(self) -> None | date:
        # Находит во второй строке дату
        # регулярка привязана к тексту в шаблоне "for the year ended {month} {day}, {year}"

        # Можно добавить вариантов регулярок
        # и искать совпадения в цикле пока не найдём первое совпадение
        page = self.pdf.pages[0]
        page_text = page.extract_text()
        pattern = r"for\sthe\syear\sended\s(\w*)\s(.*)"

        regex_res = re.search(pattern, page_text)
        if not regex_res:
            logger.warning("Date. Check regex pattern.")
            return

        month = regex_res.group(1).strip().lower()
        month = MONTH_MAPPING[month]

        regex_date = regex_res.group(2).strip()
        day = regex_date.split(",")[0].strip()
        year = regex_date.split(",")[1].strip()

        return date.fromisoformat(f"{year}-{month}-{day}")

    def _get_pdf_file_to_scan(self) -> None | PdfReader:
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
