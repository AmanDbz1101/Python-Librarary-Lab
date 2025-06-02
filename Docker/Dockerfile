#base image 
FROM python:3.12

# set the working directory in the container
WORKDIR /app

# copy the current directory contents into the container at /app
COPY . /app

# install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# port
EXPOSE 8501

# command 
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]