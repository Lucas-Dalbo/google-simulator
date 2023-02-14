# Projeto: Google Simulator
Este projeto foi desenvolvido enquanto estudante da Trybe no módulo de Ciências da Computação.

---
## Sobre o projeto
O objetivo é utilizar o **Python** para implementar um programa que simula um algoritmo de indexação de documentos similiar ao do Google, possuindo a habilidade de identificar ocorrências de termos em arquivos _.txt_.

O programa é dividio em dois módulos:
  - **Módulo de gerenciamento de arquivos**: que permite a anexação de arquivos de texto(_.txt_);
  - **Módulo de busca**: que permite realizar buscas nos arquivos anexados.

---
## Habilidades desenvolvidas
- Manipulação de Pilhas (*Stacks*).
- Manipulaão de Filas (*Queues*).
- Manipulação de Nós (*Nodes*) e Listas Ligadas (*Linked Lists*).
- Manipular Listas Duplamente Ligadas.

---
## Código desenvolvido
### Pacote `ting_file_management`:
#### 01. Implementação da fila de arquivos (`queue.py`).

#### 02. Importador de arquivos de texto para o formato *list*.
  - Módulo `file_management.py`, função `txt_importer`.

#### 03. Transformação de uma *list* gerada por `txt_importer` em um *dict*, que será armazenado em uma instância de *Queue*.
  - Módulo `file_process`, função `process`.

#### 04. Função `remove` do módulo `file_process`, para a remoção do primeiro elemento de uma instância de *Queue*.

#### 05. Apresentação de infromações superficiais de um arquivo processado.
 - Módulo `file_process`, função `fila_metadata`.

#### 06. Testes para a classe *PriorityQueue*, que armazena arquivos menores de forma prioritária.

### Pacote `ting_word_searches`:
#### 07. Ferramenta de busca que verifica se uma palavra especifica **existe** nos arquivos processados em uma instância de *Queue*.
  - Módulo `word_search`, função `exists_words`;

#### 08. Ferramenta de busca por uma palavra em todos os arquivos processados e retorna todas as linhas em que ela aparece.
  - Módulo `word_search`, função `search_by_word`

---
## O que foi utilizado?
  - Python.
  - Pytest, Pytest-json, Pytest-cov.
  - Flake8, Black.

---
## Rodando Localmente
1. Clone o repositório e abra a pasta raiz.
2. Ative o ambiente virtual do python pelo terminal:
  ```bash
    python3 -m venv .venv && source .venv/bin/activate
  ```
3. Instale as dependências pelo terminal:
  ```bash
    python3 -m pip install -r dev-requirements.txt
  ```
