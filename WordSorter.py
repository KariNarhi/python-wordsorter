file = open("words.txt","r")

content = file.readlines()

file.close()

content.sort()

print("\nWords sorted in alphabetical order:\n")

for i in content:
	print(i)
