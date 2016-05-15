import markovify

def generate(s=2):
	with open('corpus.txt') as f:
		text = f.read()
	model = markovify.Text(text)
	gen = ''
	for i in range(s):
		sentence = model.make_sentence()
		if sentence != None:
			gen += sentence
	return gen

def generate_sentence(char=140):
	with open('corpus.txt') as f:
		text = f.read()
	model = markovify.Text(text)
	return model.make_short_sentence(char)

if __name__ == '__main__':
	print(generate())
