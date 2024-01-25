# dockerized-stanza-nlp

docker build -t lazerjesus/dockerized-stanza-nlp .

docker run -p 5050:5000 -v stanza_resources:/root/stanza_resources lazerjesus/dockerized-stanza-nlp
