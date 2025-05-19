import streamlit as st
import subprocess

st.set_page_config(page_title="OSINT Tool", page_icon="🔍")

st.title("🔍 OSINT Tool")
st.markdown("Podaj domenę lub adres IP, a narzędzie sprawdzi publiczne podatności.")

target = st.text_input("🎯 Cel (domena lub IP):")

if st.button("Skanuj"):
    if target:
        with st.spinner("Skanowanie w toku..."):
            try:
                result = subprocess.run(
                    ["python3", "src/scanner.py", "--target", target],
                    capture_output=True, text=True, check=True
                )
                st.success("Skanowanie zakończone!")
                st.code(result.stdout)
            except subprocess.CalledProcessError as e:
                st.error("Wystąpił błąd podczas skanowania.")
                st.code(e.stderr)
    else:
        st.warning("Podaj domenę lub IP, by rozpocząć.")
