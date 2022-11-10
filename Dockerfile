FROM python:3.7
COPY . /app
EXPOSE 8080
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "app:app"]