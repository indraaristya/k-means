import matplotlib.pyplot as plt
fig, ax = plt.subplots()
sse2 = 12699.3934
sse3 = 10607.0473
sse4 = 9047.8614
sse5 = 6696.8527
sse6 = 6572.9681
sse7 = 6070.0399

sse = [sse2,sse3,sse4,sse5,sse6,sse7]
plt.plot(sse,'g--d')
plt.show()