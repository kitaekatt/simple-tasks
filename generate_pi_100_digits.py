import decimal

# Set precision high enough to get 100 digits
decimal.getcontext().prec = 110

# Compute pi using the Gauss-Legendre algorithm
# For simplicity and accuracy, use decimal.Decimal for all calculations

def compute_pi():
    a = decimal.Decimal(1)
    b = decimal.Decimal(1) / decimal.Decimal(2).sqrt()
    t = decimal.Decimal(0.25)
    p = decimal.Decimal(1)
    for _ in range(6):  # Slightly more iterations for extra precision
        an = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - an) ** 2
        a = an
        p *= 2
    pi = (a + b) ** 2 / (4 * t)
    return pi

if __name__ == "__main__":
    pi = compute_pi()
    # Format pi to 100 digits after the decimal point
    pi_str = f"{pi:.100f}"
    # Truncate in case of rounding errors
    pi_str = pi_str[:1 + 1 + 100]  # '3.' + 100 digits
    with open("pi_100_digits.txt", "w") as f:
        f.write(pi_str + "\n") 