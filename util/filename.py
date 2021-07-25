from datetime import datetime


def filename(count: int = 0):
    base = f"output-{datetime.now().day}-{datetime.now().month}-{datetime.now().year}"
    if count != 0:
        return base + f" ({count})"
    else:
        return base
