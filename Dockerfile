FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

# Start both the API and Streamlit
CMD ["sh", "-c", "flask run --host=0.0.0.0 --port=5000 & streamlit run app.py --server.port=8501 --server.address=0.0.0.0"]

