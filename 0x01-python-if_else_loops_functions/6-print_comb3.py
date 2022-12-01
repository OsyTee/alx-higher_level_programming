for d in range(1, 100):
    digit_1 = d/10
    digit_2 = d%10
    if d < 10 and digit_1 < digit_2:
        print("{}{}".format(0, d), end=",")
    elif digit_1 < digit_2:
        if d == 89:
            break
            print(d, end=",")


