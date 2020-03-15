#Time Stamps:4:43:08
#Simplified counting with get()
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
