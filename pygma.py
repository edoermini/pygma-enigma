#-*- coding: utf-8 -*-

class m3():
	def __init__(self):
		self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
		
		self.rotor_1 = ["a:h", "b:s", "c:u", "d:t", "e:v", "f:y", "g:r", "h:m", "i:a", "j:q", "k:o", "l:z", "m:x", "n:l", "o:c", "p:i", "q:f", "r:n", "s:b", "t:j", "u:d", "v:g", "w:p", "x:e", "y:k", "z:w"]
		self.rotor_1_left = []
		self.rotor_1_right = []
		
		self.rotor_2 = ["a:w", "b:q", "c:v", "d:m", "e:u", "f:z", "g:r", "h:t", "i:s", "j:i", "k:x", "l:y", "m:o", "n:a", "o:d", "p:n", "q:p", "r:j", "s:k", "t:l", "u:c", "v:e", "w:f", "x:g", "y:b", "z:h"]
		self.rotor_2_left = []
		self.rotor_2_right = []

		self.rotor_3 = ["a:v", "b:r", "c:w", "d:x", "e:z", "f:i", "g:q", "h:j", "i:y", "j:t", "k:m", "l:u", "m:s", "n:p", "o:k", "p:l", "q:n", "r:o", "s:d", "t:a", "u:h", "v:b", "w:f", "x:c", "y:e", "z:g"]
		self.rotor_3_left = []
		self.rotor_3_right = []

		self.reflector = ["a:z", "b:y", "c:x", "d:w", "e:v", "f:u", "g:t", "h:s", "i:r", "j:q", "k:p", "l:o", "m:n", "n:m", "o:l", "p:k", "q:j", "r:i", "s:h", "t:g", "u:f", "v:e", "w:d", "x:c", "y:b", "z:a"]
		self.reflector_left = []
		self.reflector_right = []

	def set_key(self, key):

		self.__init__()

		key = key.lower()
		
		if (len(key) > 4 or len(key) < 4):
			raise ValueError("The encryption key must be 4 letters\n")

		self.indexKey = []
		for i in key:
			self.indexKey.append(i)

		return self.set_rotors(self.indexKey)

	def set_rotors(self, key):
		count = 0

		for k in key:
			count += 1
			try:
				if (count == 1):

					for i in self.rotor_1:
						self.rotor_1_left.append(i.split(":")[0])
						self.rotor_1_right.append(i.split(":")[1])
					
					index = self.rotor_1_left.index(k)
					self.rotor_1_left = self.rotor_1_left[index:] + self.rotor_1_left[:index]
					self.rotor_1_right = self.rotor_1_right[index:] + self.rotor_1_right[:index]

				elif (count == 2):
					for i in self.rotor_2:
						self.rotor_2_left.append(i.split(":")[0])
						self.rotor_2_right.append(i.split(":")[1])
					
					index = self.rotor_2_left.index(k)
					self.rotor_2_left = self.rotor_2_left[index:] + self.rotor_2_left[:index]
					self.rotor_2_right = self.rotor_2_right[index:] + self.rotor_2_right[:index]

				elif (count == 3):
					for i in self.rotor_3:
						self.rotor_3_left.append(i.split(":")[0])
						self.rotor_3_right.append(i.split(":")[1])
					
					index = self.rotor_3_left.index(k)
					self.rotor_3_left = self.rotor_3_left[index:] + self.rotor_3_left[:index]
					self.rotor_3_right = self.rotor_3_right[index:] + self.rotor_3_right[:index]

				else:
					for i in self.reflector:
						self.reflector_left.append(i.split(":")[0])
						self.reflector_right.append(i.split(":")[1])
					
					index = self.reflector_left.index(k)
					self.reflector_left = self.reflector_left[index:] + self.reflector_left[:index]
					self.reflector_right = self.reflector_right[index:] + self.reflector_right[:index]
			except ValueError:
				if k.isdigit() == True:
					raise TypeError("Unsupported numbers")
				else:
					raise ValueError("The letter %s is not present in the rotors" % (k))

	def set_stecker(self, words):
		self.stecker = {}
		count = 0
		steckcheck = []

		words = words.lower()

		if words == "":
			self.stecker = {}
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
			self.stecker.update({i[0]:i[1], i[1]:i[0]})

	def stecker_check(self, word):
		changed = ""
		
		for i in word:
			try:
				ch = self.stecker[i.lower()]
				if i == i.lower():
					changed += ch
				elif i == i.upper():
					changed += ch.upper()
			except:
				if i == i.lower():
					changed += i
				elif i == i.upper():
					changed += i.upper()

		return changed

	def enc_dec(self, word):
		Word = ""
		rotor_1_count = 0
		rotor_2_count = 0
		rotor_3_count = 0
		rotor_1_left_mv = self.rotor_1_left
		rotor_1_right_mv = self.rotor_1_right
		rotor_2_left_mv = self.rotor_2_left
		rotor_2_right_mv = self.rotor_2_right
		rotor_3_left_mv = self.rotor_3_left
		rotor_3_right_mv = self.rotor_3_right
		reflector_left_mv = self.reflector_left
		reflector_right_mv = self.reflector_right

		for i in word:
			rotor_1_count += 1

			i = self.stecker_check(i)
				
			try:
				index = self.alphabet.index(i.lower())

				word = rotor_1_left_mv[index]
				index = rotor_1_right_mv.index(word)

				word = rotor_2_left_mv[index]
				index = rotor_2_right_mv.index(word)

				word = rotor_3_left_mv[index]
				index = rotor_3_right_mv.index(word)

				word = reflector_left_mv[index]
				index = reflector_right_mv.index(word)

				word = rotor_3_right_mv[index]
				index = rotor_3_left_mv.index(word)

				word = rotor_2_right_mv[index]
				index = rotor_2_left_mv.index(word)

				word = rotor_1_right_mv[index]
				index = rotor_1_left_mv.index(word)

				if i == i.upper():
					Word += self.alphabet[index].upper()
				elif i == i.lower():
					Word += self.alphabet[index].lower()
			
			except ValueError:
				Word += i
			
			rotor_1_left_mv = rotor_1_left_mv[1:] + rotor_1_left_mv[:1]
			rotor_1_right_mv = rotor_1_right_mv[1:] + rotor_1_right_mv[:1]

			if rotor_1_count == 26:
				rotor_2_left_mv = rotor_2_left_mv[1:] + rotor_2_left_mv[:1]
				rotor_2_right_mv = rotor_2_right_mv[1:] + rotor_2_right_mv[:1]
				
				rotor_2_count += 1
				rotor_1_count = 0

			elif rotor_2_count == 26:
				rotor_3_left_mv = rotor_3_left_mv[1:] + rotor_3_left_mv[:1]
				rotor_3_right_mv = rotor_3_right_mv[1:] + rotor_3_right_mv[:1]

				rotor_3_count +=1
				rotor_2_count = 0
				rotor_1_count = 0

			elif rotor_3_count == 26:
				rotor_3_count = 0
				rotor_2_count = 0
				rotor_1_count = 0

		Word = self.stecker_check(Word)		
		return Word
