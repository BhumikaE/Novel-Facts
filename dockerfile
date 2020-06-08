FROM python:3.7 
WORKDIR /app
copy requirements.txt ./requirements.txt
RUN apt-get install libsm6 libxrender1 libfontconfig1
RUN pip install -r requirements.txt
EXPOSE 8080
copy ./src/ /app
CMD streamlit run --server.port 8080 --server.enableCORS false app.py