#!/usr/bin/python3
"""The prime game module"""


def isWinner(x, nums):
    """Determine the winner of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list of int): Array of n values for each round.
    Returns:
        str: Name of the player that won the most rounds,
        or None if it's a tie.
    """
    def checkPrime(n):
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
            if prime[p]:
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        return prime

    def play(n):
        primes = checkPrime(n)
        return sum(primes[2:]) % 2 == 1

    Maria = Ben = 0
    for n in nums:
        if play(n):
            Maria += 1
        else:
            Ben += 1

    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    else:
        return None
