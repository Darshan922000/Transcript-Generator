from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

llm = ChatGroq(model="gemma2-9b-it")
#gemma2-9b-it
# llama-4-maverick-17b-128e-instruct