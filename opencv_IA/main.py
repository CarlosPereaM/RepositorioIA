import cv2
import numpy as np
#CARGAMOS IMAGEN
image = cv2.imread('AI.jpg')
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#OBTENER DIMENSIONES DE LA IMAGEN
hight, width = image.shape[:2]
center = (width/2, hight/2)
#ROTAR LA IMAGEN
angulo = 90
matrix = cv2.getRotationMatrix2D(center, angulo, 1.0)
rotated = cv2.warpAffine(image, matrix, (width, hight))
cv2.imshow('Image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
#DEFINIR LA MATRIZ DE TRASLACIÓN
tx, ty = 100, 50 
M = np.float32([[1, 0, tx], [0, 1, ty]])
#APLICAR LA MATRIZ DE TRASLACIÓN A LA IMAGEN
translated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
#MOSTRATRE LA IMAGEN TRASLADADA
cv2.imshow('Image', translated)
cv2.waitKey(0)
cv2.destroyAllWindows() 
#ESCALA
# DEFINIR LA NUEVA ALTURA Y ANCHO DE LA IMAGEN
new_height, new_width = 300, 250
#APLICAR LA ESCALA DE LA IMAGEN
scaled = cv2.resize(image, (new_width, new_height))
#MOSTRAR LA IMAGEN ESCALADA
cv2.imshow('Image', scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()
#RECORTE
# DEFINIR LAS COORDENADAS DEL ÁREA DE INTERÉS ROI 
x, y, w, h = 100, 100, 200, 150
#RECORTAR LA REGIÓN DE INTERÉS ROI
cropped = image[y:y+h, x:x+w] 
#MOSTRAR LA IMAGEN RECORTADA
cv2.imshow('Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
# SUAVIZADO
# APLICAR EL FILTRO GAUSSIANO PARA SUAVISAR LA IMAGEN 
smoothed = cv2.GaussianBlur(image, (5, 5), 0)
#MOSTRAR LA IMAGEN SUAVISADA
cv2.imshow('Image', smoothed)
cv2.waitKey(0)
cv2.destroyAllWindows()
#REALCE
# DEFINIR EL KERNEL PARA EL FILTRO DE AFILADO
kernel = np.array([[-1, -1, -1], 
                   [-1, 9, -1], 
                   [-1, -1, -1]])
#APLICAR EL FILTRO DE AFILADO PARA REALZAR LOS DETALLES
sharpened = cv2.filter2D(image, -1, kernel)
#MOSTRAR LA IMAGEN REALZADA
cv2.imshow('Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
#DETECCIÓN DE BORDES
# CARGAR LA IMAGEN EN ESCALA DE GRISES 
image = cv2.imread('AI.jpg', cv2.IMREAD_GRAYSCALE)
# APLICAR EL OPERADOR SOBEL PARA DETECTAR LOS BORDES
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
#COMBINAR LAS RESPUESTAS EN MAGNITUD
edges = cv2.magnitude(sobelx, sobely) 
#NORMALIZAR LOS VALORES PARA MOSTRAR LA IMAGEN CORRECTAMENTE
edges = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
#MOSTRAR LA IMAGEN CON LOS BORDES DETECTADOS
cv2.imshow('Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()