import streamlit as st
from ai_tools import correct_grammar, generate_paragraph

# Page config
st.set_page_config(page_title="HashWrite AI", page_icon="✍️", layout="centered")

# Title
st.markdown("<h1 style='text-align: center;'>✍️ HashWrite AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Grammar Checker & Paragraph Generator</p>", unsafe_allow_html=True)

st.divider()

# Tabs
tab1, tab2 = st.tabs(["📝 Grammar Checker", "🤖 Paragraph Generator"])

# ------------------ TAB 1 ------------------
with tab1:
    st.subheader("Check Your Grammar")

    text = st.text_area("Enter your text (minimum 30 words):", height=200)

    word_count = len(text.split())
    st.caption(f"Word Count: {word_count}")

    if st.button("🔍 Check Grammar"):
        if word_count < 30:
            st.warning("Please enter at least 30 words.")
        else:
            result = correct_grammar(text)   # ✅ FIXED
            st.success("Corrected Text:")
            st.write(result)

# ------------------ TAB 2 ------------------
with tab2:
    st.subheader("Generate Paragraph")

    topic = st.text_input("Enter a topic:")

    if st.button("✨ Generate"):
        if topic:
            paragraph = generate_paragraph(topic)
            st.success("Generated Paragraph:")
            st.write(paragraph)
        else:
            st.warning("Please enter a topic.")

st.divider()

# Footer
st.markdown("<p style='text-align: center;'> ❤️ </p>", unsafe_allow_html=True)