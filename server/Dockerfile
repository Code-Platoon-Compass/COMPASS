FROM python:3.12-trixie
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "task_api.wsgi", "--bind", "0.0.0.0:8000"]