#!/bin/bush

docker build -t fastapiapp .
docker run -d --name fastapiapp -p 8000:80 fastapiapp
docker run -d -v ollama:/root/.ollama -p 11434:11434  ollama/ollama