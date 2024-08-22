FROM python:3.9-slim-buster

WORKDIR /myportfolio

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

# Copy the wait-for-it script into the container
COPY wait-for-it.sh /wait-for-it.sh

# Ensure the database is initialized after MySQL is ready
CMD ["sh", "-c", "/wait-for-it.sh mysql:3306 -- python -c 'from app import initialize_database; initialize_database()' && flask run --host=0.0.0.0"]


EXPOSE 5001