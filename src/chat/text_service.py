from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")


class ChatService:
    def __init__(self) -> None:
        pass

    def generate(self, text: str):
        result = generator(text, max_length=30, num_return_sequences=1)
        return result[0]["generated_text"]


text_service = ChatService()
