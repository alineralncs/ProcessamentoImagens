import cv2
import numpy as np
#____________________________________________________________
# ler, salvar e redmensionar imagem 
def lerImagem(imagePath):
    return cv2.imread(imagePath)

def salvarImagem(name, imagePath):
    save = cv2.imwrite(name, imagePath)
    print('Successfully saved')
    return save

def tamanhoigualImagem(img2, img1):
    return cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Operações Aritméticas
#____________________________________________________________

def adicao(img1, img2):
    return cv2.add(img1,img2)

def subtracao(img1, img2):
    return cv2.subtract(img1, img2)

def divisao(img1, img2):
    return cv2.divide(img1, img2)

def multiplicacao(img1, img2):
    return cv2.multiply(img1, img2)
#____________________________________________________________
# Transformações Geométricas
# Translação, Rotação, Escala, Reflexão.
def escala_cubic(img):
    return cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    
def translacao(img):
    rows = img.shape[0]
    cols = img.shape[1]
    M = np.float32([[1,0,100], [0, 1, 50]])
    transl = cv2.warpAffine(img, M, (cols, rows))
    return transl

def rotacao(img):
    rows = img.shape[0]
    cols = img.shape[1]
    MN = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
    #AARUMAER LINHA 48
    return cv2.warpAffine(img, MN, (cols, rows))

def reflexao_vertical(img):
    vertical = cv2.flip(img, 0)
    return vertical 
def reflexao_horizontal(img):
    horizontal = cv2.flip(img, 1)
    return horizontal
def reflexao_vert_hori(img):
    vert_hori = cv2.flip(img, -1)
    return vert_hori
    


def mostrar_antes(img):
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def mostrar_salvar(name, imagePath, funcao):
    print ("""
    
    1. Ver Imagem
    2. Salvar Nova Imagem
    """)

    opc =input('Deseja ver ou salvar?')
    if opc=='2':
        salvarImagem(name, imagePath)
    elif opc=='1':
        cv2.imshow('image',funcao)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



# import cv2
# import os
# class Imagens:
#     def __init__(self, img) :
#         self.img = img
#     def __str__(self):
#         return self.img
#     def lerImagem(self):
#         return cv2.imread(self.img)
#     def salvarImagem(imagePath, name):
#        return cv2.imwrite(name, imagePath)


# path_img1 = Imagens('imagens/vi.jpg')
# path_img2 = Imagens('imagens/jiinx.jpg')
# # img1 = 'imagens/200.png'
# # img2 = 'imagens/lena.png'

# img1 = Imagens.lerImagem(path_img1)
# img2 = Imagens.lerImagem(path_img2)


# img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
# dst = cv2.add(img1,img2_resized)
# Imagens.salvarImagem('save.png', dst)
# print("After saving image:")  
# print(os.listdir('imagens'))
  
# print('Successfully saved')