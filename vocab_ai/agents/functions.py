from langchain_community.document_loaders import YoutubeLoader
from vocab_ai.exception_handler.exception import SystemException
import sys

def transcript(link: str): 
    try:
        loader = YoutubeLoader.from_youtube_url(youtube_url=link, add_video_info=False)
        docs = loader.load()
        content = docs[0].page_content
        return content
    except Exception as e:
        raise SystemException(e, sys)
    
