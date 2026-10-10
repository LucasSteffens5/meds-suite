# MEDS: fundamento para planejamento e revisão

Síntese original de Baskerville, R., Pries-Heje, J., & Venable, J. R. (2026).
*MEDS: Methodology for Evaluation in Design Science*. European Journal of
Information Systems, 35(5), 830–847. DOI:
[10.1080/0960085X.2026.2627280](https://doi.org/10.1080/0960085X.2026.2627280).

## Processo e seus quatro passos

MEDS organiza o programa de **avaliações** de um projeto DSR. O **avaliando** é o
artefato examinado; um **episódio** é uma avaliação realizada em determinado
momento para atender a um ou mais objetivos. O **programa** reúne a estratégia,
a trajetória e os episódios de avaliação do projeto. Os quatro passos são:

| Passo | Pergunta central | Orientação |
|---|---|---|
| 1. Definir objetivos | O que o programa de avaliações precisa alcançar? | Caracterizar os artefatos avaliados, necessidades de rigor, eficiência, redução de riscos/incertezas e ética |
| 2. Escolher estratégia e trajetória | Que combinação e sequência de avaliações atende ao projeto? | Usar [FEDS](feds.md) considerando objetivos, riscos e recursos |
| 3. Escolher propriedades | Quais características ou efeitos do artefato importam? | Identificar candidatos e priorizar com MuSCoW |
| 4. Planejar episódios | Como avaliar as propriedades selecionadas em cada ocasião? | Usar DSREMSF, condições de escolha e short-scoping quando pertinente |

Planeje objetivos e estratégia cedo para descobrir riscos e recursos que precisam
ser tratados antes de avançar no projeto. Refine propriedades durante o desenho e
desenvolvimento; detalhe cada episódio perto de sua realização, quando sua
necessidade e finalidade estiverem mais claras. As escolhas podem ser revisitadas
conforme o projeto muda. Mais objetivos e propriedades tendem a ampliar o trabalho
de planejamento e execução.

## Objetivos e propriedades

Caracterize o avaliando: produto ou processo; técnico ou sociotécnico; crítico ou
não crítico para segurança. Artefatos sociotécnicos costumam exigir atenção ao uso
e à efetividade no contexto humano; a criticidade de segurança pode exigir
avaliações mais rigorosas.

Os objetivos concernem ao programa; as propriedades, às características do
artefato, ao seu uso ou aos efeitos práticos pretendidos. Considere quatro
objetivos: rigor e confiança na evidência; eficiência diante de tempo, dinheiro,
equipamentos e acesso; redução de incertezas e riscos de falha ou retrabalho; e
ética, incluindo a minimização de riscos a pessoas, animais e organizações.
Priorize segurança e ética; em seguida, avalie a utilidade pretendida com rigor
suficiente para pesquisadores e outros destinatários da evidência. Equilibre o
esforço de avaliação com os recursos necessários para as demais atividades de
DSR. Reavalie essas prioridades quando o contexto ou as restrições mudarem.

Gere propriedades candidatas a partir da finalidade e dos efeitos práticos do
artefato, usando listas existentes como inspiração e brainstorming. Exemplos
incluem usabilidade, segurança, confiabilidade e desempenho; cada uma precisa ser
pertinente ao problema ou à questão de pesquisa. Primeiro identifique candidatas,
depois priorize e selecione as que serão avaliadas conforme objetivos e recursos.

MuSCoW prioriza propriedades relevantes para a finalidade do artefato:

| Grupo | Significado |
|---|---|
| Must | Propriedades que precisam ser avaliadas |
| Should | Propriedades que deveriam ser avaliadas |
| Could | Propriedades que poderiam ser avaliadas |
| Would | Propriedades que seria desejável incluir também |

O corpo do artigo define a quarta categoria como **Would** (“seria desejável”)
. Até cinco propriedades é uma recomendação de parcimônia, não um
limite: o caso Intelligrid priorizou seis. A quantidade final depende da relevância
e dos recursos; uma propriedade candidata ou classificada como Would não precisa
ser selecionada para avaliação.

## DSREMSF: métodos candidatos por quadrante

Formativa/somativa descreve a finalidade da avaliação. Artificial/naturalística
descreve o ambiente. A estratégia FEDS orienta a trajetória; o quadrante caracteriza
um episódio; o método descreve como obter evidência nesse episódio.

Há cinco posições por quadrante, vinte posições e dezenove métodos distintos,
pois Lab Experiment aparece em dois quadrantes. A matriz é uma seleção parcimoniosa
de métodos candidatos extraídos e classificados a partir da literatura; não é um
catálogo exaustivo nem uma prescrição. Use suas regras tecnológicas junto com os
objetivos, as restrições, o tipo de artefato e a evidência pretendida. A estratégia
e a trajetória definem o contexto do episódio; o método define como obter evidência.

| Quadrante | Métodos candidatos |
|---|---|
| Formativa artificial | Criteria-Based Evaluation; Scenarios; Prototype Demo; Lab Experiment; Theorem Proof |
| Formativa naturalística | Action Research; Interview/Focus Group; Field Experiment; Think Aloud Protocol Analysis; Qualitative Survey |
| Somativa artificial | Lab Experiment; Optimisation Analysis; Testing; Role Playing Simulation; Computer Simulation |
| Somativa naturalística | Quantitative Survey; Participant Observation; Pilot Study; Field Study or Case Study; Ethnography |

### Condições para orientar a escolha

Recomendações condicionais de escolha, não garantias de adequação ou protocolos de execução.

| Quadrante | Método | Condição relevante |
|---|---|---|
| Formativa artificial | Criteria-Based Evaluation | Critérios verificáveis por julgamento ou medida |
| Formativa artificial | Scenarios / Scenario Analysis | Situações de uso que possam ser previstas em uma árvore de decisão |
| Formativa artificial | Prototype Demo | Protótipo possivelmente parcial e de baixa fidelidade, desenvolvido rapidamente e apresentado a interessados |
| Formativa artificial | Lab Experiment | Protótipo possivelmente parcial, mas utilizável em tarefa controlada |
| Formativa artificial | Theorem Proof | Artefato puramente técnico representável matemática ou logicamente |
| Formativa naturalística | Action Research | Acesso a usuário/cliente real disposto a participar do desenho formativo |
| Formativa naturalística | Interview/Focus Group | Informação detalhada sobre sentimentos, percepções, opiniões ou sugestões pessoais ou de grupo |
| Formativa naturalística | Field Experiment | Protótipo utilizável e necessidade de dados objetivos em ambiente no qual usuários reais se comportem mais naturalmente |
| Formativa naturalística | Think Aloud Protocol Analysis | Protótipo utilizável e retorno detalhado sobre facilidade de aprendizagem ou usabilidade |
| Formativa naturalística | Qualitative Survey | Protótipo utilizável e problemas ou sugestões de um grupo maior de usuários |
| Somativa artificial | Lab Experiment | Protótipo utilizável quando evidência de efetividade em uso real não é essencial ao episódio |
| Somativa artificial | Optimisation Analysis | Artefato puramente técnico para o qual alto nível de eficiência é essencial |
| Somativa artificial | Testing | Software como artefato predominante quando funcionamento e saídas corretas são essenciais; testes funcionais/caixa-preta ou estruturais/caixa-branca |
| Somativa artificial | Role Playing Simulation | Uso em organização real inviável, mas interação entre papéis importante |
| Somativa artificial | Computer Simulation | Uso em situação real inviável ou arriscado, e sistema e uso passíveis de modelagem e execução |
| Somativa naturalística | Quantitative Survey | Características percebidas importantes e evidência estatística necessária para avaliar uma teoria de design |
| Somativa naturalística | Participant Observation | Necessidade de compreensão aprofundada da experiência, difícil de expressar, quando a exigência de rigor não é alta |
| Somativa naturalística | Pilot Study | Acesso limitado para implementar o artefato na organização, como em um ensaio de baixo risco |
| Somativa naturalística | Field Study or Case Study | Acesso pleno à implementação na organização e necessidade de evidência que a abranja |
| Somativa naturalística | Ethnography | Acesso pleno à implementação, uso que requer conhecimento aprofundado e prolongado, e exigência de evidência altamente rigorosa |

O artigo indica que alguns métodos podem ser adaptados a outro quadrante. Justifique
qual finalidade e ambiente a adaptação atende e que evidência produzirá; não basta
trocar o rótulo. A escolha do método tampouco fornece o protocolo de execução: use
literatura própria do método para desenhar coleta, análise e salvaguardas. Rigor e
força das conclusões dependem do desenho concreto, não apenas do nome do método.

## Short-scoping e sinergias

Short-scoping adapta um método para incluir apenas o trabalho necessário a avaliar
os efeitos práticos do artefato no nível de rigor requerido. Pode reaproveitar
decisões já tomadas na DSR, como a formulação do problema; dispensar análises,
etapas ou teorização redundantes; e limitar variáveis às necessárias para observar
os efeitos de uso pretendidos. Reduzir participantes ou o escopo e realismo da
tarefa também é possível, desde que a evidência continue suficiente. É especialmente
útil em avaliações formativas e pode caber em somativas quando os destinatários
aceitam o nível de rigor previsto. Eficiência, por si só, não justifica rigor
insuficiente.

A eficiência pode melhorar por quatro caminhos: escolher métodos menos intensivos
em recursos que ainda atendam ao rigor necessário; escolher um método que cubra
mais de um objetivo ou propriedade; desenhar um episódio para reunir avaliações
que poderiam ocorrer separadamente; e planejar avaliações formativas com o rigor
mínimo suficiente para confiar na decisão sobre como prosseguir. Ao reunir
propriedades, preserve as relações relevantes entre elas. Uma avaliação formativa
precisa produzir a informação específica que a próxima decisão exige.

Nesta suíte, uma proposta de corte explicita escopo original, alteração,
justificativa, economia esperada, consequências para rigor/cobertura, riscos e
decisão do pesquisador. Esse registro é uma convenção operacional da suíte.

## Aplicação e limites

MEDS pode ser incorporado a metodologias gerais de DSR, como [DSRM](dsrm.md). Aplique objetivos,
estratégia e propriedades iniciais durante a formulação do projeto; refine
propriedades e episódios formativos durante design e desenvolvimento; e prepare
propriedades e episódios somativos antes das avaliações correspondentes. A
integração é flexível e não cria dependência entre as etapas de MEDS. Componentes
distintos do artefato podem exigir estratégias diferentes.

O artigo avalia MEDS com workshops e sua aplicação ao projeto Intelligrid, além de
analisar retrospectivamente estudos que usaram FEDS. Esses relatos ilustram o uso
e sugerem benefícios; não constituem comparação direta com outros métodos de
planejamento nem estabelecem limiares universais de qualidade. A orientação de
MEDS é mais limitada para avaliar a clareza de constructos de teorias de design,
artefatos intermediários como formulações de problema e requisitos, e pesquisas
de proof-of-use. MEDS complementa metodologias gerais de DSR e não avalia o texto
ou a qualidade editorial da publicação. Eficiência não substitui utilidade do
artefato nem rigor suficiente; as conclusões não devem exceder a evidência obtida.
