from transformers import pipeline

pipe = pipeline("translation", model="t5-base")


def translate(text: str):
    return pipe(text)[0]["translation_text"]
