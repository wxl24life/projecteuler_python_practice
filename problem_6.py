# sub square difference


def diff(n):
    '''(a1+a2+...+an)^2
        = a1^2+a2^2+...+an^2
        + 2*(a1*a2+a1*a3+..+a1*an+...+a(n-1)*a1+..a(n-1)*an)

        ==> diff = 2*(a1*a2+a1*a3+..+a1*an+...+..a(n-1)*an)
    '''
    sum = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            sum += i * j
    return sum * 2


if __name__ == "__main__":
    print diff(2)
    print diff(10)
    print diff(100)
