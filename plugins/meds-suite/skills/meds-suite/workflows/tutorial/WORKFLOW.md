# Tutorial guiado de MEDS

## Propósito

Ensine MEDS por meio de um caso fictício curto, fazendo a pessoa escolher poucas
propostas e ver como elas se conectam. Use português. Apresente os conceitos
quando forem necessários, com explicações breves. Faça no máximo uma pergunta
por resposta; ofereça aceitar, ajustar ou deixar a proposta pendente. Não faça
perguntas cuja resposta já esteja no caso abaixo. Cite sínteses pelo título e
tópico, sem mostrar caminhos ou links internos da instalação da skill.

O pedido “Use $meds-suite para me ensinar MEDS com um exemplo simples” inicia o
tutorial. O plano de prática fica em `casos/tutorial-meds/plano-meds.md`, relativo
ao projeto aberto no Codex, nunca à pasta da skill. Planejamento, retomada e revisão
de uma pesquisa real continuam nos fluxos específicos.

Antes de escrever, leia o destino. Se ele contiver o plano deste tutorial, retome
do ponto registrado sem perguntar de novo por decisões aceitas. Se pertencer a
outro caso, peça à pessoa um caminho diferente. Se não puder salvar, conduza a
prática no chat e diga que o arquivo não foi salvo. Ao iniciar, salve o contexto e
as escolhas disponíveis como propostas ou pendências, seguindo o modelo
[`plano-meds.md`](../../assets/plano-meds.md). Identifique o documento como
exercício fictício; não atribua decisões ou resultados a uma pesquisa real.

## Caso fornecido

Um protótipo v0.1 ajuda estudantes a encontrar documentos acadêmicos por título e
etiqueta. A busca ignora maiúsculas e minúsculas. O principal risco técnico é
retornar documentos errados; rótulos pouco claros também podem dificultar a busca.
O prazo fictício é de duas semanas, com até duas horas para avaliação e sem verba
adicional. Acesso a estudantes e ao contexto real ainda não foi confirmado. Use
dados sintéticos, não colete documentos pessoais nem meça notas. Os resultados
da tabela são expectativas de teste, não resultados observados.

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
relatório”, etiqueta escrita. Questão de pesquisa, critérios de clareza da
interface e protocolo de execução não foram definidos.

## Planejar

Leia a síntese [MEDS](../../references/meds.md). Ao trabalhar a estratégia, leia
também [FEDS](../../references/feds.md). Conduza os quatro passos em sequência
curta, mantendo decisões como propostas até a pessoa aceitá-las. Após cada resposta,
atualize o mesmo plano, resuma a escolha e pergunte somente pela próxima decisão.

1. **Objetivos.** Explique que o objetivo do organizador (encontrar documentos)
   não é o objetivo da avaliação. Proponha O1: identificar falhas que orientem
   melhorias; O2: julgar a correção das buscas nos cenários cobertos. Pergunte se
   esses objetivos servem ao exemplo ou devem ser ajustados.
2. **Estratégia.** Proponha Technical Risk & Efficacy, pois o risco técnico de
   buscas incorretas é prioritário e o acesso ao uso real não está confirmado.
   Sugira inspeção artificial formativa seguida de testes artificiais somativos;
   deixe o uso naturalístico para uma etapa futura condicionada ao acesso. Explique
   finalidade formativa/somativa e ambiente artificial/naturalístico. Pergunte se
   a proposta serve ou deve mudar.
3. **Propriedades.** Proponha correção das buscas como Must e clareza como Should.
   Aparência visual pode ficar como Could e personalização como Would, fora da
   avaliação inicial. Mantenha critérios de clareza pendentes. Explique MuSCoW
   brevemente e pergunte se a priorização serve.
4. **Episódios.** Proponha E1 formativo artificial com Criteria-Based Evaluation
   para inspecionar correção e clareza, mantendo critérios de clareza pendentes;
   proponha E2 somativo artificial com Testing para comparar as buscas aos
   resultados esperados em S1–S6. Justifique cada método pela evidência. Protocolos,
   responsáveis e critérios desconhecidos continuam pendentes. Pergunte se esses
   episódios servem ou precisam de ajuste.

Se a pessoa deixar uma escolha pendente, registre-a assim e continue apenas as
partes que não dependem dela. Ao concluir o planejamento, mostre o caminho salvo,
as decisões, pendências e o que aprendeu; ofereça continuar o tutorial ou parar.
Não trate plano como avaliação executada, resultado ou validação do organizador.

## Retomar

Quando a pessoa disser “continuar tutorial” após o planejamento, leia o plano e
preserve escolhas aceitas. Apresente a mudança fictícia: o prazo para avaliação
caiu de duas semanas para três dias; acesso a estudantes segue sem confirmação.
Explique que objetivos podem continuar válidos, mas a cobertura pode diminuir.

Proponha reduzir E2 de S1–S6 para S1–S3. Diga claramente que S4–S6 deixam de ser
avaliados e que as conclusões ficam restritas aos três cenários cobertos. Isso é
short-scoping, uma redução de escopo com consequência explícita para cobertura e
rigor. Pergunte se a pessoa aceita, quer outro corte ou prefere manter a escolha
pendente. Só atualize a decisão e os episódios afetados após a resposta. Registre
a mudança de contexto e mantenha O1, O2 e decisões não afetadas. Mostre o efeito
no plano e ofereça a revisão como próxima parte.

Se a pessoa retomar o tutorial em outra conversa, ela pode enviar “Continue o
tutorial MEDS” ou informar o caminho do plano. Leia o arquivo antes de perguntar.

## Revisar

Quando a pessoa pedir a revisão do tutorial, carregue o fluxo
[Revisar](../revisar/WORKFLOW.md) e a síntese MEDS. Revise o plano salvo na conversa
e examine os vínculos entre objetivos, estratégia, propriedades, episódios e
conclusões. Considere as pendências e o corte de escopo, se aceito. Apresente
recomendações no chat; preserve o arquivo. Edite apenas ajustes que a pessoa
solicitar explicitamente. Termine mostrando o que aprendeu e ofereça encerrar.
