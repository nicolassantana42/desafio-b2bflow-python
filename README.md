# Solução: Desafio de Estágio b2bflow ⚡

Este repositório contém a solução para o desafio técnico para a vaga de Estágio em Desenvolvimento Python na b2bflow.

O projeto consiste em um script Python que cumpre a missão de ler contatos de um banco de dados Supabase e enviar uma mensagem de saudação personalizada via WhatsApp, utilizando a Z-API.

## ✅ Requisitos Cumpridos

O projeto foi desenvolvido seguindo todas as regras estipuladas:

- [x] **Stack:** Utiliza Python, Supabase e Z-API, todos com planos gratuitos.
- [x] **Fonte dos Dados:** Os contatos são lidos dinamicamente do banco de dados no Supabase.
- [x] **Mensagem:** A mensagem enviada é exatamente "Olá {{nome_contato}}, tudo bem com você?", com o nome personalizado.
- [x] **Entrega:** O código está publicado em um repositório público no GitHub.
- [x] **Boas Práticas:** O código inclui tratamento de erros, logs simples, uso de `.env` para segurança e commits objetivos.

## 🛠️ Setup e Execução

Para rodar este projeto, siga os passos abaixo.

### 1. Configuração do Banco de Dados (Supabase)

-   Crie uma conta gratuita e um novo projeto no **Supabase**.
-   No "Table Editor", crie uma nova tabela chamada `contatos`.
-   Adicione as seguintes colunas à tabela:
    -   `nome` (tipo `text`)
    -   `numero` (tipo `text`)
-   Insira os contatos para teste. O número deve seguir o formato internacional (ex: `5511999998888`).

### 2. Configuração do Ambiente Local

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/nicolassantana42/desafio-b2bflow-python.git](https://github.com/nicolassantana42/desafio-b2bflow-python.git)
    cd desafio-b2bflow-python
    ```
2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Unix/macOS:
    python3 -m venv venv && source venv/bin/activate
    
    # Para Windows (PowerShell):
    python -m venv venv; .\venv\Scripts\activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### 3. Variáveis de Ambiente

1.  Crie um arquivo chamado `.env` na raiz do projeto.
2.  Preencha o arquivo com suas chaves, conforme o exemplo abaixo:
    ```env
    # Credenciais do Supabase (encontre em Project Settings > API)
    SUPABASE_URL="SUA_URL_DO_PROJETO_SUPABASE"
    SUPABASE_KEY="SUA_CHAVE_ANON_PUBLICA_DO_SUPABASE"

    # Credenciais da Z-API (encontre no painel da sua instância)
    ZAPI_INSTANCE_ID="SEU_ID_DE_INSTANCIA_NA_ZAPI"
    ZAPI_TOKEN="SEU_TOKEN_DA_INSTANCIA_NA_ZAPI"
    ```

### 4. Execução do Script

-   Com o ambiente virtual ativado e o `.env` configurado, rode o comando:
    ```bash
    python main.py
    ```
-   Os logs da execução aparecerão no terminal.

## 📂 Estrutura do Projeto

A organização dos arquivos foi mantida simples e clara para facilitar a avaliação:
```
desafio-b2bflow-python/
│
├── .gitignore        # Ignora arquivos sensíveis e desnecessários
├── main.py           # Script principal com toda a lógica
├── requirements.txt  # Lista de dependências Python
├── README.md         # Esta documentação
└── .env              # Arquivo local para as credenciais (não versionado)
```
