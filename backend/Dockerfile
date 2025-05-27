FROM python:3.9-slim

WORKDIR /code

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 80

CMD ["fastapi", "run" , "app/main.py", "--port", "80"]
