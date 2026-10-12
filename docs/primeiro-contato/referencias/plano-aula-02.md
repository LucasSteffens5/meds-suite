# Plano MEDS — Organizador de documentos acadêmicos

**Exemplo ilustrativo fictício. Avaliações futuras, não executadas.** Aceitações
abaixo pertencem à história didática de Ana, não ao leitor nem a pesquisa real.

## Contexto

- Identificador: tutorial-organizador.
- Última atualização: rodada fictícia 2; sem data de execução.
- Etapa atual: planejamento de E1; próximo passo: definir seus critérios e preparar E2 com cobertura reduzida.
- Problema/finalidade: encontrar documentos acadêmicos por título e etiqueta.
- Artefato: produto de software sociotécnico, protótipo local v0.1, não crítico para segurança.
- Estágio DSR: design e desenvolvimento; questão de pesquisa pendente.
- Destinatários: Ana e orientador; decidir melhorias e próximo passo.
- Recursos de avaliação: três dias de prazo após mudança; até duas horas de Ana, computador próprio, sem verba.
- Demais atividades DSR: restante do prazo para desenvolvimento e documentação.
- Acesso a estudantes e contexto real: não confirmado.
- Restrição: **“Não quero medir notas nem coletar documentos pessoais.”**
- Riscos: buscas incorretas e dificuldade de entender a interface; dados sintéticos.

## 1. Objetivos da avaliação

| ID | Objetivo | Relação com a finalidade | Rigor/riscos/recursos | Situação |
|---|---|---|---|---|
| O1 | Identificar falhas para orientar melhorias | Busca e apresentação compreensíveis | Evidência suficiente para decidir correções; sem alegar usabilidade real | Aceito na rodada fictícia 1 |
| O2 | Julgar correção das buscas nos cenários sintéticos cobertos | Recuperar resultados previstos | Resultados comparáveis à ficha, conclusão limitada aos cenários | Aceito na rodada fictícia 1 |

## 2. Estratégia e trajetória

- Technical Risk & Efficacy aceita para a trajetória **inicial**, por priorizar o risco de recuperação incorreta.
- Trajetória: E1 artificial formativo para orientar correções; E2 artificial somativo para julgar resultados esperados nos cenários definidos, depois das correções.
- Ambos ocorrem durante desenvolvimento. O caráter somativo de E2 vem do julgamento pretendido, não de ocorrer depois.
- Artefato sociotécnico: estes episódios não cobrem sua utilidade em uso real. Acesso e desenho de avaliação posterior com estudantes permanecem pendentes.
- Alternativa futura: examinar Human Risk & Effectiveness se houver contexto e acesso adequados; apenas proposta.
- Justificativa contextual: começar pelo risco técnico é viável com os recursos informados. Não implica que testes de saídas provem causalidade ou benefício sustentado.

## 3. Propriedades a avaliar

| ID | Propriedade | Objetivos | MuSCoW | Justificativa/como observar | Situação |
|---|---|---|---|---|---|
| P1 | Correção das buscas | O1, O2 | Must | Comparar IDs retornados com esperados S1–S3 após corte; protocolo detalhado pendente | Aceita |
| P2 | Clareza da interface | O1 | Should | Inspecionar rótulos e apresentação; critérios ainda pendentes | Aceita |
| P3 | Aparência visual | O1 | Could | Possível melhoria; sem observação inicial selecionada | Aceita como candidata fora do escopo inicial |
| P4 | Personalização | O1 | Would | Desejável posteriormente; sem observação inicial selecionada | Aceita como candidata fora do escopo inicial |

MuSCoW usa Would conforme a referência MEDS da suíte. Prioridade não significa
que uma propriedade fora do escopo já tenha sido avaliada.

## 4. Episódios planejados

### E1 — Inspeção para orientar correções

- Finalidade principal: formativa; O1; orientar ajustes do protótipo. Uso complementar: preparar critérios de E2, sem substituí-lo.
- Propriedades: P1 e P2; artefato v0.1 em desenvolvimento.
- Ambiente principal: artificial; Ana inspecionará a interface e consultas sintéticas, sem estudantes em suas tarefas reais.
- Método aceito: Criteria-Based Evaluation, candidato DSREMSF para critérios verificáveis por julgamento/medida.
- Alternativa considerada: Prototype Demo poderia mostrar o protótipo, mas isoladamente não fornece critérios de inspeção; não selecionada.
- Momento: intermediário, durante desenvolvimento, antes das correções decididas com E1.
- Escopo: verificar organização da busca e apresentação de resultados; critérios operacionais de clareza pendentes.
- Responsável previsto: Ana; acesso: computador e descrição/protótipo local, sem participantes.
- Evidência esperada: discrepâncias e observações para recomendar correções; não há achados registrados.
- Decisão apoiada: quais problemas corrigir antes de E2.
- Sinergia: inspecionar correção e clareza no mesmo episódio, preservando observações distintas.
- Short-scoping: não proposto nesta rodada.
- Pendências: definir critérios de clareza, confirmar versão inspecionável e buscar literatura/protocolo próprio do método.

### E2 — Julgamento de resultados sintéticos

