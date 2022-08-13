FROM python:3.10

ENV TZ=Europe/Prague
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
RUN chmod +x /app/start.sh
ENTRYPOINT ["./start.sh"]