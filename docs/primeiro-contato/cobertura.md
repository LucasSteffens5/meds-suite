# Cobertura das capacidades da versão local 0.1.1

Este mapa cobre o uso da suíte, não todos os métodos possíveis ou tipos de pesquisa.
Os exercícios não exigem passar por todos os quadrantes de FEDS.

| Capacidade | Onde experimentar | O que conferir |
|---|---|---|
| Contexto, artefato, recursos, riscos e restrições | [Aula 1](aulas/01-planejar.md), passos 1–2 | Informações fornecidas separadas de lacunas |
| Explicação gradual de conceitos; posição no projeto DSRM | [Ficha](materiais/ficha-caso.md) e aula 1 | Avaliação não confundida com demonstração ou projeto inteiro |
| Objetivos distintos da finalidade da solução | Aula 1, passo 2 | Evidência e destinatários definidos |
| Estratégia e trajetória FEDS | Aula 1, passo 3 | Justificativa contextual, acesso desconhecido explícito |
| Finalidade, ambiente e momento distintos | Aula 1, passos 3–4 | Classificação pela evidência e condições reais |
| Propriedades, MuSCoW e observabilidade | Aula 1, passo 4 | Must/Should/Could/Would; critérios desconhecidos pendentes |
| Métodos candidatos DSREMSF e alternativas justificadas | Aula 1, passo 4; [exemplo](referencias/plano-aula-01.md) | Escolha não tratada como protocolo completo |
| Relação O/P/E, evidência, responsáveis e próxima decisão | Aula 1, passos 4–5 | IDs estáveis e detalhe proporcional ao estágio |
| Salvar plano parcial e distinguir proposta/aceitação | Aula 1, passo 5 | Aceitação disponível registrada; sem decisões inventadas |
| Retomada com preservação de escolhas | [Aula 2](aulas/02-retomar.md), passo 1 | Ler antes de perguntar; reutilizar aceitação aplicável |
| Mudança de contexto e aplicabilidade histórica | Aula 2, passo 2 | Histórico e IDs afetados preservados |
| Short-scoping, rigor, economia e riscos residuais | Aula 2, passos 3–4 | Corte proposto antes de aceito; conclusões delimitadas |
| Revisão localizada sem edição | [Aula 3](aulas/03-revisar.md), passos 1–3 | Observações fundamentadas; SHA-256 igual |
| Correções autorizadas e conferência contextual | Aula 3, passos 4–5 | Somente ajustes escolhidos; sentido e restrições preservados |
| Planejamento apenas no chat | [Opcional A](opcionais.md#a-planejar-somente-no-chat) | Nenhum arquivo criado |
| Caminho personalizado e fontes portáveis | [Opcional B](opcionais.md#b-caminho-personalizado-e-portabilidade) | Plano compreensível fora da instalação |
| Compatibilidade com plano antigo | [Opcional C](opcionais.md#c-retomar-um-formato-antigo) | Lacunas explícitas, sem inventar aceitação |
| Estratégias por componente ou combinação | [Opcional D](opcionais.md#d-estratégias-por-componente) | Riscos e condições distintos fundamentam propostas |
| Adaptação de método e condições parcialmente reais | [Opcional E](opcionais.md#e-adaptar-um-método) | Examinar o desenho, não apenas a posição na matriz |
| Sinergias e usos complementares da evidência | [Opcional F](opcionais.md#f-reunir-propriedades-com-sinergia) e planos de referência | Redução de trabalho não confunde finalidades |
| Limites: planejado ≠ executado; coerência ≠ eficácia | Todas as aulas | Sem resultados, aprovações ou benefícios inventados |

## Consulta à implementação

A conferência editorial usa a [entrada da skill](../../plugins/meds-suite/skills/meds-suite/SKILL.md),
o [fluxo Planejar](../../plugins/meds-suite/skills/meds-suite/workflows/planejar/WORKFLOW.md),
o [fluxo Revisar](../../plugins/meds-suite/skills/meds-suite/workflows/revisar/WORKFLOW.md)
e o [modelo de plano](../../plugins/meds-suite/skills/meds-suite/assets/plano-meds.md).
São links de consulta deste material no checkout; planos exportáveis identificam
as fontes metodológicas por título e DOI, sem caminhos de instalação.

[Voltar ao início](README.md).

## Conferência editorial — 10/10/2026

Os 16 arquivos foram conferidos contra a entrada, os fluxos e o modelo locais
0.1.1. A checagem verificou 38 links locais e suas âncoras, tabelas, cinco passos
por aula e extensão de 478, 435 e 405 palavras. Os exemplos corrigidos preservam
restrições, prioridades legítimas e histórico do corte. O validador do pacote
retornou estrutura OK.

Os 23 arquivos preexistentes acompanhados no início foram preservados por SHA-256.
`git check-ignore` confirmou os 16 materiais e três caminhos representativos de
saída sob a regra existente `/docs/`.

Esta é uma conferência editorial e estrutural. Não foram executadas novas sessões
da suíte com os prompts desta trilha nem testes com leitores. Os hashes solicitados
na aula 3 devem ser calculados na prática; não há valores de execução fabricados.