- Finalidade principal: somativa; O2; julgar atendimento às saídas previstas. Eventuais falhas também poderão orientar melhorias, uso complementar formativo.
- Propriedade: P1; versão posterior às correções de E1, ainda a identificar.
- Ambiente principal: artificial; consultas e documentos sintéticos, sem uso real por estudantes.
- Método aceito: Testing, candidato DSREMSF para software com funcionamento e saídas corretas essenciais.
- Alternativa considerada: Lab Experiment se fosse necessário outro desenho controlado com protótipo utilizável; não necessário ao julgamento simples das saídas planejadas.
- Momento: intermediário ao projeto, após as correções; não depende de estar no final da pesquisa.
- Escopo original: S1–S6 da ficha. Escopo atual aceito: S1–S3. IDs esperados por consulta disponíveis; procedimento de registro e execução ainda pendente.
- Responsável previsto: Ana; recursos: parte das duas horas disponíveis, sem participantes.
- Evidência esperada: correspondências/discrepâncias entre IDs esperados e observados, quando a avaliação for executada.
- Limites: julgamento restrito a S1–S3; S4–S6 sem cobertura. Não demonstra correção universal, usabilidade, causalidade ou benefício sustentado em uso real.
- Decisão apoiada: corrigir falhas detectadas ou preparar etapa seguinte com cobertura delimitada.
- Sinergia: reutilizar dados sintéticos preparados para E1 sem tratar inspeção e teste como a mesma evidência.
- Short-scoping aceito na rodada fictícia 2:
  - Original: S1–S6; corte: manter S1–S3, retirar S4–S6.
  - Justificativa: prazo caiu de duas semanas para três dias; preservar verificação básica viável sem prometer cobertura original.
  - Economia esperada: menos preparação, registro e análise; qualitativa, sem percentual de tempo estimado.
  - Efeito sobre rigor/cobertura: menor variedade de comportamento observável; evidência insuficiente para afirmar o atendimento dos seis cenários.
  - Riscos residuais: falhas em consulta sem resultado, variação de maiúsculas e múltiplas correspondências por título podem passar despercebidas.
  - Escolha: Ana aceitou o corte e a conclusão restrita, sem inferir benefício real. Se essa cobertura for necessária à próxima decisão, reabrir o corte antes de executar.
- Pendências: identificar versão e protocolo de testes; episódios com estudantes dependem de acesso e desenho próprio.

## Decisões e mudanças

| Contexto | IDs | Escolha | Situação | Origem fictícia | Aplicabilidade |
|---|---|---|---|---|---|
| Rodada 1 | O1, O2 | Objetivos do programa | Aceita | Ana: “Aceito O1 e O2.” | Aplicáveis ao contexto inicial |
| Rodada 1 | Estratégia, E1, E2 | Trajetória inicial e métodos | Aceita historicamente | Ana: “Aceito Technical Risk & Efficacy, E1 com Criteria-Based Evaluation e E2 com Testing em S1–S6.” | Estratégia e métodos mantidos; escopo de E2 substituído na rodada 2 |
| Rodada 1 | P1–P4 | Must, Should, Could, Would; P3/P4 fora da avaliação inicial | Aceita | Ana: “Aceito essas prioridades; P3 e P4 ficam para depois.” | P1/P2 cobertas; P3/P4 não selecionadas |
| Rodada 1 | Etapa futura | Examinar Human Risk & Effectiveness com acesso adequado | Proposta | Alternativa da IA, sem aceitação | Depende de contexto e acesso |

| Rodada 2 | Contexto, E1, E2 | Prazo de duas semanas para três dias | Informação fornecida | Ana: “O prazo caiu para três dias; continuo sem acesso confirmado.” | Recursos e cobertura reexaminados; O1/O2 preservados |
| Rodada 2 | E2/P1/O2 | Corte S1–S6 para S1–S3 e julgamento restrito | Aceita | Ana: “Aceito o corte para S1–S3; não aceito correção geral nem benefício em uso real.” | Cobertura original deixou de se aplicar; objetivos mantidos com limite explícito |

## Pendências e próximo passo

| Pendência | Item | Informação necessária |
|---|---|---|
| Critérios de clareza | P2/E1 | Definir o que Ana observará e com qual justificativa |
| Protocolos e versões | E1/E2 | Literatura específica e artefato disponível no momento da execução |
| Uso real | Estratégia futura | Confirmar acesso, contexto, recursos e salvaguardas |
| Questão de pesquisa | Contexto | Formulação ainda não fornecida |

Próximo passo: detalhar critérios de E1 e conferir se S1–S3 bastam à próxima decisão; manter acesso e execução pendentes.

## Fontes e materiais do caso

- Ficha fictícia e cenários S1–S6 em `docs/primeiro-contato/materiais/ficha-caso.md` (caminho do material do exercício, não da instalação do plugin).
- Baskerville, Pries-Heje e Venable (2026), *MEDS: Methodology for Evaluation in Design Science*, DOI 10.1080/0960085X.2026.2627280: quatro etapas, MuSCoW, candidatos DSREMSF e short-scoping.
- Venable, Pries-Heje e Baskerville (2016), *FEDS: a Framework for Evaluation in Design Science Research*, DOI 10.1057/ejis.2014.36: estratégia, finalidade e ambiente.
- Peffers et al. (2007), *A Design Science Research Methodology for Information Systems Research*, DOI 10.2753/MIS0742-1222240302: posição no projeto e distinção entre demonstração e avaliação.

Os artigos orientam o planejamento; O1/P1/E1 são IDs da suíte, e os métodos,
prioridades e quantidades deste caso são julgamentos contextuais da simulação.
A literatura específica de execução dos métodos continua necessária.
