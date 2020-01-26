#program to count bits in an integer. O(n) time complexity

def count_bits(x: int):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

print (count_bits(3442))


