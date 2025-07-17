import os
import sys
import locale
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def configure_encoding():
    """Configure system encoding settings"""
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
    
    try:
        locale.setlocale(locale.LC_ALL, 'pl_PL.utf8')
    except locale.Error:
        try:
            locale.setlocale(locale.LC_ALL, 'C.utf8')
        except:
            os.environ['PYTHONIOENCODING'] = 'utf-8'

# Wywołaj funkcję przy imporcie
configure_encoding()