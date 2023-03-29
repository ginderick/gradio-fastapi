import gradio as gr

from src.chat import chat_service

chat_demo = gr.Interface(fn=chat_service.greet, inputs="text", outputs="text")
