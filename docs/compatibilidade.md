# Compatibilidade entre harnesses

A skill é publicada no padrão Agent Skills e pode ser instalada pelo projeto `skills`
da Vercel em vários agentes. A compatibilidade de formato e a validação do
comportamento são estados separados: a presença de `SKILL.md` no diretório certo
não demonstra que os fluxos e as gravações funcionem corretamente.

## Matriz da versão 0.2.0

| Harness e superfície | Estado | Harness CLI | Modelo | Data |
|---|---|---|---|---|
| Codex CLI/plugin | Instalável pelo padrão, sem validação comportamental | Codex CLI 0.155.1 | `gpt-6.1-sol` e `gpt-5.3-codex` rejeitados pela combinação CLI/conta | 2026-10-24 (smoke sem resposta) |
| Claude Code CLI | Instalável pelo padrão, sem validação comportamental | Não executado | — | — |
| Antigravity CLI | Instalável pelo padrão, sem validação comportamental | Não executado | — | — |
| OpenCode CLI | Instalável pelo padrão, sem validação comportamental | Não executado | — | — |
| Cursor CLI | Instalável pelo padrão, sem validação comportamental | Não executado | — | — |
| GitHub Copilot CLI | Instalável pelo padrão, sem validação comportamental | Não executado | — | — |
| Plugins nativos de terceiros e integrações MCP próprias de fornecedores | Não suportado nesta versão | — | — | — |

“Instalável pelo padrão” significa que o ecossistema Agent Skills lista o harness
como alvo de instalação e que o diretório de skill segue a documentação disponível.
A CLI `skills` e os cinco harnesses além do Codex não estão instalados neste
ambiente. A tentativa de consultar `skills` via `pnpm dlx` não alcançou
`registry.npmjs.org` por falha DNS (`ENOTFOUND`), então não há versão do instalador
testada para registrar. O smoke test da cópia padrão no Codex CLI 0.155.1 iniciou a sessão, mas
parou antes da resposta porque essa combinação rejeitou `gpt-6.1-sol` para uma conta
ChatGPT; repetir com `gpt-5.3-codex` teve o mesmo bloqueio. Os recibos não contam
como validação comportamental. A suíte tem evidências
históricas de comportamento no Codex CLI 0.160.0
para v0.1.4, em [resultados de 17/10/2026](../tests/behavior/resultados-separacao-tutorial-2026-10-17.md);
essas evidências não substituem a execução da nova versão compatível.

A matriz cobre superfícies CLI. Ela não afirma que a UI do Antigravity, a extensão
Copilot para VS Code nem as interfaces gráficas do Cursor e Codex foram verificadas.
Para atualizar um estado, registre CLI `skills` usada, versão do harness, superfície,
modelo, data, comandos, recibos, descoberta da skill e revisão humana das respostas.
Marque comportamento como **validado** somente depois de executar e revisar os
cenários aplicáveis, incluindo leitura e gravação de um plano. Execução indisponível,
falha de autenticação ou resposta vazia permanecem pendentes.

## Instalação de projeto

Execute a partir do projeto de pesquisa. O comando requer Node.js 22.20 ou superior e
usa cópias para não depender de links simbólicos:

```sh
npx skills --version
npx skills add LucasSteffens5/meds-suite --skill meds-suite \
  -a codex -a claude-code -a antigravity-cli -a opencode -a cursor -a github-copilot --copy
npx skills list
```

Durante o desenvolvimento de uma cópia local:

```sh
npx skills add ../meds-suite --skill meds-suite \
  -a codex -a claude-code -a antigravity-cli -a opencode -a cursor -a github-copilot --copy
```

No Windows, ajuste o caminho relativo ao checkout e use os mesmos argumentos. Para
instalação pessoal acrescente `-g`. Se o Codex já carregar o plugin `meds-suite@meds-local`,
retire `-a codex` para evitar uma segunda cópia carregada.

## Execução comportamental

O executor cria uma pasta de caso separada, instala uma cópia da skill no caminho
descoberto pelo harness, prepara o plano fictício, chama a CLI headless e salva
resposta e recibo fora do repositório. Use uma pasta de saída nova fora do checkout:

```sh
python scripts/run_behavior_checks.py --harness codex \
  --scenario sem-contexto --output /tmp/meds-codex
python scripts/run_behavior_checks.py --harness claude-code \
  --scenario sem-contexto --output /tmp/meds-claude
python scripts/run_behavior_checks.py --harness antigravity \
  --scenario sem-contexto --output /tmp/meds-antigravity
python scripts/run_behavior_checks.py --harness opencode \
  --scenario revisao-preservacao --output /tmp/meds-opencode
python scripts/run_behavior_checks.py --harness cursor \
  --scenario planejamento-parcial --output /tmp/meds-cursor
python scripts/run_behavior_checks.py --harness github-copilot \
  --scenario antigo-exportado --output /tmp/meds-copilot
```

Repita os cenários de retomada, mudança de contexto e revisão sem edição três vezes
por harness. Use `--model <nome-do-modelo>` para solicitar um modelo explícito quando
o harness permitir. O recibo registra versão da suíte e CLI, o modelo quando informado
pela CLI, sistema, cenário, arquivos antes/depois e status; verifique a autenticação antes
de iniciar a bateria completa. `--installed-plugin` é exclusivo do Codex e exige que
a versão instalada corresponda ao manifesto.

Para testar a transferência, exporte `plano-meds.md` de uma execução no harness de
origem e use o mesmo arquivo, sem edição intermediária, na execução do harness de
destino:

```sh
python scripts/run_behavior_checks.py --harness codex --scenario transferencia \
  --output /tmp/meds-transferencia-codex
python scripts/run_behavior_checks.py --harness claude-code --scenario transferencia \
  --plan-file /tmp/meds-transferencia-codex/transferencia-1/plano-meds.md \
  --output /tmp/meds-transferencia-claude
```

O recibo registra hashes de entrada e saída. A revisão humana compara a resposta
com a entrada e confere IDs, decisões aceitas, pendências, fontes e legenda; repita
para cada harness de destino.

Os adaptadores bloqueiam shell quando o harness oferece uma lista explícita de
ferramentas e usam sandbox nas CLIs que a disponibilizam. Cada execução trabalha numa
pasta efêmera de caso. Revise as permissões efetivas da CLI antes de executar cenários
com texto malicioso. O protocolo completo e critérios metodológicos ficam em
[tests/behavior/README.md](../tests/behavior/README.md).

## Empacotamento

O arquivo `.zip` contém a skill Agent Skills completa, sem metadados exclusivos do
Codex. Gere-o após validar o pacote e escolha um destino fora do checkout:

```sh
python scripts/package_skill.py --output /tmp/meds-suite-0.2.0.zip
```

Copie a pasta `meds-suite` do arquivo para o diretório de skills do harness ou instale
pelo CLI `skills`. O arquivo compactado não é um plugin nativo; a integração Codex
continua documentada no [README](../README.md).
