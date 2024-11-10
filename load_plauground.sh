#!/bin/bush

wget https://github.com/alastergrume/OllamaLocalFastApi/archive/master.zip
sudo apt install unzip
unzip master.zip
rm master.zip
cd OllamaLocalFastApi-main/
docker build -t fastapiapp .
docker run -d --name fastapiapp -p 8000:80 fastapiapp
docker run -d -v ollama:/root/.ollama -p 11434:11434  ollama/ollama