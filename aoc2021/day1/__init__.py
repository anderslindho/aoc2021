def count_increasing(numbers: list, smoothening: bool = False) -> int:
    if smoothening:
        numbers = [
            sum(int(x) for x in triplet)
            for triplet in zip(numbers, numbers[1:], numbers[2:])
        ]
    return sum(
        [
            1 if int(second) > int(first) else 0
            for first, second in zip(numbers, numbers[1:])
        ]
    )


def solve(part: int, data: list) -> int:
    if part == 1:
        return count_increasing(data)
    elif part == 2:
        return count_increasing(data, smoothening=True)
    else:
        raise NotImplementedError
