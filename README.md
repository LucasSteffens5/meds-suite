# MEDS Suite para Codex

Plugin `meds-suite` v0.1.0 com uma skill coordenadora para planejar, retomar e revisar
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

## Verificação de uso em uma nova conversa

Após instalar, conferir os seguintes cenários em um projeto de teste separado:

| Cenário | Comportamento esperado |
|---|---|
| Informações incompletas | Perguntar pelo essencial, sem inventar contexto, acesso ou resultados |
| Plano parcial | Salvar o que já é conhecido e manter propostas e pendências identificadas |
| Retomada | Ler o plano, preservar decisões aceitas e continuar do ponto registrado |
| Episódio incompatível | Apontar o problema e a seção correspondente, sem alterar o arquivo em revisão |

Para o último cenário, use um plano que proponha provar benefício em uso real
apenas por testes artificiais de funcionamento. A revisão deve reconhecer a lacuna
entre a evidência prevista e a conclusão pretendida, sem exigir um método único.

Registre versão do plugin, ambiente, entrada utilizada, arquivo antes/depois e
comportamento observado. Esses exercícios verificam uso e coerência do fluxo;
não constituem avaliação científica da eficácia da suíte.

## Verificações realizadas em 2026-10-03

A validação estrutural confirmou catálogo e manifesto JSON, versões consistentes,
uma única skill, metadados de interface e 17 links locais resolvidos. O validador
de `skill-creator` retornou `Skill is valid!`. A matriz DSREMSF foi conferida contra
a Figura 2 do PDF MEDS consultado, incluindo as vinte posições e a repetição de
Lab Experiment. `git diff --check` não apontou problemas de whitespace.

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

As referências são sínteses originais com seções e páginas dos PDFs consultados.
Os artigos originais prevalecem na interpretação da metodologia e não são
redistribuídos no pacote. Não há caminhos pessoais fixos nos recursos do plugin.

A [ARS-Codex](https://github.com/Imbad0202/academic-research-skills-codex) inspirou
a organização em entrada única, fluxos e carregamento progressivo. O conteúdo,
as instruções e os modelos desta suíte foram escritos para MEDS.

Esta versão apoia planejamento e revisão. Execução dos métodos exige protocolos
e literatura próprios. Não requer API, servidor MCP, hooks, biblioteca Python,
estado JSON ou um modelo específico. A IA preserva a separação entre planejamento,
execução e evidência; a aprovação metodológica pertence ao pesquisador.

Formato e instalação: [documentação oficial de plugins](https://developers.openai.com/plugins/build/plugins).
Código e instruções do projeto: licença Apache-2.0, conforme [LICENSE](LICENSE).
