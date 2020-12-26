from PIL import Image, ImageFont, ImageDraw
from PyQt5 import QtCore, QtWidgets, QtGui

def convert_pil_image_to_pixmap(image):
    data = image.convert("RGBA").tobytes("raw", "RGBA")
    qim = QtGui.QImage(data, *image.size, QtGui.QImage.Format_RGBA8888)
    pixmap = QtGui.QPixmap.fromImage(qim)
    return pixmap
