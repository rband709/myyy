FROM python:latest

WORKDIR /app

COPY requirements.txt /app/
RUN apt update && apt upgrade -y

RUN pip3 install -U pyrogram
RUN pip3 install -U pyrogram tgcrypto

COPY . /app

#set a default command

CMD python3 bot.py
