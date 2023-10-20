## Calcula Salarios prestação de serviço baseado em horas
Utilizar um script de cálculo de salário por horas não é apenas uma economia de minutos, é uma economia de energia e foco.   

Liberte-se da complexidade, elimine o estresse de cálculos manuais e concentre-se no que realmente importa: seu trabalho e seu sucesso.   

Simplifique sua vida e impulsione sua produtividade com um simples atalho para o sucesso!


## Configurações Atuais
- Valor: R$ 100,00 hora
- Dias: 20 ao 19 no mês

### Requisitos
- Python 3
- Virtualenv
- Pandas
- Linux (Opcional para utilizar script)

### Configuração Inicial
```
python3 -m venv env
source env/bin/activate
pip3 install pandas
```

### Modo de uso
São possivel utilizar de duas formas

#### 1. Acesso direto
```sh
./Workspace/horas-uteis/hora-uteis.sh
```

#### 2. Configurar ao ambiente
Adicione a linha abaixo no `.bashrc` ou `.zshrc`:
```sh
alias pagode=$HOME/Workspace/horas-uteis/hora-uteis.sh
```

Execute os comandos abaixo
```sh
source ~/.bashrc
source ~/.zshrc
```

Rodando
```sh
pagode
```

#### Saida:
> Horas úteis em 2023-10: 168 horas - Serviço; R$ 18,480 
 
> Total anual: R$ 221,760  


### Créditos
##### Sham Vinicius Fiorin