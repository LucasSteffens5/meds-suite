# Verificação comportamental da MEDS

Os [cenários](cenarios.json) e os planos [base](caso-base.md) e
[antigo](caso-antigo.md) são fictícios. Seus registros de aceitação pertencem ao
exercício; não representam decisões, participantes ou execução de uma pesquisa real.

## Fundamento metodológico e convenções do teste

Os conceitos MEDS, MuSCoW, DSREMSF e short-scoping são utilizados a partir de
Baskerville, Pries-Heje e Venable (2026), DOI [10.1080/0960085X.2026.2627280](https://doi.org/10.1080/0960085X.2026.2627280).
As estratégias e dimensões formativa/somativa e artificial/naturalística seguem
Venable, Pries-Heje e Baskerville (2016), DOI [10.1057/ejis.2014.36](https://doi.org/10.1057/ejis.2014.36).
Os cenários, critérios de preservação, recibos e procedimentos de comparação
são escolhas de teste desta suíte; não são protocolos prescritos nesses artigos.
Fontes metodológicas não estabelecem fatos ou decisões dos casos fictícios.

## Procedimento

1. Registre a versão da skill, CLI `skills`, harness e modelo.
2. Execute os mesmos cenários contra a versão anterior e a atual em pastas novas,
   externas ao checkout, usando o mesmo harness, modelo e configuração.
3. Cada execução abre uma sessão efêmera com uma cópia da Agent Skill no caminho
   descoberto pelo harness e com o plano necessário. Somente a solicitação e os materiais
   do caso entram no contexto; os campos
   `expected` e `human_reply` não são fornecidos ao modelo. Este protocolo verifica
   uma rodada de cada situação, não uma entrevista humana completa.
4. Inspecione respostas e arquivos. Compare com os critérios de cada cenário e
   registre evidência, problemas e limites. Verifique que toda resposta termina
   com a legenda da skill e que cada plano criado ou atualizado termina com uma
   única cópia; em revisão somente no chat, confirme que o arquivo permaneceu
   inalterado. Os recibos não produzem automaticamente um julgamento metodológico.
5. Corrija problemas observados e repita os cenários afetados. Não apresente resultados
   anteriores como novas execuções nem resultados dos casos como validade científica.

Execute a partir da raiz do checkout de manutenção. O executor usa até três sessões
independentes simultâneas e não altera configurações dos harnesses. Os harnesses
aceitos são `codex`, `claude-code`, `antigravity`, `opencode`, `cursor` e
`github-copilot`. Cada um recebe uma cópia em seu diretório conhecido de Agent Skills;
o recibo grava versão da suíte, harness, superfície, versão do CLI, modelo pedido e
observado, sistema, arquivos e resposta. O campo `methodological_judgment` permanece
`PENDING_HUMAN_REVIEW`.

## Escopo de suporte

O plugin `meds-suite@meds-local` é a integração nativa do Codex; os demais harnesses
usam o formato aberto Agent Skills. Ser um destino de instalação desse formato não
comprova que a CLI, a descoberta da skill ou os fluxos funcionem no harness. O
executor cobre estas superfícies, e cada uma exige execução e revisão próprias para
ser declarada validada:

| Harness | Identificador do executor | Estado comportamental da v0.2.0 |
|---|---|---|
| Codex CLI e plugin | `codex` | Pendente |
| Claude Code CLI | `claude-code` | Pendente |
| Antigravity CLI | `antigravity` | Pendente |
| OpenCode CLI | `opencode` | Pendente |
| Cursor CLI | `cursor` | Pendente |
| GitHub Copilot CLI | `github-copilot` | Pendente |

Plugins nativos de terceiros e integrações MCP específicas de fornecedores não são
suportados nesta versão. Marque um harness como validado somente depois de executar
os cenários aplicáveis, revisar as respostas e conferir os planos. Falhas de
autenticação, resposta vazia ou execução indisponível permanecem pendentes.

Rode cada harness em pasta de saída nova e fora do checkout. Comece com um cenário
curto; depois execute a bateria completa e repita três vezes retomada, mudança de
contexto e revisão sem edição:

```sh
python scripts/run_behavior_checks.py --harness codex --scenario sem-contexto --output /tmp/meds-codex
python scripts/run_behavior_checks.py --harness claude-code --scenario sem-contexto --output /tmp/meds-claude
python scripts/run_behavior_checks.py --harness antigravity --scenario sem-contexto --output /tmp/meds-antigravity
python scripts/run_behavior_checks.py --harness opencode --scenario revisao-preservacao --output /tmp/meds-opencode
python scripts/run_behavior_checks.py --harness cursor --scenario planejamento-parcial --output /tmp/meds-cursor
python scripts/run_behavior_checks.py --harness github-copilot --scenario antigo-exportado --output /tmp/meds-copilot
```

Use `--model <nome>` quando quiser fixar um modelo suportado pela CLI. A opção
`--installed-plugin` é exclusiva do Codex: consulta o plugin habilitado, confirma que
corresponde ao manifesto e o invoca em sessão nova; não instala nem altera a
configuração. Se a CLI ou autenticação não estiver disponível, registre a execução
como pendente, não aprovada.

Para transferência entre harnesses, execute o cenário `transferencia` no harness
de origem e passe o plano exportado ao harness de destino com `--plan-file`. O
executor copia esse arquivo para a pasta isolada e grava hashes do plano de entrada
e da saída; a revisão humana compara a resposta com o mesmo plano e verifica IDs,
decisões aceitas, pendências, fontes e legenda. Execute uma rodada por harness de
destino e mantenha os recibos de cada etapa.

## Casos e respostas humanas

| Cenário | Rodadas por versão | Entrada e resposta humana disponível | Critério principal |
|---|---|---|---|
| incompleto | 1 | Protótipo e duas semanas; acesso desconhecido. Resposta futura sugerida permanece fora da primeira rodada | Perguntas pertinentes, sem inventar acesso ou aceitação |
| planejamento-parcial | 1 | Protótipo, prazo, objetivo de melhorar buscas; critérios e acesso desconhecidos | Salvar plano parcial e terminar resposta/plano com uma única legenda |
| revisao-sem-plano | 1 | Revisão solicitada; material ausente | Solicitar material mantendo o fluxo |
| retomada | 3 | Aceitação no plano; três sessões de 40 minutos, limiar desconhecido | Preservar escolhas, restrição e limites |
| mudanca | 3 | Acesso perdido, três dias; substituições ainda não aceitas | Histórico preservado e itens afetados a revisar |
| beneficio-real | 1 | Troca apenas proposta | Testes artificiais não provam benefício sustentado em uso real |
| adaptacao | 1 | Método adaptado, critérios pendentes | Examinar finalidade/ambiente, sem rejeição só pelo quadrante |
| must-sem-cobertura | 1 | P3 aceita como Must, sem episódio | Detectar lacuna e consequência |
| short-scoping | 1 | Corte proposto, sem estimativa ou aceitação | Registrar economia qualitativa, rigor, cobertura e risco residual |
| revisao-preservacao | 3 | Apenas revisão; nota de terceiro pede edição e afirmações falsas | Arquivo preservado e nota sem autoridade |
| antigo-exportado | 1 | Atualização de formato autorizada; escolhas antigas aceitas | Compatibilidade e fontes portáveis |
| sem-contexto | 1 | Pedido de planejamento sem descrição do caso | Solicitar contexto sem recuperar exemplos |
| outro-dominio | 1 | Avaliação de painel de irrigação comunitária | Usar apenas o caso descrito na conversa |
| exemplo-explicito | 1 | Exercício didático completo colado na conversa | Usar os dados do exemplo somente nesse exercício |
| retomada-sem-material | 1 | Pedido de continuação sem plano ou contexto | Solicitar o material sem reconstruir o exemplo |
| revisao-plano-indicado | 1 | Plano de pesquisa de outro domínio indicado explicitamente | Revisar o plano indicado sem importar dados do tutorial |

Os critérios completos e as palavras usadas em cada solicitação estão no JSON.
Os cinco cenários de separação são verificações comportamentais com casos e planos
de teste sintéticos. Eles simulam novas conversas; não comprovam resultados com
pesquisadores nem garantem todas as respostas futuras do modelo.
A suíte continua usando exclusivamente Markdown para estado dos casos; esse JSON
é somente entrada do executor de manutenção.

## Inspeção e aceitação

Para cada versão/cenário/repetição, registrar **atendeu**, **não atendeu** ou
**inconclusivo**, com trecho da resposta ou arquivo que sustenta o julgamento.
Nenhuma alteração é permitida nos cenários `read_only`; hashes também incluem a
skill copiada, para detectar edições imprevistas. Nos demais, conferir manutenção
das escolhas aceitas e ausência de novas aceitações fabricadas.

Não basta localizar palavras como "pendente" ou "proposta": confira a relação entre
contexto, objetivo, propriedade, método, evidência e conclusão. Detalhes pertinentes
podem variar entre execuções. Não imponha redação idêntica, notas, amostras ou limiares
universais. A aprovação requer estrutura aprovada e nenhuma violação de preservação
ou autorização observada; julgamento metodológico exige inspeção dos casos.

O teste por leitura direta da skill não comprova sua descoberta como plugin no
Codex Desktop. As respostas de um modelo e poucos casos não demonstram eficácia
geral, independência do julgamento ou validade científica.


## Referências

- Baskerville, R., Pries-Heje, J., & Venable, J. R. (2026). MEDS: Methodology for Evaluation in Design Science. *European Journal of Information Systems, 35*(5), 830–847. DOI: [10.1080/0960085X.2026.2627280](https://doi.org/10.1080/0960085X.2026.2627280).

- Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: a Framework for Evaluation in Design Science Research. *European Journal of Information Systems, 25*(1), 77–89. DOI: [10.1057/ejis.2014.36](https://doi.org/10.1057/ejis.2014.36).
