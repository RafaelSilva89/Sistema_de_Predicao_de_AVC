# 🧠 Sistema de Predição de AVC (Acidente Vascular Cerebral)

## 📋 Descrição do Projeto

Este projeto implementa um sistema de machine learning para predizer a probabilidade de um paciente desenvolver um Acidente Vascular Cerebral (AVC) com base em características clínicas e demográficas. O sistema foi desenvolvido como parte do Tech Challenge 6IADT da FIAP, utilizando metodologia CRISP-DM e técnicas avançadas de machine learning.

## 🎯 Objetivo

Desenvolver um modelo preditivo que estime a probabilidade de um paciente sofrer um AVC, auxiliando profissionais da saúde na identificação de grupos de risco para prevenção e priorização de atendimentos.

## 🏗️ Arquitetura do Sistema

O projeto está estruturado em três componentes principais:

### 1. **Modelo de Machine Learning** (`modelo.py`)
- Carrega o modelo XGBoost treinado e otimizado
- Processa dados de entrada e retorna probabilidades de AVC
- Utiliza técnicas de pré-processamento para variáveis categóricas

### 2. **Aplicação Web Flask** (`app.py`)
- Interface web para coleta de dados dos pacientes
- Processa formulários e exibe resultados
- Integra com o modelo de predição

### 3. **Interface de Usuário**
- Formulário de coleta de dados (`templates/formulario.html`)
- Página de resultados (`templates/resultado.html`)
- Estilização responsiva (`static/style.css`)

## 📊 Variáveis do Modelo

O sistema utiliza as seguintes variáveis para predição:

| Variável | Tipo | Descrição |
|----------|------|-----------|
| **Gênero** | Categórica | Masculino, Feminino, Outro |
| **Idade** | Numérica | Idade do paciente em anos |
| **Hipertensão** | Binária | Sim/Não |
| **Doença Cardíaca** | Binária | Sim/Não |
| **Estado Civil** | Binária | Casado/Não |
| **Tipo de Trabalho** | Categórica | Criança, Funcionário Público, Nunca Trabalhou, Área Privada, Autônomo |
| **Tipo de Residência** | Categórica | Rural/Urbano |
| **Nível de Glicose** | Numérica | mg/dL |
| **IMC** | Numérica | Índice de Massa Corporal |
| **Status de Fumante** | Categórica | Ex-fumante, Nunca fumou, Fuma |

## 🚀 Como Executar

### Pré-requisitos
```bash
pip install flask numpy pandas scikit-learn xgboost joblib
```

### Execução
```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5000`

## 📈 Performance do Modelo

O modelo XGBoost otimizado apresenta excelente performance:

- **Acurácia**: 98.56%
- **F1-Score**: 99%
- **Precisão**: 97%
- **Recall**: 100%

### Métricas de Validação
```
Classification metrics:
               precision    recall  f1-score   support
           0       1.00      0.97      0.99       973
           1       0.97      1.00      0.99       972
    accuracy                           0.99       1945
```

## 🔬 Metodologia de Desenvolvimento

### 1. **Entendimento do Negócio**
- Análise do contexto médico e impacto do AVC
- Definição de objetivos e stakeholders
- Planejamento baseado na metodologia CRISP-DM

### 2. **Coleta e Análise de Dados**
- Dataset: healthcare-dataset-stroke-data.csv (Kaggle)
- 5.110 registros de pacientes
- Análise exploratória detalhada com visualizações

### 3. **Preparação dos Dados**
- Tratamento de valores nulos (IMC)
- Codificação de variáveis categóricas
- Balanceamento de classes com Resample
- Divisão em conjuntos de treino, validação e teste

### 4. **Modelagem**
- Teste de múltiplos algoritmos:
  - Random Forest
  - XGBoost
  - LightGBM
- Otimização de hiperparâmetros com GridSearchCV
- Seleção do XGBoost como modelo final

### 5. **Avaliação**
- Métricas de classificação abrangentes
- Matriz de confusão
- Validação cruzada
- Teste em dados não vistos

### 6. **Implementação**
- Serialização do modelo com joblib
- Desenvolvimento da aplicação web
- Interface de usuário responsiva

## 📁 Estrutura do Projeto

```
Projeto_final/
├── app.py                          # Aplicação Flask principal
├── modelo.py                       # Módulo de predição
├── Projeto_fase_final.ipynb       # Notebook de desenvolvimento
├── model/
│   └── modelo_xgb_otimizado_avc.pkl  # Modelo treinado
├── templates/
│   ├── formulario.html            # Formulário de entrada
│   └── resultado.html             # Página de resultados
├── static/
│   └── style.css                  # Estilos CSS
├── archive/
│   └── healthcare-dataset-stroke-data.csv  # Dataset original
├── dataset_avc_50_linhas.csv      # Dataset de teste
└── Imagens/                       # Visualizações e gráficos
```

## 🎨 Visualizações Geradas

O projeto inclui análises visuais abrangentes:

- Distribuição de AVC por gênero
- Incidência por faixa etária
- Análise de fatores de risco
- Comparação de modelos
- Importância das variáveis
- Distribuições antes e após balanceamento

## 🔍 Insights Principais

1. **Perfis de Risco Combinados**: Pacientes com múltiplos fatores de risco apresentam incidência muito superior
2. **Intervenções Direcionadas**: Homens fumantes com doenças cardíacas merecem atenção prioritária
3. **Idade como Gatilho**: O aumento da idade eleva o risco em praticamente todos os cenários
4. **Estilo de Vida**: Atividade profissional influencia significativamente o risco de AVC
5. **Uniformidade Geográfica**: Tipo de residência não apresentou relação significativa

## 🚧 Próximos Passos

### Melhorias Técnicas
- Implementar API REST para integração com sistemas hospitalares
- Adicionar autenticação e controle de acesso
- Implementar logging e monitoramento de performance
- Adicionar testes automatizados

### Expansão do Modelo
- Incorporar mais variáveis clínicas (histórico familiar, exames laboratoriais)
- Técnicas de Balanceamento (no conjunto de treino):
    - Oversampling (Superamostragem): Aumenta o número de instâncias da classe minoritária (quem teve AVC).
    - Undersampling (Subamostragem): Reduz o número de instâncias da classe majoritária (quem não teve AVC). Pode ser útil, mas há o risco de descartar informações importantes da classe majoritária.
    - Combinação (SMOTE + Undersampling): Técnicas como SMOTEENN ou SMOTETomek combinam as duas abordagens para otimizar o balanceamento.
    - Importante balancear o dataset por idade para evitar overfitting
    - Considerar transformações logarítmicas ou exponenciais da idade
- Adicionar interpretabilidade com SHAP ou LIME
- Desenvolver versão mobile da aplicação

## 📚 Tecnologias Utilizadas

- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, XGBoost, LightGBM, Radom Forest
- **Processamento de Dados**: Pandas, NumPy
- **Visualização**: Matplotlib, Seaborn, Plotly
- **Balanceamento**: Resample, Imbalanced-learn
- **Serialização**: Joblib

## 👥 Autores

Desenvolvido como parte do Tech Challenge 6IADT da FIAP - Pós-Tech Fase 1 em AI para desenvolvedores.

## 📄 Licença

Este projeto é de uso educacional e de pesquisa. Para uso comercial ou clínico, é necessária validação médica adequada.


---

*Última atualização: Dezembro 2024*
