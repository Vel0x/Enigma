class Rotor(object):

	def __init__(self, index, position):
		mappings = {
			1:"EKMFLGDQVZNTOWYHXUSPAIBRCJ",
			2:"AJDKSIRUXBLHWTMCQGZNPYFVOE",
			3:"BDFHJLCPRTXVZNYEIWGAKMUSQO",
			4:"ESOVPZJAYQUIRHXLNFTGKDCMWB",
			5:"VZBRGITYUPSDNHLXAWMJQOFECK",
			6:"JPGVOUMFYQBENHZRDKASXLICTW",
			7:"NZJHGRCXMYSWBOUFAIVLPEKQDT",
			8:"FKQHTLXOCBJSPDZRAMEWNIUYGV"
		}
		
		mapping = mappings[index]
		
		forward = {}
		reversed = {}
		counter = 0
		for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			forward[c] = mapping[counter]
			reversed[mapping[counter]] = c
			counter += 1
		
		self.map = {'forward':forward, 'reversed':reversed}
		self.position = position
	
	def increment_position(self):
		print "Incrementing Position from:", self.position, "to",
		self.position += 1
		if self.position == 26:
			if self.left_rotor:
				self.left_rotor.increment_position()
			self.position = 0
		print self.position
	
	def set_position(self, value):
		self.position = value
		
	def set_neighbours(self, left, right):
		self.left_rotor = left
		self.right_rotor = right
		
	def convert_forward(self, character):
		converted_char = chr(((ord(character) - ord('A') + self.position) % 26) + ord('A'))
		return self.map['forward'][converted_char]
	
	def convert_backward(self, character):
		converted_char = chr(((ord(character) - ord('A') + self.position) % 26) + ord('A'))
		return self.map['reversed'][converted_char]
			
class Reflector(object):

	reflectors ={	"Beta":		"LEYJVCNIXWPBQMDRTAKZGFUHOS",
					"Gamma":	"FSOKANUERHMBTIYCWLQPZXVGJD",
					"A":		"EJMZALYXVBWFCRQUONTSPIKHGD",
					"B":		"YRUHQSLDPXNGOKMIEBFZCWVJAT",
					"C":		"FVPJIAOYEDRZXWGCTKUQSBNMHL",
					"B Thin":	"ENKQAUYWJICOPBLMDXZVFTHRGS",
					"C Thin":	"RDOBJNTKVEHMLFCWZAXGYIPSUQ",
					"ETW":		"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
				}
				
	def __init__(self, reflector_type):
		self.reflector = reflector_type
	
	def reflect(self, character):
						
		return self.reflectors[self.reflector][ord(character) - ord('A')]	

class Plugboard(object):

	def __init__(self, pairs_str):
		pairs = pairs_str.split()
		pairs = map(lambda x : (x[0],x[1]), pairs)
		
		if len(pairs) != 10:
			return None
		
		self.pairs_dict = {}
		for p1,p2 in pairs:
			self.pairs_dict[p1] = p2
			self.pairs_dict[p2] = p1
		
		for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			if c not in self.pairs_dict.keys():
				self.pairs_dict[c] = c
			
	
	def convert(self, character):
		return self.pairs_dict[character]
		
class Enigma(object):
	
	def __init__(self, reflector, left_rotor, middle_rotor, right_rotor, plugboard):
		self.reflector = reflector
		self.left_rotor = left_rotor
		self.middle_rotor = middle_rotor
		self.right_rotor = right_rotor
		self.plugboard = plugboard
		
		self.left_rotor.set_neighbours(None, self.middle_rotor)
		self.middle_rotor.set_neighbours(self.left_rotor, self.right_rotor)
		self.right_rotor.set_neighbours(self.left_rotor, None)
		

	def encrypt(self, plaintext):
		encrypted = ""
		for c in plaintext:
			e = self.plugboard.convert(c)
			e = self.right_rotor.convert_forward(e)
			e = self.middle_rotor.convert_forward(e)
			e = self.left_rotor.convert_forward(e)
			e = self.reflector.reflect(e)
			e = self.left_rotor.convert_backward(e)
			e = self.middle_rotor.convert_backward(e)
			e = self.right_rotor.convert_backward(e)
			e = self.plugboard.convert(e)
			self.right_rotor.increment_position()
			encrypted += e
			
		return encrypted
	

r_right = Rotor(1, 0)
r_middle = Rotor(2, 0)
r_left = Rotor(3, 0)
reflector = Reflector("A")
plugboard = Plugboard("AB CD EF GH IJ KL MN OP QR ST")

input_text = "HELLOWORLD"

print "Input:", input_text

e = Enigma(reflector, r_left, r_middle, r_right, plugboard)
encrypted = e.encrypt(input_text)
print "Encrypted:", encrypted

r_left.set_position(0)
r_middle.set_position(0)
r_right.set_position(0)

decrypted = e.encrypt(encrypted)
print "Decrypted:", decrypted
