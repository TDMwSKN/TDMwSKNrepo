import numpy as np
import matplotlib.pyplot as plt

no_strategies = 3
xA = [1/no_strategies]
xB = [1/no_strategies]
xC = [1/no_strategies]
dt = 0.001

# Strategy A: Functional Weighting
# Strategy B: Architectural Weighting
# Strategy C: Severity Weighting
# Pay off Table
#       A       B       C
# A     0       0       0
# B     0       0       0
# C     0       0       0

for t in range(10000):
    fA = xA[t] * 0 + xB[t] * 0 + xC[t] * 0
    fB = xA[t] * 0 + xB[t] * 0 + xC[t] * 0
    fC = xA[t] * 0 + xB[t] * 0 + xC[t] * 0
    f = xA[t] * fA + xB[t] * fB + xC[t] * fC
    xA.append(xA[t] + (xA[t] * (fA - f)) * dt)
    xB.append(xB[t] + (xB[t] * (fB - f)) * dt)
    xC.append(xC[t] + (xC[t] * (fC - f)) * dt)

print(np.average(xA))
print(np.average(xB))
print(np.average(xC))

fig = plt.figure(figsize=(20,5))
fig.add_subplot(1,3,1)
plt.plot(xA, 'g', label = 'Strategy A')
plt.plot(xB, 'b', label = 'Strategy B')
plt.plot(xC, 'r', label = 'Strategy C')
plt.title('Replicator dynamics of strategies ')
plt.legend(loc='best')
plt.grid()

fig.add_subplot(1,3,2)
plt.plot(xA, xB)
plt.title('Phase space of Strategy A vs Strategy B')
plt.xlabel('Strategy A')
plt.ylabel('Strategy B')
plt.grid()

fig.add_subplot(1,3,3)
plt.plot(xA, xC)
plt.title('Phase space of Strategy A vs Strategy C')
plt.xlabel('Strategy A')
plt.ylabel('Strategy C')
plt.grid()

plt.show()