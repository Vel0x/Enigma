from rotor import Rotor
from plugboard import Plugboard
from reflector import Reflector
		
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
			print "Plugboard", e
			e = self.right_rotor.convert_forward(e)
			print "RRF", e
			e = self.middle_rotor.convert_forward(e)
			print "RMF", e
			e = self.left_rotor.convert_forward(e)
			print "RLF", e
			e = self.reflector.reflect(e)
			print "R", e
			e = self.left_rotor.convert_backward(e)
			print "RLB", e
			e = self.middle_rotor.convert_backward(e)
			print "RMB", e
			e = self.right_rotor.convert_backward(e)
			print "RRB", e
			e = self.plugboard.convert(e)
			print "Plugboard", e
			self.right_rotor.increment_position()
			encrypted += e
			
		return encrypted
	
if __name__ == "__main__":
	r_right = Rotor(3, 0)
	r_middle = Rotor(2, 0)
	r_left = Rotor(1, 0)
	reflector = Reflector("A")
	plugboard = Plugboard("AZ BP CH DN EM FS GW JY KT LQ")

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

	if input_text == decrypted:
		print "Decryption successful"
	else:
		print "Decryption failed"