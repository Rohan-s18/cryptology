"""
Code to find modulo Primitive Roots
Author: Rohan Singh
"""



# code to find the greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a



# code to check if a number is a primitive root
def is_primitive_root(g, p):
    powers_set = set()
    for k in range(1, p):
        power = pow(g, k, p)
        if power in powers_set:
            return False  # g^k repeats
        powers_set.add(power)

    if pow(g, p - 1, p) != 1:
        return False  # g^(p-1) not congruent to 1
    return True



# code to find all primitive roots
def find_primitive_roots(p):
    primitive_roots = []
    for g in range(2, p):
        if gcd(g, p) == 1 and is_primitive_root(g, p):
            primitive_roots.append(g)
    return primitive_roots



# main function
def main():
    p = 11
    roots = find_primitive_roots(p)
    print(f"Primitive roots for p={p}: {roots}")



if __name__ == "__main__":
    main()
