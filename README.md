# Instalação do Git e Clone do Repositório

## 1. Instalar o Git

1. Acesse: [https://git-scm.com/install/windows](https://git-scm.com/install/windows)
2. Clique em **Standalone Installer**
3. Baixe o instalador: **[Git for Windows/x64 Setup](https://github.com/git-for-windows/git/releases/download/v2.55.0.windows.5/Git-2.55.0.5-64-bit.exe)**
4. Execute o instalador e siga os passos padrão

## 2. Criar Fork no GitHub

1. No VS Code, abra o painel **Source Control** (Ctrl+Shift+G)
2. Clique em **"Publish to GitHub"**
3. Selecione **"Fork Repository"**
4. Escolha sua conta GitHub
5. O fork será criado automaticamente

## 3. Clonar o Repositório

1. Crie uma pasta onde deseja baixar o projeto
2. Clique com o botão direito na pasta
3. Selecione: **Abrir no terminal** (ou "Open in Terminal" ou "Open git bash here") 
4. Execute o comando:
   ```bash
   git clone link-do-seu-fork
   ```
4. Acesse a pasta do projeto com o vscode, abra o terminal e digite os seguintes comandos:
Para pegar as branches do meu repositório (este):
```bash
   git remote add upstream https://github.com/gabrielgv13/exercicio-merge-controle-de-erros
   git fetch upstream
   ```


No campo inferior esquerdo, selecione a branch copiada upstream/feature/desconto.
Para copiar para o seu fork:
```bash
   git push origin feature/desconto
   ```
Faça o mesmo para feature/imposto
Comece a atividade.

---

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

ANTES DE TUDO:
git remote add upstream https://github.com/gabrielgv13/exercicio-merge-controle-de-erros
git fetch upstream
git push origin feature/desconto
git push origin feature/imposto

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

## Terminologia Técnica do Git

### Conceitos Fundamentais

| Termo | Significado |
|-------|-------------|
| **Repository (Repo)** | Repositório - pasta onde o Git guarda todo o histórico de alterações |
| **Commit** | Snapshot/ponto de salvamento do código em um momento específico |
| **Branch** | Ramificação - linha paralela de desenvolvimento |
| **Merge** | Junção de duas branches em uma |
| **Conflict** | Conflito quando o Git não consegue mesclar automaticamente |
| **HEAD** | Ponteiro que indica onde você está no histórico |

### Branch Local vs Remota

| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| **Local** | Branch que existe apenas no seu computador | `main`, `feature/desconto` |
| **Remote** | Branch que existe no servidor GitHub | `origin/main`, `origin/feature/desconto` |

**Estrutura:**
```
Seu Computador (LOCAL)          GitHub (REMOTO)
─────────────────────           ────────────────
main                         ←  origin/main
feature/desconto             ←  origin/feature/desconto
feature/imposto              ←  origin/feature/imposto
```

### Remote (Origin)

| Termo | Significado |
|-------|-------------|
| **origin** | Nome padrão do repositório remoto (pode ser alterado) |
| **remote** | Servidor onde o código fica armazenado |
| **fetch** | Baixar dados do remote sem mesclar |
| **pull** | Baixar e mesclar dados do remote |
| **push** | Enviar commits para o remote |

### Workflow Git Typical

```
1. git clone <URL>        → Copia repo do GitHub para PC
2. git checkout -b xxx   → Cria branch local
3. git add + commit       → Salva alterações localmente
4. git push -u origin xxx → Envia branch para GitHub
5. Pull Request           → Solicita mesclar no GitHub
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
# Listar branches locais
git branch

# Listar TODAS as branches (locais + remotas)
git branch -a

# Criar branch sem trocar
git branch <nome>

# Criar e trocar para branch
git checkout -b <nome>

# Trocar de branch
git checkout <nome>

# Deletar branch local
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

# Renomear remote (opcional)
git remote rename origin upstream

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
