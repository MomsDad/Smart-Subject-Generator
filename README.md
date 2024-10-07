# Smart-Subject-Generator
Subject Generator for CSCI

### For Group Mates: Hi everyone I have created our dockerfile, our main.py for our code and finally our requirements.txt file. Here are steps to get started

1. The First Step is installling docker here is the link https://docs.docker.com/desktop/install/windows-install/
2. You need to clone the project repository using
git clone https://github.com/MomsDad/Smart-Subject-Generator.git
cd Smart-Subject-Generator
3.Build the Docker Image using please include the '.' it's a require arguement
docker build -t smart-subject-generator .
4. Run the docker container. We are by default always going to be on port 8000
docker run -d -p 8000:8000 smart-subject-generator
5. Test that it all works, open up your browser of choice I used chrome and enter this as the url
http://localhost:8000/

You will see the message on your browser, pretty cool stuff! This is our entire key to our project, work in main.py or add more files and create a web application for our subject generation.


### Explainations for how everything works is below, i've got no problem with changing anything or everything please just let me know !

# Dockerfile
The Dockerfile is key because it creates a virtual machine similar to VMWARE. By using Docker we are able to test our porject consistently across a wide range of different environments,
this helps us eliminate individual setup issues, once I build it we will all consistently have the same exact setup.

# Inside the Docker is the following

Our Base Image: We are using Python 3.11
Dependencies: Installs all of our packages I listed in requirements.txt
Runs FastApi on Start using port 8000(default)
Here's a breakdown of fastapi it's gonna be simple ! https://realpython.com/fastapi-python-web-apis/

# example below of fastapi usage, this will allow you to visit on you local machine the message Hello, World!

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


