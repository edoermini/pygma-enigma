#-*- coding: utf-8 -*-

class m3():
	def __init__(self):
		self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "z"]
		self.init = ["a:b", "b:a", "c:d", "d:c", "e:f", "f:e", "g:h", "h:g", "i:l", "l:i", "m:n", "n:m", "o:p", "p:o", "q:r", "r:q", "s:t", "t:s", "u:v", "v:u", "x:z", "z:x"]
		
		self.rotor_1 = []
		self.rotor_1_left = []
		self.rotor_1_right = []
		
		self.rotor_2 = []
		self.rotor_2_left = []
		self.rotor_2_right = []

		self.rotor_3 = []
		self.rotor_3_left = []
		self.rotor_3_right = []

		self.reflector = []
		self.reflector_left = []
		self.reflector_right = []

	def set_key(self, key):

		self.__init__()

		key = str(key)
		
		if (len(key) > 4 or len(key) < 4):
			raise ValueError("La chiave di cifratura deve essere composta da 4 numeri\n")

		try:
			int(key)
		except ValueError:
			raise ValueError("La chiave di cifratura deve essere composta da 4 numeri\n")

		self.indexKey = []
		for i in key:
			self.indexKey.append(i)

		return self.set_rotors(self.indexKey)

	def set_rotors(self, key):
		count = 0

		for i in key:
			count += 1

			if (count == 1):
				self.rotor_1 = self.init[int(i)-1:] + self.init[:int(i)-1]

				for i in self.rotor_1:
					self.rotor_1_left.append(i.split(":")[0])
					self.rotor_1_right.append(i.split(":")[1])

			elif (count == 2):
				self.rotor_2 = self.init[int(i)-1:] + self.init[:int(i)-1]

				for i in self.rotor_2:
					self.rotor_2_left.append(i.split(":")[0])
					self.rotor_2_right.append(i.split(":")[1])

			elif (count == 3):
				self.rotor_3 = self.init[int(i)-1:] + self.init[:int(i)-1]
				
				for i in self.rotor_3:
					self.rotor_3_left.append(i.split(":")[0])
					self.rotor_3_right.append(i.split(":")[1])

			else:
				self.reflector = self.init[int(i)-1:] + self.init[:int(i)-1]
				
				for i in self.reflector:
					self.reflector_left.append(i.split(":")[0])
					self.reflector_right.append(i.split(":")[1])

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

			rotor_1_left_mv = rotor_1_left_mv[1:] + rotor_1_left_mv[:1]
			rotor_1_right_mv = rotor_1_right_mv[1:] + rotor_1_right_mv[:1]

			if rotor_1_count == 22:
				rotor_2_left_mv = rotor_2_left_mv[1:] + rotor_2_left_mv[:1]
				rotor_2_right_mv = rotor_2_right_mv[1:] + rotor_2_right_mv[:1]
				
				rotor_2_count += 1
				rotor_1_count = 0

			elif rotor_2_count == 22:
				rotor_3_left_mv = rotor_3_left_mv[1:] + rotor_3_left_mv[:1]
				rotor_3_right_mv = rotor_3_right_mv[1:] + rotor_3_right_mv[:1]

				rotor_3_count +=1
				rotor_2_count = 0
				rotor_1_count = 0

			elif rotor_3_count == 22:
				rotor_3_count = 0
				rotor_2_count = 0
				rotor_1_count = 0

		return Word

