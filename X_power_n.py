# n is an integer

def x_power_n (x,n):
    if n==0:
        return 1
    else:
        abs_n = abs(n)
        s = 1
        while abs_n > 0:
            s = s * x
            abs_n = abs_n-1
        if n > 0:
            return s
        else:
            return (1/s)

#12
if __name__ == '__main__':
    print(x_power_n(3, 3))
    print(x_power_n(3, 0))
    print(x_power_n(3, -2))
    # import matplotlib.pyplot as plt
    # import matplotlib
    # matplotlib.use('TKAgg')  #
    # plt.plot([1, 2], [2, 1], 'k')
    # plt.figure(1)
    # plt.plot([1, 2], [2, 1], 'k')