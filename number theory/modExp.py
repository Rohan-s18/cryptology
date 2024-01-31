"""
Python Code for modulo inverse, modulo exponents and modulo discrete logarithms
Author: Rohan Singh
"""



# function for modulo inverse, finds the inverse of a mod m
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None



# function to find the modular exponent
def mod_exp(base, power, prime):
    result = 1
    for _ in range(power):
        result = (result*base)%prime
    return result



# function to find the discrete logarithm
def discrete_logarithm(base, target, prime):
    result = 1
    base = base % prime
    for x in range(1, prime):
        result = (result * base) % prime
        if result == target:
            return x
    return None



# main function
def main():

    a = 43
    m = 541
    inv = mod_inverse(34,541)
    print(f"The inverse of {a} modulo {m} is: {inv}")


    base = 805
    power = 587
    prime = 1373
    print(f"The modular exponent of {base} to the power {power} modluo {prime} is: {mod_exp(base,power,prime)}")


    p_a = 23
    g_a = 2
    target_a = 13
    log_a = discrete_logarithm(g_a, target_a, p_a)
    print(f"log_{g_a}({target_a}) mod {p_a} = {log_a}")






if __name__ == "__main__":
    main()