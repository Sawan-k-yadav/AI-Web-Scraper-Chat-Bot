# import streamlit as st
# from utils.web_scrape import scrape_website
# from transformers import DistilBertTokenizer, DistilBertModel, pipeline


# tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
# model = DistilBertModel.from_pretrained("distilbert-base-uncased")


# # Scrape website data
# website_url = st.text_input("Enter your url?")
# website_data = scrape_website(website_url)


# # Generate chatbot responses
# def generate_response(user_input):
#     # Process user input and generate response using model

#     # check if the user input is a URL
#     if 'http' in user_input or 'www' in user_input:
#         scraped_text = scrape_website(user_input)
#         user_input += " " + scraped_text

#     # encode the input text
#     user_input = tokenizer.encode(user_input, return_tensors='pt')

#     # Create an input dictionary for DistilBertModel
#     input_dict = {'input_ids': user_input}
#     # generate a response
#     # response = model.generate(user_input, max_length=500, num_return_sequences=1)
#     response = model(**input_dict)

#     first_sequence = response[0]

#     print(first_sequence[0])

#     token_ids = first_sequence[0]

#     print(tokenizer.decode(token_ids))
#     # decode the response
#     response_text = int(tokenizer.decode(token_ids))

#     return response_text


# # Streamlit UI
# st.title("Web Scrape Chatbot Demo")
# user_input = st.text_input("Ask me anything")
# response = generate_response(user_input)
# st.write(response)

# #---------------------------------------

# # Load model and tokenizer
# model_name = "distilbert-base-uncased"
# model = pipeline("text-generation", model=model_name)

# # Scrape website data
# website_url = st.text_input("Enter website URL")
# website_data = scrape_website(website_url)

# # Generate chatbot responses
# def generate_response(user_input):
#     # Process user input and generate response using model
#     response = model(user_input)
#     return response

# # Streamlit UI
# st.title("Chatbot Demo")
# user_input = st.text_input("Ask me anything")
# response = generate_response(user_input)
# st.write(response)
    



