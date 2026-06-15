# 🥤 Copiloto de Vendas FYS - O Parça das Bebidas

Este repositório contém a definição e especificação de um Agente de IA (Copiloto de Vendas) projetado para resolver um desafio real de mercado da marca **FYS** (refrigerante do grupo **HEINEKEN**): **a falta de conhecimento da marca pelo grande público.**

O agente foi desenhado para atuar no canal de vendas e atendimento final, adotando a personalidade de um "amigo especialista em bebidas" que educa o consumidor sobre a marca, quebra objeções com humor sincero e impulsiona a experimentação (primeira compra).

---

## 🎯 O Desafio Escolhido: *"Quem é FYS mesmo?"*
Muitos consumidores desconhecem a marca FYS ou não sabem que ela pertence ao grupo Heineken, o que gera desconfiança no ponto de venda e faz com que comprem sempre as marcas líderes tradicionais.

**Como a IA ajuda a resolver:**
Através de um chatbot interativo que utiliza o tom de voz informal e levemente ácido da marca. A IA deixa de lado o formato corporativo chato de propaganda e fala como um amigo sincero no churrasco, apresentando os benefícios do produto (como ter 30% menos açúcar) e alavancando a credibilidade da Heineken para gerar desejo de experimentação.

---

## 🛠️ Estrutura do Agente

O projeto é composto por dois arquivos estruturais que dão vida ao assistente:
* **[AGENTS.md](file:///c:/Meus%20documentos/CURSOS/DIO_HEINEKEN%20-%20IA%20Aplicada%20a%20Vendas/5%20-%20Construindo%20um%20Copiloto%20Especialista%20de%20Vendas%20%28Projeto%20Final%29/dio-agent-antigravity/projeto-copiloto-fys/AGENTS.md)**: Contém as regras de comportamento, diretrizes de tom de voz e exemplos de interação da IA.
* **[knowledge/fys-brand.md](file:///c:/Meus%20documentos/CURSOS/DIO_HEINEKEN%20-%20IA%20Aplicada%20a%20Vendas/5%20-%20Construindo%20um%20Copiloto%20Especialista%20de%20Vendas%20%28Projeto%20Final%29/dio-agent-antigravity/projeto-copiloto-fys/knowledge/fys-brand.md)**: A base de conhecimento oficial que serve como fonte única de verdade sobre a marca, os produtos, composições e sugestões de harmonizações.

### Principais Pilares do Copiloto:
- **Tom de voz:** Informal, direto, sincero e bem-humorado (amigo especialista).
- **Diferenciais FYS:** Menos açúcar, sem conservantes, chancela do grupo Heineken.
- **Estratégia de Vendas:** Sugestões de harmonizações (hambúrguer, churrasco, pizza) e quebra de objeções tradicionais.

---

## 💬 Exemplos de Prompts e Testes rápidos
Você pode testar este agente em qualquer modelo de linguagem (ChatGPT, Claude, Gemini). Basta copiar o conteúdo do [AGENTS.md](file:///c:/Meus%20documentos/CURSOS/DIO_HEINEKEN%20-%20IA%20Aplicada%20a%20Vendas/5%20-%20Construindo%20um%20Copiloto%20Especialista%20de%20Vendas%20%28Projeto%20Final%29/dio-agent-antigravity/projeto-copiloto-fys/AGENTS.md) e colar como **Instruções do Sistema (System Instructions)** ou enviar como o primeiro prompt:

> *"A partir de agora, comporte-se exatamente de acordo com as especificações do AGENTS.md abaixo:"*
> *(Cole o conteúdo de AGENTS.md)*

### Exemplos de perguntas para testar o agente:
1. *"Nunca ouvi falar dessa tal de FYS. Vale a pena mesmo?"*
2. *"Por que eu trocaria a minha Coca por uma FYS Cola?"*
3. *"Quero fazer uma noite de pizza com os amigos. Qual FYS você me recomenda?"*

## ⚙️ Como rodar o protótipo localmente (app.py)

Além da documentação, você pode testar o comportamento do agente diretamente no seu terminal utilizando o script Python interativo:

### 1. Pré-requisitos
Certifique-se de ter o Python instalado e as seguintes bibliotecas adicionadas:
```bash
pip install google-generativeai python-dotenv
```

### 2. Configurando a Chave da API
Crie um arquivo `.env` na raiz do projeto ou configure sua variável de ambiente:
```env
GEMINI_API_KEY=sua_chave_aqui
```
*Dica:* Se você não criar o arquivo `.env`, o script irá perguntar sua chave diretamente no terminal ao iniciar.

### 3. Executando o script
```bash
python app.py
```

---

## 📂 Estrutura completa do repositório
* `README.md` - Documentação principal do projeto.
* `AGENTS.md` - Especificação da persona do Agente.
* `app.py` - Script executável de interação com o Gemini.
* `knowledge/fys-brand.md` - Base de conhecimento oficial dos produtos e receitas.
* `tests/test-scenarios.md` - Cenários para testar e validar respostas da IA.
