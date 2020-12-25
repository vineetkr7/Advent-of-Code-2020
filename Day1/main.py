with open("test_input.txt", "r") as file:
	lines = file.readlines()
# part 1
	for i in range(len(lines) - 1):
		for j in range(i + 1, len(lines)):
			if int(lines[i].strip()) + int(lines[j].strip()) == 2020:
				print(int(lines[i].strip()), int(lines[j].strip()))
				ans1 = int(lines[i].strip()) * int(lines[j].strip())

# part 2
	for i in range(len(lines) - 2):
		for j in range(i + 1, len(lines) - 1):
			for k in range(i + 2, len(lines)):
				if (int(lines[i].strip()) + int(lines[j].strip()) + int(lines[k].strip())) == 2020:
					print(int(lines[i].strip()), int(lines[j].strip()), int(lines[k].strip()))
					ans2 = int(lines[i].strip()) * int(lines[j].strip()) * int(lines[k].strip())

print(ans1, ans2)