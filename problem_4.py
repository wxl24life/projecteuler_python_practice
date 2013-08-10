# Largest palindrome product

def is_palindrome(n):
    """ n should be an non-negative integer"""
    a = []
    tmp = n
    while tmp / 10 != 0:
        k = tmp % 10
        a.append(k)
        tmp = tmp / 10
    a.append(tmp) # append the last digit

    size = len(a)

    i = 0
    j = size - 1
    while i < j:
        if a[i] != a[j]:
            return False
        i = i + 1
        j = j - 1

    return True

def find_largest_palindrome_product_of_range(a, b):
    largest = -1
    i = b
    while i >= a:
        j = b
        while j >= a:
            multi = i * j
            # for debug
            # print multi,
            if is_palindrome(multi) and largest < multi:
                largest = multi
            j = j - 1
        i = i - 1

    return largest





if __name__ == "__main__":
    print is_palindrome(1)
    print is_palindrome(0)
    # print is_palindrome(-1) # wrong! goole key words: python negative devision
    print is_palindrome(9009)
    print is_palindrome(10010)


    #print find_largest_palindrome_product_of_range(10, 99)
    print find_largest_palindrome_product_of_range(100, 999)
