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

#print (reverse_digits(-432))

#not using string method
def reverse_digits_nostring(x: int):
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
    return -result if x < 0 else result


#print(reverse_digits_nostring(-24))

#check if number is a palendrome
def is_num_palendrome(x: int):
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
    return "true" if result == x else "false"

print (is_num_palendrome(4114))
print (is_num_palendrome(4115))



#move all even integers to the beginning of array
def even_odd_array(A):
    array_low, array_high = 0, len(A)-1
    while array_low < array_high:
        if A[array_low] % 2 == 0:
            array_low += 1
        else:
            A[array_low],A[array_high] = A[array_high], A[array_low]
            array_high -= 1
    print(A)


even_odd_array([3,4,6,7,8,9])








