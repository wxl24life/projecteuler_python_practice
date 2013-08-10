# Multiples of 3 and 5
# git test

def sum_of_multiples_of_three_and_five(n):
    sum = 0
    for i in range(1, n):
        if (i % 3 == 0) or (i % 5 == 0):
            sum = sum + i
    return sum

if __name__=="__main__":
    print sum_of_multiples_of_three_and_five(1000)
