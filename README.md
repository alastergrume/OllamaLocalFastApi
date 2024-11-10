Клонирование репозитория:
    
    wget https://github.com/alastergrume/OllamaLocalFastApi/archive/master.zip

Распаковка архива
    
    sudo apt install unzip
    unzip master.zip
    rm master.zip

Запуска приложений

    cd OllamaLocalFastApi-main/
    chmod +x load.sh
    bash load.sh

# TODO Создание docker-compose для настройки внутренней сети взаимодействия контейнеров
# TODO Сделать функцию и страницу для отображения загруженных моделей. Так же написать логику для загрузки моделей при первом запуске. Сейчас работает на загрузку модели 'llama3.2:1b'
