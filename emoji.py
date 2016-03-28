import markovify

with open("corpus.txt") as f:
	text = f.read()

model = markovify.Text(text)

for i in range(5):
	print(model.make_sentence())
