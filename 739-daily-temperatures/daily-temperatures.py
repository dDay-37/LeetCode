
def dailyTemperatures(temperatures: List[int]) -> List[int]:

    output = [0]*len(temperatures)
    stack = []
    for cindex,ctemp  in enumerate(temperatures):
        while stack and stack[-1][0] < ctemp:#cause it is monotonically decreasing
                t,i = stack.pop()
                output[i] = cindex-i
        stack.append((ctemp, cindex))
    return output
with open('user.out', 'w') as f:
    for case in map(loads, stdin):
        f.write(f"[{','.join([str(x) for x in dailyTemperatures(case)])}]\n")
exit()