#Based on Python
FROM python

# Install the python library flask and requests
RUN pip install Flask
RUN pip install requests

# Creating a volume
VOLUME app

# Creating a WORKDIR app to unify all the elements
WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["api.py"]