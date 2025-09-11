from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (precision_score, recall_score, f1_score,
                             roc_auc_score, classification_report)
from sklearn.model_selection import train_test_split

# Carregar os dados
data = load_breast_cancer()
X = data.data
y = data.target

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criar e treinar o modelo RandomForest
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Realizar previsões
y_pred = model.predict(X_test)
# A previsão de probabilidade ainda é necessária para o cálculo do AUC
y_pred_proba = model.predict_proba(X_test)[:, 1]

# --- Exibição Completa dos Resultados ---

print("--- Métricas de Avaliação (Random Forest) ---")

# 1. Relatório de Classificação Detalhado
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred, target_names=data.target_names))

# 2. Métricas Individuais (arredondadas)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1score = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)

print("\nMétricas Individuais:")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1score:.4f}")
print(f"ROC AUC: {roc_auc:.4f}")