from transformers import pipeline

pipe = pipeline("translation", model="t5-base")


class TranslateService:
    def translate(self, text: str):
        return pipe(text)[0]["translation_text"]


translate_service = TranslateService()
