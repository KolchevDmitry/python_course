def kol_les(n, k):
    if n == 0:
        return 1
    ans = 0

    for i in range(k + 1, n + 1):
        ans += kol_les(n - i, i)
    return ans


print(kol_les(5, 0))


