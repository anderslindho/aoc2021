"""https://adventofcode.com/2021/day/4"""

from typing import List, Tuple

import numpy as np

BOARD_DIMS = 5

Board = np.array
Boards = List[np.array]
Order = List[int]


def parse_data(data: list) -> Tuple[Order, Boards]:
    numbers = [int(x) for x in data[0].split(",")]
    boards = np.loadtxt(data[1:], int).reshape(-1, 5, 5)
    return numbers, boards


def mark_number(boards: Boards, number: int) -> Boards:
    return [np.where(board == number, 0, board) for board in boards]


def has_won(board: Board) -> bool:
    return any(np.sum(board, axis=0) == 0) or any(np.sum(board, axis=1) == 0)


def find_first_winner(boards: Boards) -> int:
    for idx, board in enumerate(boards):
        if has_won(board):
            return idx
    return None


def bingo(numbers: Order, boards: Boards, last_wins: bool = False) -> Tuple[int, Board]:
    winners = []
    for number in numbers:
        boards = mark_number(boards, number)
        finished = find_first_winner(boards)
        if finished is not None:
            # why aren't the boards removed ???
            winners.append((number, boards.pop(finished)))
        if not boards:
            break
    number, winner = winners[0] if not last_wins else winners[-1]
    return number, winner


def score(number: int, board: Board) -> int:
    return np.sum(board) * number


def solve(part: int, data: list) -> int:
    if part == 1:
        return score(*bingo(*parse_data(data)))
    elif part == 2:
        return score(*bingo(*parse_data(data), last_wins=True))
    else:
        raise NotImplementedError
