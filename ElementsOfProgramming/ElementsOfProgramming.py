#program to count bits in an integer. O(n) time complexity

#def count_bits(x: int):
#    num_bits = 0
#    while x:
#        num_bits += x & 1
#        x >>= 1
#    return num_bits

#print (count_bits(12))


#program to reverse digits eg 42 -> 24 and -324 -> -423

def reverse_digits(x: int):
    string_as_num = 0
    num_as_string = str(abs(x)) [::-1]
    string_as_num = int(num_as_string)
    return -string_as_num if x < 0 else string_as_num
#why isn't negative int returning negative answers? (hint: make sure you have a print statement!!!!!)

print (reverse_digits(-432))

#using modulo method to reduce time complexity to O(n)
def reverse_digits_nostring(x: int):
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
    return -result if x < 0 else result

print(reverse_digits_nostring(-24))







