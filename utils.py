import os
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
def get_chat_response(prompt,memory,api_key):
    model_config = {
        "openai_api_key": api_key,
        "base_url": "https://openrouter.ai/api/v1",
        "model": "openai/gpt-3.5-turbo",
    }
    model = ChatOpenAI(**model_config)
    chain=ConversationChain(llm=model, memory=memory)
    response = chain.invoke({"input":prompt})
    return response["response"]
memory = ConversationBufferMemory(return_messages=True)


