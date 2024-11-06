# Monitoramento de Sistema com Interface PySide2

Este projeto é um monitor de sistema em tempo real que utiliza PySide2 para fornecer uma interface gráfica. Ele exibe informações de utilização e desempenho de CPU, GPU e memória, permitindo monitoramento de métricas específicas e ajustáveis para cada componente.

## Funcionalidades

- **Monitoramento da CPU**: exibe o nome do processador e a porcentagem de uso em tempo real.
- **Monitoramento da GPU**: exibe o nome da GPU, temperatura, utilização de memória, codificação e decodificação de vídeo, e utilização do CUDA (caso esteja disponível).
- **Monitoramento de Memória RAM**: exibe o total de RAM disponível e o uso atual em tempo real.
- **Visualização Gráfica**: utiliza barras de progresso circulares para uma visualização clara e intuitiva das métricas monitoradas.
  
## Requisitos

- **Python 3.8+**
- **Bibliotecas Necessárias**:
  - https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
  - PySide2
  - GPUtil
  - psutil
  - firebase-admin (opcional, para integração com Firebase)
  - pip install PySide2extn
