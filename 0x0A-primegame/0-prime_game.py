def isWinner(x, nums):
    if not nums or x <= 0:
        return None

    # Determine all primes up to a given number n using Sieve of Eratosthenes
    def sieve(n):
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p] is True:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
        return prime_numbers

    # Find the maximum number in nums to generate primes up to that number
    max_num = max(nums)
    primes_up_to_max = sieve(max_num)

    # Function to determine the winner of a single round
    def determine_winner(n):
        primes = [p for p in primes_up_to_max if p <= n]
        player_turn = 0  # 0 for Maria, 1 for Ben
        remaining_numbers = set(range(1, n + 1))

        while primes:
            prime = primes.pop(0)
            if prime in remaining_numbers:
                multiples = set(range(prime, n + 1, prime))
                remaining_numbers -= multiples
                player_turn = 1 - player_turn  # Switch turns

        # If player_turn is 1 after the last turn,
        # Maria made the last move and won
        return "Maria" if player_turn == 1 else "Ben"

    # Play x rounds and determine the winner of each round
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = determine_winner(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
