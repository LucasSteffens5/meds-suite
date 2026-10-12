# Verificação da legenda em sessões novas — 2026-10-12 (v0.1.2)

Foram concluídas nove sessões efêmeras do Codex CLI 0.160.0, todas com o modelo
observado `gpt-6.1-sol` e uma cópia local da skill carregada em cada pasta isolada.
As respostas e os planos foram conferidos depois da execução. Uma tentativa
inicial do cenário `incompleto` foi bloqueada antes de iniciar o modelo por
permissões do sandbox; ela não produziu resposta e não entra nas contagens abaixo.

| Cenário | Sessões | Resultado observado |
|---|---:|---|
| `incompleto` | 1 | Resposta de pergunta inicial termina com uma legenda; nenhum arquivo foi criado, conforme o pedido de trabalhar somente no chat. |
| `planejamento-parcial` | 1 | Resposta e plano parcial terminam com uma legenda cada; estratégia, propriedades e episódios dependentes permaneceram pendentes. |
| `retomada` | 3 | As três respostas e os três planos atualizados terminam com uma legenda única. |
| `revisao-preservacao` | 3 | As três respostas terminam com uma legenda; recibos mostram zero arquivos alterados em todas as revisões. |
| `antigo-exportado` | 1 | Resposta e plano migrado terminam com uma legenda; O1, P1 e E1 mantêm seus significados registrados. |

Nas nove respostas e nos cinco planos criados ou atualizados, `Legenda` e `Siglas`
aparecem uma vez e a legenda é o conteúdo final. As três revisões somente no chat
mantiveram os arquivos intactos segundo os recibos. As respostas, cópias de planos
e recibos completos ficaram em pastas externas ao repositório, sob
`/private/tmp/meds-legend-*-20261012`.

Esta conferência verifica a regra de apresentação nos cenários executados. Não
abrange os demais cenários do protocolo, descoberta automática da skill no Codex
Desktop, julgamento metodológico independente, eficácia da suíte ou validade
científica.
