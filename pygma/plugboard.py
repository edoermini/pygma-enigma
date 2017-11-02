def PlugBoard(words):
	pb = {}
	count = 0
	pb_check = []

	words = words.lower()

	if words == "":
		pb = {}
		return None

	pb_list = words.replace(" ", "")
	pb_list = pb_list.split(",")

	for i in pb_list:
		if len(i) > 2 or len(i) < 2:
			raise ValueError("Comma-separated groups of two letters are required")

	for i in pb_list:
		for j in i:
			if j.isdigit() == True:
				raise TypeError("Unsupported numbers")

	for i in pb_list:
		pb_check.append(i)

	for i in pb_check:
		del pb_check[count]
		
		for j in pb_check:
			if i[0] == j[0] or i[1] == j[1] or i[0] == j[1] or i[1] == j[0]:
				raise ValueError("Same element found several times")
				return None

		count += 1

		del pb_check[:]
		for i in pb_list:
			pb_check.append(i)

	if len(pb_list) > 10:
		raise ValueError("Can not do more than 10 links")

	for i in pb_list:
		pb.update({i[0]:i[1], i[1]:i[0]})

	return pb
