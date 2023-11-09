import os
from dotenv import load_dotenv
from typing import List
from langchain.schema import Document
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders.sitemap import SitemapLoader

from opencopilot import OpenCopilot
from opencopilot.domain.chat.models.local import LocalLLM

load_dotenv()



llm = LocalLLM(
    temperature=0.7,
    llm_url="http://127.0.0.1:8000/",
)

embeddings = HuggingFaceEmbeddings(model_name="thenlper/gte-base")


copilot = OpenCopilot(
    prompt_file="prompt_template.txt",
    question_template=" {question} [/INST] ",
    response_template="{response} </s><s> [INST]",
    copilot_name="oss_copilot",
    llm=llm,
    embedding_model=embeddings,    
    host="0.0.0.0",
    api_port=3000,
    weaviate_url="http://weaviate:8080"
)
copilot.add_local_files_dir("data")

copilot()
