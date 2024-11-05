import os
from fastapi import FastAPI
from pydantic import BaseModel
from langchain import LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from the .env file
load_dotenv()

# Access the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the ChatOpenAI model with our API key
chat_model = ChatOpenAI(api_key=openai_api_key, model="gpt-3.5-turbo")

# Define the FastAPI app
app = FastAPI()

# Enable CORS for all origins (for development purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, adjust this if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the data model for the email content
class EmailBody(BaseModel):
    content: str

# Define a prompt template for generating subject lines
prompt_template = PromptTemplate(
    input_variables=["email_content"],
    template="Generate three engaging subject lines for the following email content:\n{email_content}"
)

# Create an LLMChain to link the prompt and the ChatGPT model
subject_generation_chain = LLMChain(
    llm=chat_model,
    prompt=prompt_template
)

# Root endpoint for basic connectivity
@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Subject Generator!"}

# Main endpoint for generating subject lines
@app.post("/generate")
async def generate_subject(email_body: EmailBody):
    email_content = email_body.content
    logger.info("Generating subject for content: %s", email_content)

    try:
        result = subject_generation_chain({"email_content": email_content})
        logger.info("Received result: %s", result)
    except Exception as e:
        logger.error("Error in generating subject: %s", e)
        return {"error": str(e)}

    # Split the `text` field by newline to create a list of suggestions
    subject_suggestions = [line.strip() for line in result["text"].split("\n") if line.strip()]
    return {"suggestions": subject_suggestions}
