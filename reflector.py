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