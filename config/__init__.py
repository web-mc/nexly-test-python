from pathlib import Path
from logging import DEBUG, INFO


from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv(override=True)


class AppSettings(BaseSettings):
    debug: bool = True
    app_dir: Path = Path(__file__).parents[1]


app_config = AppSettings()


class LogCongfig(BaseSettings):
    log_dir: Path = app_config.app_dir / "logs"
    log_level: int = DEBUG if app_config.debug else INFO

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.log_dir.mkdir(exist_ok=True, parents=True)


log_settings = LogCongfig()
