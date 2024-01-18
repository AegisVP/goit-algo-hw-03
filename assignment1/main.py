import argparse
import shutil

from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', type=Path, help="directory to copy from", required=True)
    parser.add_argument('-d', '--dest', type=Path, help="directory to copy to", default=Path('dist'))
    return parser.parse_args()


def parse_directory(source: Path, dest: Path):
    for file in source.iterdir():
        if (file == dest):
            continue

        if (file.is_dir()):
            parse_directory(file, dest)
        else:
            process_file(file, dest)


def process_file(source: Path, dest: Path):
    extension = source.suffix[1:]
    dest_path = Path(f"{dest}/{extension}")

    if (Path(dest_path / source.name).exists()):
        print(f"File {dest_path}/{source.name} already exists, skipping")
        return

    if (not dest_path.exists()):
        dest_path.mkdir()

    shutil.copy(source, dest_path)
    print(f"{source} -> {dest}/{extension}/{source.name}")


if __name__ == "__main__":
    args = parse_args()
    if (args.source.exists()):
        args.dest.mkdir(exist_ok=True)
        parse_directory(args.source, args.dest)
    else:
        raise Exception(f"{args.source} does not exist")
