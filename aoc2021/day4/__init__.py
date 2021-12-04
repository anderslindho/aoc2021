"""https://adventofcode.com/2021/day/4"""

from typing import List, Tuple

import numpy as np

BOARD_DIMS = 5

Board = np.array
Boards = List[np.array]
Order = List[int]


def parse_data(data: list) -> Tuple[Order, Boards]:
    numbers = [int(x) for x in data[0].split(",")]
    boards = np.loadtxt(data[1:]).reshape(-1, 5, 5)
    return numbers, boards


def mark_number(boards: Boards, number: int) -> Boards:
    return [np.where(board == number, 0, board) for board in boards]


def has_won(board: Board) -> bool:
    return any(np.sum(board, axis=0) == 0) or any(np.sum(board, axis=1) == 0)


def find_first_winner(boards: Boards) -> Board:
    for board in boards:
        if has_won(board):
            return board
    return None


def find_last_unfinished(boards: Boards) -> Board:
    unfinished = []
    for board in boards:
        if not has_won(board):
            unfinished.append(board)
    if len(unfinished) == 1:
        return unfinished[0]
    else:
        return None


def bingo(numbers: Order, boards: Boards, last_wins: bool = False) -> Tuple[int, Board]:
    # TODO: Store the winners in a list instead and take either first or
    #       last elem depending of `last_wins`.
    #       If so, delete `find_last_unfinished`, and return idx in `find_first_winner` (to pop)
    winner = None
    for number in numbers:
        boards = mark_number(boards, number)
        if not last_wins:
            winner = find_first_winner(boards)
            if winner is not None:
                break
        else:
            if winner is None:
                winner = find_last_unfinished(boards)
            else:
                winner = mark_number(winner, number)
                if has_won(winner):
                    break
    else:
        raise RuntimeError
    return number, winner


def score(number: Order, board: Board) -> int:
    return np.sum(board) * number


def solve(part: int, data: list) -> int:
    if part == 1:
        return score(*bingo(*parse_data(data)))
    elif part == 2:
        return score(*bingo(*parse_data(data), last_wins=True))
    else:
        raise NotImplementedError
