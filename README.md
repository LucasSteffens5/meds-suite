# MEDS Suite

MEDS Suite 0.2.0 oferece uma skill coordenadora para planejar, retomar e revisar
programas de avaliação de artefatos em Design Science Research (DSR). A skill usa
o padrão aberto Agent Skills; o pacote de plugin Codex continua disponível.

## Compatibilidade

A skill comum está em `skills/meds-suite/`. A documentação da especificação e dos
harnesses cobre [Agent Skills](https://agentskills.io/home), [Codex](https://learn.chatgpt.com/docs/build-skills), [Claude Code](https://code.claude.com/docs/en/skills), [Antigravity](https://antigravity.google/docs/skills), [OpenCode](https://opencode.ai/docs/skills/), [Cursor](https://cursor.com/docs/skills) e [GitHub Copilot](https://docs.github.com/en/copilot/concepts/customizations/agent-skills).

Para instalar no projeto de pesquisa com o CLI aberto `skills`, execute no diretório
desse projeto. O Node.js precisa ser 22.20 ou posterior:

```sh
npx skills add LucasSteffens5/meds-suite --skill meds-suite \
  -a codex -a claude-code -a antigravity-cli -a opencode -a cursor -a github-copilot --copy
```

A instalação cria cópias nos diretórios de skill dos harnesses selecionados. Use
`npx skills add <caminho-local-da-suite>` para testar uma cópia local. Para atualizar,
repita o comando de instalação. Acrescente `-g` para instalação pessoal. O CLI mostra
a seleção de harnesses disponíveis com `npx skills add --help`; a compatibilidade
comportamental validada está registrada em [docs/compatibilidade.md](docs/compatibilidade.md).

Se o Codex já usa o plugin local abaixo, remova `-a codex` do comando para evitar
carregar duas cópias da mesma skill. A instalação pelo padrão também pode substituir
o plugin, removendo os comandos `codex plugin` da seção seguinte.

### Plugin Codex

Dentro deste repositório, instale o plugin existente com:

```sh
codex plugin marketplace add .
codex plugin add meds-suite@meds-local
```

Depois abra uma nova conversa no projeto de pesquisa e invoque `$meds-suite`. Para
reinstalar uma atualização local, repita `codex plugin add meds-suite@meds-local`.

## Uso

Abra uma conversa no harness em que instalou a skill e descreva o caso. Por exemplo:

```text
Use meds-suite para planejar a avaliação do meu artefato. Vou descrever o caso e as informações disponíveis.
```

Para aprender o método, uma pergunta por vez, consulte o [tutorial do repositório](docs/primeiro-contato/README.md).

## Arquitetura

```text
skills/meds-suite/                       Fonte comum Agent Skills
  SKILL.md                                Entrada e seleção do fluxo
  workflows/planejar/WORKFLOW.md          Planejamento e retomada
  workflows/revisar/WORKFLOW.md           Revisão de coerência e lacunas
  references/                             MEDS, FEDS e contexto DSRM
  assets/plano-meds.md                    Modelo de plano por caso
plugins/meds-suite/
  .codex-plugin/plugin.json               Identidade e diretório de skills
  agents/openai.yaml                      Metadados de interface Codex
  skills/meds-suite/                      Espelho gerado da fonte comum
```

Gere ou verifique o espelho Codex com `python scripts/sync_codex_package.py` e
`python scripts/sync_codex_package.py --check`. A skill carrega o fluxo solicitado e
suas referências conforme a etapa. O plano é salvo no projeto de pesquisa, fora do
pacote instalado. Os metadados de interface Codex não criam subagentes.

A organização metodológica segue Baskerville, Pries-Heje e Venable (2026), MEDS,
DOI [10.1080/0960085X.2026.2627280](https://doi.org/10.1080/0960085X.2026.2627280);
as estratégias e trajetórias FEDS seguem Venable, Pries-Heje e Baskerville (2016),
DOI [10.1057/ejis.2014.36](https://doi.org/10.1057/ejis.2014.36). O contexto do
processo DSRM segue Peffers et al. (2007), DOI
[10.2753/MIS0742-1222240302](https://doi.org/10.2753/MIS0742-1222240302). Os
registros, identificadores e regras de continuidade são convenções da suíte.

## Verificações

Execute os testes estruturais e do executor com:

```sh
python scripts/sync_codex_package.py --check
python scripts/validate_package.py
python -m unittest discover -s tests
```

Para executar cenários comportamentais em um harness específico, consulte
[tests/behavior/README.md](tests/behavior/README.md). Os recibos ficam em uma pasta
externa ao checkout.

## Referências

- Baskerville, R., Pries-Heje, J., & Venable, J. R. (2026). MEDS: Methodology for Evaluation in Design Science. *European Journal of Information Systems, 35*(5), 830–847. DOI: [10.1080/0960085X.2026.2627280](https://doi.org/10.1080/0960085X.2026.2627280).
- Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: a Framework for Evaluation in Design Science Research. *European Journal of Information Systems, 25*(1), 77–89. DOI: [10.1057/ejis.2014.36](https://doi.org/10.1057/ejis.2014.36).
- Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A Design Science Research Methodology for Information Systems Research. *Journal of Management Information Systems, 24*(3), 45–77. DOI: [10.2753/MIS0742-1222240302](https://doi.org/10.2753/MIS0742-1222240302).
