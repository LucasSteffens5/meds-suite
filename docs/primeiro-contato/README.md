# Tutorial MEDS para copiar no chat

Para usá-lo,abra uma conversa no Codex na pasta em que deseja salvar o plano e cole a mensagem
de contexto abaixo. O caso é fictício e serve somente ao exercício explicitamente
identificado. Os outros casos da sua pesquisa devem vir da conversa ou do plano que
você indicar.

## Contexto do exercício

Copie o bloco inteiro para iniciar. Ele fornece o caso e pede que a suíte conduza
o aprendizado sem impor respostas prontas:

```text
Use $meds-suite para me ensinar MEDS. Quero planejar
a avaliação de um protótipo que ajuda estudantes a encontrar documentos
acadêmicos por título e etiqueta. A busca ignora maiúsculas e minúsculas. O risco
técnico principal é retornar documentos errados. Rótulos pouco claros também
podem dificultar a busca.

O prazo do exercício é de duas semanas, com até duas horas para avaliação e sem
verba adicional. O acesso a estudantes e ao contexto real ainda não foi confirmado.
Use dados sintéticos não colete documentos pessoais nem meça notas. Os resultados
abaixo são expectativas de teste, não resultados observados. A questão de pesquisa,
os critérios de clareza da interface e o protocolo de execução continuam sem
definição.

| Cenário | Consulta | IDs esperados | Cobertura |
|---|---|---|---|
| S1 | calendário | D1 | Palavra no título |
| S2 | matrícula | D2 | Palavra no título |
| S3 | escrita | D3, D4 | Correspondências múltiplas |
| S4 | estágio | Nenhum | Sem correspondência |
| S5 | CALENDÁRIO | D1 | Maiúsculas e minúsculas |
| S6 | guia | D2, D4 | Várias correspondências |

D1 é “Calendário acadêmico”, etiqueta planejamento; D2 é “Guia de matrícula”,
etiqueta secretaria; D3 é “Modelo de relatório”, etiqueta escrita; D4 é “Guia de
relatório”, etiqueta escrita.

Conduza objetivos da avaliação, estratégia, prioridades e episódios
com métodos candidatos em etapas curtas. Explique os conceitos quando
forem necessários e faça no máximo uma pergunta por resposta. Peça minha decisão
em cada etapa; mantenha propostas como propostas e lacunas como pendências até eu
responder. Não invente uma resposta correta para este exercício. Salve o plano em
casos/tutorial-meds/plano-meds.md, relativo a esta pasta do projeto. Não atribua suas decisões ou resultados a outra pesquisa.
```

## Continuar o planejamento

Depois de responder à pergunta da suíte, cole esta mensagem para avançar no caso:

```text
Continue o planejamento deste exercício MEDS. Leia o plano salvo, preserve o que
aceitei, mostre a próxima decisão que depende de mim e faça somente uma pergunta.
Não complete lacunas usando exemplos ou casos de outros arquivos.
```

O exercício passa por objetivos de avaliação, estratégia e trajetória FEDS,
priorização das propriedades com MuSCoW e escolha de episódios e métodos com
DSREMSF. Decida cada item com base nas informações do caso e no que você aceitar.
Os termos do protótipo ajudam a praticar o método; não são respostas universais.

## Retomar com mudança de prazo

Após concluir o primeiro planejamento, use este cenário de prática para discutir
short-scoping.

```text
Continue o exercício. Houve uma mudança: agora restam três dias para a
avaliação, e o acesso a estudantes continua sem confirmação. Proponha alternativas
para reduzir o escopo e explique o efeito de cada uma sobre cobertura, rigor e
conclusões. Pode considerar, como uma possibilidade, limitar os testes de busca
a S1–S3; deixe explícito que S4–S6 não seriam cobertos. Não aplique nem aceite um
corte sem minha decisão. Faça uma pergunta.
```

## Revisar o plano do exercício

Para revisar sem editar o arquivo, cole:

```text
Revise a coerência do plano do exercício MEDS salvo em
casos/tutorial-meds/plano-meds.md. Examine os vínculos entre objetivos, estratégia,
propriedades, episódios e conclusões, considerando apenas decisões aceitas e
pendências registradas no plano. Apresente recomendações no chat e não edite o
arquivo.
```

Se você pedir para continuar este tutorial em outra conversa, envie o contexto do
exercício ou indique o plano salvo. Sem esse material, a suíte pedirá que você o
forneça em vez de reconstruir o exemplo.
