import sys
import os

# Adiciona a pasta raiz ao path do Python para encontrar o modulo src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import soma, status

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0

def test_status():
    resultado = status()
    assert resultado["status"] == "online"
    assert resultado["ambiente"] == "dev"