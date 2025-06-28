# from vocab_ai.system.graph import vocab
import streamlit as st
from vocab_ai.agents.functions import transcript

# def vocabulary(link : str):
#     graph = vocab()
#     response = graph.invoke({"link": link})
#     result = response["vocabs"].content
#     return result
# Streamlit app setup
def main():
    # Center the title using HTML
    st.markdown("<h1 style='text-align: center;'>🤖Vocab AI🤖</h1>", unsafe_allow_html=True)

    # Input box for user request
    user_input = st.text_input("Enter a YouTube video link to get the vocabulary from the video:")
    
    if st.button("Get transcripts"):
        if user_input:
            # result = vocabulary(user_input)
            # Increase font size of the result
            print(type(user_input))
            result = transcript(user_input)
            print(result)
            st.markdown(f"<div style='font-size:20px;'>{result}</div>", unsafe_allow_html=True)
        else:
            st.write("Please enter a request.")

if __name__ == "__main__":
    main()

