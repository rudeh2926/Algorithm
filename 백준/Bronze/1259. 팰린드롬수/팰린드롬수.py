while True:
    a = input()
    if a == '0': break
    elif a[::1] == a[::-1]:
        print("yes")
    else:
        print("no")