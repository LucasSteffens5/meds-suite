# MEDS Suite para Codex

Plugin `meds-suite` v0.1.4 com uma skill coordenadora para planejar, retomar e revisar
programas de avaliação de artefatos em Design Science Research (DSR).
O planejamento fica em um arquivo Markdown por caso.


## Instalação local

Requer um Codex com suporte a plugins e acesso aos comandos `codex plugin`.
No terminal, dentro deste repositório Git:

```sh
codex plugin marketplace add .
codex plugin add meds-suite@meds-local
```

O catálogo resolve `./plugins/meds-suite` a partir da raiz deste repositório.
Esses comandos registram o catálogo e instalam o plugin na configuração local do
Codex. Execute-os no ambiente em que deseja usar a suíte. A instalação permite
usar o plugin também em outros projetos.

Depois da instalação, abra uma nova conversa do Codex no projeto da pesquisa.
Confira que a skill MEDS Suite aparece no seletor de skills e invoque `$meds-suite`.
Se o pacote local for atualizado, reinstale o plugin e abra uma nova conversa:

```sh
codex plugin add meds-suite@meds-local
```

## Uso

Depois de instalar a suite, abra uma conversa do Codex na pasta do projeto da
pesquisa e descreva o caso que deseja planejar:

```text
Use $meds-suite para planejar a avaliação do meu artefato. Vou descrever o caso e as informações disponíveis.
```

Para aprender a planejar uma avaliação, uma pergunta por vez, use o [tutorial do repositório](docs/primeiro-contato/README.md).

## Arquitetura

```text
.agents/plugins/marketplace.json       Catálogo local meds-local
plugins/meds-suite/
  .codex-plugin/plugin.json            Identidade e diretório de skills
  skills/meds-suite/
    SKILL.md                          Entrada e seleção do fluxo
    agents/openai.yaml                Metadados da interface
    workflows/planejar/WORKFLOW.md     Planejamento e retomada
    workflows/revisar/WORKFLOW.md      Revisão de coerência e lacunas
    references/                       MEDS, FEDS e contexto DSRM
    assets/plano-meds.md               Modelo de plano por caso
```

A skill carrega o fluxo solicitado e suas referências conforme a etapa. O caso vem
da conversa e do plano indicado pelo pesquisador. Exemplos colados são contexto
somente do exercício que a pessoa identificar. O plano é salvo no projeto da
pesquisa, fora do pacote instalado. Os metadados em `agents/` não criam subagentes.

A organização metodológica do planejamento segue Baskerville, Pries-Heje e Venable (2026), DOI [10.1080/0960085X.2026.2627280](https://doi.org/10.1080/0960085X.2026.2627280);
as estratégias e trajetórias FEDS seguem Venable, Pries-Heje e Baskerville (2016), DOI [10.1057/ejis.2014.36](https://doi.org/10.1057/ejis.2014.36).
O contexto do processo DSRM segue Peffers, Tuunanen, Rothenberger e Chatterjee (2007), DOI [10.2753/MIS0742-1222240302](https://doi.org/10.2753/MIS0742-1222240302).
Os registros, identificadores e regras de continuidade são convenções desta suíte.

O fluxo de planejamento organiza objetivos, estratégia FEDS, propriedades
priorizadas por MuSCoW e episódios com métodos candidatos DSREMSF. As escolhas podem
ser revisitadas. A revisão relaciona observações a seções e episódios concretos.


## Referências

- Baskerville, R., Pries-Heje, J., & Venable, J. R. (2026). MEDS: Methodology for Evaluation in Design Science. *European Journal of Information Systems, 35*(5), 830–847. DOI: [10.1080/0960085X.2026.2627280](https://doi.org/10.1080/0960085X.2026.2627280).

- Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: a Framework for Evaluation in Design Science Research. *European Journal of Information Systems, 25*(1), 77–89. DOI: [10.1057/ejis.2014.36](https://doi.org/10.1057/ejis.2014.36).

- Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A Design Science Research Methodology for Information Systems Research. *Journal of Management Information Systems, 24*(3), 45–77. DOI: [10.2753/MIS0742-1222240302](https://doi.org/10.2753/MIS0742-1222240302).
