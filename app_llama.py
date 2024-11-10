from ollama import Client

client = Client(host='http://127.0.0.1:11434')


def ollama_response(history, message):
    """
    Взаимодействие с Ollama
    """
    # client.pull(model='llama3.2')
    response = client.chat(model='llama3.2:1b', messages=[
        {
            'role': 'user',
            'content': f'{message}, History:{history}'
        },
    ])

    return [response['message']['content']], response


def pull_model(model):
    client.pull(model=model)
