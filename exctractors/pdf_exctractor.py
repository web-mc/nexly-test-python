import re
from pathlib import Path
from datetime import date
from logging import getLogger

from pypdf import PdfReader

from .utils import MONTH_MAPPING


logger = getLogger()


class PdfExctarctor:
    def __init__(self, pdf_file: Path) -> None:
        self.pdf = PdfReader(pdf_file)
        self.total_pages = len(self.pdf.pages)

    def get_company_name(self) -> str:
        page = self.pdf.pages[0]
        page_text = page.extract_text()
        return page_text.split("\n")[0].strip()

    def get_report_date(self) -> None | date:
        # Находит во втрой строке дату
        # регулярка привязана к тексту в шаблоене "for the year ended {month} {day}, {year}"

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
