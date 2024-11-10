# import fastapi
import os
import httpx
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi import FastAPI, WebSocket, Request, Form
from starlette import status
from app_llama import ollama_response, pull_model

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/model")
def model():
    return FileResponse('templates/model.html')


@app.post('/postdata')
def postdata(model=Form()):
    pull_model(model)
    return RedirectResponse('/', status_code=status.HTTP_302_FOUND)


@app.get("/", response_class=HTMLResponse)
def read_index(request: Request):
    """
    Страница чата
    """
    # Render the HTML template
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    Сокет для обработки сообщения, он подключается в форме шаблона через JS.
    Отправляет сообщение пользователя в подключенную модель.
    Возвращает сообщение от модели
    """
    history = []

    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
            text, text_response = ollama_response(data, history)
            history.append([text, text_response])
            try:
                await websocket.send_text(text)
            except Exception as e:
                print(e)
        except httpx.ConnectError:
            await websocket.send_text("Модель не отвечает. Обновите страницу, и попробуйте снова")
