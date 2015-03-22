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
