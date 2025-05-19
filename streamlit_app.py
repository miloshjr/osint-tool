import streamlit as st
import subprocess
import sys
import subprocess

print("Python executable:", sys.executable)

try:
    import dns
    print("dnspython version:", dns.__version__)
except Exception as e:
    print("dnspython import error:", e)

# Pokaz zainstalowane pakiety (wielkie gówno, ale czasem pomaga)
subprocess.run([sys.executable, "-m", "pip", "freeze"])

st.set_page_config(page_title="OSINT Tool", page_icon="🔍")

st.title("🕵️ OSINT Tool 🔍")
st.markdown("Podaj domenę, a narzędzie sprawdzi publiczne podatności.")

target = st.text_input("🎯 Cel:")

if st.button("Skanuj") or st.spinner:
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
