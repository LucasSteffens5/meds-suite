# Ficha — Organizador de documentos acadêmicos

**Caso inteiramente fictício para treinamento.** Não descreve pesquisa realizada.
Este documento fornece contexto; não contém aceitação de escolhas metodológicas.

## Situação

Ana desenvolve um organizador para ajudar estudantes a encontrar documentos
acadêmicos por título e etiqueta. O protótipo local v0.1 tem uma interface de busca
e um mecanismo de indexação. É um produto de software sociotécnico, não crítico
para segurança neste exercício. Erros podem devolver documentos errados e rótulos
confusos podem dificultar o uso. Ser software não o torna puramente técnico.

O projeto está em design e desenvolvimento, antes de executar avaliações.
DSRM (Design Science Research Methodology) situa esse estágio no projeto; MEDS
organiza o programa de avaliações, sem conduzir toda a pesquisa.

## Recursos fornecidos

- Prazo inicial: duas semanas.
- Avaliação: até duas horas de Ana no computador próprio; sem orçamento extra.
- Outras atividades DSR: o restante do prazo é destinado a corrigir e documentar o protótipo.
- Destinatários da evidência: Ana e seu orientador, para decidir melhorias e o próximo passo.
- Acesso a estudantes e contexto real: ainda não confirmado.
- Restrição de Ana: **“Não quero medir notas nem coletar documentos pessoais.”**
- Dados do exercício: títulos e etiquetas totalmente sintéticos, sem pessoas identificáveis.
- Questão de pesquisa, limiar de clareza e protocolo detalhado de coleta: não definidos.

## Propriedades para discutir

Correção das buscas; clareza da interface; aparência visual; personalização.
São candidatas, não prioridades aceitas. A utilidade no uso real é uma preocupação
futura: os cenários abaixo não a demonstram.

## Dados sintéticos do protótipo descrito

| ID | Título | Etiqueta |
|---|---|---|
| D1 | Calendário acadêmico | planejamento |
| D2 | Guia de matrícula | matrícula |
| D3 | Modelo de relatório | escrita |
| D4 | Guia de relatório | escrita |

Para este exercício, a busca descrita ignora maiúsculas/minúsculas e compara palavras
nos títulos e etiquetas. Os resultados esperados são dados de entrada planejados,
**não saídas observadas de software executado**. Não é necessário construir o protótipo.

| Cenário | Consulta sintética | IDs esperados | O que cobre |
|---|---|---|---|
| S1 | calendário | D1 | Palavra no título |
| S2 | matrícula | D2 | Recuperação do guia |
| S3 | escrita | D3, D4 | Busca por etiqueta |
| S4 | estágio | Nenhum | Ausência de correspondência |
| S5 | CALENDÁRIO | D1 | Variação de maiúsculas |
| S6 | guia | D2, D4 | Várias correspondências no título |

Esses seis cenários são uma escolha didática, não uma quantidade prescrita por MEDS.
Depois do corte para S1–S3, ficam sem observação planejada a ausência de resultados,
a variação de maiúsculas e as múltiplas correspondências por título.
