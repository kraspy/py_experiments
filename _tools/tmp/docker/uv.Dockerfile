FROM astral/uv:python3.14-alpine

WORKDIR /app

COPY . /app/

ARG TMPARG

RUN echo "TMPARG: ${TMPARG}"

CMD ["uv", "run", "python", "main.py"]