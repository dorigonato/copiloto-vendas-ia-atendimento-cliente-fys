import os
import sys

# Tenta carregar variáveis do arquivo .env, se houver
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Tenta importar a biblioteca do Google Gemini
try:
    import google.generativeai as genai
except ImportError:
    print("\n[Erro] A biblioteca 'google-generativeai' não está instalada.")
    print("Por favor, instale as dependências usando: pip install google-generativeai python-dotenv\n")
    sys.exit(1)

def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"[Erro] Não foi possível ler o arquivo {filepath}: {e}")
        sys.exit(1)

def main():
    print("=====================================================")
    print("         🥤 FYS Agent - O Parça das Bebidas 🥤       ")
    print("=====================================================")
    
    # 1. Configurar API Key do Gemini
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("\nAPI Key do Gemini não encontrada nas variáveis de ambiente.")
        api_key = input("Cole sua GEMINI_API_KEY aqui para iniciar: ").strip()
        if not api_key:
            print("[Erro] Chave inválida. Encerrando.")
            sys.exit(1)
        genai.configure(api_key=api_key)
    else:
        genai.configure(api_key=api_key)

    # 2. Carregar as instruções e a base de conhecimento
    agents_spec = read_file("AGENTS.md")
    knowledge_base = read_file("knowledge/fys-brand.md")

    # Combinamos as regras do AGENTS.md com o banco de dados da marca
    system_instruction = f"""
    {agents_spec}

    Use a base de conhecimento abaixo para responder perguntas de forma precisa sobre produtos, fórmulas e receitas de drinks:
    ---
    {knowledge_base}
    """

    # 3. Inicializar o modelo de IA
    # Usando gemini-1.5-flash por ser rápido, leve e perfeito para chatbots
    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=system_instruction
        )
        chat = model.start_chat(history=[])
    except Exception as e:
        print(f"\n[Erro] Falha ao inicializar o modelo Gemini: {e}")
        sys.exit(1)

    print("\n[Sucesso] Copiloto FYS iniciado com sucesso!")
    print("Ele já está carregando as regras do AGENTS.md e o manual de marca.")
    print("Converse com ele! Digite 'sair' para encerrar a conversa.\n")
    print("Parça FYS: Fala, parça! E aí, qual a boa de hoje? Já garantiu o refri ou ainda tá na dúvida?")

    # 4. Loop de conversa no terminal
    while True:
        try:
            user_input = input("\nVocê: ")
            if user_input.strip().lower() in ['sair', 'exit', 'quit']:
                print("\nParça FYS: Valeu, parça! Na próxima ida ao mercado, não esquece de olhar a prateleira da Heineken. Até mais!")
                break
                
            if not user_input.strip():
                continue
                
            # Gera a resposta do bot
            response = chat.send_message(user_input)
            print(f"\nParça FYS: {response.text}")
            
        except KeyboardInterrupt:
            print("\n\nParça FYS: Saindo de fininho... Até logo!")
            break
        except Exception as e:
            print(f"\n[Erro] Ocorreu um problema ao gerar a resposta: {e}")

if __name__ == "__main__":
    main()
