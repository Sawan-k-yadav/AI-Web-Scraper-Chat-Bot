## For learning how streamlit work to create UI using streamlit in python

import streamlit as st

# with st.chat_message(name='assistant', avatar=""):   # We can keep name as user or assistant and avatar will 
                                                       # any emoji or picture path
#     st.write("Hello")

# with st.chat_message(name='user'):
#     st.write("Hello....")

st.title("Echo Bot")

# Initialize chat history so that all the precious chats which we will do with bot will be appear above
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
# We used the := operator to assign the user's input to the prompt variable 
# and checked if it's not None in the same line.

# prompt = st.chat_input("What is up?")

# if prompt:

# Above condition can also be written as below using := operator

if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})