# Início

## Perguntas de partida e hipóteses

### 1. Existem dados faltantes, se sim quantos e em quais variáveis?
Não há dados faltantes/nan no conjunto de dados

### 2. Qual a distribuição dos dados (variável por variável)?
 1. **Count:** Há um total de 10.000 observações em cada variável.
  2. **Unique:** A coluna "Surname" tem 2.932 valores únicos. "Geography" tem 3 valores únicos, enquanto "Gender" tem 2.
  3. **Top:** O sobrenome mais comum é "Smith". O país mais comum é a França e o gênero mais comum é masculino.
  4. **Freq:** "Smith" é o sobrenome mais frequente, aparecendo 32 vezes.
  5. **Mean (Média):** A pontuação de crédito média é de aproximadamente 650,53. A idade média é de aproximadamente 38,92 anos. O saldo médio é de cerca de 76.485,89. A média de produtos adquiridos é de aproximadamente 1,53. A média de clientes com cartão de crédito é de cerca de 0,71. A média de membros ativos é de aproximadamente 0,52. O salário estimado médio é de cerca de 100.090,24.
  6. **Std (Desvio Padrão):** O desvio padrão da pontuação de crédito é de aproximadamente 96,65. A idade tem um desvio padrão de cerca de 10,49 anos. O saldo tem um desvio padrão de cerca de 62.397,41.
  7. **Min (Mínimo):** A menor pontuação de crédito é 350. A idade mínima é 18 anos. O menor saldo é 0.
  8. **25% (Percentil 25):** 25% das pontuações de crédito são iguais ou inferiores a 584. 25% das idades são iguais ou inferiores a 32 anos.
  9. **50% (Percentil 50 ou Mediana):** Metade das pontuações de crédito são iguais ou inferiores a 652. Metade das idades são iguais ou inferiores a 37 anos.
  10. **75% (Percentil 75):** 75% das pontuações de crédito são iguais ou inferiores a 718. 75% das idades são iguais ou inferiores a 44 anos.
  11. **Max (Máximo):** A pontuação de crédito máxima é 850. A idade máxima é 92 anos. O saldo máximo é 250.898,09.

#### 2.1. Como estão distribuídas as variáveis presentes no dataset?
Analisando os histogramas, alguns insights podem ser considerados:

- **Saldo da Conta (Balance)**
    - Há uma grande quantidade de clientes com saldo zero, o que pode indicar contas inativas ou recém-abertas. **Isso pode ser um ponto de interesse, especialmente se uma proporção significativa dessas contas com saldo zero está dando churn**. <br/><br/>

- **Número de Produtos (NumOfProducts)**
    - A maioria dos clientes possui 1 ou 2 produtos bancários. Poucos clientes têm 3 ou 4 produtos, e esses podem ter uma tendência maior de churn.

> Uma hipótese pode ser que clientes com muitos produtos possam se sentir sobrecarregados ou insatisfeitos com a complexidade do gerenciamento de múltiplos serviços. <br/>

- **Possui Cartão de Crédito (HasCrCard)**
    - A maioria dos clientes possui um cartão de crédito. A presença de um cartão de crédito por si só pode não ser um fator significativo de churn, mas combinado com outras variáveis (como saldo ou número de produtos), pode haver insights mais profundos a explorar. <br/><br/>

- **Membro Ativo (IsActiveMember)**
   - A distribuição de membros ativos e não ativos é relativamente equilibrada. Pode ser útil investigar como a atividade do membro interage com outras variáveis, como saldo e número de produtos, para influenciar o churn. <br/><br/>

- **Salário Estimado (EstimatedSalary)**
    - O salário estimado parece estar uniformemente distribuído, o que sugere que não está diretamente relacionado ao churn. Isso sugere que o salário por si só pode não ser um fator determinante para o churn. <br/><br/>

- **Score de Crédito (CreditScore)**
    - O score de crédito segue uma distribuição aproximadamente normal, sem grandes distorções que sugerem uma relação direta com o churn. No entanto, é importante avaliar se há interações com outras variáveis que possam impactar o churn. <br/><br/>

- **Idade (Age)**
    - A distribuição de idade mostra que a base de clientes é mais jovem, com uma queda significativa após os 40 anos. <br/><br/>

- **Permanência (Tenure)**
    - A permanência dos clientes no banco é uniformemente distribuída, o que indica que não há uma concentração significativa de churn em nenhuma faixa específica de permanência.

#### 2.3. Como é a correlação entre as variáveis?
Este gráfico destaca as correlações entre todas as variáveis. Uma observação importante é a **correlação negativa fraca (-0.304) entre NumberOfProducts e Balance**, que pode indicar que **clientes com mais produtos tendem a ter saldos mais baixos**.

### 3. Qual a relação entre o cliente ser um membro ativo e a saída dos clientes do banco? 
Como é possível ver no gráfico, clientes não ativos tendem a ter maior taxa de saída do banco.

