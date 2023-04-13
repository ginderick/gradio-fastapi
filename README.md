# Gradio Text

Text generation and translation from English to German using Gradio and FastAPI


## Installing

There are 2 ways to get a development env running:

### Method 1: Install From Source

```
$ git clone https://github.com/ginderick/gradio-text.git
$ pip3 install -r requirements.txt
$ uvicorn src.main:app -p 8000:8000 --reload
```

### Method 2: Docker
```
$ git clone https://github.com/ginderick/gradio-text.git
$ docker build -t gradio-text .
$ docker run -d --name gradio-text -p 8000:8000 gradio-text
```


### Access Gradio Web App

Go to https://localhost:8000/text-gradio

### Access SwaggerUI

Go to https://localhost:8000/docs



## Built With

* [FastAPI](https://fastapi.tiangolo.com/) - The backend framework used
* [Gradio](https://gradio.app/) - Web interface used
