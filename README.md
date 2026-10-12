# MEDS Suite para Codex

Plugin `meds-suite` v0.1.2 com uma skill coordenadora para planejar, retomar e revisar
programas de avaliação de artefatos em Design Science Research (DSR).
O planejamento fica em um arquivo Markdown por caso.

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

A skill carrega o fluxo solicitado e suas referências conforme a etapa. O plano
do pesquisador é salvo no projeto da pesquisa, fora do pacote instalado. Os recursos
mantêm uma única cópia no plugin; os metadados em `agents/` não criam subagentes.

O fluxo de planejamento organiza objetivos, estratégia FEDS, propriedades
priorizadas por MuSCoW e episódios com métodos candidatos DSREMSF. As escolhas podem
ser revisitadas. A revisão relaciona observações a seções e episódios concretos.

Na v0.1.1, a entrevista aprofunda a etapa atual, explica por que uma informação é
necessária e mantém escolhas sem fundamento suficiente como pendências. O plano
preserva restrições, a origem da aceitação e a aplicabilidade das decisões após
mudanças de contexto. Planos antigos continuam utilizáveis. O modelo exportável
identifica as fontes por título e DOI, sem caminhos da instalação.

Na v0.1.2, respostas dirigidas ao pesquisador e planos MEDS terminam com uma
legenda curta de identificadores e conceitos. Ao atualizar um plano, a suíte
mantém uma única legenda no fim; uma revisão somente no chat preserva o arquivo.

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

A presença dos arquivos, sozinha, não comprova que o plugin foi instalado ou
carregado em uma conversa. Registre a observação ao fazer essa verificação.

## Uso

### Planejar

```text
Use $meds-suite para planejar a avaliação do caso organizador-documentos.
Meu artefato é um organizador de documentos para estudantes. Tenho um protótipo,
duas semanas e ainda não confirmei acesso a usuários. Quero avaliar sua utilidade.
Pergunte o que faltar e salve o plano parcial.
```

O caminho padrão será `casos/organizador-documentos/plano-meds.md` no projeto da
pesquisa. O plano reúne contexto, quatro etapas MEDS, decisões, pendências e próximo
passo. Propostas da IA não são registradas como aceitas sem confirmação disponível.

### Retomar

```text
Use $meds-suite para retomar casos/organizador-documentos/plano-meds.md.
Leia o plano antes de perguntar e continue a partir das pendências registradas.
```

### Revisar

```text
Use $meds-suite para revisar casos/organizador-documentos/plano-meds.md.
Verifique a coerência entre objetivos, estratégia, propriedades e episódios.
Apresente a revisão na conversa, sem editar o plano.
```

Para alterar o plano após a revisão, solicite os ajustes desejados. Também é
possível informar outro caminho de saída ou pedir planejamento somente no chat.

## Verificações de manutenção

Os scripts abaixo usam Python 3.9 ou superior e somente a biblioteca padrão.
São ferramentas de desenvolvimento fora do plugin; usar MEDS não depende deles.

```sh
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -v
```

O validador lê manifestos, caminhos, versões, entrada única e links locais dos
recursos e do README. Confere a legenda no modelo e nos materiais de primeiro
contato; rejeita links locais e caminhos da instalação no modelo exportável. Retorna
código 0 para estrutura aprovada e 1 para falhas localizadas, sem editar arquivos.
Seu leitor de links cobre a sintaxe simples usada no pacote; não verifica âncoras,
disponibilidade de URLs externas nem conteúdo metodológico.

### Comportamento em sessões novas

O [protocolo dos cenários](tests/behavior/README.md) usa casos de teste e registra
entradas, respostas humanas previstas e critérios de avaliação. Inclui onze cenários
e três repetições para retomada, mudança de contexto e revisão sem edição: dezessete
sessões por versão. Não envie os critérios esperados ao modelo avaliado.

O executor requer Codex CLI autenticado. Usa o modelo configurado no ambiente,
registra o modelo anunciado pelo CLI e cria sessões efêmeras em pastas separadas.
Ele não instala o plugin nem muda a configuração do Codex.

```sh
python3 scripts/run_behavior_checks.py --output /tmp/meds-v012-nova-execucao
```

A pasta de saída deve ser nova e ficar fora do checkout. O executor grava prompts,
respostas, transcrições, hashes dos arquivos antes/depois e recibos. Seus códigos
de saída verificam execução e preservação em revisão; o julgamento metodológico
permanece pendente de inspeção humana. Ele não atribui notas nem certifica planos.

Separar três tipos de evidência: **estrutura do pacote**, **comportamento observado
nos cenários** e **avaliação científica da eficácia**. As duas primeiras não
substituem a terceira. A descoberta automática no seletor de uma nova conversa
continua sendo uma verificação específica da instalação.

