if __name__ == '__main__':
    lst = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst[name] = score
    sMin = min([x for x in lst.values() if x != min(lst.values())])
    s = sorted([k for k,v in lst.items() if v == sMin])
    print(*s, sep="\n")