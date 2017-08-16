import sys
print(sys.version)

colors = ['red', 'green', 'blue']

for i in colors:
	print(i)

for i in reversed(colors):
	print(i)

for i, color in enumerate(colors):
	print(i, '-->', color)

names = ['aj', 'franz']

for name, color in zip(names, colors):
	print(name, '-->', color)

for color in sorted(colors):
	print(color)

for color in sorted(colors, reverse = True):
	print(color)

print(sorted(colors, key=len))