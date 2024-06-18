from PIL import Image
ris = Image.open("котик33.jpg")
sc_image = ris.convert("L")
tra_image = sc_image.transpose(Image.FLIP_LEFT_RIGHT)
h_g = (400, 300)
new_image = tra_image.resize(h_g)
new_image.save("котик333.jpg")
new_image.show()