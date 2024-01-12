# dockerized-stanza-nlp

## Clone project 

````
git clone https://github.com/vivalence/dockerized-stanza-nlp.git
````

## Change directory
````
cd dockerized-stanza-nlp
````

## Build Docker image

````
docker build -t stanza-nlp .
````

## Create and run container
````
docker run -it  stanza-nlp
````

## Try stanza-nlp
````
>>> import stanza
>>> stanza.download('en')       # This downloads the English models for the neural pipeline
>>> nlp = stanza.Pipeline('en') # This sets up a default neural pipeline in English
>>> doc = nlp("Barack Obama was born in Hawaii.  He was elected president in 2008.")
>>> doc.sentences[0].print_dependencies()

````
