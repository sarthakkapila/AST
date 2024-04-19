import os
from langchain_community.chat_models import ChatCohere
from langchain_community.chat_models import ChatAnthropic
import google.generativeai as genai
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from getpass import getpass

anthropic_api_key = ""
groq_api_key = ""
gemini_api_key = ""
# os.environ["ANTHROPIC_API_KEY"] = getpass()

class LLM:
    def __init__(self, base_model):
        self.base_model = base_model
        self.groq_api_key = groq_api_key
        self.anthropic_api_key = anthropic_api_key
        self.gemini_api_key = gemini_api_key

        try:
            if self.base_model == "Gemini":
                os.environ['GOOGLE_API_KEY'] = self.gemini_api_key
                genai.configure(api_key=self.gemini_api_key)
            elif self.base_model == "Anthropic":
                os.environ['ANTHROPIC_API_KEY'] = self.anthropic_api_key
            elif self.base_model == "Groq":
                os.environ['GROQ_API_KEY'] = self.groq_api_key
        except Exception as e:
            print("There's some problem with your model", e)

    def inference(self, prompt):
        if self.base_model == "Gemini":
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt).text
        elif self.base_model == "Anthropic":
            model = ChatAnthropic(temperature=0, model_name="claude-3-sonnet-20240229")
            chain = model | StrOutputParser()
            response = chain.invoke(prompt)
        elif self.base_model == "Groq":
            model = ChatGroq(temperature=0, api_key=self.groq_api_key, model_name="mixtral-8x7b-32768")
            chain = model | StrOutputParser()
            response = chain.invoke(prompt)
        return response

# --------------------------USAGE------------------------
# base_model = "Groq"
# llm = LLM(base_model)
# while True:
#     prompt = input("Enter your prompt: ")
#     result = llm.inference(prompt)
#     print(result)
#     break