# Smallest multiple
import datetime

########################
"""The following shows that, we can use LCM(Least Common Multiple)
iteratively to get the smallest multiple...

1 2 ==> 2
2 3 ==> 6
3 4 ==> 12
4 5 ==> 20
5 6 ==> 30
6 7 ==> 42
7 8 ==> 56
8 9 ==> 72
9 10 ==> 90

2 6 ==> 6
6 12 ==> 12
12 20 ==> 60
20 30 ==> 60
...

6 12 ==> 12
12 60 ==> 60
...

"""
######################
"""Oops... The efficiency of following version of algorithem
is incrediblly poor... """
######################


# find LCM(Least Common Multiple) of two integer
def find_lcm_first_version(a, b):
    """ assume a < b """
    if b % a == 0:
        return b

    for i in range(1, a + 1):
        c = i * b
        if c % a == 0:
            return c

######################
"""Then after some working around on a whitepaper, i recalled
a beter solution -- using LCD (Largest Common Divisor) to
hack the LCM """
######################


def find_lcd(a, b):
    """ assume a < b """
    # if b < a:
    #     tmp = b
    #     b = a
    #     a = tmp
    if b < a:
        a, b = b, a  # a simpler and better way

    if b % a == 0:
        return a

    r = b % a
    b = a
    a = r
    return find_lcd(a, b)


def find_lcm_second_version(a, b):
    """using lcd to hack lcm

        lcm = lcd * (a / lcd) * (b / lcd) = a * b / lcd

    """
    lcd = find_lcd(a, b)
    return a * b / lcd


def find_smalllest_multiple_of_consecutive_integer(a, b):
    time1 = datetime.datetime.now()
    if a > b:
        raise Exception("invalid range: a should smaller than b")

    li = range(a, b + 1)
    while len(li) > 1:
        tmp_list = []
        j = 1
        while j < len(li):
            lcm = find_lcm_second_version(li[j - 1], li[j])
            tmp_list.append(lcm)
            j = j + 1
        li = tmp_list

    time2 = datetime.datetime.now()
    print "Total runing time: ", time2 - time1
    return li[0]


if __name__ == "__main__":
    # test find_lcm(a, b)
    print find_lcm_second_version(6, 12)
    print find_lcm_second_version(12, 20)
    print find_lcm_second_version(8, 9)

    print find_lcd(12, 20)
    print find_lcd(8, 9)
    print find_lcd(6, 12)
    print find_lcd(6, 6)
    # test find_smalllest_multiple_of_consecutive_integer(a, b)
    print find_smalllest_multiple_of_consecutive_integer(1, 2)
    print find_smalllest_multiple_of_consecutive_integer(5, 5)

    print find_smalllest_multiple_of_consecutive_integer(1, 10)
    print find_smalllest_multiple_of_consecutive_integer(1, 20)

    print find_smalllest_multiple_of_consecutive_integer(1, 30)
    print find_smalllest_multiple_of_consecutive_integer(1, 40)
    print find_smalllest_multiple_of_consecutive_integer(1, 50)
    print find_smalllest_multiple_of_consecutive_integer(1, 100)
    print find_smalllest_multiple_of_consecutive_integer(1, 200)
    print find_smalllest_multiple_of_consecutive_integer(1, 500)

    # need 13+s on my computer
    print find_smalllest_multiple_of_consecutive_integer(1, 1000)



    # should raise exception
    #print find_smalllest_multiple_of_consecutive_integer(5, 4)
