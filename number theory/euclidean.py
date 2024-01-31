"""
Author: Rohan Singh
Code for the gcd and extended gcd algorithm
"""



# this function contains code for the euclidean algorithm to find the greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a



# this function contains code for the extended gcd algorithm
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)
    


# this function contains the whole extended table
def print_extended_gcd_table(m, n):
    print(f"Extended GCD Table for {m} and {n}:\n")
    print("i\tai\tbi\tqi\tri\txi\tyi")
    print("-" * 40)

    a, b = m, n
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    q, r = divmod(a, b)

    print(f"0\t{a}\t{b}\t-\t-\t{x0}\t{y0}")
    print(f"1\t{b}\t{r}\t{q}\t1\t{x1}\t{y1}")

    i = 2
    while r != 0:
        a, b = b, r
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
        q, r = divmod(a, b)

        print(f"{i}\t{a}\t{b}\t{q}\t{r}\t{x0}\t{y0}")

        i += 1



# main function
def main():
    m = 47
    n = 11

    print_extended_gcd_table(m, n)



if __name__ == "__main__":
    main()