FROM python:3.10

RUN apt-get update -y && apt-get install -y build-essential

COPY . . 

RUN pip install -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]