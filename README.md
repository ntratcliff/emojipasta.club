# emojipasta.club
[emojipasta.club](http://emojipasta.club/) is a web service that exposes RESTful endpoints for generating emojipastas, as well as a simple frontend for generating and tweeting emojipasta sentences. 

# How it works
emojipasta.club uses [Markovify](https://github.com/jsvine/markovify) to generate a text model from a corpus of text scraped from [/r/emojipasta](https://reddit.com/r/emojipasta). 

# API
emojipasta.club exposes two RESTful API endpoints, at `emojipasta.club/gen/` and `emojipasta.club/gen/s/` respectively.

#### /gen/
`/gen/<int: length>` produces a block of text of the specified sentence length. If no length is provided, the default length of 2 is used.

Due to the grammatical nature of emojipasta, the sentence length is not always reliable. However, it works as a rough estimate of block size.

#### /gen/s/
`/gen/s/<int: length>` produces a sententence of the specified maximum character length. If no length is provided, the default length of 140 is used.


