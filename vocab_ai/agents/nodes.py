from langgraph.constants import Send
from vocab_ai.instructor.instructions import instruction
from vocab_ai.structure.schema import State
from vocab_ai.llm.planner import llm
from langchain_core.messages import SystemMessage, HumanMessage
from vocab_ai.logging.logger import logging
from vocab_ai.exception_handler.exception import SystemException
import sys
import os
from dotenv import load_dotenv
load_dotenv()
from vocab_ai.agents.functions import transcript


os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_PROJECT"]=os.getenv("LANGSMITH_PROJECT")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Nodes
def vocab_ai(state: State):
    """AI agent that understand user query and extract vocabs"""
    logging.info("Entered in Vocab AI")
    try:

        content = transcript(state['link'])
        print(content)

        vocabs = llm.invoke(
            [
            SystemMessage(content=instruction),
            HumanMessage(
                content=f"Here is the transcript of the video: {content}"
            ),
        ]
    )

        
        logging.info(f"Out from Vocab AI")
        return {"vocabs": vocabs}
    except Exception as e:
        raise SystemException(e, sys)
    