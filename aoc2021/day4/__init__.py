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


def has_won(board) -> bool:
    if any(np.sum(board, axis=0) == 0):
        return True
    elif any(np.sum(board, axis=1) == 0):
        return True
    else:
        return False


def find_winner(boards):
    for board in boards:
        if has_won(board):
            return board
    return None


def find_last(boards):
    unfinished = []
    for board in boards:
        if not has_won(board):
            unfinished.append(board)
    if len(unfinished) == 1:
        return unfinished[0]
    else:
        return None


def bingo(data: list, last_wins: bool = False) -> tuple:
    numbers, boards = parse(data)
    winner = None
    for number in numbers:
        boards = process(boards, number)
        if not last_wins:
            winner = find_winner(boards)
            if winner is not None:
                break
        else:
            if winner is None:
                winner = find_last(boards)
            else:
                winner = process(winner, number)
                if has_won(winner):
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
        return score(*bingo(data, last_wins=True))
    else:
        raise NotImplementedError
