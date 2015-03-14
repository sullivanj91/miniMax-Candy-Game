import sys
import random

fn = sys.argv[1]
i = int(sys.argv[2])
t = int(sys.argv[3])

fq = open(fn, "w")
fq.write("%d %d" % (i, t))
trees = 0
for j in range(i * i):
    ran = random.randint(0, i * i - j - 1)
    if ran < t - trees:
        trees = trees + 1
        fq.write("\n%d %d" % (j / i + 1, j % i + 1))
fq.close()