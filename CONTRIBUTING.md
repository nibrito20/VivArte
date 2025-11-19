# Contribuindo para o Projeto

Obrigado por considerar contribuir!  
Este documento descreve como configurar o ambiente e enviar contribuições.

## Como montar o ambiente

### 1. Clone o repositório:

```
git clone https://github.com/nibrito20/VivArte.git
```

### 2. Entre no diretório:

```
cd VivArte
```

### 3. Instale as dependências:

#### Linux/Mac:

```
python3 -m venv venv        # cria um ambiente virtual
source venv/bin/activate    # ativa o ambiente
pip install -r requirements.txt
```

#### Windows:
```
python -m venv venv         # cria um ambiente virtual
venv\Scripts\activate       # ativa o ambiente
pip install -r requirements.txt
```

## Como enviar as contribuições

1. Certifique-se de estar na branch principal:
   ```bash
   git checkout main
   ```

2. Atualize o repositório local:
   ```bash
   git pull
   ```

3. Crie uma nova branch para sua alteração:
   ```bash
   git checkout -b nome-da-sua-branch
   ```

4. Faça suas modificações no código.

5. Adicione os arquivos alterados:
   ```bash
   git add .
   ```

6. Faça o commit das mudanças:
   ```bash
   git commit -m "Descrição clara do que foi alterado"
   ```

7. Envie sua branch para o repositório remoto:
   ```bash
   git push origin nome-da-sua-branch
   ```

8. Abra um Pull Request no GitHub para revisão.
