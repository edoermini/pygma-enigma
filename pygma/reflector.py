def Reflector(letters, position):
	reflector = []
	letter_link = {"a":"z", "b":"y", "c":"x", "d":"w", "e":"v", "f":"u", "g":"t", "h":"s", "i":"r", "j":"q", "k":"p", "l":"o",
	"m":"n", "n":"m", "o":"l", "p":"k", "q":"j", "r":"i", "s":"h", "t":"g", "u":"f", "v":"e", "w":"d", "x":"c", "y":"b", "z":"a"}

	letters = letters.lower()

	if position < 1 or position > 26:
		raise ValueError("A number between 1 and 26 with 1 and 26 included is required")

	if len(letters) > 26 or len(letters) < 26:
		raise ValueError("26 letters are required")

	for index,letter in enumerate(letters):
		for letter_2 in letters[0:index] + letters[index+1:]:
			if letter == letter_2:
				raise ValueError("Same element found several times")

	for letter in letters:
		if letter.isalpha() == True:
			reflector.append(letter + letter_link[letter])
		else:
			raise TypeError("Unsupported element")

	word = reflector[position-1]
	index = reflector.index(word)
	reflector = reflector[index:] + reflector[:index]



	return reflector
