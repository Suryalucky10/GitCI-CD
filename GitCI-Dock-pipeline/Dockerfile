FROM python:3.12
WORKDIR /simplecalculator
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "simplecalculator.py"]
