""""garbage sorter is sorted files in dir"""
import argparse
import logging
import shutil
from pathlib import Path
from shutil import copyfile
from threading import Thread

parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-s", help="Source folder", required=True)
parser.add_argument("--output", "-o", help="Output folder", default="sorted_folder")

args = vars(parser.parse_args())

source = Path(args.get("source"))
output = Path(args.get("output"))

folders = []


def grabs_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folder(el)


def copy_file(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            new_path = output / ext
            try:
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(el,new_path / el.name)
            except OSError as error:
                logging.error(error)


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR, format="%(threadName)s %(message)s")
    folders.append(source)
    grabs_folder(source)
    threads = []
    for folder in folders:
        th = Thread(target=copy_file, args=(folder,))
        th.start()
        threads.append(th)

    [th.join() for th in threads]

    is_delete_source_dir = input("Delete source dir? [y/n] ")

    if is_delete_source_dir.lower() == "y":
        shutil.rmtree(source)

        print("Source dir was deleted")

