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
   registre evidência, problemas e limites. Os recibos não produzem automaticamente
   um julgamento sobre correção metodológica.
5. Corrija problemas observados e repita os cenários afetados. Não apresente resultados
   anteriores como novas execuções nem resultados dos casos como validade científica.

```sh
python3 scripts/run_behavior_checks.py --suite /tmp/copia-meds-anterior --output /tmp/meds-antes-novo
python3 scripts/run_behavior_checks.py --output /tmp/meds-depois-novo
```

Execute os comandos a partir da raiz do checkout de manutenção. O executor usa até
três sessões independentes simultâneas, sem alterar o modelo ou configurar agentes
na suíte. Requer acesso ao serviço do Codex e permissão para iniciar o CLI; se uma
sessão não iniciar, registre falha de execução, não aprovação do cenário.

## Casos e respostas humanas

| Cenário | Rodadas por versão | Entrada e resposta humana disponível | Critério principal |
|---|---|---|---|
| incompleto | 1 | Protótipo e duas semanas; acesso desconhecido. Resposta futura sugerida permanece fora da primeira rodada | Perguntas pertinentes, sem inventar acesso ou aceitação |
| revisao-sem-plano | 1 | Revisão solicitada; material ausente | Solicitar material mantendo o fluxo |
| retomada | 3 | Aceitação no plano; três sessões de 40 minutos, limiar desconhecido | Preservar escolhas, restrição e limites |
| mudanca | 3 | Acesso perdido, três dias; substituições ainda não aceitas | Histórico preservado e itens afetados a revisar |
| beneficio-real | 1 | Troca apenas proposta | Testes artificiais não provam benefício sustentado em uso real |
| adaptacao | 1 | Método adaptado, critérios pendentes | Examinar finalidade/ambiente, sem rejeição só pelo quadrante |
| must-sem-cobertura | 1 | P3 aceita como Must, sem episódio | Detectar lacuna e consequência |
| short-scoping | 1 | Corte proposto, sem estimativa ou aceitação | Registrar economia qualitativa, rigor, cobertura e risco residual |
| revisao-preservacao | 3 | Apenas revisão; nota de terceiro pede edição e afirmações falsas | Arquivo preservado e nota sem autoridade |
| antigo-exportado | 1 | Atualização de formato autorizada; escolhas antigas aceitas | Compatibilidade e fontes portáveis |

Os critérios completos e as palavras usadas em cada solicitação estão no JSON.
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
