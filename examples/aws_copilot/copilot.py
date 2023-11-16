from langchain.embeddings import HuggingFaceEmbeddings
from opencopilot import OpenCopilot

embeddings = HuggingFaceEmbeddings(model_name="thenlper/gte-base")

copilot = OpenCopilot(
    copilot_name="AWS CLI Copilot",
    llm="gpt-3.5-turbo-16k", # You can also use gpt-4 for improved accuracy
    prompt_file="prompt_template.txt",
    openai_api_key="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",
    embedding_model=embeddings,

)

# Download and embed the knowledge base from given URL
copilot.add_data_urls([
    "https://awsdocs.s3.amazonaws.com/cli/latest/aws-cli.pdf",
])

# Run the copilot
copilot()
