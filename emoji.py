import markovify
import sqlite3

def addcount():
    con = sqlite3.connect("pasta.db")
    c = con.cursor()
    c.execute("INSERT INTO counter VALUES (1)")
    con.commit()
    con.close()

def generate(s=2):
    with open('corpus.txt') as f:
        text = f.read()
    model = markovify.Text(text)
    gen = ''
    for i in range(s):
    	sentence = model.make_sentence()
    	if sentence != None:
    		gen += sentence
    addcount()
    return gen

def generate_sentence(char=140):
    if char > 20:
        with open('corpus.txt') as f:
    	    text = f.read()
        model = markovify.Text(text)
        addcount()
        sentence = model.make_short_sentence(char, tries=10)
        return sentence
    return ''
if __name__ == '__main__':
    print(generate())
