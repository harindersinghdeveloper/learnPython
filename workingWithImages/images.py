from PIL import Image

#Change format and save
m_one = Image.open("image.avif")
print(m_one.format)
m_one.show()
m_two = m_one.convert("RGB")
m_two.save("image.jpg")

#open the new image
m_three = Image.open("image.jpg")
m_three.show()

#crop image
cropped_image = m_three.crop((0,0,500,500))
cropped_image.save("cropped.jpg")
m_four = Image.open("cropped.jpg")
m_four.show()