from pathlib import Path
from logging import getLogger

from config import app_config


logger = getLogger()

MONTH_MAPPING = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}


def get_pdf_file_to_scan() -> None | Path:
    """
    Checks the folder, file and its format.
    If everything is OK, returns the path to the file.
    """

    scan_dir = app_config.app_dir / "report_to_scan"
    if not scan_dir.exists():
        logger.warning(f"Dir '{scan_dir}' doesn't exists.")
        return

    file_to_scan = scan_dir / "report.pdf"
    if not file_to_scan.exists():
        logger.warning(f"File '{file_to_scan}' doesn't exists.")
        return

    logger.debug("Found PDF to scan.")
    return file_to_scan
