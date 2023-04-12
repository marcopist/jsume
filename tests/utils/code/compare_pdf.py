from wand.image import Image


def compare_pdf(pdfa: bytes, pdfb: bytes) -> bool:
    """Checks if two pdfs are the same.

    Args:
        pdfa (bytes): The first pdf.
        pdfb (bytes): The second pdf.

    Returns:
        tuple[Image, float]: The difference as a wand image and a float.
    """
    imga = Image(blob=pdfa, resolution=150)
    imgb = Image(blob=pdfb, resolution=150)

    diff = imga.compare(imgb, metric="root_mean_square")

    same: bool = diff[1] < 0.01  # Are the images the same?

    return same
