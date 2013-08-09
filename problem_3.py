#Largest prime factor

import datetime


####################################
############ is_prime ##############
####################################

def is_prime_first_version(n):
    # n needs to be an integer
    if n < 2:
        return False

    fac_count = 0;
    for i in range(1, n+1):
        if n % i == 0:
            fac_count = fac_count + 1
    if fac_count > 2:
        return False
    else:
        return True

####################################
def is_prime_second_version(n):
    i = 2
    while i <= n/2:
        if n % i == 0:
            return False
        i = i + 1
    return True

# 1st attempt: got OverFlowError for large list
#def find_factors(n):
#    factors = []
#    for i in range(1, n+1):
#        if n % i == 0:
#            factors.append(i)
#    return factors


#def find_max_prime_factors(n):
#    start_time = datetime.datetime.now()
#    factors = find_factors(n)
#    max_prime_factor = -1
#    for i in factors:
#        if is_prime(i) and max_prime_factor < i:
#            max_prime_factor = i
#
#    end_time = datetime.datetime.now()
#    print end_time-start_time
#
#    return max_prime_factor


####################################
####find_max_prime_factors##########
####################################
def find_max_prime_factors_first_version(n):
    start_time = datetime.datetime.now()
    max_prime_factor = n
    # got OverFlowError: range() result has too many values
    #for i in range(1, n+1):
    #    if (n % i == 0) and is_prime(i) and max_prime_factor < i:
    #        max_prime_factor = i

    i = n/2 + 1
    while i > 0:
        if (n % i == 0) and is_prime_second_version(i):
            return i
        i = i - 1

    end_time = datetime.datetime.now()
    print end_time-start_time
    return max_prime_factor


####################################
def find_max_prime_factors_second_version(n):
    max_prime_factor = -1
    i = 1
    j = n
    while i <= j:
        if n % i == 0:
            if is_prime_second_version(i) and max_prime_factor < i:
                max_prime_factor = i
            k = n / i
            if is_prime_second_version(k) and max_prime_factor < k:
                max_prime_factor = k
        i = i + 1
        j = n / i
    return max_prime_factor

####################################
def find_max_prime_factors_third_version(n):
    max_prime_factor = -1
    i = 1
    j = n
    while i <= j:
        if n % i == 0:
            k = n / i
            max_prime_factor = check_out_max_prime_factor(i, max_prime_factor)
            max_prime_factor = check_out_max_prime_factor(k, max_prime_factor)
        i = i + 1
        j = n / i
    return max_prime_factor

def check_out_max_prime_factor(i, max_prime_factor):
    if is_prime_second_version(i) and max_prime_factor < i:
        return i
    else:
        return max_prime_factor


if __name__ == "__main__":
    print is_prime_second_version(0)
    print is_prime_second_version(1)
    print is_prime_second_version(29)
    print is_prime_second_version(28)

    #print is_prime(2.5)


    print find_max_prime_factors_second_version(28)
    print find_max_prime_factors_second_version(9)
    print find_max_prime_factors_second_version(13195)
    print find_max_prime_factors_second_version(600851475143)
