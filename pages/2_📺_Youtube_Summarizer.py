import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from tools.youtube_summarizer import youtube_summarizer as ys

st.set_page_config(
    page_title="Youtube Summarizer",
    page_icon="📺",
)

st.title('📺 Youtube Summarizer')

st.markdown('''Enter a Youtube video URL and get a summary of the video!''')

url = st.text_input('URL', 'https://www.youtube.com/watch?v=TEa3-O4tgr8&ab_channel=TOPDEIMPACTO')

if st.button('Summarize'):
    st.write('Summarizing...')
    summary = ys.summarize(url)
    st.write('Done!')
    st.write(summary)


# Sidebar contents
with st.sidebar:
    st.title('🤗💬 HugChat App')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [HugChat](https://github.com/Soulter/hugging-chat-api)
    - [OpenAssistant/oasst-sft-6-llama-30b-xor](https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor) LLM model
    
    💡 Note: No API key required!
    ''')
    add_vertical_space(5)
    st.write('Made by [Noel Moreno Lemus](https://www.linkedin.com/in/nmlemus/)')