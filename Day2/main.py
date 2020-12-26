with open("test_input.txt", "r") as file:
	lines = file.readlines()
	count1, count2 = 0, 0
	for line in lines:
		items = line.strip().split()
		least = int(items[0].split("-")[0])
		most = int(items[0].split("-")[1])
		char = items[1][0]
		if items[2].count(char) >= least and items[2].count(char) <= most:
			count1 += 1

		if (items[2][least-1] == char and items[2][most-1] != char) or (items[2][least-1] != char and items[2][most-1] == char):
			count2 += 1

print(count1, count2)