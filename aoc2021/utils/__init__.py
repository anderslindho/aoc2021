import pathlib

PACKAGE_DIR = pathlib.Path(__file__).parent.parent


def read_data(path: str) -> list:
    with open(path, "r") as f:
        return f.read().split("\n")


def convert_strbits_to_dec(bits: str) -> int:
    return int("".join(map(str, bits)), 2)
