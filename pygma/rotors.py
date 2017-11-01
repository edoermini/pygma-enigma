def Rotor(letters, position):
	rotor = []
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

	letters = letters.lower()
	
	if position < 1 or position > 26:
		raise ValueError("A number between 1 and 26 with 1 and 26 included is required")

	if len(letters) > 26 or len(letters) < 26:
		raise ValueError("26 letters are required")

	for index,letter in enumerate(letters):
		if letter.isalpha() == True:
				rotor.append(alphabet[index] + letter)
		else:
			raise TypeError("Unsupported element")

	word = rotor[position-1]
	index = rotor.index(word)
	rotor = rotor[index:] + rotor[:index]

	return rotor
