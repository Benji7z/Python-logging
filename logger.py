
from datetime import datetime

defaultFormat = "%Y-%m-%d %H:%M:%S"
Format = defaultFormat


class config:
    @staticmethod
    def setFormat(userFormat):
        global Format

        try:
            datetime.now().strftime(userFormat)
            Format = userFormat
        except (ValueError, TypeError) as e:
            print(f"[ERROR] Invalid datetime format '{userFormat}': {e}")
            Format = defaultFormat


def get_timestamp():
    return datetime.now().strftime(Format)


class Log:
    @staticmethod
    def init(filename):
        return LogFile(filename)


class LogFile:
    def __init__(self, filename):
        self.filename = filename

    def clean(self):
        with open(self.filename, "w"):
            pass

    def info(self, message):
        self._append("INFO", message)

    def error(self, message):
        self._append("ERROR", message)

    def warning(self, message):
        self._append("WARNING", message)

    def _append(self, level, message):
        with open(self.filename, "a") as f:
            f.write(f"[{level}] [{get_timestamp()}] {message}\n")


if __name__ == "__main__":
    Log.init("example.log").info("This is an example.")
    print("Created example.log")
else:
    print("[INFO] Using logger.py v0.0.1")
