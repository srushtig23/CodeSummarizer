import streamlit as st
from model_utils import load_model, summarize_code
from parser_utils import extract_functions

st.set_page_config(page_title="CodeSummarizer Mini", layout="wide")
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stSpinner {
        color: #ff4b4b !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧠 CodeSummarizer Mini")
st.markdown("Upload a Python file and get ML-generated summaries of its functions and classes.")

uploaded_file = st.file_uploader("📄 Upload a `.py` file", type=["py"])

if uploaded_file:
    file_content = uploaded_file.read().decode("utf-8")
    functions = extract_functions(file_content)
    
    if not functions:
        st.warning("No functions or classes found in the uploaded file.")
    else:
        tokenizer, model = load_model()
        st.success(f"✅ Found {len(functions)} function(s)/class(es).")
        
        for name, code in functions:
            with st.expander(f"📘 {name}"):
                st.code(code, language="python")
                with st.spinner("🔍 Generating summary..."):
                    summary = summarize_code(code, tokenizer, model)
                    st.markdown(f"**📝 Summary:** {summary}")
