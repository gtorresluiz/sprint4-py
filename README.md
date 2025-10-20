# 🧠 Orión - Sistema de Reconhecimento Facial para Autenticação
Este projeto é uma prova de conceito (PoC) que demonstra o uso de reconhecimento facial com Python e OpenCV integrado a um sistema de login em uma plataforma de investimentos.
O objetivo é autenticar usuários por meio da detecção facial local, validando se a face está presente na base antes de permitir o acesso.

## Link Vídeo Explicativo

https://youtu.be/-yNP0U6BM9s

## 👥 Integrantes

- **Eduardo Fedeli Souza** — RM550132  
- **Gabriel Torres Luiz** — RM98600  
- **Otávio Vitoriano Da Silva** — RM552012  

## 🎯 Objetivo do Projeto

Simular o processo de login inteligente em uma aplicação de investimentos, utilizando a face do usuário como fator de autenticação.

Quando o sistema é iniciado, ele:

Abre o módulo de detecção facial (OpenCV).
Verifica se a face capturada existe na base de dados.
Caso seja reconhecida, autoriza o acesso ao sistema.
Caso contrário, nega o login e sugere um novo cadastro facial.

## ⚙️ Tecnologias Utilizadas

Python 3.12+
OpenCV (com módulo contrib)
Haar Cascade Classifier (para detecção de rosto)
LBPH Face Recognizer (para identificação facial)
Simulação de Banco Oracle (armazenando rostos cadastrados)
Ambiente local (Desktop)

# 🧩 Arquitetura Simplificada

```

+--------------------+        +---------------------------+
|   Plataforma Web   | -----> |   Módulo de Login Facial  |
|  (Investimentos)   |        |   (Python + OpenCV)       |
+--------------------+        +-----------+---------------+
                                         |
                                         v
                               +---------------------+
                               |  Banco Simulado     |
                               |  (Faces Cadastradas)|
                               +---------------------+

```

## 💻 Execução do Projeto
Pré-requisitos

Certifique-se de ter o Python instalado.
No terminal, execute:
pip install opencv-contrib-python numpy

### Executando
No terminal, dentro da pasta do projeto:
python faces.py

### O sistema:
Treina o modelo com as faces cadastradas (simulando o banco).
Analisa as imagens presentes na pasta images/.
Exibe se cada face foi ou não reconhecida.

### Exemplo de saída
💾 Conexão simulada com o banco Oracle estabelecida.

✅ Modelo treinado com as faces do banco.

✅ face1.jpg corresponde à face cadastrada: Gabriel (confiança: 0.0)
❌ face2.jpg não encontrada no banco (confiança: 85.2)
❌ face3.jpg não encontrada no banco (confiança: 92.1)

🔍 Verificação concluída.

## ⚖️ Nota Ética sobre Uso de Dados Faciais

O uso de reconhecimento facial deve seguir as boas práticas de privacidade e consentimento.
As imagens utilizadas neste projeto são apenas para fins educacionais.
Nenhum dado biométrico é armazenado permanentemente.
O sistema é local e não transmite informações a servidores externos.
