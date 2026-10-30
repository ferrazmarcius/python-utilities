# ⚙️ Python Utilities Monorepo

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Type Checking: Mypy](https://img.shields.io/badge/type--checking-mypy-informational.svg)](https://mypy-lang.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Monorepo focado no desenvolvimento de ferramentas CLI (Command-Line Interface) e utilitários de backend para automação de tarefas cotidianas, processamento de dados e gestão financeira pessoal. O ecossistema foi projetado priorizando simplicidade de execução, modularidade e boas práticas em Python.

---

## 🧭 Visão Geral da Arquitetura

O repositório opera sob a estrutura de **monorepo**, isolando responsabilidades de negócio e utilitários em diretórios dedicados:

```plaintext
python-utilities/
├── financial-control/       # Módulo CLI para gestão de fluxo de caixa e relatórios
│   ├── main.py              # Ponto de entrada do módulo financeiro
│   └── README.md            # Documentação específica e regras de domínio
├── projeto-compras/         # Utilitário de orçamentação e lista de aquisições
│   ├── main.py              # Ponto de entrada da aplicação de compras
│   └── README.md            # Regras e especificação das operações
├── requirements.txt         # Dependências do ecossistema
└── README.md                # Documentação global do ecossistema
```

---

## 📦 Aplicações Integradas

### 1. `financial-control` (Controle Financeiro)
Ferramenta para monitoramento e controle de despesas e receitas, auxiliando no planejamento financeiro pessoal.
* **Principais Funcionalidades:**
  * Lançamento categorizado de receitas e despesas.
  * Cálculo em tempo real de saldo líquido e balanço por categoria.
  * Visualização estruturada de movimentações diretamente no terminal.

### 2. `projeto-compras` (Gestão de Compras e Orçamentos)
Solução ágil voltada para planejamento e simulação de custos em listas de compras antes da execução.
* **Principais Funcionalidades:**
  * Registro de itens com quantidade e custo unitário projetado.
  * Sumarização automática do total da compra.
  * Validação de orçamento teto contra valor consolidado.

---

## 🚀 Como Começar

### Pré-requisitos
* **Python 3.10+** instalado.
* **Git** configurado localmente.

### 1. Clonagem e Configuração do Ambiente

```bash
# Clonar o repositório
git clone https://github.com/ferrazmarcius/python-utilities.git

# Aceder ao diretório raiz
cd python-utilities

# Criar um ambiente virtual isolado (recomendado)
python -m venv .venv

# Ativar o ambiente virtual:
# No Linux/macOS:
source .venv/bin/activate
# No Windows (PowerShell):
.venv\Scripts\Activate.ps1
```

### 2. Instalação de Dependências

```bash
# Caso existam dependências globais registradas:
pip install -r requirements.txt
```

---

## 💻 Execução dos Módulos

Cada aplicação é auto-contida e pode ser executada de forma independente a partir da raiz:

### Executar o Módulo Financeiro:
```bash
python financial-control/main.py
```

### Executar a Gestão de Compras:
```bash
python projeto-compras/main.py
```

---

## 🛠️ Qualidade de Código e Boas Práticas

Para manter a consistência, manutenibilidade e confiabilidade do código em todo o repositório:

* **Formatador de Código:** `black` (PEP 8 compliance).
* **Análise Estática e Tipagem:** `mypy` e `flake8`.
* **Testes Automatizados:** Estruturação orientada a `pytest` para testes unitários de lógica de cálculo e persistência.

Comandos para verificação de integridade:
```bash
# Formatação do código
black .

# Validação com linter
flake8 .

# Verificação de tipos
mypy financial-control/ projeto-compras/
```

---

## 🗺️ Roadmap de Evolução Técnica

- [ ] Unificar formatos de persistência de dados (migração para SQLite/JSON padronizado).
- [ ] Exportação de relatórios em formato CSV e planilhas `.xlsx`.
- [ ] Implementação de pipelines automatizadas via **GitHub Actions** (CI com lint e unit tests).
- [ ] Implementação de interfaces interativas via terminal com bibliotecas como `Rich` ou `Typer`.

---

## 👤 Autor

Desenvolvido por **Marcius Ferraz**.  
* Conecte-se comigo no [LinkedIn](https://www.linkedin.com/in/ferrazmarcius/) *(adicione seu link se aplicável)*
* Repositório no GitHub: [@ferrazmarcius](https://github.com/ferrazmarcius)

---

## 📄 Licença

Este projeto é distribuído sob os termos da licença **MIT**. Consulte o ficheiro `LICENSE` para mais informações.