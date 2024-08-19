from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

genai.configure(api_key=os.getenv("gemini_key"))
model = genai.GenerativeModel('gemini-1.5-pro')

def getResponse(question:str) :
    response =  model.generate_content(f"Check whether the comment is positive or negative and respond with only positive or neagtive keyword \n {question}")
    return str(response.text).replace('\n','').replace(' ','')


