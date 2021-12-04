"""https://adventofcode.com/2021/day/4"""

import numpy as np

BOARD_DIMS = 5


def parse_board(data: list) -> np.array:
    nbrs = [[int(x) for x in line.split()] for line in data]
    mtrx = np.array(nbrs)
    return mtrx


def parse(data: list) -> tuple:
    numbers = [int(x) for x in data[0].split(",")]
    boards = [
        parse_board(data[1 + BOARD_DIMS * idx : 1 + BOARD_DIMS + BOARD_DIMS * idx])
        for idx, _ in enumerate(data[1::BOARD_DIMS])
    ]
    return numbers, boards


def process(boards, number) -> list:
    return [np.where(board == number, 0, board) for board in boards]


def find_winner(boards):
    for board in boards:
        if any(np.sum(board, axis=0) == 0):
            return board
        elif any(np.sum(board, axis=1) == 0):
            return board
    return None


def bingo(data: list) -> tuple:
    numbers, boards = parse(data)
    for number in numbers:
        if number == 0:
            continue
        boards = process(boards, number)
        winner = find_winner(boards)
        if winner is not None:
            break
    else:
        raise RuntimeError
    return number, winner


def score(number, board) -> int:
    return np.sum(board) * number


def solve(part: int, data: list) -> int:
    if part == 1:
        return score(*bingo(data))
    elif part == 2:
        raise NotImplementedError
    else:
        raise NotImplementedError
