# import fastapi
import os
import httpx
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi import FastAPI, WebSocket, Request, Form
from starlette import status
from app_llama import ollama_response


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def root():
    """
    Страница ввода Ключа
    """
    return FileResponse("templates/get_key.html")


@app.post("/postdata")
def postdata(api_token=Form()):
    """
    Сохранение ключа в переменные виртуального окружения
    :param api_token: Ключ.
    :return: перенаправление на страницу чата с GPT
    """

    # Сохраняем введенное значение API_TOKEN в переменную окружения
    os.environ['API_TOKEN'] = api_token
    return RedirectResponse('/message', status_code=status.HTTP_302_FOUND)


@app.get("/message", response_class=HTMLResponse)
def read_index(request: Request):
    """
    Страница чата
    """
    # Render the HTML template
    return templates.TemplateResponse("index.html", {"request": request})


# def get_ai_response(message):
#     """
#     Функция, которая работает с моделью
#     :param message:
#     :return:
#     """
#     if message:
#         # Достаем переменную из виртуального окружения и выводим в сообщение
#         API_TOKEN = os.getenv('API_TOKEN')
#         return [message,]


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

            # Добавление истории в разговор
            # TODO Нужно сохранять историю в базу данных
            history.append([text, text_response])
            try:
                # async for text in texts:
                await websocket.send_text(text)
            except Exception as e:
                print(e)
        except httpx.ConnectError:
            await websocket.send_text("Модель не отвечает. Обновите страницу, и попробуйте снова")


