import os
import logging
from dotenv import load_dotenv
from supabase import create_client, Client
import requests

# Configura o logging para um output mais claro
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Função principal que orquestra todo o processo.
    """
    load_dotenv()
    logging.info("Iniciando o script de notificação...")

    # --- 1. Carregar Configurações do .env ---
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
    ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")

    # Validação crítica das variáveis de ambiente
    if not all([SUPABASE_URL, SUPABASE_KEY, ZAPI_INSTANCE_ID, ZAPI_TOKEN]):
        logging.critical("ERRO: Uma ou mais variáveis de ambiente não foram encontradas. Verifique seu arquivo .env.")
        return

    # URL da Z-API com o token no caminho, conforme a documentação da instância
    ZAPI_URL = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"

    # --- 2. Conectar ao Supabase e Buscar Contatos ---
    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        logging.info("Conexão com Supabase estabelecida com sucesso.")
        
        # Corrigido para buscar pela coluna "numero"
        response = supabase.table('contatos').select("nome, numero").execute()
        
        contatos = response.data
        if not contatos:
            logging.warning("Nenhum contato encontrado na tabela do Supabase. Finalizando.")
            return
        logging.info(f"{len(contatos)} contatos encontrados.")
    except Exception as e:
        logging.error(f"Falha ao buscar dados do Supabase: {e}")
        return

    # --- 3. Iterar e Enviar Mensagens ---
    logging.info("Iniciando o processo de envio de mensagens...")
    for contato in contatos:
        nome = contato.get('nome')
        numero = contato.get('numero') # Corrigido para pegar a coluna "numero"
        
        if not nome or not numero:
            logging.warning(f"Registro inválido (sem nome ou numero), pulando: {contato}")
            continue

        mensagem = f"Olá {nome}, tudo bem com você?"
        
        payload = {"phone": numero, "message": mensagem}
        
        # Headers corretos com as duas chaves necessárias
        headers = {
            "Content-Type": "application/json",
            "Client-Token": ZAPI_TOKEN
        }

        try:
            response = requests.post(ZAPI_URL, json=payload, headers=headers, timeout=15)
            response_data = response.json()

            # Lógica de verificação robusta
            if response.status_code == 200 and "error" not in response_data:
                logging.info(f"✅ Sucesso! Mensagem enviada para {nome} ({numero}).")
            else:
                error_message = response_data.get('message', str(response_data))
                logging.error(f"❌ Falha ao enviar para {nome} ({numero}): {error_message}")

        except requests.exceptions.RequestException as e:
            logging.critical(f"🚨 Erro crítico de conexão ao tentar enviar para {nome}: {e}")
    
    logging.info("Script finalizado.")

if __name__ == "__main__":
    main()