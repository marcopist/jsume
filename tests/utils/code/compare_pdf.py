from wand.image import Image

def compare_pdf(pdfa, pdfb):
    imga = Image(blob=pdfa, resolution=150)
    imgb = Image(blob=pdfb, resolution=150)

    diff = imga.compare(imgb, metric='root_mean_square')

    return diff