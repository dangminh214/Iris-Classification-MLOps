FROM python:3.12
LABEL authors="dang-minh"

WORKDIR /src

COPY model.pkl /src/model.pkl 
COPY server.py /src/server.py
COPY requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8888"]