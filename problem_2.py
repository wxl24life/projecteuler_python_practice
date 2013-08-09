#Even Fibonacci numbers

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return fib(n-1) + fib(n-2)

def sum_of_even_terms_under_range(n):
    sum = 0
    i = 1
    #can't do this!
    #using an assignment in an expression is not supported in Python
    #while (k = fib(i)) <= n:

    while True:
        k = fib(i)
        if k > n:
            break

        if k % 2 == 0:
            sum = sum + k
        i = i + 1

    return sum


if __name__=="__main__":
    print sum_of_even_terms_under_range(4000000)
    #for test
    #print sum_of_even_terms_under_range(20)

