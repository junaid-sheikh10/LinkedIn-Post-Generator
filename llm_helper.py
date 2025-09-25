from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
load_dotenv()

groq_api_key=os.getenv("GROK_API")

llm=ChatGroq(api_key=groq_api_key,model="llama-3.3-70b-versatile")
#llm_response=llm.invoke("What are the main ingredients of a Margherita pizza?")

if __name__=="__main__":
    response = llm.invoke("Two most important thing is samosa are")
    print(response.content)