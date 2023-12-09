#!/usr/bin/python3
# coding=utf-8

def sheet_cutting(w, h, p):
    # print('\n', "New Sheet:", w, h)
    mem = {}

    def _sheet_cutting(w, h, p):
        if (w, h) in mem:
            return mem[(w, h)]
        if w == 0 or h == 0:
            return 0
        # print("Sheet:", w, h)
        q = float('-inf')
        for x in range(1, w+1):
            for y in range(1, h+1):
                # print("x, y:", x, y)
                q = max(q, p[(x, y)] + _sheet_cutting(x,
                        h-y, p) + _sheet_cutting(w-x, h, p))
        mem[(w, h)] = q
        return q

    ans = _sheet_cutting(w, h, p)
    # print("\n Sheet:", w, h)
    # non_zero_p = {k: v for k, v in p.items() if v > 0 and k[0] <= w and k[1] <= h and mem[k] != v}
    # print('\n', "Prices:")
    # print(non_zero_p)
    # print('\n')
    # print("Mem:", mem)
    # print("Rev:", ans)
    return ans
