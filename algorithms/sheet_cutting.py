#!/usr/bin/python3
# coding=utf-8


def sheet_cutting(w, h, p):
    # print("New sheet")
    mem = {}
    q = _sheet_cuttting(w, h, p, mem)
    return q


def _sheet_cuttting(w, h, prices, mem):
    # Solution in memory
    if (w, h) in mem:
        return mem[(w, h)]
    # Done when either dimension is 0
    if w <= 0 or h <= 0:
        value = 0.0
    else:
        value = float("-inf")
        for cut_x in range(1, w+1):
            for cut_y in range(1, h+1):
                right = _sheet_cuttting(w-cut_x, h, prices, mem)
                down = _sheet_cuttting(cut_x, h-cut_y, prices, mem)
                new_value = prices[(cut_x, cut_y)] + right + down
                # print(f"""cut:{cut_x},{cut_y} = {prices[(cut_x, cut_y)]} + right:{w-cut_x}, {h} = {right} + down:{w}, {h-cut_y} = {down}""")
                value = max(value, new_value)
    # print(f"w:{w}, h:{h} => value: {value}")
    mem[(w, h)] = value
    return value
