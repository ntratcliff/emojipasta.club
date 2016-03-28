import markovify

def generate():
	with open('corpus.txt') as f:
		text = f.read()
	model = markovify.Text(text)
	gen = ''
	for i in range(14):
		sentence = model.make_sentence()
		if sentence != None:
			gen += sentence
	return gen

if __name__ == '__main__':
	print(generate())
