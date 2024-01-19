# dockerized-stanza-nlp

docker build -t lazerjesus/dockerized-stanza-nlp .

docker run -p 5050:5000 -v stanza_resources:/root/stanza_resources lazerjesus/dockerized-stanza-nlp


## Clone project 

````
git clone https://github.com/vivalence/dockerized-stanza-nlp.git
````

## Change directory
````
cd dockerized-stanza-nlp
````

## First running option

### Build Docker image

````
docker build -t stanza-nlp .
````
stanza-nlp is image name. You can custome this name.

### Create and run container
````
docker run -it -v "./script.py:/app/stanza/script.py" stanza-nlp python3 script.py
````

'./script.py' is file location of python script.
stanza-nlp is image name that already build.


## Second running option

### Build and running container
````
docker compose up -d
```` 

### Check container name 
````
docker compose ps -a
````

### Check output of container
````
docker logs -f  stanza-nlp
````
stanza-nlp is container name, please make sure it right.

### Modify script
To modify script, open `script.py` file, modify and saved. Then restart docker container with `docker compose restart`. Finally, check script result with show log `docker logs -f  stanza-nlp`.


## API use
Open you API client, i.e : postman, insomnia, etc. Use this details below.
````
url : http://localhost:5000/nlp
method : POST
data :
	langfrom : .....
	stringnlp : text will be proccess
	annotations : pos,upos,ner,lemma,depparse,parse
````

````
langfrom value :
-af->Afrikaans
-grc->Ancient Greek
-ar->Arabic
-hy->Armenian
-eu->Basque
-be->Belarusian
-bg->Bulgarian
-bxr->Buryat
-ca->Catalan
-zh->Chinese (simplified)
-zh-Hant->Chinese (traditional)
-lzh->Classical Chinese
-cop->Coptic
-hr->Croatian
-cs->Czech
-da->Danish
-nl->Dutch
-en->English
-et->Estonian
-fi->Finnish
-fr->French
-gl->Galician
-de->German
-got->Gothic
-el->Greek
-he->Hebrew
-hi->Hindi
-hu->Hungarian
-id->Indonesian
-ga->Irish
-it->Italian
-ja->Japanese
-kk->Kazakh
-ko->Korean
-kmr->Kurmanji
-la->Latin
-lv->Latvian
-lt->Lithuanian
-olo->Livvi
-mt->Maltese
-mr->Marathi
-sme->North Sami
-no->Norwegian (Bokmål)
-nn->Norwegian (Nynorsk)
-cu->Old Church Slavonic
-fro->Old French
-orv->Old Russian
-fa->Persian
-pl->Polish
-pt->Portuguese
-ro->Romanian
-ru->Russian
-gd->Scottish Gaelic
-sr->Serbian
-sk->Slovak
-sl->Slovenian
-es->Spanish
-sv->Swedish
-swl->Swedish Sign Language
-ta->Tamil
-te->Telugu
-tr->Turkish
-uk->Ukrainian
-hsb->Upper Sorbian
-ur->Urdu
-ug->Uyghur
-vi->Vietnamese
-wo->Wolof
````
<div align="center"><img src="https://github.com/vivalence/dockerized-stanza-nlp/blob/docker/post-example.png" /></div>

