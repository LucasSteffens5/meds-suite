# Verificação comportamental da MEDS

Os [cenários](cenarios.json) e os planos [base](caso-base.md) e
[antigo](caso-antigo.md) são fictícios. Seus registros de aceitação pertencem ao
exercício; não representam decisões, participantes ou execução de uma pesquisa real.

## Procedimento

1. Preserve uma cópia da versão anterior antes de alterar suas instruções.
2. Execute os mesmos cenários contra a cópia anterior e a versão atual, em novas
   pastas externas ao checkout, usando o mesmo ambiente e modelo configurado.
3. Cada execução abre uma sessão efêmera com uma cópia da skill e o plano necessário.
   Somente a solicitação e os materiais do caso entram no contexto; os campos
   `expected` e `human_reply` não são fornecidos ao modelo. Este protocolo verifica
   uma rodada de cada situação, não uma entrevista humana completa.
4. Inspecione respostas e arquivos. Compare com os critérios de cada cenário e
   registre evidência, problemas e limites. Verifique que toda resposta termina
   com a legenda da skill e que cada plano criado ou atualizado termina com uma
   única cópia; em revisão somente no chat, confirme que o arquivo permaneceu
   inalterado. Os recibos não produzem automaticamente um julgamento metodológico.
5. Corrija problemas observados e repita os cenários afetados. Não apresente resultados
   anteriores como novas execuções nem resultados dos casos como validade científica.

```sh
python3 scripts/run_behavior_checks.py --suite /tmp/copia-meds-anterior --output /tmp/meds-antes-novo
python3 scripts/run_behavior_checks.py --output /tmp/meds-depois-novo
```

Execute os comandos a partir da raiz do checkout de manutenção. O executor usa até
três sessões independentes simultâneas, sem alterar o modelo ou configurar agentes
na suíte. Por padrão, copia os arquivos da skill para cada sessão. A opção
`--installed-plugin` verifica a versão já instalada, chama `$meds-suite` em sessões
novas e não instala nem altera a configuração do Codex. Ela requer que a versão
instalada corresponda ao manifesto do checkout. Requer acesso ao serviço do Codex e
permissão para iniciar o CLI; se uma sessão não iniciar, registre falha de execução,
não aprovação do cenário.

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
