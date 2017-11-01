def Stecker(words):
	stecker = {}
	count = 0
	steckcheck = []

	words = words.lower()

	if words == "":
		stecker = {}
		return None

	steck = words.replace(" ", "")
	steck = steck.split(",")

	for i in steck:
		if len(i) > 2 or len(i) < 2:
			raise ValueError("Comma-separated groups of two letters are required")

	for i in steck:
		for j in i:
			if j.isdigit() == True:
				raise TypeError("Unsupported numbers")

	for i in steck:
		steckcheck.append(i)

	for i in steckcheck:
		del steckcheck[count]
		
		for j in steckcheck:
			if i[0] == j[0] or i[1] == j[1] or i[0] == j[1] or i[1] == j[0]:
				raise ValueError("Same element found several times")
				return None

		count += 1

		del steckcheck[:]
		for i in steck:
			steckcheck.append(i)

	if len(steck) > 10:
		raise ValueError("Can not do more than 10 links")

	for i in steck:
		stecker.update({i[0]:i[1], i[1]:i[0]})

	return stecker