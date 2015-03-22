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
			8:"FKQHTLXOCBJSPDZRAMEWNIUYGV",
			9:"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		}
		
		self.position = position
		self.mapping = mappings[index]
		self.create_mapping()
		
	
	def create_mapping(self):
		forward = {}
		reversed = {}
		counter = 0
		
		alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		
		rotated = (alphabet + alphabet)[self.position:self.position+26]
		
		for c in rotated:
			forward[c] = self.mapping[counter]
			reversed[self.mapping[counter]] = c
			counter += 1
		
		self.map = {'forward':forward, 'reversed':reversed}
		
	def increment_position(self):
		print "Incrementing Position from:", self.position, "to",
		self.position += 1
		if self.position == 26:
			if self.left_rotor:
				self.left_rotor.increment_position()
			self.position = 0
		print self.position
		self.create_mapping()
		
	
	def set_position(self, value):
		self.position = value
		self.create_mapping()
		
	def set_neighbours(self, left, right):
		self.left_rotor = left
		self.right_rotor = right
		
	def convert_forward(self, character):
		return self.map['forward'][character]
	
	def convert_backward(self, character):
		return self.map['reversed'][character]