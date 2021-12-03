
def read_data(path: str) -> list:
    with open(path, "r") as f:
        return f.read().split("\n")
