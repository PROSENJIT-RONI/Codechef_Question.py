if __name__ == '__main__':

    # No of test cases input
    T = int(input())
    sumlst = []
    for e in range(0, T):
        n, q = input().split()
        n = int(n)
        q = int(q)
        # Array input
        lst = [int(n) for n in input().split()]
        l = []
        for i in range(0, q):
            x, y = input().split()
            x = int(x)
            y = int(y)
            l.append([x, y])
        sumsblst = []
        for i in range(0, len(l)):
            s = 0
            # This loop will replace all occurrence of x in array with y
            # and will find the value of array
            for j in range(0, len(lst)):
                if l[i][0] == lst[j]:
                    lst[j] = l[i][1]
                if j > 0:
                    s += abs(lst[j] - lst[j - 1])
            sumsblst.append(s)
        sumlst.append(sumsblst)

    # Output of all test cases
    for i in range(0, T):
        print('Case ', (i + 1), ':')
        for j in sumlst[i]:
            print(j)
