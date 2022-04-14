from PIL import Image

image = Image.new(mode="RGB", size=(400,400), color=(189,183, 107) )
image.save("pil_green.png")
image.show()
#image.save('pil_text.png')