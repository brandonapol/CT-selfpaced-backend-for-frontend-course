FROM python

WORKDIR /app

COPY requirements.txt requirements.txt 
RUN python -m venv venv 
RUN apt-get update
RUN apt install build-essential
RUN venv/bin/pip install -r requirements.txt 
RUN pip3 install -r requirements.txt

COPY app app 
COPY config.py config.py 
COPY models.py models.py
COPY forms.py forms.py
COPY helpers.py helpers.py
COPY boot.sh boot.sh 
RUN chmod +x boot.sh 

EXPOSE 5000

RUN ./boot.sh

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]