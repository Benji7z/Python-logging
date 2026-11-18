from datetime import datetime

VERSION = "0.0.3"

DEFAULT_FORMAT = "%Y-%m-%d %H:%M:%S"
_format = DEFAULT_FORMAT


class config:
    @staticmethod
    def setFormat(user_format):
        global _format
        _format = user_format


def get_timestamp():
    return datetime.now().astimezone().strftime(_format)


class Log:
    @staticmethod
    def init(filename):
        return LogFile(filename)


class LogFile:
    def __init__(self, filename):
        self.filename = filename
        self._f = open(filename, "a", encoding="utf-8", buffering=1) # thanks random stranger who suggested that. I don't appreicate you critisizing my code.

    def clean(self):
        self._f.truncate(0)

    def close(self):
        if not self._f.closed:
            self._f.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()

    def _append(self, level, message):
        self._f.write(f"[{level}] [{get_timestamp()}] {message}\n")

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
    with Log.init("example.log") as log:
        log.info("This is an example.")
    print(f"Created example.log (logger v{VERSION})")