FROM python:3.8.2
WORKDIR /app
COPY . /app
EXPOSE 8080
RUN pip install -r requirements.txt
CMD python3 co-lab.py
