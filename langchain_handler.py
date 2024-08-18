from langchain import LangChain
from langchain_openai import OpenAI
from langchain_core import ChainType

class LangChainHandler:
    def __init__(self, config):
        self.config = config
        self.lang_chain = LangChain(OpenAI(), chain_type=ChainType.LLM_MATH)

    def generate_response(self, input_text):
        response = self.lang_chain.generate(input_text)
        return response.text