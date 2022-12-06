import argparse
from random import randrange
from typing import List


def rand_gen(start: int = 1, stop: int = 87, limit: int = 15) -> List[int]:
    """

    Args:
        start:(int): First numeric value of the range
        stop:(int): last numeric value of the range
        limit: (int): number of result to yield

    Returns:
        List(int): random value in range(start:stop) with count listed
        to "limit"

    """
    random = [randrange(start, stop+1) for _ in range(limit)]
    return random


if __name__ == "__main__":
    example = """example:
    
    python task.py --max 87 --any 15"""

    parser = argparse.ArgumentParser(
        description="CLI tool to fetch resources from API",
        epilog=example
    )
    parser.add_argument("-m",
                        "--max",
                        type=int,
                        default=87,
                        help="max number of resources to be fetched",
                        )
    parser.add_argument("-a",
                        "--any",
                        type=int,
                        default=15,
                        help="random  sized chunk of resources to be fetched",
                        )
    args = parser.parse_args()
    # print(args)
    # print(type(args))
    breakpoint()
    print(args.any)
    print(args.max)
    # print(parser.print_help())
    result = rand_gen(1, args.max, args.any)
    print(result)
    print()