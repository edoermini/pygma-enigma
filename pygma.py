#-*- coding: utf-8 -*-

class m3():
	def __init__(self):
		self.stecker = {}
		self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "z"]
		
		self.rotor_1 = ["a:x", "b:z", "c:u", "d:v", "e:s", "f:t", "g:q", "h:r", "i:o", "l:p", "m:l", "n:m", "o:n", "p:h", "q:i", "r:f", "s:g", "t:d", "u:e", "v:b", "x:c", "z:a"]
		self.rotor_1_left = []
		self.rotor_1_right = []
		
		self.rotor_2 = ["a:o", "b:t", "c:u", "d:l", "e:n", "f:z", "g:q", "h:r", "i:x", "l:p", "m:v", "n:a", "o:s", "p:g", "q:i", "r:c", "s:h", "t:d", "u:b", "v:e", "x:f", "z:m"]
		self.rotor_2_left = []
		self.rotor_2_right = []

		self.rotor_3 = ["a:u", "b:v", "c:x", "d:z", "e:l", "f:r", "g:q", "h:t", "i:p", "l:o", "m:s", "n:m", "o:g", "p:f", "q:d", "r:h", "s:n", "t:i", "u:a", "v:c", "x:b", "z:e"]
		self.rotor_3_left = []
		self.rotor_3_right = []

		self.reflector = ["a:z", "b:x", "c:v", "d:u", "e:t", "f:s", "g:r", "h:q", "i:p", "l:o", "m:n", "n:m", "o:l", "p:i", "q:h", "r:g", "s:f", "t:e", "u:d", "v:c", "x:b", "z:a"]
		self.reflector_left = []
		self.reflector_right = []

	def set_key(self, key):

		self.__init__()
		
		if (len(key) > 4 or len(key) < 4):
			raise ValueError("La chiave di cifratura deve essere composta da 4 lettere\n")

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
				raise ValueError("Lettera %s non presente nei rotori" % (k))

	def set_stecker(self, words):
		count = 0
		steckcheck = []

		if words == "":
			self.stecker = {}
			return None

		steck = words.replace(" ", "")
		steck = steck.split(",")
		steckcheck = steck

		for i in steck:
			del steck[count]
			
			for j in steck:
				if i[0] == j[0] or i[1] == j[1] or i[0] == j[1] or i[1] == j[0]:
					raise ValueError("Stessa lettera trovata multiple volte")
					return None

			count += 1
			steckcheck = steck

		for i in steck:
			self.stecker.update({i[0]:i[1], i[1]:i[0]})

		if len(steck) > 10:
			raise ValueError("Impossibile fare più di 10 collegamenti")


	def stecker_check(self, word):
		changed = ""
		
		for i in word:
			try:
				ch = self.stecker[i]
				changed += ch
			except:
				changed += i

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
				index = self.alphabet.index(i)

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

				Word += self.alphabet[index]
			
			except ValueError:
				Word += i

			rotor_3_left_mv = rotor_3_left_mv[1:] + rotor_3_left_mv[:1]
			rotor_3_right_mv = rotor_3_right_mv[1:] + rotor_3_right_mv[:1]

			if rotor_3_count == 22:
				rotor_2_left_mv = rotor_2_left_mv[1:] + rotor_2_left_mv[:1]
				rotor_2_right_mv = rotor_2_right_mv[1:] + rotor_2_right_mv[:1]
				
				rotor_2_count += 1
				rotor_1_count = 0

			elif rotor_2_count == 22:
				rotor_1_left_mv = rotor_1_left_mv[1:] + rotor_1_left_mv[:1]
				rotor_1_right_mv = rotor_1_right_mv[1:] + rotor_1_right_mv[:1]

				rotor_1_count +=1
				rotor_2_count = 0
				rotor_3_count = 0

			elif rotor_1_count == 22:
				rotor_3_count = 0
				rotor_2_count = 0
				rotor_1_count = 0

		Word = self.stecker_check(Word)		
		return Word
