import pathlib

PACKAGE_DIR = pathlib.Path(__file__).parent.parent


def read_data(path: str) -> list:
    with open(path, "r") as f:
        # advent-of-code-data will download files that end with a newline
        # so we have to make sure that there aren't any empty strings
        return [line for line in f.read().split("\n") if line]


def convert_strbits_to_dec(bits: str) -> int:
    return int("".join(map(str, bits)), 2)
