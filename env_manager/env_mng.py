from dotenv import dotenv_values
from pathlib import Path


class EnvironmentManager:
    def __init__(self) -> None:
        self.dotenv_values = None
        self.env_path = None

        self._url1 = None
        self._url2 = None
        self._url3 = None

    def set_env(self, filepath: str):
        self.env_path = Path(filepath)
        if not self.env_path.exists():
            raise RuntimeError(
                f'File "{self.env_path}" not exists. Please provide other path'
            )
        self.dotenv_values = dotenv_values(self.env_path)

    @property
    def url1(self):
        url1 = self.dotenv_values.get("URL1")

        if url1 is None:
            raise RuntimeError(f'"URL1" not specified in "{self.env_path}" file')

        if self._url1 is None:
            self._url1 = url1

        return self._url1

    @property
    def url2(self):
        url2 = self.dotenv_values.get("URL2")

        if url2 is None:
            raise RuntimeError(f'"URL2" not specified in "{self.env_path}" file')

        if self._url2 is None:
            self._url2 = url2

        return self._url2

    @property
    def url3(self):
        url3 = self.dotenv_values.get("URL3")

        if url3 is None:
            raise RuntimeError(f'"URL3" not specified in "{self.env_path}" file')

        if self._url3 is None:
            self._url3 = url3

        return self._url3