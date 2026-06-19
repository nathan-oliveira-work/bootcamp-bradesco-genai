# Prompt: Extraindo Insights do Feedback de Clientes Bancários

## Informações do Desafio

**Bootcamp:** Bradesco - Dados, Cibersegurança e GenAI  
**Desafio:** Extraindo Insights do Feedback de Clientes Bancários  
**Tipo:** Desafio Criativo com IA Generativa  
**Ferramenta utilizada:** ChatGPT / Claude / Gemini (IA Generativa)

---

## Prompt Desenvolvido

### Contexto

Você é um especialista em análise de experiência do cliente (CX) no setor bancário. Sua missão é analisar feedbacks de clientes e extrair insights estratégicos que possam melhorar os produtos e serviços financeiros.

### Prompt Principal

```
Analise os seguintes feedbacks de clientes de um banco digital e extraia insights estratégicos:

FEEDBACKS:
1. "O aplicativo cai toda vez que tento pagar um boleto no final do mês"
2. "Adoro a facilidade de abrir conta, mas o suporte demora muito para responder"
3. "As taxas são competitivas, mas precisava de mais opções de investimento"
4. "O reconhecimento facial não funciona bem com óculos"
5. "Excelente! Transferência instantânea via Pix funcionou perfeitamente"
6. "Gostaria de ter um cartão de crédito com limite maior para minha renda"
7. "A interface é muito intuitiva, mas falta modo escuro"
8. "Tive problemas com a portabilidade de salário, levou 5 dias úteis"

Para cada categoria identificada, forneça:

1. **CATEGORIZAÇÃO**: Agrupe os feedbacks por tema (Tecnologia, Atendimento, Produtos, UX/Interface)

2. **ANÁLISE DE SENTIMENTO**: Classifique cada feedback como Positivo, Negativo ou Neutro com justificativa

3. **INSIGHTS ESTRATÉGICOS**: Para cada categoria, gere:
   - Principal dor do cliente
      - Oportunidade de melhoria
         - Sugestão de ação imediata
            - Métrica de sucesso para monitorar

            4. **PRIORIZAÇÃO**: Crie uma matriz de prioridade considerando:
               - Impacto no cliente (1-5)
                  - Urgência (1-5)
                     - Facilidade de implementação (1-5)

                     5. **RESUMO EXECUTIVO**: Em até 5 linhas, apresente os principais achados para a diretoria

                     Formato de saída: Use tabelas para a categorização e priorização, e parágrafos para os insights e resumo executivo.
                     ```

                     ---

                     ## Resultado Obtido com a IA

                     ### Categorização dos Feedbacks

                     | Feedback | Categoria | Sentimento |
                     |----------|-----------|------------|
                     | App cai ao pagar boleto | Tecnologia | Negativo |
                     | Facilidade de abertura, suporte lento | Atendimento | Misto |
                     | Taxas boas, poucas opções de investimento | Produtos | Misto |
                     | Reconhecimento facial com óculos | Tecnologia | Negativo |
                     | Pix instantâneo funcionou | Tecnologia | Positivo |
                     | Limite de crédito insuficiente | Produtos | Negativo |
                     | Interface intuitiva, sem modo escuro | UX/Interface | Misto |
                     | Portabilidade de salário demorada | Atendimento | Negativo |

                     ### Insights Estratégicos por Categoria

                     **Tecnologia:**
                     - Principal dor: Instabilidade no app em períodos de pico
                     - Oportunidade: Melhorar infraestrutura e biometria
                     - Ação imediata: Testes de carga e atualização do SDK de reconhecimento facial
                     - Métrica: Taxa de crashes < 0,1% e taxa de sucesso biométrico > 99%

                     **Atendimento:**
                     - Principal dor: Demora no suporte e processos burocráticos
                     - Oportunidade: Implementar chatbot com IA para primeiro nível de atendimento
                     - Ação imediata: Definir SLA máximo de 2h para respostas
                     - Métrica: NPS de atendimento e tempo médio de resposta

                     **Produtos:**
                     - Principal dor: Portfólio limitado de investimentos e crédito
                     - Oportunidade: Expandir produtos financeiros com personalização por perfil
                     - Ação imediata: Análise de perfil de risco e oferta proativa de produtos
                     - Métrica: Taxa de adoção de novos produtos e ticket médio

                     **UX/Interface:**
                     - Principal dor: Falta de personalização (modo escuro, acessibilidade)
                     - Oportunidade: Melhorar customização da interface
                     - Ação imediata: Implementar modo escuro e preferências de acessibilidade
                     - Métrica: Tempo médio no app e taxa de retenção

                     ### Resumo Executivo

                     Os feedbacks revelam que a infraestrutura tecnológica precisa de atenção prioritária, especialmente em períodos de alta demanda. O atendimento ao cliente é o segundo ponto crítico, com oportunidade de automação via IA. Os produtos financeiros carecem de expansão e personalização. A experiência do usuário é geralmente positiva, mas falta acessibilidade. Recomenda-se investimento imediato em estabilidade do sistema e implementação de chatbot inteligente.

                     ---

                     ## Reflexão sobre o Uso da IA

                     ### O que funcionou bem:
                     - A IA organizou os feedbacks de forma estruturada e clara
                     - Gerou insights acionáveis e relevantes para cada categoria
                     - Criou métricas de sucesso alinhadas com as práticas de mercado
                     - O formato de tabela facilitou a visualização e apresentação executiva

                     ### O que poderia melhorar:
                     - Com mais feedbacks, a análise quantitativa seria mais robusta
                     - A IA poderia ser treinada com dados históricos do banco para contexto específico
                     - Integração com ferramentas de BI tornaria o processo mais automatizado

                     ### Aprendizados:
                     O prompt estruturado com contexto claro, dados reais e formato de saída definido produziu resultados muito mais precisos do que prompts genéricos. A especificação do papel da IA (especialista em CX) e o formato desejado foram determinantes para a qualidade da resposta.

                     ---

                     ## Tecnologias e Ferramentas

                     - **IA Generativa:** Claude/ChatGPT/Gemini para análise de feedbacks
                     - **Técnica de Prompt:** Chain-of-Thought com contexto estruturado
                     - **Metodologia:** CX Analytics com matriz de priorização
                     - **Repositório:** https://github.com/nathan-oliveira-work/bootcamp-bradesco-genai