### Execução comparativa em 2026-10-10 (v0.1.0 → v0.1.1)

O [relatório com evidências](tests/behavior/resultados-2026-10-10.md) registra
32 sessões novas do Codex CLI `0.160.0`, com `gpt-6.1-sol`: dezesseis por versão,
incluindo as repetições previstas. As dezesseis sessões somente de leitura
preservaram os arquivos por SHA-256. Nos oito planos salvos por cada versão,
caminhos locais da skill apareceram em oito na v0.1.0 e em nenhum na v0.1.1.
As decisões aceitas e os limites da evidência foram preservados nos casos inspecionados.

Estrutura aprovada pelo validador, treze testes `unittest` aprovados e verificação
da skill aprovada. O relatório identifica a inspeção feita pela IA implementadora;
não apresenta parecer humano ou independente. Os recibos não atribuem aprovação
metodológica. Descoberta do plugin instalado e eficácia científica não foram testadas.

## Histórico: verificações realizadas em 2026-10-03 (v0.1.0)

A validação estrutural confirmou catálogo e manifesto JSON, versões consistentes,
uma única skill, metadados de interface e 17 links locais resolvidos. O validador
de `skill-creator` retornou `Skill is valid!`. A matriz DSREMSF foi conferida com
Baskerville, Pries-Heje e Venable (2026): cinco posições por quadrante, vinte no
total, com Lab Experiment em dois quadrantes. Os métodos e suas condições de
escolha constam da [referência MEDS](plugins/meds-suite/skills/meds-suite/references/meds.md#dsremsf-métodos-candidatos-por-quadrante).
`git diff --check` não apontou problemas de whitespace.

Uma nova execução efêmera do Codex CLI v0.160.0, com o modelo configurado no CLI
(`gpt-6-luna`), exercitou os quatro pedidos sequencialmente. A skill foi carregada
por leitura direta de seu arquivo; os casos fictícios ficaram em pasta temporária.

| Cenário | Observação |
|---|---|
| Informações incompletas | Formulou perguntas sem escolher estratégia ou método; manteve a saída somente no chat conforme pedido |
| Plano parcial | Criou o plano Markdown, distinguindo informações fornecidas, propostas e pendências; não presumiu acesso a usuários |
| Retomada | Atualizou o plano, preservando as escolhas aceitas no caso fictício e mantendo critérios desconhecidos como pendências |
| Revisão | Apontou a incompatibilidade entre testes artificiais e a conclusão de benefício em uso real; manteve o plano intacto |

A igualdade do arquivo revisado antes/depois foi verificada por SHA-256:
`b21bab1401fb672654993fbc88ea7fef9707e8c5ee8f988549ca3c19c4647dd9`.
Os planos produzidos e a resposta foram inspecionados após a execução.

O teste verificou os fluxos pelo arquivo da skill, não sua descoberta automática
como plugin instalado. A instalação e a presença no seletor de uma nova conversa
continuam como verificações do procedimento acima. Os resultados são observações
desses casos fictícios, não garantia de comportamento em toda pesquisa.

## Fontes e limites

- [MEDS](plugins/meds-suite/skills/meds-suite/references/meds.md): Baskerville,
  Pries-Heje e Venable (2026), DOI 10.1080/0960085X.2026.2627280.
- [FEDS](plugins/meds-suite/skills/meds-suite/references/feds.md): Venable,
  Pries-Heje e Baskerville (2016), DOI 10.1057/ejis.2014.36.
- [DSRM](plugins/meds-suite/skills/meds-suite/references/dsrm.md): Peffers et al.
  (2007), DOI 10.2753/MIS0742-1222240302.

As referências contêm sínteses originais do conhecimento necessário ao planejamento
e à revisão, com atribuição bibliográfica e DOI. As explicações, matrizes e condições
de escolha estão em Markdown e não exigem consulta aos PDFs. Os artigos não são
redistribuídos no repositório nem no pacote. Não há caminhos pessoais fixos nos recursos do plugin.

A [ARS-Codex](https://github.com/Imbad0202/academic-research-skills-codex) inspirou
a organização em entrada única, fluxos e carregamento progressivo. O conteúdo,
as instruções e os modelos desta suíte foram escritos para MEDS.

Esta versão apoia planejamento e revisão. Execução dos métodos exige protocolos
e literatura próprios. Não requer API, servidor MCP, hooks, biblioteca Python,
estado JSON ou um modelo específico. A IA preserva a separação entre planejamento,
execução e evidência; a aprovação metodológica pertence ao pesquisador.

Formato e instalação: [documentação oficial de plugins](https://developers.openai.com/plugins/build/plugins).
Código e instruções do projeto: licença Apache-2.0, conforme [LICENSE](LICENSE).
