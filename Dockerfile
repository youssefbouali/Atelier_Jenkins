FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
#RUN pip install -r requirements.txt
#RUN pip install --progress-bar off -r requirements.txt
COPY . .
CMD ["python", "app.py"]