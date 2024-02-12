import statistics
f = open("user.out", 'w')
for line in stdin:
    l = sorted(map(int, line.rstrip()[1:-1].split(',')))
    print(l[len(l) // 2], file=f)
exit(0)