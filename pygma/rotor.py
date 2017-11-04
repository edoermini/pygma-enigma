class Rotor:
	
	def __init__(self, letters, position):
		self.rotor = []
		self.letters = letters.lower()
		self.position = position
		
		self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
		
		#check if a letter between the alphabet has been chosen
		if self.position < 1 or self.position > 26:
			raise ValueError("A number between 1 and 26 with 1 and 26 included is required")

		#check if all the alphabet has been writed
		if len(self.letters) > 26 or len(self.letters) < 26:
			raise ValueError("26 letters are required")

		for index,letter in enumerate(self.letters):
			for letter2 in self.letters[0:index] + self.letters[index+1:]:
				if letter == letter2:
					raise ValueError("Same element found several times")

		for index,letter in enumerate(self.letters):
			if letter.isalpha() == True:
					self.rotor.append(self.alphabet[index] + letter)
			else:
				raise TypeError("Unsupported element")

		word = self.rotor[position-1]
		index = self.rotor.index(word)
		
		self.rotor = self.rotor[index:] + self.rotor[:index]
