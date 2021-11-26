# NOTE: File is not running at the moment
FROM python:3.9

COPY . .


RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

CMD ["========== running CI Pipeline =========="]
RUN ls \
    && mkdir ./unittest \
    && python3 -m unittest \
    && pwd && ls

