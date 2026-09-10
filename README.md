# Exercício: Resolução de Conflito de Merge

## Objetivo
Resolver um conflito de merge usando o **VS Code Merge Editor**.

## Cenário Preparado

```
main ──────────────────────────────────────────
       ↘ (código base: return preco_base * quantidade)

feature/desconto ──────────────────────────
       → desconto = 0.10

feature/imposto ───────────────────────────
       → imposto = 0.15
```

---

## PASSO A PASSO DO ALUNO

### 1. Estar na branch `feature/imposto`

```bash
git checkout feature/imposto
```

### 2. Executar o merge

```bash
git merge feature/desconto
```

**Resultado:**
```
CONFLICT (content): Merge conflict in calculadora.py
```

### 3. Abrir o VS Code Merge Editor

O VS Code abrirá automaticamente o Merge Editor com os marcadores de conflito.

### 4. Resolver o conflito

No painel **RESULT**, combine o código de ambas as branches:

```python
def calcular_preco_total(preco_base, quantidade):
    desconto = 0.10  # 10% de desconto
    imposto = 0.15    # 15% de imposto
    subtotal = preco_base * quantidade
    return subtotal * (1 - desconto) * (1 + imposto)
```

### 5. Salvar e finalizar

```bash
git add calculadora.py
git commit -m "merge: combina desconto e imposto"
```

---

## Verificação

```python
preco = 100.0
qtd = 2
# 100 * 2 = 200
# 200 * 0.90 = 180 (desconto)
# 180 * 1.15 = 207 (imposto)
print(calcular_preco_total(preco, qtd))  # 207.0
```
