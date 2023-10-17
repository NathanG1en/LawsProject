import streamlit as st
from dotenv import load_dotenv



def main():
    load_dotenv()
    st.set_page_config(page_title="Welcome to the Phone Guru", page_icon=":phone:")

    st.header("Learn about Environmental Laws")
    st.text_input("What do you want to know?")

    with st.sidebar:
        st.subheader("PDFs go here")
        st.file_uploader("Upload your PDFs here and click on Process") # change the subheader to match what I need 
        st.button("Process")


if __name__ == '__main__':
    main()