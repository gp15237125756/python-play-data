import panda as np
import matplotlib.pyplot as plt
import random
t = np.arange(0, 4, 0.1)
plt.plot(t, t, t, t + 2, t, t ** 2)
number = ""
for x in range(6):
    number = number + str(random.randint(0, 9))
print(str(number))