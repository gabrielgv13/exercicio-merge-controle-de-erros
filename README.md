# Exercício: Resolução de Conflito de Merge

## Objetivo
Resolver um conflito de merge usando o **VS Code Merge Editor**.

## Cenário Preparado

```
main
       ↘ (código base: return preco_base * quantidade)

feature/desconto
       → desconto = 0.10

feature/imposto
       → imposto = 0.15
```

---

## PASSO A PASSO DO ALUNO

### 1. Configuração Inicial (primeira vez)

#### 1.1 Logar no GitHub no VS Code
1. Clique no ícone de usuário no canto inferior esquerdo do VS Code
2. Selecione "Sign in with GitHub"
3. Complete a autenticação no navegador

#### 1.2 Configurar usuário e email no Git
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"
```

### 2. Estar na branch `feature/imposto`

```bash
git checkout feature/imposto
```

### 3. Executar o merge

```bash
git merge feature/desconto
```

**Resultado:**
```
Auto-merging calculadora.py
CONFLICT (content): Merge conflict in calculadora.py
Automatic merge failed; fix conflicts and then commit.
```

### 4. Abrir o VS Code Merge Editor

O VS Code abrirá automaticamente o Merge Editor com os marcadores de conflito.

### 5. Resolver o conflito

No painel **RESULT**, combine o código de ambas as branches:

```python
def calcular_preco_total(preco_base, quantidade):
    desconto = 0.10  # 10% de desconto
    imposto = 0.15    # 15% de imposto
    subtotal = preco_base * quantidade
    return subtotal * (1 - desconto) * (1 + imposto)
```

### 6. Salvar e finalizar

```bash
git add calculadora.py
git commit -m "merge: combina desconto e imposto"
```

---

## Explicação dos Comandos Utilizados

| Comando | Explicação |
|---------|------------|
| `git checkout -b <branch>` | Cria e troca para uma nova branch |
| `git merge <branch>` | Mescla a branch especificada na branch atual |
| `git status` | Mostra o estado atual do repositório |
| `git add <arquivo>` | Marca o arquivo como "staged" para commit |
| `git commit -m "<msg>"` | Registra as alterações no histórico local |
| `git checkout <branch>` | Troca para outra branch existente |

---

## Mini Guia de Comandos Git e GitHub

### Comandos Básicos

```bash
# Inicializar repositório
git init

# Clonar repositório existente
git clone <URL>

# Verificar status
git status

# Ver diferenças
git diff

# Ver histórico de commits
git log --oneline
```

### Branches

```bash
# Listar branches
git branch

# Listar todas as branches (incluindo remotas)
git branch -a

# Criar branch sem trocar
git branch <nome>

# Criar e trocar para branch
git checkout -b <nome>

# Trocar de branch
git checkout <nome>

# Deletar branch
git branch -d <nome>
```

### Commits e Merge

```bash
# Adicionar arquivo ao staging
git add <arquivo>
git add .  # todos os arquivos

# Commitar
git commit -m "mensagem"

# Merge simples
git merge <branch>

# Abortar merge em conflito
git merge --abort
```

### GitHub (Remoto)

```bash
# Adicionar remote
git remote add origin <URL>

# Ver remotes configurados
git remote -v

# Enviar branch para GitHub
git push -u origin <branch>

# Buscar atualizações
git pull

# Buscar sem mesclar
git fetch
```

### GitHub (Criar Repositório)

1. Acesse [github.com/new](https://github.com/new)
2. Preencha o nome do repositório
3. Não inicialize com README (já temos código)
4. Copie a URL do repositório
5. Execute:
   ```bash
   git remote add origin <URL_COPIADA>
   git push -u origin main
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
