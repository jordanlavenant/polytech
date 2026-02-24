def estPremier(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print([i for i in range(1, 10_000) if estPremier(i)])