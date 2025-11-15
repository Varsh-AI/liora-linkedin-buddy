import streamlit as st
from fewshot import SampleRetriever
from post_generator import generate_post

# Initialize retriever
retriever = SampleRetriever()

LENGTHS = ["Short", "Medium", "Long"]
LANGS = ["English", "Hinglish"]

# Streamlit page config
st.set_page_config(
    page_title="Liora - LinkedIn Post Buddy",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="auto",
)

# Custom CSS for blue-white theme and black text for labels/headings
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f8ff;  /* Light blue background */
        color: #0d1b2a;  /* Default text */
    }
    .css-18e3th9 {
        background-color: #ffffff;  /* White main container */
        border-radius: 15px;
        padding: 20px;
        box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #1e90ff;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        font-weight: bold;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #0b66c3;
    }
    /* Make the widget labels black */
    label {
        color: #000000 !important;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def main():
    # App header
    st.markdown(
        "<h1 style='text-align:center; color:#1e90ff;'>Liora 🤖</h1>", 
        unsafe_allow_html=True
    )
    st.markdown(
        "<h3 style='text-align:center; color:#0d1b2a;'>Your LinkedIn Post Buddy</h3>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align:center; color:#0d1b2a;'>Generate engaging LinkedIn posts in seconds!</p>",
        unsafe_allow_html=True
    )

    # Inputs
    col1, col2, col3 = st.columns(3)

    with col1:
        topic = st.selectbox("Choose Topic", retriever.list_tags())

    with col2:
        size = st.selectbox("Post Length", LENGTHS)

    with col3:
        lang = st.selectbox("Language", LANGS)

    # Generate post button
    if st.button("Generate Post"):
        post = generate_post(length=size, language=lang, tag=topic)
        # Styled heading for generated post
        st.markdown("<h3 style='color:#000000;'>Generated Post</h3>", unsafe_allow_html=True)
        st.write(post)

if __name__ == "__main__":
    main()
