import sys, random

class Parser:
	def __init__(self, content):
		self.chain = {}
		self.parse(content)
	
	def parse(self, content):
		prev_word = (None, None)

		for word in content.replace("\n", " ").split(" "):
			if not None in prev_word:
				if not prev_word in self.chain:
					self.chain[prev_word] = []

				self.chain[prev_word].append(word)

			prev_word = (prev_word[1], word)

class Generator:
	def __init__(self, chain):
		self.chain = chain

	def generate(self, start, length):
		result = "%s %s" % (start[0], start[1])

		key = start
		while(length):
			if key in self.chain:
				words = self.chain[key] 
				word = random.choice(words)

				result += " %s" % word
			else:
				break

			key = (key[1], word)
			length -= 1

		return result

if __name__ == "__main__":
	content = open(sys.argv[1], "rb").read()
	p = Parser(content)
	
	g = Generator(p.chain)

	print(g.generate((sys.argv[2], sys.argv[3]), int(sys.argv[4])))
