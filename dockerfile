FROM python:3.6.12
WORKDIR /
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY factorial-digits.py .
ENTRYPOINT ["python", "-m", "factorial-digits"]
