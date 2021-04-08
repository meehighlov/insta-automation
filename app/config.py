import os

from dotenv import load_dotenv


load_dotenv()


cast_to = lambda type_: lambda *args, value: type_(value)


class Config:
    MAX_WAIT_ELEMENT_APPEARANCE_SEC = cast_to(int)
    CHROME_DRIVER_PATH = cast_to(str)

    INSTAGRAM_LOGIN = cast_to(str) # noqa
    INSTAGRAM_PASSWORD = cast_to(str)  # noqa
    INSTAGRAM_URL = cast_to(str)  # noqa

    def __init__(self, **kwargs):
        for var, raw_value in kwargs.items():
            if hasattr(self, var):
                value = getattr(self, var)(value=raw_value)
                setattr(self, var, value)


config = Config(**os.environ)