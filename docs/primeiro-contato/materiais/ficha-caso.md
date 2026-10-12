# Organizador de documentos acadêmicos

## Contexto

O organizador ajuda estudantes a encontrar documentos acadêmicos por título e
etiqueta. O protótipo local v0.1 tem uma interface de busca e um mecanismo de
indexação. É um produto de software sociotécnico, ainda em design e desenvolvimento.
MEDS organiza seu programa de avaliações dentro do projeto DSR.

O risco técnico principal é retornar documentos incorretos. Rótulos ou resultados
pouco claros também podem dificultar o uso. A solução é sociotécnica: suas
características técnicas e a forma como as pessoas a usam se relacionam. O
organizador não é crítico para segurança neste exemplo.

## Recursos e limites

- Prazo inicial: duas semanas.
- Tempo dedicado à avaliação: até duas horas; sem verba adicional.
- Acesso a estudantes e ao contexto real de uso: ainda não confirmado.
- Restrição: não medir notas nem coletar documentos pessoais.
- Os dados da tabela são sintéticos; questão de pesquisa, critérios de clareza e
  protocolo detalhado ainda não foram definidos.
- A evidência deve ajudar a decidir correções e o próximo passo.

## Propriedades candidatas

Correção das buscas, clareza da interface, aparência visual e personalização.
São possibilidades para priorizar; a ficha ainda não define quais entram na
avaliação.

## Cenários para verificar as buscas

A busca ignora maiúsculas e minúsculas e procura palavras em títulos e etiquetas.
Os resultados esperados são critérios planejados para comparação, não resultados
observados de uma execução.

| Cenário | Consulta | IDs esperados | O que cobre |
|---|---|---|---|
| S1 | calendário | D1 | Palavra no título |
| S2 | matrícula | D2 | Recuperação do guia |
| S3 | escrita | D3, D4 | Busca por etiqueta |
| S4 | estágio | Nenhum | Ausência de correspondência |
| S5 | CALENDÁRIO | D1 | Variação de maiúsculas |
| S6 | guia | D2, D4 | Várias correspondências |

| ID | Título | Etiqueta |
|---|---|---|
| D1 | Calendário acadêmico | planejamento |
| D2 | Guia de matrícula | matrícula |
| D3 | Modelo de relatório | escrita |
| D4 | Guia de relatório | escrita |

Os cenários ajudam a planejar uma verificação de correção. Cobrir alguns deles não
demonstra correção geral nem utilidade em contexto real.
