# 💰 Sistema bancário simples em python

Este é um projeto de terminal que simula um sistema bancário básico. O usuário pode realizar depósitos, saques e visualizar o extrato de movimentações. 

## 📋 Funcionalidades

- **Depósito:** permite adicionar valores ao saldo da conta.
- **Saque:** permite retirar valores da conta, respeitando:
  - Um **limite por saque** (R$500.00).
  - Um **limite diário de saques** (3 por dia).
  - A condição de saldo suficiente.
- **Extrato:** exibe todas as movimentações realizadas (depósitos e saques) e o saldo atual.
- **Sair:** finaliza a aplicação.

## 🚀 Como usar

1. Certifique-se de ter o **Python 3** instalado.
2. Clone o repositório ou copie o código.
3. Execute o script:

```bash
python banco.py
```

4. Use o menu interativo para navegar pelas opções:

```
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
```

## 🧠 Exemplo de uso

```text
=> d
Digite o valor do depósito: 200
Depósito realizado com sucesso!

=> s
Digite o valor do saque: 100
Saque realizado com sucesso!

=> e
------------EXTRATO------------
DEPÓSITO - R$200.00
SAQUE - R$100.00
SALDO - R$100.00
-------------------------------
```

## 📌 Regras de negócio

- Não é permitido realizar saques que excedam o saldo disponível.
- Não é permitido sacar mais do que R$500.00 por operação.
- O número de saques é limitado a 3 por execução.
- Depósitos com valor inválido (zero ou negativo) não são permitidos.

