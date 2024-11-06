# Smart-Subject-Generator
Subject Generator for CSCI

### For Group Mates: Hi everyone below is detailed instructions on how to run a virtual machine on our local machine for our testing and web application

1. The First Step is installling Python 3.8 + if you don't have that I have attached that here https://www.python.org/downloads/
2. Use Git to Clone the project repository and navigate to our project directory

   
git clone https://github.com/MomsDad/Smart-Subject-Generator.git

cd Smart-Subject-Generator

3. Setup our virtual environment
python -m venv venv
# WINDOWS:
venv\Scripts\activate
# Mac  :
source venv/bin/activate

4. Install our dependencies!
pip install -r requirements.txt
5. Run a test to make sure it works by running our fastapi
   
uvicorn app.main:app --reload

6. Confirm it all works by going to this url on any browser you would like!
http://localhost:8000/

You will see the message on your browser, pretty cool stuff! This is the entire key to our project, work in main.py or add more files and create a web application for our subject generation.

### Project Workflow
All work should be done inside the app/main.py file or by adding additional files as needed.

### Explainations for how everything works is below, i've got no problem with changing anything or everything please just let me know !

# FastApi
Runs FastApi on Start using port 8000(default)
Here's a breakdown of fastapi it's gonna be simple ! https://realpython.com/fastapi-python-web-apis/

example below of fastapi usage, this will allow you to visit on you local machine the message Hello, World. I added this to our code for our setup so we can see how it works!

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


# uvicorn 
This is the server that runs FastApi
Here's a breakdown of it but it's not that important to learn https://www.uvicorn.org/

example below of how we will run our main.py:

uvicorn app.main:app --reload

# langchain
This is a library that will help us integrate our LLMs into our project basically langchain is a way to interact with Chatgpt like how a person would send a chat message!
Here is a guide on langchain for simple integeration: https://python.langchain.com/docs/tutorials/llm_chain/

# pydantic
Helps us define and validate our data in our FastApi App it will ensure that the data we are filling is correct and formatted
For example for our project we will use the pydantic function to validate the content in our emails to our API for subject generation
If you scroll to pydantic examples it shows exactly how it works, https://docs.pydantic.dev/latest/#why-use-pydantic

example below included in main.py:

from pydantic import BaseModel

class EmailContent(BaseModel):
    content: str

the above code will very simply make sure that whatever content is being entered in is indeed a STRING!


# ADDED How to USE

1. **Clone the Repository:**
   ```bash
   git clone https://your-repository-url.git
   cd Smart-Subject-Generator

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

OPENAI_API_KEY=your-openai-api-key

uvicorn app.main:app --reload

http://127.0.0.1:8000 I WOULD JUST USER THE USERINTERFACE.html !
