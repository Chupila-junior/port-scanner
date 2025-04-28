![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)


# PortScanner 🔎

Um scanner de portas TCP simples e eficiente, desenvolvido em Python.

## Como funciona?

Este projeto escaneia portas abertas em um endereço IP ou hostname fornecido pelo usuário, utilizando múltiplas threads para acelerar o processo.

## Instalação

Clone o repositório:
```bash
git
cd portscanner

Instale as dependências:
pip install -r requirements.txt

Uso:
python scanner/scanner.py --ip 192.168.0.1 --start-port 20 --end-port 80

Parâmetros:
--ip ➔ Endereço IP ou URL que você deseja escanear.

--start-port ➔ Porta inicial (opcional, padrão = 1)

--end-port ➔ Porta final (opcional, padrão = 65535)
