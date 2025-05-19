import streamlit as st
from src.scanner import scan
from src.reporter import generate_report

st.set_page_config(page_title="OSINT Tool", page_icon="🔍")

st.title("🕵️ OSINT Tool 🔍")
st.markdown("Podaj domenę, a narzędzie sprawdzi publiczne podatności.")

target = st.text_input("🎯 Cel:")

if st.button("Skanuj"):
    if target:
        with st.spinner("Skanowanie w toku..."):
            result = scan(target)
        
        report = generate_report(result)
        st.markdown(report)
        st.success("Skanowanie zakończone!")
    else:
        st.warning("Podaj domenę lub IP, by rozpocząć.")
