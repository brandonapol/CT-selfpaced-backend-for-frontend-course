FROM python:3.10

WORKDIR /app

# Copy all source files
COPY app app 
COPY config.py config.py 
COPY models.py models.py
COPY forms.py forms.py
COPY helpers.py helpers.py
COPY boot.sh boot.sh 
RUN chmod +x boot.sh

# Create virtual environment
RUN python -m venv venv 

# Activating a virtual environment requires the use of `source` (using `. boot.sh` is the same as using source).
# Sourcing from WITHIN a bash script will source it inside that script,
# and the configuration will be lost when you exit boot.sh,
# meaning you are not IN the virtual environment.
# Think of running a script as starting a totally new bash terminal,
# while `source` is like you copy pasted the script into your current terminal.
# Wrong
# RUN ./boot.sh
# Correct
RUN . ./boot.sh
# Can now install packages inside the virtual environment
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV FLASK_APP=app
ENV FLASK_ENV=development

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]