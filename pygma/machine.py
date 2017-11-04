from .rotor import Rotor
from .reflector import Reflector
from .plugboard import PlugBoard

class Machine():
	
	def __init__(self, rotor, reflector, plugboard):
		self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

		self.rotor_1 = rotor[0].rotor
		self.rotor_1_left = []
		self.rotor_1_right = []

		self.rotor_2 = rotor[1].rotor
		self.rotor_2_left = []
		self.rotor_2_right = []

		self.rotor_3 = rotor[2].rotor
		self.rotor_3_left = []
		self.rotor_3_right = []

		self.reflector = reflector.reflector
		self.reflector_left = []
		self.reflector_right = []

		self.plugboard = plugboard.plugboard

		for i in self.rotor_1:
			self.rotor_1_right.append(i[0])
			self.rotor_1_left.append(i[1])

		for i in self.rotor_2:
			self.rotor_2_right.append(i[0])
			self.rotor_2_left.append(i[1])

		for i in self.rotor_3:
			self.rotor_3_right.append(i[0])
			self.rotor_3_left.append(i[1])

		for i in self.reflector:
			self.reflector_right.append(i[0])
			self.reflector_left.append(i[1])
			
	def plugboard_check(self, word):
		changed = ""
		
		for i in word:
			try:
				ch = self.plugboard[i.lower()]
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
		rotor_1_rotations = 0
		rotor_2_rotations = 0
		rotor_3_rotations = 0
		rotor_1_left_mv = self.rotor_1_left
		rotor_1_right_mv = self.rotor_1_right
		rotor_2_left_mv = self.rotor_2_left
		rotor_2_right_mv = self.rotor_2_right
		rotor_3_left_mv = self.rotor_3_left
		rotor_3_right_mv = self.rotor_3_right
		reflector_left_mv = self.reflector_left
		reflector_right_mv = self.reflector_right

		for i in word:
			rotor_1_rotations += 1

			i = self.plugboard_check(i)
				
			try:
				index = self.alphabet.index(i.lower())

				word = rotor_1_right_mv[index]
				index = rotor_1_left_mv.index(word)

				word = rotor_2_right_mv[index]
				index = rotor_2_left_mv.index(word)

				word = rotor_3_right_mv[index]
				index = rotor_3_left_mv.index(word)

				word = reflector_right_mv[index]
				index = reflector_left_mv.index(word)

				word = rotor_3_left_mv[index]
				index = rotor_3_right_mv.index(word)

				word = rotor_2_left_mv[index]
				index = rotor_2_right_mv.index(word)

				word = rotor_1_left_mv[index]
				index = rotor_1_right_mv.index(word)
				
				if i == i.upper():
					Word += self.alphabet[index].upper()
				elif i == i.lower():
					Word += self.alphabet[index].lower()

				rotor_1_left_mv = rotor_1_left_mv[1:] + rotor_1_left_mv[:1]
				rotor_1_right_mv = rotor_1_right_mv[1:] + rotor_1_right_mv[:1]

				if rotor_1_rotations == 26:
					rotor_2_left_mv = rotor_2_left_mv[1:] + rotor_2_left_mv[:1]
					rotor_2_right_mv = rotor_2_right_mv[1:] + rotor_2_right_mv[:1]
					
					rotor_2_rotations += 1
					rotor_1_rotations = 0

				elif rotor_2_rotations == 26:
					rotor_3_left_mv = rotor_3_left_mv[1:] + rotor_3_left_mv[:1]
					rotor_3_right_mv = rotor_3_right_mv[1:] + rotor_3_right_mv[:1]

					rotor_3_rotations +=1
					rotor_2_rotations = 0
					rotor_1_rotations = 0

				elif rotor_3_rotations == 26:
					rotor_3_rotations = 0
					rotor_2_rotations = 0
					rotor_1_rotations = 0
			
			except ValueError:
				Word += i

		Word = self.plugboard_check(Word)		
		return Word
