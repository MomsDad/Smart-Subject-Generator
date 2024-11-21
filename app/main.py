import os
from fastapi import FastAPI
from pydantic import BaseModel
from langchain import LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import logging

# set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# load environment variables from the .env file
load_dotenv()

# access the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# initialize the ChatOpenAI model with our API key
chat_model = ChatOpenAI(api_key=openai_api_key, model="gpt-3.5-turbo")

# define the FastAPI app
app = FastAPI()

# enable CORS for all origins (for development purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allows all origins, adjust this if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# define the data model for the email content
class EmailBody(BaseModel):
    content: str

# define a prompt template for generating subject lines
prompt_template = PromptTemplate(
    input_variables=["emailContent"],
    template="Generate three engaging subject lines for the following email content:\n{emailContent}"
)

# create an LLMChain to link the prompt and the ChatGPT model
subject_generation_chain = LLMChain(
    llm=chat_model,
    prompt=prompt_template
)

# root endpoint for basic connectivity
@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Subject Generator!"}

# main endpoint for generating subject lines
@app.post("/generate")
async def generate_subject(email_body: EmailBody):
    emailContent = email_body.content
    logger.info("Generating subject for content: %s", emailContent)

    try:
        result = subject_generation_chain({"emailContent": emailContent})
        logger.info("Received result: %s", result)
    except Exception as e:
        logger.error("Error in generating subject: %s", e)
        return {"error": str(e)}

    # split the `text` field by newline to create a list of suggestions
    subject_suggestions = [line.strip() for line in result["text"].split("\n") if line.strip()]
    return {"suggestions": subject_suggestions}

#Work on Backend Clear DONE and color and container fitting