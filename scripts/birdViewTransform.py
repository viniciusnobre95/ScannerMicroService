# Bibliotecas necessárias
from scipy.spatial import distance as dist
import numpy as np
import cv2 as cv
import imutils

# Funções de transformação

def order_points(pts):
	xSorted = pts[np.argsort(pts[:, 0]), :]

	leftMost = xSorted[:2, :]
	rightMost = xSorted[2:, :]

	leftMost = leftMost[np.argsort(leftMost[:, 1]), :]
	(tl, bl) = leftMost

	D = dist.cdist(tl[np.newaxis], rightMost, "euclidean")[0]
	(br, tr) = rightMost[np.argsort(D)[::-1], :]

	return np.array([tl, tr, br, bl], dtype="float32")

def four_point_transform(image, pts):
	rect = order_points(pts)
	print(rect)
	(tl, tr, br, bl) = rect

	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))
 
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))
	dst = np.float32([[0, 0],[maxWidth - 1, 0],[maxWidth - 1, maxHeight - 1], [0, maxHeight - 1]])
	M = cv.getPerspectiveTransform(rect, dst)
	warped = cv.warpPerspective(image, M, (maxWidth, maxHeight))
 
	return warped

def edge_detection_canny(image):
    image_resized = imutils.resize(image.copy(), height = 500)
    image_filtered = cv.GaussianBlur(image_resized.copy(), (5, 5), 0) # Filtro Gaussiano 5x5
    image_edge = cv.Canny(image_filtered, 75, 200)
    return image_edge

def finding_four_points(image):
    contornos = cv.findContours(image.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    contornos = imutils.grab_contours(contornos)
    contornos = sorted(contornos, key = cv.contourArea, reverse = True)[:5]

    quatro_pontos = []

    for contorno in contornos:
        peri = cv.arcLength(contorno, True)
        aprox = cv.approxPolyDP(contorno, 0.01 * peri, True)

        if (len(aprox) == 4):
            quatro_pontos = aprox
            break
    x = [ponto[0][0] for ponto in quatro_pontos]
    y = [ponto[0][1] for ponto in quatro_pontos]
    pontos = [(x, y) for x, y in zip(x,y)]
    pontos = np.float32(pontos)
    return pontos

def transform(image):

    image_gray = cv.cvtColor(image.copy(), cv.COLOR_RGB2GRAY)
    image_edge = edge_detection_canny(image_gray)
    four_points = finding_four_points(image_edge)
    image_warped = four_point_transform(imutils.resize(image.copy(), height = 500),four_points)
    return image_warped
