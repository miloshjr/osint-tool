# src/config.py

import os
import shodan

# Klucz Shodan z ENV (bezpieczniej)
SHODAN_API_KEY = os.getenv("D5rraHjoRL6beiIm3E9BtkfpJsRar58D",)

# Domyślna liczba wyników do pobrania
RESULT_LIMIT = 1
