class PageSourceNotConfigured(Exception):

    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return "Page source isn't configured. %s" % self.message
