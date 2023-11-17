from langchain.embeddings import HuggingFaceEmbeddings
from opencopilot import OpenCopilot

embeddings = HuggingFaceEmbeddings(model_name="thenlper/gte-base")

copilot = OpenCopilot(
    copilot_name="come2sabah copilot",
    llm="gpt-3.5-turbo-16k", # You can also use gpt-4 for improved accuracy
    prompt_file="prompt_template.txt",
    openai_api_key="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",
    embedding_model=embeddings,
    openai_api_base="http://127.0.0.1:1337/v1" #"http://SengTaks-MacBook-Air.local:1234/v1"
)

# Download and embed the knowledge base from given URL
copilot.add_data_urls([
    "https://en.wikipedia.org/wiki/Sabah",
    "https://sabahtourism.com", #tourism
    "https://sedia.com.my", #investment
])

# Run the copilot
copilot()
