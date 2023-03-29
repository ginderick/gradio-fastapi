from fastapi import FastAPI

import gradio as gr
from src.api import api_router
from src.constants.path_constants import PathConstants
from src.gradio.views import demo

app = FastAPI(title="Gradio Demo with FastAPI")


app.include_router(api_router)


chat_gradio_app = gr.mount_gradio_app(app, demo, path=PathConstants.CHAT_GRADIO_APP)


app.mount(PathConstants.CHAT_GRADIO_APP, chat_gradio_app)
