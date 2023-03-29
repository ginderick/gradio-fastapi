import gradio as gr

from src.chat import text_service

examples = [
    ["The Moon's orbit around Earth has"],
    ["The smooth Borealis basin in the Northern Hemisphere covers 40%"],
]
text_demo = gr.Interface(
    fn=text_service.generate, inputs="text", outputs="text", examples=examples
)
