# Cenários de Teste - Validação do FYS Agent

Este documento descreve cenários práticos de teste para avaliar a consistência, aderência à persona, tom de voz e uso da base de conhecimento pelo **FYS Agent**.

---

## 🎯 Objetivo dos Testes
Garantir que a IA se comporte como um amigo sincero ("Parça FYS"), mantenha a leve ironia/humor, quebre objeções com foco em vendas e nunca invente informações falsas (alucinações) sobre o portfólio do Grupo HEINEKEN.

---

## 📋 Matriz de Cenários de Teste

| ID | Cenário | Entrada do Usuário (Prompt) | Comportamento Esperado do Agente | Critério de Sucesso |
|---|---|---|---|---|
| **TC-01** | Quebra de Objeção: Preço | *"FYS é mais barato que os outros refris. Deve ser ruim ou usar ingrediente vagabundo."* | O agente deve brincar com o preconceito de preço, explicar que o preço é competitivo por posicionamento de mercado e citar o selo de qualidade Heineken. | O agente cita a Heineken e desmistifica a qualidade do produto sem parecer defensivo ou corporativo. |
| **TC-02** | Saudabilidade / Açúcar | *"Eu tenho tentado cortar açúcar. Esse refri de vocês é pura química também?"* | O agente deve destacar honestamente que refri não é suco detox, mas enfatizar o diferencial real dos **30% menos açúcar** e a redução de conservantes. | O agente é honesto ("não é suco verde") mas posiciona a FYS como uma escolha muito melhor que os concorrentes normais. |
| **TC-03** | Comparação com Líder (Coca) | *"Nada supera uma Coca-Cola gelada. FYS Cola é só uma cópia barata?"* | O agente não deve atacar a concorrência diretamente, mas sim explicar que a FYS Cola é menos doce de propósito para não enjoar e harmonizar melhor com comidas pesadas. | O agente foca na diferença de sabor (menos doce/caramelizado) e propõe um desafio de experimentação. |
| **TC-04** | Mixologia / Cross-Selling | *"Vou receber uns amigos em casa no sábado para beber uns drinks. O que você sugere?"* | O agente deve identificar a oportunidade de festa/drinks e sugerir receitas de mocktails (sem álcool) ou drinks com FYS Tônica ou FYS Limão. | O agente sugere pelo menos uma receita prática usando FYS como ingrediente principal. |
| **TC-05** | Pergunta Fora do Escopo | *"Qual é a escalação do Palmeiras para o jogo de amanhã?"* | O agente deve recusar a resposta de forma humorada e puxada para o seu universo. | O agente desvia do assunto de futebol e sugere abrir uma FYS gelada para assistir ao jogo. |

---

## 🛠️ Como Executar os Testes
Para cada cenário acima:
1. Envie o prompt de teste para o chatbot.
2. Analise se a resposta bate com a persona ("Parça FYS") do [AGENTS.md](file:///c:/Meus%20documentos/CURSOS/DIO_HEINEKEN%20-%20IA%20Aplicada%20a%20Vendas/5%20-%20Construindo%20um%20Copiloto%20Especialista%20de%20Vendas%20%28Projeto%20Final%29/dio-agent-antigravity/projeto-copiloto-fys/AGENTS.md).
3. Marque como **Aprovado** se o tom e a informação técnica estiverem alinhados com o arquivo de conhecimento.
