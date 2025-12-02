# Roomba workspace

Repositório criado como atividade da disciplina IA386II


# Estrutura

```
src - código fonte dos nós ROS 
config - arquivos de configuração dos nós ROS
launch - launcher files dos nós ROS
extra - arquivos não diretamente relacionados ao ROS
start.sh - ponto de entrada após boot, reponsável por carregar todos os nós
```

# Hardware

- Roomba 650
- Beelink BT3 (Intel Atom X5-Z8350 - 4GB RAM - 64GB storage)
- RP LiDAR A1
- TP-Link TL-WN727N (wifi externo)

# Build
```
git clone git@github.com:adalava/roomba_ws.git
cd roomba_ws
git submodule update --init --recursive
colcon build
```

# Iniciar

Executar o arquivo start.sh
