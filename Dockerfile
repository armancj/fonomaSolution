FROM tiangolo/uvicorn-gunicorn:python3.8

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--reload"]