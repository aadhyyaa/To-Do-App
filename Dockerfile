FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt
RUN python -m ensurepip --upgrade && \
    pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ['python', 'app.py']
