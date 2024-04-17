def solution(phone_book):
    a = {}
    for b in phone_book:
        a[b] = 1

    for b in phone_book:
        c = ""
        for num in b:
            c += num

            if c in a and c != b:
                return False

    return True