class m4:
	def __init__(self):
		self.indexKey = []

		self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "z"]
		self.init = ["a:b", "b:a", "c:d", "d:c", "e:f", "f:e", "g:h", "h:g", "i:l", "l:i", "m:n", "n:m", "o:p", "p:o", "q:r", "r:q", "s:t", "t:s", "u:v", "v:u", "x:z", "z:x"]
		
		self.rotor_1 = []
		self.rotor_1_left = []
		self.rotor_1_right = []
		
		self.rotor_2 = []
		self.rotor_2_left = []
		self.rotor_2_right = []

		self.rotor_3 = []
		self.rotor_3_left = []
		self.rotor_3_right = []

		self.rotor_4 = []
		self.rotor_4_left = []
		self.rotor_4_right = []

		self.reflector = []
		self.reflector_left = []
		self.reflector_right = []

	def set_key(self, key):

		self.__init__()

		key = str(key)
		
		if (len(key) > 5 or len(key) < 5):
			raise ValueError("La chiave di cifratura deve essere composta da 5 numeri\n")

		try:
			int(key)
		except ValueError:
			raise ValueError("La chiave di cifratura deve essere composta da 5 numeri\n")
		
		for i in key:
			self.indexKey.append(i)

		return self.set_rotors(self.indexKey)

	def set_rotors(self, key):
		count = 0

		for i in key:
			count += 1 
			if (count == 1):
				self.rotor_1 = self.init[int(i)-1:] + self.init[:int(i)-1]
				
				for i in self.rotor_1:
					self.rotor_1_left.append(i.split(":")[0])
					self.rotor_1_right.append(i.split(":")[1]) 

			elif (count == 2):
				self.rotor_2 = self.init[int(i)-1:] + self.init[:int(i)-1]
				
				for i in self.rotor_2:
					self.rotor_2_left.append(i.split(":")[0])
					self.rotor_2_right.append(i.split(":")[1])

			elif (count == 3):
				self.rotor_3 = self.init[int(i)-1:] + self.init[:int(i)-1]
				
				for i in self.rotor_3:
					self.rotor_3_left.append(i.split(":")[0])
					self.rotor_3_right.append(i.split(":")[1])


			elif (count == 4):
				self.rotor_4 = self.init[int(i)-1:] + self.init[:int(i)-1]
				
				for i in self.rotor_3:
					self.rotor_4_left.append(i.split(":")[0])
					self.rotor_4_right.append(i.split(":")[1])			

			else:
				self.reflector = self.init[int(i)-1:] + self.init[:int(i)-1]
				
				for i in self.reflector:
					self.reflector_left.append(i.split(":")[0])
					self.reflector_right.append(i.split(":")[1])

	def enc_dec(self, word):
		Word = ""
		rotor_1_count = 0
		rotor_2_count = 0
		rotor_3_count = 0
		rotor_4_count = 0
		rotor_1_left_mv = self.rotor_1_left
		rotor_1_right_mv = self.rotor_1_right
		rotor_2_left_mv = self.rotor_2_left
		rotor_2_right_mv = self.rotor_2_right
		rotor_3_left_mv = self.rotor_3_left
		rotor_3_right_mv = self.rotor_3_right
		rotor_4_left_mv = self.rotor_4_right
		rotor_4_right_mv = self.rotor_4_right
		reflector_left_mv = self.reflector_left
		reflector_right_mv = self.reflector_right

		for i in word:
			rotor_1_count += 1
			
			try:
				index = self.alphabet.index(i)

				word = rotor_1_left_mv[index]
				index = rotor_1_right_mv.index(word)

				word = rotor_2_left_mv[index]
				index = rotor_2_right_mv.index(word)

				word = rotor_3_left_mv[index]
				index = rotor_3_right_mv.index(word)

				word = rotor_4_left_mv[index]
				index = rotor_4_right_mv.index(word)

				word = reflector_left_mv[index]
				index = reflector_right_mv.index(word)

				word = rotor_4_right_mv[index]
				index = rotor_4_left_mv.index(word)

				word = rotor_3_right_mv[index]
				index = rotor_3_left_mv.index(word)

				word = rotor_2_right_mv[index]
				index = rotor_2_left_mv.index(word)

				word = rotor_1_right_mv[index]
				index = rotor_1_left_mv.index(word)

				Word += self.alphabet[index]
			
			except ValueError:
				Word += i

			rotor_1_left_mv = rotor_1_left_mv[1:] + rotor_1_left_mv[:1]
			rotor_1_right_mv = rotor_1_right_mv[1:] + rotor_1_right_mv[:1]

			if rotor_1_count == 22:
				rotor_2_left_mv = rotor_2_left_mv[1:] + rotor_2_left_mv[:1]
				rotor_2_right_mv = rotor_2_right_mv[1:] + rotor_2_right_mv[:1]
				
				rotor_2_count += 1
				rotor_1_count = 0

			elif rotor_2_count == 22:
				rotor_3_left_mv = rotor_3_left_mv[1:] + rotor_3_left_mv[:1]
				rotor_3_right_mv = rotor_3_right_mv[1:] + rotor_3_right_mv[:1]

				rotor_3_count +=1
				rotor_2_count = 0
				rotor_1_count = 0

			elif rotor_3_count == 22:
				rotor_4_left_mv = rotor_3_left_mv[1:] + rotor_3_left_mv[:1]
				rotor_4_right_mv = rotor_3_right_mv[1:] + rotor_3_right_mv[:1]
				
				rotor_4_count +=1
				rotor_3_count = 0
				rotor_2_count = 0
				rotor_1_count = 0

			elif rotor_4_count == 22:
				rotor_4_count =1
				rotor_3_count = 0
				rotor_2_count = 0
				rotor_1_count = 0				

		return Word
