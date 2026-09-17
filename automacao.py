import time
import pyautogui
import pyperclip
from pathlib import Path

ARQUIVO_PROMPTS = "prompts.txt"
INTERVALO = 120  # segundos entre cada envio

arquivo = Path(ARQUIVO_PROMPTS)

if not arquivo.exists():
    print(f"Arquivo '{ARQUIVO_PROMPTS}' não encontrado.")
    exit()

with open(arquivo, "r", encoding="utf-8") as f:
    prompts = [linha.strip() for linha in f if linha.strip()]

total = len(prompts)

print(f"Foram encontrados {total} prompts.")
print("Abra a conversa, clique UMA VEZ no campo de mensagem.")
print("O envio começará em 10 segundos...")
time.sleep(10)

for i, prompt in enumerate(prompts, start=1):

    # Copia o texto
    pyperclip.copy(prompt)

    # Pequena pausa
    time.sleep(0.3)

    # Cola
    pyautogui.hotkey("ctrl", "v")

    time.sleep(0.2)

    # Envia
    pyautogui.press("enter")

    print(f"[{i}/{total}] Enviado: {prompt}")

    # Aguarda o próximo envio
    if i != total:
        time.sleep(INTERVALO)

print("\nTodos os prompts foram enviados!")