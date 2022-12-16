length = 7
cost = 2
prices = [0,1,4,3,6,8,5,9]

def cut_rod(length, cost, prices):
    mem = [0]*(length+1)
    for j in range(1, length+1):
        value = float("-inf")
        for i in range(1, j+1):
            if i < j:
                value = max(value, prices[i] + mem[j-i] - cost)
            else:
                value = max(value, prices[i] + mem[j-i])
        mem[j] = value

    print(mem)
    return mem[length]

print(cut_rod(length, cost, prices))
