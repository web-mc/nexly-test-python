from pathlib import Path
from logging import DEBUG, INFO
from logging import getLogger


from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv(override=True)

logger = getLogger()


class AppSettings(BaseSettings):
    debug: bool = True
    app_dir: Path = Path(__file__).parents[1]


app_config = AppSettings()
logger.debug(f"App config: {app_config}")


class LogCongfig(BaseSettings):
    log_dir: Path = app_config.app_dir / "logs"
    log_level: int = DEBUG if app_config.debug else INFO

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.log_dir.mkdir(exist_ok=True, parents=True)


log_settings = LogCongfig()
logger.debug(f"Log config: {app_config}")
