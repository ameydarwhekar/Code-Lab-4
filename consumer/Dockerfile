FROM python

# Install the python library flask and requests
RUN pip install Flask
RUN pip3 install requests

# Creating volume
VOLUME app

# Creating a WORKDIR app to unify all the elements
WORKDIR /app

EXPOSE 80

ENTRYPOINT ["python"]
CMD ["consumer.py"]