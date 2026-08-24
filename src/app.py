def soma(a: int, b: int) -> int:
    return a + b

def status() -> dict:
    return {"status": "online", "ambiente": "dev"}

if __name__ == "__main__":
    print(f"Status da Aplicação: {status()}")