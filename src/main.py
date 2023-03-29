import gradio as gr
from fastapi import FastAPI

from src.api import api_router
from src.text.text_gradio_views import text_demo
from src.constants.path_constants import PathConstants

app = FastAPI(title="Gradio Demo with FastAPI")


app.include_router(api_router)


chat_gradio_app = gr.mount_gradio_app(
    app, text_demo, path=PathConstants.CHAT_GRADIO_APP
)


app.mount(PathConstants.CHAT_GRADIO_APP, chat_gradio_app)
