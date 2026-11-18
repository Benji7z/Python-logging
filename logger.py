
from datetime import datetime, timezone


DEFAULT_FORMAT = "%Y-%m-%d %H:%M:%S"
VERSION = "0.0.2"


class config:
    @staticmethod
    def setFormat(user_format):
        global DEFAULT_FORMAT
        DEFAULT_FORMAT = user_format


def get_timestamp():
    return datetime.now().astimezone().strftime(DEFAULT_FORMAT)


class Log:
    @staticmethod
    def init(filename):
        return LogFile(filename)


class LogFile:
    def __init__(self, filename):
        self.filename = filename

    def clean(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            pass

    def _append(self, level, message):
        timestamp = get_timestamp()

        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"[{level}] [{timestamp}] {message}\n")

    def info(self, message):
        self._append("INFO", message)

    def warning(self, message):
        self._append("WARNING", message)

    def error(self, message):
        self._append("ERROR", message)

    def debug(self, message):
        self._append("DEBUG", message)

    def critical(self, message):
        self._append("CRITICAL", message)


if __name__ == "__main__":
    log = Log.init("example.log")
    log.info("This is an example.")
    print(f"Created example.log (logger v{VERSION})")
