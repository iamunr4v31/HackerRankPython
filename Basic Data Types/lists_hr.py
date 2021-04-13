if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        cmd, *args = input().split()
        if cmd != "print":
            cmd += "("+ ",".join(args) +")"
            eval("lst."+cmd)
        else:
            print(lst)