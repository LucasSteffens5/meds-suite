# Verificação da revisão v0.1.1 — 2026-10-10

Esta é uma execução nova, com casos fictícios. A comparação usa a v0.1.0 do
commit `70b72b4` e os arquivos locais da v0.1.1, antes de publicação. Não reutiliza
as observações de 2026-10-03 como resultados novos.

## Ambiente e procedimento

- Codex CLI `0.160.0`; modelo anunciado em cada sessão: `gpt-6.1-sol`.
- macOS, Darwin `27.0.0 arm64`, conforme cada recibo.
- Mesmos prompts e planos iniciais nas duas versões. Os critérios `expected` e as
  respostas humanas previstas não foram enviados ao modelo.
- Dez cenários, dezesseis sessões por versão. Retomada, mudança de contexto e
  revisão sem edição foram repetidas três vezes cada.
- Sessões efêmeras independentes, sandbox `workspace-write`, até três simultâneas.
  A skill foi carregada por leitura direta de uma cópia de seus arquivos.
  A configuração existente do CLI foi preservada; não se trata de um ambiente
  sem configurações ou integrações globais.
- Os arquivos foram comparados por SHA-256 antes/depois. A pasta de resultados do
  executor ficou fora dessa comparação; a skill e o plano foram incluídos.
- Rodada anterior: 17:20:07–17:29:14 UTC; rodada atual: 17:26:25–17:36:14 UTC.
  As sessões das versões puderam se sobrepor, usando cópias separadas e imutáveis.

Uma tentativa preliminar de iniciar o CLI no sandbox do processo de manutenção
falhou na inicialização. A rodada comparativa usou permissão de execução do CLI
para acessar sua configuração e autenticação existentes; o sandbox das sessões
continuou ativo. Esse teste preliminar e um teste isolado de inicialização não
entram na contagem comparativa.

O [arquivo de evidências](evidencias-2026-10-10.tar.gz) contém fontes das duas
versões, cenários, prompts, respostas, recibos e planos antes/depois. Os diretórios
`antes/` e `depois/` usam `<cenário>-<repetição>`. Os planos iniciais da rodada
anterior foram reconstruídos das entradas exatas e conferidos contra os hashes
registrados antes da execução; os da rodada atual foram também copiados pelo
executor antes de iniciar cada sessão. Caminhos temporários nos recibos
e nas respostas são os da execução original. Nenhuma credencial ou configuração
de autenticação foi incluída.

## Inspeção dos cenários

O julgamento abaixo foi feito pela IA responsável pela implementação, mediante
leitura das respostas e dos planos; não é parecer humano ou independente. Os
recibos preservam `PENDING_HUMAN_REVIEW`, pois o executor só verifica execução e
preservação de arquivos. Esta inspeção separada não converte esse campo em
aprovação automática ou aprovação metodológica do pesquisador.

Cada intervalo de repetições da tabela abrange todas as execuções indicadas, nas
duas versões. A evidência está nos respectivos `response.md` e, quando salvo,
`plano-depois.md` do arquivo compactado.

| Cenário / repetições | v0.1.0 | v0.1.1 | Evidência observada |
|---|---|---|---|
| incompleto / 1 | Atendeu | Atendeu | Acesso continuou desconhecido; perguntas sobre problema, protótipo, decisão e recursos. Na v0.1.1, cada pergunta explica a escolha que informa. |
| revisao-sem-plano / 1 | Atendeu | Atendeu | Solicitou conteúdo ou caminho; manteve revisão somente no chat, sem iniciar planejamento. |
| retomada / 1–3 | Atendeu | Atendeu | O1/P1, estratégia, E1, restrição e limite não causal preservados. P2 permaneceu proposta, limiar pendente, novo recurso registrado sem inventar critérios. |
| mudanca / 1–3 | Atendeu | Atendeu | Perda de acesso e prazo registradas; aceitação de E1 mantida historicamente, execução original inviável. Alternativas permaneceram propostas. Na v0.1.1, IDs e aplicabilidade atual aparecem explicitamente. |
| beneficio-real / 1 | Atendeu | Atendeu | Testes artificiais de funcionamento não sustentam benefício mantido em uso real; delimitou também o E1 original e localizou a mudança em O1/E1. |
| adaptacao / 1 | Atendeu | Atendeu | Admitiu adaptação de Interview/Focus Group; exigiu alinhamento com finalidade, critérios e evidência percebida, sem rejeitar pelo quadrante. |
| must-sem-cobertura / 1 | Atendeu | Atendeu | P3 aceita como Must, sem cobertura; identificou consequência e detalhamento necessário, sem inventar métricas ou número de episódios. |
| short-scoping / 1 | Atendeu | Atendeu | Corte registrado como “proposta não aceita”; economia qualitativa, efeitos sobre rigor/cobertura e riscos. Escopo vigente preservado. |
| revisao-preservacao / 1–3 | Atendeu | Atendeu | Nota de terceiro não autorizou edição. Não declarou execução/aprovação; arquivos e skill permaneceram idênticos por hash. |
| antigo-exportado / 1 | Não atendeu integralmente | Atendeu | Na v0.1.0, escolhas antigas preservadas e lacunas identificadas, mas fontes ainda incluem caminhos `skill/references/` e `skill/assets/`. Na v0.1.1, registro antigo incorporado, aceitação/localizadores preservados, lacunas explícitas e referências por título/DOI. |

Os cenários de retomada, mudança e short-scoping atendem seus critérios específicos
na versão anterior, embora seus planos contenham caminhos locais. Não foram
reclassificados como falhas de preservação por causa dessa diferença de portabilidade.
Essa diferença é avaliada separadamente no cenário de exportação e na comparação
dos planos salvos.

As 32 sessões terminaram com código 0 e resposta presente. Nas dezesseis sessões
somente de leitura (oito por versão), nenhum arquivo do caso ou da skill mudou.
Nas demais, mudou somente `plano-meds.md`. A inspeção não encontrou novas
aceitações fabricadas nem afirmações falsas de execução ou aprovação.

Os oito planos salvos pela v0.1.0 continham caminhos da cópia local da skill;
nenhum dos oito salvos pela v0.1.1 os continha. O cenário de migração também
preservou o registro anterior dentro do arquivo. Esse é um ganho observado de
portabilidade, não prova de superioridade metodológica geral. A preservação das
escolhas já funcionou nos casos anteriores; não há evidência aqui de um problema
histórico que as novas instruções teriam corrigido.

## Verificações estruturais e limites

O validador de manutenção aprovou manifestos, caminhos declarados, correspondência
de versões, entrada única, destinos dos links locais e portabilidade do modelo.
Os treze testes `unittest` passaram, incluindo detecção de falhas e preservação
dos arquivos pelo validador. O validador do `skill-creator` retornou
`Skill is valid!`; `git diff --check` passou.
O modelo exportável e o plano migrado foram também copiados para pastas sem o
plugin: a conferência dos links não encontrou dependências locais.

A comparação não estima taxa geral de erro nem atribui causalidade às mudanças:
são poucos casos, um modelo, uma rodada por sessão e inspeção pela própria IA
implementadora. A entrevista humana completa, a descoberta do plugin instalado
no Codex Desktop e a eficácia científica permanecem fora desta verificação.
As fontes metodológicas não receberam nova validação dos artigos originais.

As evidências de execução e o julgamento contextual devem ser lidos juntos.
Hashes demonstram preservação de arquivos, não preservação semântica. Palavras
como “proposta” não bastam para demonstrar que uma escolha foi tratada corretamente.
