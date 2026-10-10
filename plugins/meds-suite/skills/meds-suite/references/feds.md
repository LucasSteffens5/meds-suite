# FEDS: estratégia, trajetória e desenho da avaliação

Síntese original de Venable, J., Pries-Heje, J., & Baskerville, R. (2016).
*FEDS: a Framework for Evaluation in Design Science Research*. European Journal
of Information Systems, 25(1), 77–89. Publicação antecipada online em 2014;
2016 é o ano da edição.
DOI: [10.1057/ejis.2014.36](https://doi.org/10.1057/ejis.2014.36).

FEDS orienta **por que, quando, como e o que avaliar** em DSR. Considera tanto a
utilidade do artefato em seu ambiente quanto a qualidade da contribuição de
conhecimento, incluindo evidência sobre teorias de design. Combina um quadro de
estratégias e trajetórias com um processo de quatro passos para desenhar avaliações.

## Finalidade, ambiente e momento

**Formativa** fornece uma base para aperfeiçoar o artefato e decidir como prosseguir.
**Somativa** julga em que medida os resultados atendem às expectativas, requisitos
ou padrões, por exemplo, para adoção, certificação ou aprovação de continuidade.
A distinção é pela finalidade, não pelo conteúdo ou pela mecânica do método. Uma
mesma atividade pode produzir evidência útil às duas finalidades.

**Artificial** abstrai ou se afasta de uma ou mais condições reais: pessoas
usuárias, sistema ou problema/tarefa. Pode ser empírica, como experimentos de
laboratório e simulações, ou não empírica, como argumentos teóricos e provas
matemáticas. **Naturalística** examina o artefato em seu ambiente real de uso,
considerando pessoas usuárias reais, sistema real e problema/tarefa reais em um
contexto real. É sempre empírica. Usuários reais executando uma tarefa fictícia
não bastam para tornar uma avaliação naturalística; o artigo ilustra esse caso
como artificial. O nome do método tampouco resolve a classificação.
Uma prova matemática é artificial e não empírica; seu uso para aperfeiçoar ou
julgar o artefato é que determina sua finalidade formativa ou somativa.

Os eixos formativa/somativa e artificial/naturalística são **contínuos e
independentes**. Uma trajetória combina episódios ao longo do projeto; os quatro
quadrantes ajudam a situá-los, sem esgotar posições intermediárias ou usos mistos
da evidência. Avaliações artificiais e naturalísticas podem servir a qualquer uma
das duas finalidades.

O momento é uma distinção separada: **ex ante**, antes da escolha, aquisição,
design ou construção; **intermediário**, durante esse percurso; e **ex post**,
após aquisição, desenvolvimento ou implementação. Indique a atividade em relação
à qual o momento é definido. Uma avaliação somativa pode ser ex ante ou
intermediária, como ao julgar uma proposta para aprovar sua continuidade; uma
avaliação ex post pode ser formativa, ao orientar melhorias no artefato implementado.

**Eficácia** examina se o benefício decorre do artefato, isolando outros fatores;
**efetividade** examina se o benefício se mantém em uso real, incluindo adoção e
contexto social. Avaliações artificiais costumam favorecer controle de
confundidores, repetibilidade e atribuição causal, frequentemente com menor custo;
sua abstração pode limitar a correspondência com o uso real e a generalização.
Avaliações naturalísticas favorecem realismo e evidência de efetividade, mas a
complexidade, os confundidores e os custos podem dificultar a interpretação e a
atribuição dos efeitos. Nenhum ambiente garante rigor por si só; as conclusões
dependem do desenho e da evidência obtida.

## Estratégias arquetípicas

| Estratégia | Quando considerar | Trajetória típica |
|---|---|---|
| Quick & Simple | Construção pequena **e** simples, com baixos riscos **e incertezas** sociais e técnicos | Pouca avaliação formativa e avanço rápido para somativa mais naturalística; poucos episódios, podendo haver apenas uma avaliação somativa |
| Human Risk & Effectiveness | Risco principal social/de uso **e/ou** avaliação com usuários reais em seu contexto real relativamente barata diante dos recursos **e/ou** objetivo crítico de estabelecer rigorosamente benefício sustentado em situações reais e no longo prazo | Formativa cedo, possivelmente artificial, avançando rapidamente para formativa mais naturalística; depois somativa com foco no rigor da evidência de efetividade |
| Technical Risk & Efficacy | Risco principal técnico **e/ou** avaliação com usuários, sistemas e contexto reais proibitivamente custosa **e/ou** objetivo crítico de estabelecer rigorosamente que o benefício se deve ao artefato, e não a outros fatores | Artificial formativa iterativa cedo, avançando para artificial somativa de eficácia; avaliações mais naturalísticas perto do fim |
| Purely Technical Artefact | Artefato puramente técnico, sem aspectos sociais, não usado por nem afetando pessoas, **ou** aplicação humana tão distante que torne a avaliação naturalística irrelevante ou inviável no projeto | Semelhante a Quick & Simple, mas favorece avaliações artificiais em todo o percurso, com finalidades formativas e/ou somativas conforme os objetivos |

Essas condições são orientações contextuais. Custo é relativo aos recursos do
projeto e pode envolver tempo, dinheiro, saúde ou vida. Construção simples com
risco elevado não justifica Quick & Simple apenas pela simplicidade; descobrir
falhas somente na avaliação final pode tornar essa trajetória arriscada. Ser
software não implica ser puramente técnico. Na aplicação humana distante, verifique
se usuários e contexto reais estão inacessíveis ou ainda não existem.

As estratégias são protótipos, podem ser combinadas e revisitadas; outras são
possíveis. Objetivos ou riscos distintos podem justificar combinações. Na suíte,
elas também podem ser registradas por componente, conforme [MEDS](meds.md).
No exemplo hospitalar do artigo, uma estratégia híbrida pode
examinar primeiro o funcionamento técnico da tecnologia e depois a interação
entre médicos com Human Risk & Effectiveness. A quantidade, o momento e a posição
dos episódios dependem do projeto, sem sequência obrigatória nem exigência de
passar pelos quatro quadrantes.

## Processo original de quatro passos

| Passo | Orientação operacional sintetizada do FEDS |
|---|---|
| 1. Explicitar objetivos | Considerar rigor (eficácia e efetividade), redução de incertezas/riscos, ética e eficiência. Definir a evidência necessária sobre utilidade, sustentação de teoria de design, comparação com alternativas/estado da arte, propriedades relevantes, efeitos indesejáveis e explicação de por que o artefato funciona ou não, conforme o projeto |
| 2. Escolher estratégia(s) | Identificar e priorizar riscos de design; avaliar custo e acesso a usuários, sistemas e contexto reais diante dos recursos; considerar natureza do artefato, distância da aplicação humana e complexidade da construção; justificar a estratégia ou combinação e a trajetória |
| 3. Determinar propriedades | Gerar candidatas e alinhá-las aos objetivos e à estratégia; selecionar conforme finalidade, contexto, estágio e riscos. Avaliações formativas iniciais tendem a focar menos propriedades, ligadas aos riscos prioritários, que avaliações somativas posteriores |
| 4. Desenhar episódios | Identificar restrições e recursos escassos, como tempo, pessoas, orçamento e local; priorizar fatores essenciais, importantes, menos importantes, desejáveis ou irrelevantes; definir quantidade de episódios e quem fará o quê, quando e como |

Os objetivos podem competir. Avalie riscos técnicos e humanos cedo, quando
praticável, para orientar o design antes de investimentos elevados. Considere os
riscos da própria avaliação e do uso futuro, sobretudo em artefatos críticos para
segurança; eficiência precisa equilibrar recursos com rigor, redução de riscos e
ética. As seis necessidades de evidência acima são possibilidades a selecionar
conforme o projeto, não uma lista obrigatória de avaliações.

Exemplos de propriedades, como usabilidade, confiabilidade, desempenho ou ajuste
organizacional, são inspiração contextual, não critérios universais. Os passos
podem mudar de ordem e iterar: propriedades podem afetar a finalidade ou o
ambiente escolhidos. FEDS já apresentava esse processo de quatro passos; [MEDS](meds.md)
o desenvolve com MuSCoW, DSREMSF e short-scoping, detalhados naquela referência.

## Evidência e limites

O artigo analisa retrospectivamente dois estudos existentes, GIST e o trabalho de
Zhao e colaboradores, e relata a aplicação do quadro ao projeto Site-Storming.
Esta aplicação é apresentada pelos autores como avaliação naturalística somativa
do próprio FEDS, por sua utilidade no planejamento de um projeto DSR. As propostas
de melhoria das análises retrospectivas são sugestões sobre o que poderia ter
sido feito, não benefícios demonstrados por executar essas alternativas.
Os autores reconhecem a limitação de poucos estudos e a necessidade de mais
aplicações e avaliações com artefatos variados, inclusive estratégias híbridas.

Nome de estratégia ou trajetória não comprova rigor, eficácia ou efetividade.
Conclusões sobre efetividade exigem evidência adequada de uso real; testes
artificiais, por si só, não a estabelecem. Relatos incompletos não permitem
concluir que episódios não mencionados deixaram de ocorrer.

## Aplicação na suíte

Explique a relação entre contexto, objetivos, estratégia proposta e trajetória.
Quando faltarem informações, mantenha alternativas e pendências. Não use o nome
de um método como se fosse estratégia nem deduza finalidade pela cronologia.

Para consultar DSREMSF, esta suíte registra uma **classificação principal** do
episódio, justificando finalidade predominante e ambiente pelas condições previstas.
Registre também usos complementares da evidência e condições parcialmente reais.
Essa classificação discreta é uma convenção operacional da suíte; não transforma
os contínuos de FEDS em categorias exclusivas nem garante adequação de um método.
Consulte [MEDS](meds.md) para priorização de propriedades, seleção de métodos e
ajuste de escopo; protocolos de execução exigem literatura específica do método.
