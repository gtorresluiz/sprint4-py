import cv2
import os
import numpy as np

# SIMULAÇÃO DO BANCO ORACLE

# Imagine que o "banco Oracle" tem apenas a face1 cadastrada
banco_faces_cadastradas = {
    "face1.png": "Gabriel"
}

print("💾 Conexão simulada com o banco Oracle estabelecida.\n")

# CONFIGURAÇÃO DO RECONHECIMENTO

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


# FUNÇÃO PARA CARREGAR FACES

def carregar_face(caminho):
    img = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"⚠️  Erro ao carregar imagem: {caminho}")
        return None
    rostos = face_detector.detectMultiScale(img)
    for (x, y, w, h) in rostos:
        return img[y:y+h, x:x+w]
    return None

# TREINA O MODELO COM AS FACES CADASTRADAS

faces_treino, ids = [], []
for i, (arquivo, nome) in enumerate(banco_faces_cadastradas.items()):
    caminho = os.path.join("images", arquivo)
    face = carregar_face(caminho)
    if face is not None:
        faces_treino.append(face)
        ids.append(i)

if not faces_treino:
    print("⚠️ Nenhuma face cadastrada no banco para treinar.")
    exit()

face_recognizer.train(faces_treino, np.array(ids))
print("✅ Modelo treinado com as faces do banco.\n")


# VERIFICA AS FACES PRESENTES NA PASTA

for arquivo in os.listdir("images"):
    caminho = os.path.join("images", arquivo)
    face_verificar = carregar_face(caminho)
    if face_verificar is None:
        continue

    label, confianca = face_recognizer.predict(face_verificar)

    if confianca < 40:
        nome = list(banco_faces_cadastradas.values())[label]
        print(f"✅ {arquivo} corresponde à face cadastrada: {nome} (confiança: {round(confianca, 2)})")
    elif confianca >= 100:
        nome = list(banco_faces_cadastradas.values())[label]
        print(f"✅ {arquivo} corresponde à face cadastrada: {nome} (confiança: {round(confianca, 2)})")
    else:
        print(f"❌ {arquivo} não encontrada no banco (confiança: {round(confianca, 2)})")

print("\n🔍 Verificação concluída.")
