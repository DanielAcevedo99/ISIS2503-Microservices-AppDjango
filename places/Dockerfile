FROM python:3.8.10-alpine3.13

WORKDIR /app

# Copy the Django app to the working directory
COPY . /app

# Set the environment variables
ENV PLACES_DB_HOST 10.128.0.7
ENV MEASUREMENTS_DB_HOST 10.128.0.3

# Install Python dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["sh", "init.sh"]
