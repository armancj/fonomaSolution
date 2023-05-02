FROM ubuntu:latest
LABEL authors="mandi"

ENTRYPOINT ["top", "-b"]