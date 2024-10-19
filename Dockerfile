#Build

FROM python AS builder
RUN mkdir -p ./testwebsite
WORKDIR ./testwebsite
COPY . /testwebsite
RUN pip3 install flask
COPY . /testwebsite

#Runtime
FROM python AS runtime
WORKDIR /testwebsite
COPY --from=builder /testwebsite .
RUN pip3 install flask
CMD ["python3","Website.py"]
