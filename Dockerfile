FROM public.ecr.aws/lambda/python:3.9

COPY requirements.txt ./
RUN python3.9 -m pip install -r requirements.txt -t .

COPY python/app.py ./
COPY python/commands ./commands

CMD ["app.lambda_handler"]