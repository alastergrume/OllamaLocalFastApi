import ollama
from ollama import Client

client = Client(host='http://10.129.0.32:11434')



def ollama_response(history, message):
    """
    Взаимодействие с Ollama
    """
    # client.pull(model='llama3.2')
    response = client.chat(model='mistral', messages= [
                    {
                            'role': 'user',
                            'content': f'{message}, History:{history}'
                        },
                    ])

    return [response['message']['content']], response


def show_model():
    models = client.list()
    model_number = 1
    models_list = []
    for i in models['models']:
        print(f'{model_number}. {i["name"]}')
        model_number += 1
        models_list.append(i["name"])
    return models_list
    # choice_model = int(input("Выберите модель - "))
    # return models_list[choice_model - 1]