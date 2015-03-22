def create_rotor(mapping):
	forward = {}
	reversed = {}
	counter = 0
	for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		forward[c] = mapping[counter]
		reversed[mapping[counter]] = c
		counter += 1
	
	return {'forward':forward, 'reversed':reversed}
	
def rotor(index):
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
	
	return create_rotor(mappings[index])

def reflect(reflector, character):
	reflectors ={	"Beta":		"LEYJVCNIXWPBQMDRTAKZGFUHOS",
					"Gamma":	"FSOKANUERHMBTIYCWLQPZXVGJD",
					"A":		"EJMZALYXVBWFCRQUONTSPIKHGD",
					"B":		"YRUHQSLDPXNGOKMIEBFZCWVJAT",
					"C":		"FVPJIAOYEDRZXWGCTKUQSBNMHL",
					"B Thin":	"ENKQAUYWJICOPBLMDXZVFTHRGS",
					"C Thin":	"RDOBJNTKVEHMLFCWZAXGYIPSUQ",
					"ETW":		"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
				}
					
	return reflectors[reflector][ord(character) - ord('A')]

print rotor(1)
print reflect('Z')