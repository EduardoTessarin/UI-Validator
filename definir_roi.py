import matplotlib.pyplot as plt
from PIL import Image

def capturar_roi(imagem_caminho):
    img = Image.open(imagem_caminho)
    plt.imshow(img)
    
    pontos = []
    
    def onclick(event):
        pontos.append((event.xdata, event.ydata))
        print(f"Selecionado: {event.xdata}, {event.ydata}")
        if len(pontos) == 2:
            plt.close()

    fig = plt.gcf()
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()

    if len(pontos) == 2:
        x1, y1 = pontos[0]
        x2, y2 = pontos[1]
        roi = (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
        return [int(coord) for coord in roi]
    else:
        return None

imagem_caminho = 'solucao-rd/baseline/baseline_homeapp.png'
roi_selecionado = capturar_roi(imagem_caminho)
print("ROI selecionado:", roi_selecionado)
