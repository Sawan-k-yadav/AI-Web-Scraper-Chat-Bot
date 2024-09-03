# We will use ollama to work with LLM locally so that we don't need to pay anything

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

## Defining prompt template which model will take and understand the requirement as per the DOM content of website
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# model = OllamaLLM(model="llamma3") 
model = OllamaLLM(model="gemma2:2b")

def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | model   # This defines that first it will take prompt and model with prompt

    parse_results = []

    for i, chunk in enumerate(dom_chunks, start=1):   # To start the parse from 1 and not 0
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parse_results.append(response)

    return "\n".join(parse_results)