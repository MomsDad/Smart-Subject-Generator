from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# here's a really good example of how this works using pydantic, https://docs.pydantic.dev/latest/#pydantic-examples scroll to pydantic examples
class EmailBody(BaseModel):
    content: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Subject Generator!"}

# this is our main indication of our project we want to generate email subject lines
@app.post("/generate")
def generate_subject(email_body: EmailBody):
    email_content = email_body.content
    
    # I haven't looked into the specifics on how to complete this so I wrote some placegolder logic
    # in future, we can use LangChain or anything else
    subject_suggestions = [
        "Re: " + email_content[:50],  # Example: Taking the first 50 chars of email content
        "Important: " + email_content.split()[0],  # Example: Adding first word of the content
        "Don't Miss: " + email_content[:30]  # Example: First 30 chars of content
    ]
    
    return {"suggestions": subject_suggestions}