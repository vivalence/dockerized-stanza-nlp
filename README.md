# dockerized-stanza-nlp

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

