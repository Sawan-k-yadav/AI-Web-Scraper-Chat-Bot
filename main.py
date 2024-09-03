import streamlit as st
from scraper import scraper, clean_body_content, extract_body_content, split_dom_content
from parse import parse_with_ollama

st.title("AI Web Scraper")

url = st.text_input("Enter Website URL : ")

if st.button("Scrape Website"):
    st.write("Scrapping Website....")
    result = scraper(url)

    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    # Creating session of cleaned content to access it later
    st.session_state.dom_content = cleaned_content

    with st.expander("Veiw DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=400)


if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what do you want to parse? ")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(parsed_result)