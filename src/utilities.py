from datetime import datetime
from pathlib import Path
from config import OUTPUT_PATH


def get_filename():
    now = datetime.now()
    scan_datetime = now.strftime("%d-%m-%Y-%H:%M")
    return f"{scan_datetime}-scan.txt"


def get_output_path(filename):
    return Path(OUTPUT_PATH) / filename


def save_to_file(filepath, contents):
    Path(filepath).parent.mkdir(exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(contents)


def save_log(contents):
    path = get_output_path(get_filename())
    save_to_file(path, contents)

