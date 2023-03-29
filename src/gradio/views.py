import gradio as gr
from src.text import text_service
from src.translate import translate_service

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            seed = gr.Text(label="Input Phrase")
        with gr.Column():
            english = gr.Text(label="Generated Text")
            translation = gr.Text(label="Translated Text")

    seed.change(text_service.generate, inputs=[seed], outputs=[english])
    english.change(translate_service.translate, inputs=[english], outputs=[translation])

    gr.Examples(["My name is Clara and I am"], inputs=[seed])
