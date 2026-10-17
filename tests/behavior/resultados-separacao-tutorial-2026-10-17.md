# Separação do tutorial em sessões novas — 2026-10-17 (v0.1.4)

O plugin `meds-suite@meds-local` foi atualizado e confirmado instalado e habilitado
na v0.1.4. Foram concluídas cinco sessões efêmeras novas do Codex CLI 0.160.0, todas
com o modelo observado `gpt-6.1-sol`. O executor usou a skill instalada, em pastas
temporárias independentes, sem copiar a skill de teste para essas sessões.

| Cenário | Resultado observado |
|---|---|
| `sem-contexto` | Perguntou qual artefato será avaliado e que problema resolve; não criou arquivo nem introduziu dados do tutorial. |
| `outro-dominio` | Salvou um plano parcial sobre irrigação, reteve as restrições informadas e perguntou qual decisão a evidência apoiará; não introduziu estudantes, busca acadêmica, IDs D1–D4 nem prazo do tutorial. |
| `exemplo-explicito` | Usou os fatos S1–S6 e D1–D4 que a pessoa colou, registrou expectativas como não observadas e manteve O1 como proposta até a resposta. Salvou no caminho solicitado para o exercício. |
| `retomada-sem-material` | Pediu o trecho do tutorial e a última pendência, ou o arquivo do exercício; não reconstruiu dados ou decisões. |
| `revisao-plano-indicado` | Revisou o plano indicado do painel agrícola, preservou O1 e P2 aceitos e as outras escolhas pendentes; o hash confirma que o arquivo não foi editado. |

Uma primeira tentativa de `outro-dominio` foi descartada da contagem porque o cenário
estava marcado incorretamente como somente leitura, embora a solicitação autorizasse
salvar o plano. O cenário foi corrigido e repetido em sessão nova; a repetição consta
na contagem acima.

O plano do cenário de revisão é um fixture sintético e específico do domínio agrícola.
Não havia um plano de pesquisa fornecido por uma pessoa para este teste; portanto,
esta sessão verifica a leitura e a preservação de um plano indicado, mas não substitui
uma revisão com um caso real de pesquisador.

A validação estrutural também confirma que o pacote não contém o diretório de tutorial,
marcadores textuais do caso D1–D4 ou prompts de tutorial na descrição e metadados da
interface. A documentação didática completa permanece em `docs/primeiro-contato/README.md`.

Os recibos, respostas e planos gerados nas sessões estão em
`/private/tmp/meds-v014-separacao-tutorial-escalated` e
`/private/tmp/meds-v014-outro-dominio`. Esta verificação cobre os cinco cenários
executados; não comprova comportamento para todas as conversas, eficácia da suíte
ou validade científica.
