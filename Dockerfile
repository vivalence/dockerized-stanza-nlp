# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && \
    apt-get install -y  \
    --no-install-recommends \
    build-essential \
    cmake \
    wget \
    git \
    nano \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*


# Install Stanza
RUN pip install --upgrade pip

RUN git clone https://github.com/stanfordnlp/stanza.git
#RUN cd stanza
WORKDIR /app/stanza

RUN pip install -e .

# Copy the current directory contents into the container at /app/stanza
WORKDIR /app/stanza


# Run script.py when the container launches
#CMD ["python", "script.py"]
