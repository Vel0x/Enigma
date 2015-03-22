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