### 4. Como a idade (Age) dos clientes se relaciona com a propensão de saída do banco? 
De acordo com o gráfico, pessoas de meia-idade (30-60 anos) correspondem a maior parte dos churns

### 5. Os clientes com salários mais altos tendem a ficar mais tempo no banco?
De acordo com o gráfico, é possível afirmar que não há relação entre o salário estimado e o tempo de permanência no banco.

### 6. A localização geográfica pode influenciar a probabilidade de um cliente sair do banco, com diferenças significativas entre regiões?
De acordo com o mapa, França e Alemanha têm uma saída de clientes maior que Espanha.

### 7. A Média de saldo das pessoas que decidiram sair do banco e as que decidiram ficar, tem uma diferença significativa?
O Teste T-Student mostra se existe uma diferença significativa entre as médias de quem saiu e quem não saiu. Como o resultado deu acima do numero 5 no 'p-value', podemos dizer que não existe diferença significativa

### 8. Mas será que a dispersão entre os saldos desses grupos é alto?
A dispersão de saldo no grupo Não Churn e Churn são altos

## Outras conclusões relacionadas aos gráficos
Analisando os gráficos acima, aqui estão alguns insights potenciais que podemos extrair:

- **Distribuição de Idade e Saldo (Balance) por Status de Churn (Exited)**
    - Os gráficos scatterplot e regplot indicam que há uma tendência de clientes mais velhos com maiores saldos a deixar o banco (churn), sugerida pela dispersão dos pontos e pelas linhas de regressão. Esse padrão pode indicar que um segmento mais maduro não está satisfeito ou está encontrando melhores ofertas em outros lugares. <br/><br/>
    
- **Distribuição de Número de Produtos e Salário Estimado por Geografia**
    - A distribuição do número de produtos utilizados pelos clientes parece ser bastante semelhante entre os diferentes países, sem diferenças significativas que indiquem um impacto no churn.
    - A distribuição do salário estimado também não mostra diferenças substanciais entre clientes que deram churn e os que não deram, indicando que o salário por si só pode não ser um fator determinante para o churn. <br/><br/>

- **Distribuição de Tenure e Saldo por Geografia**
    - Os clientes na Alemanha parecem ter saldos maiores em média, o que poderia estar correlacionado com uma maior taxa de churn observada nesse país.
    - A distribuição do tempo de permanência (tenure) não parece variar significativamente entre as geografias ou entre os grupos de churn. <br/><br/>

- **Distribuição de Idade e CreditScore por Geografia**
   - Existe uma variação notável na idade entre os grupos de churn, especialmente na Alemanha (que possui mais outliers que saíram do banco `Exited`), sugerindo que a idade pode ser um fator mais significativo nesse mercado.
   - O CreditScore, por outro lado, não parece mostrar diferenças marcantes que possam estar relacionadas ao churn. <br/><br/>

- **Correlação com Exited**
    - A idade é a variável com a correlação mais forte com o churn, indicando que a probabilidade de churn aumenta com a idade do cliente.
    - As outras variáveis, como Balance, EstimatedSalary, Tenure, CreditScore e NumberOfProducts, têm correlações mais baixas com o churn, sugerindo que elas podem ter menos influência sobre a decisão do cliente de deixar o banco. <br/><br/>

- **Distribuições KDE**
    - A análise das distribuições KDE (Kernel Density Estimate) para variáveis-chave como Tenure, NumberOfProducts, Balance, EstimatedSalary, CreditScore e Age oferece uma visão detalhada das diferenças nas distribuições entre os clientes que deram churn e os que não deram. Por exemplo, **a distribuição de Tenure mostra que não há uma diferença significativa na densidade entre os grupos, enquanto a distribuição de Age mostra uma distinção mais clara entre os grupos de churn**. <br/><br/>


- **Boxplots de Variáveis-Chave por Exited**
    - Os boxplots revelam que há uma diferença perceptível nas distribuições de Balance e Age quando comparamos os clientes que deram churn e os que não deram. Por exemplo, clientes que deram churn tendem a ter um saldo mais alto e a serem mais velhos, o que pode sugerir que **estratégias de retenção devem ser focadas nesse grupo específico**. <br/><br/>

> A combinação dessas observações pode oferecer pistas importantes para a criação de estratégias de retenção de clientes, como **ofertas personalizadas para clientes mais velhos com saldos mais altos** ou **ajustes nos serviços oferecidos em mercados específicos como a Alemanha**. Além disso, o conhecimento de que muitos clientes têm saldo zero ou um único produto pode ser usado para **desenvolver serviços ou ofertas que incentivem a ativação e o engajamento desses clientes**.

<br/>
Seria importante também considerar análises mais profundas e modelos preditivos para entender melhor as causas do churn e identificar quais fatores são os mais preditivos.