import re

def isValid(rec):
	hgt_unit = rec["hgt"][-2:]
	height = int(rec["hgt"][:-2])

	if len(rec["byr"]) != 4 or int(rec["byr"]) > 2002 or int(rec["byr"]) < 1920:
		return False

	elif len(rec["iyr"]) != 4 or int(rec["iyr"]) > 2020 or int(rec["iyr"]) < 2010:
		return False

	elif len(rec["eyr"]) != 4 or int(rec["eyr"]) > 2030 or int(rec["eyr"]) < 2020:
		return False

	elif not re.match('^#([0-9a-f]+){6}$', rec["hcl"]):
		return False

	elif rec["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
		return False

	elif len(rec["pid"]) != 9:
		return False

	elif hgt_unit not in ["cm", "in"]:
		return False

	elif hgt_unit in ["cm", "in"]:
		if hgt_unit == "cm":
			if height > 193 or height < 150:
				return False
			else:
				return True
		else:
			if height > 76 or height < 59:
				return False
			else:
				return True

	else:
		return True


fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] # fields for validation
invalid_count, valid_count = 0, 0

with open("day4_input.txt", "r") as file:
	lines = file.read()
	psport = lines.split("\n\n") # to extract different passports
	for items in psport:

		record = ' '.join(items.strip().split("\n"))
		for f in fields:
			if f not in record and record != "":
				invalid_count += 1 # counting records which do not have the required fields
				record = ""
				break

		dict_record = {}
		if record != "":
			data = record.split(" ")

			for item in data:
				dict_record[item[:3]] = item[4:] # creating dictionary of each record to check the rules

			if isValid(dict_record):
				valid_count += 1
		else:
			continue

print(len(psport) - invalid_count, valid_count)