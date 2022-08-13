def get_prime_factors(N):
    factors = list()
    divisor = 2
    while(divisor <= N):
        if (N % divisor) == 0:
            factors.append(divisor)
            N = N//divisor
        else:
            divisor += 1
    return factors

# commands used in solution video for reference
if __name__ == '__main__':
    print(get_prime_factors(630))  # [2, 3, 3, 5, 7]
    print(get_prime_factors(13))  # [13]
