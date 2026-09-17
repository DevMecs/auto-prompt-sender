# 🤖 Auto Prompt Sender

Script simples em Python que criei para automatizar o envio em lote de prompts (ou mensagens) a partir de um arquivo de texto, com intervalo de tempo configurável entre cada envio.

Fiz essa automação para resolver uma dor real: quando preciso rodar dezenas de prompts em ferramentas de IA ou chats e não quero ficar colando e apertando enter manualmente a cada 1 ou 2 minutos.

---

## 💡 Como funciona?

1. O script lê um arquivo chamado `prompts.txt` linha por linha.
2. Dá uma contagem regressiva de **10 segundos** para você focar a janela e clicar no campo de texto onde quer que as mensagens entrem.
3. Para cada prompt, ele copia o texto para a área de transferência via `pyperclip` (evitando bugs com acentos e caracteres especiais do teclado brasileiro), cola com `Ctrl + V` e pressiona `Enter`.
4. Aguarda o tempo de intervalo definido (padrão de 2 minutos) antes de enviar o próximo.

---

## 🛠️ Tecnologias e Bibliotecas

- **Python 3.8+**
- [`pyautogui`](https://pyautogui.readthedocs.io/): automação de comandos de teclado e atalhos.
- [`pyperclip`](https://pypi.org/project/pyperclip/): manipulação confiável da área de transferência (clipboard).
- Módulos nativos: `pathlib` e `time`.

---

## 🚀 Como rodar na sua máquina

### 1. Clonar o repositório
```bash
git clone https://github.com/SEU-USUARIO/auto-prompt-sender.git
cd auto-prompt-sender
```

### 2. Criar e ativar um ambiente virtual (recomendado)
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar os prompts
Crie ou edite o arquivo `prompts.txt` na mesma pasta do script, colocando uma mensagem/prompt por linha:
```text
Escreva um post curto para LinkedIn sobre automação de tarefas.
Me dê 5 ideias de temas para carrossel no Instagram sobre tecnologia.
Crie um roteiro rápido de 30 segundos para Reels.
```

### 5. Executar o script
```bash
python automacao.py
```

> ⚠️ **Atenção:** Assim que rodar o comando, você terá 10 segundos para clicar no campo de mensagem do aplicativo ou navegador onde deseja enviar os textos. Deixe o cursor piscando lá e não mexa no teclado/mouse enquanto o envio estiver acontecendo.

---

## ⚙️ Customização

Se quiser mudar o tempo de espera entre um envio e outro, basta alterar a variável no topo de `automacao.py`:

```python
INTERVALO = 120  # Tempo em segundos (ex: 60 para 1 minuto, 30 para 30s)
```

---

## 🚨 Dica de Segurança (Fail-Safe do PyAutoGUI)
Se algo der errado ou você precisar parar o envio imediatamente, o PyAutoGUI possui um fail-safe nativo: basta **jogar o cursor do mouse com força para o canto superior esquerdo da tela (coordenada 0, 0)** ou encerrar o terminal com `Ctrl + C`.

---

Feedbacks, sugestões ou melhorias são sempre bem-vindos! Se esse script te ajudou de alguma forma, deixa uma estrela ⭐ no projeto.
