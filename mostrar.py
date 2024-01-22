import cv2
import matplotlib.pyplot as plt

def mostrar(caminho):
  img =cv2.imread(caminho)
  fig = plt.gcf()
  fig.set_size_inches(18, 10)
  plt.axis("off")
  plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
  plt.show()

  mostrar('chart.png')