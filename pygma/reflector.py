class Reflector:
	
	def __init__(self, letters, position):
		self.letters = letters.lower()
		self.position = position
		self.reflector = []
		
		letter_link = {"a":"z", "b":"y", "c":"x", "d":"w", "e":"v", "f":"u", "g":"t", "h":"s", "i":"r", "j":"q", "k":"p", "l":"o",
		"m":"n", "n":"m", "o":"l", "p":"k", "q":"j", "r":"i", "s":"h", "t":"g", "u":"f", "v":"e", "w":"d", "x":"c", "y":"b", "z":"a"}

		if self.position < 1 or self.position > 26:
			raise ValueError("A number between 1 and 26 with 1 and 26 included is required")

		if len(self.letters) > 26 or len(self.letters) < 26:
			raise ValueError("26 letters are required")

		for index,letter in enumerate(self.letters):
			for letter_2 in self.letters[0:index] + self.letters[index+1:]:
				if letter == letter_2:
					raise ValueError("Same element found several times")

		for letter in self.letters:
			if letter.isalpha() == True:
				self.reflector.append(letter + letter_link[letter])
			else:
				raise TypeError("Unsupported element")

		word = self.reflector[position-1]
		index = self.reflector.index(word)
		
		self.reflector = self.reflector[index:] + self.reflector[:index]
