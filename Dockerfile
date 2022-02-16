FROM python:3.8
LABEL maintainer="voyagerwy130 <voyager.yoshida@gmail.com>"

ENV WORKSPACE /workspace
WORKDIR $WORKSPACE

RUN pip install selenium
    
CMD ["python"]
