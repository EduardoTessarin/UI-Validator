import os, pdb
import yaml
from PIL import Image

diretorio_baseline = 'solucao-rd/baseline'
diretorio_atual = 'solucao-rd/atual'
diretorio_divergentes = 'solucao-rd/divergentes'

total_testes = 0
testes_passaram = 0
testes_falharam = 0

if not os.path.exists(diretorio_divergentes):
    os.makedirs(diretorio_divergentes)

def carregar_rois(arquivo_yaml):
    try:
        with open(arquivo_yaml, 'r') as stream:
            return yaml.safe_load(stream)
    except FileNotFoundError:
        print("Arquivo YAML de ROIs não encontrado. A comparação será feita na imagem inteira.")
        return {}

def comparar_imagens_com_rois(image1, image2, rois):
    for roi in rois:
        # image1.crop(roi).show(title="Divergente em ROI - Image 1")
        if image1.crop(roi) != image2.crop(roi):
            return False
    return True

def comparar_imagens_inteiras(image1, image2):
    return image1 == image2

rois = carregar_rois('rois.yaml')
arquivos_baseline = [f for f in os.listdir(diretorio_baseline) if f.startswith('baseline')]

for arquivo in arquivos_baseline:
    caminho_baseline = os.path.join(diretorio_baseline, arquivo)
    caminho_atual = os.path.join(diretorio_atual, arquivo.replace('baseline_', 'atual_'))

    image1 = Image.open(caminho_baseline)
    image2 = Image.open(caminho_atual)

    total_testes += 1

    if image1.size == image2.size:
        if arquivo in rois:
            resultado_comparacao = comparar_imagens_com_rois(image1, image2, rois[arquivo])
        else:
            resultado_comparacao = comparar_imagens_inteiras(image1, image2)

        if resultado_comparacao:
            testes_passaram += 1
        else:
            pixels1 = image1.load()
            pixels2 = image2.load()

            width, height = image1.size
            imagem_diferencas = Image.new('RGB', (width, height), (255, 255, 255))
            pixels_dif = imagem_diferencas.load()

            diferentes = 0

            for x in range(width):
                for y in range(height):
                    if pixels1[x, y] != pixels2[x, y]:
                        diferentes += 1
                        pixels_dif[x, y] = (255, 0, 0)
            if diferentes > 0:
                testes_falharam += 1
                nova_largura = width * 3
                imagem_combinada = Image.new('RGB', (nova_largura, height))
                imagem_combinada.paste(image1, (0, 0))
                imagem_combinada.paste(image2, (width, 0))
                imagem_combinada.paste(imagem_diferencas, (width * 2, 0))

                nome_arquivo_divergente = arquivo.replace('baseline_', '')
                imagem_combinada.save(os.path.join(diretorio_divergentes, nome_arquivo_divergente))
                print(f"Divergência encontrada e imagem combinada salva para: {nome_arquivo_divergente}")
            else:
                testes_passaram += 1
    else:
        print(f"As imagens {arquivo} têm dimensões diferentes e não puderam ser comparadas.")
        testes_falharam += 1
print("\nTestes finalizados.\n")
print(f"Total de testes realizados: {total_testes}")
print(f"Testes passaram: {testes_passaram}")
print(f"Testes falharam: {testes_falharam}")