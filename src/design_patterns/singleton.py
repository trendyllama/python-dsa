import os


class Configuration:
    def __new__(cls):
        if not hasattr(Configuration, "instance"):
            cls.instance = super().__new__(cls)

        return cls.instance

    @property
    def environment(self) -> str:
        out = os.getenv("ENVIRONMENT")

        if out is None:
            raise ValueError("ENVIRONMENT variable not set")

        return out


class ApplicationState:
    def __new__(cls):
        if not hasattr(ApplicationState, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance
