from PIL import Image
import stepic

#ENCRYPTION

original_img= Image.open('flower123.png')

encoded_img = stepic.encode(original_img, b'FLASHES TAKE CARE OF FLASHES')
encoded_img.save('flower1234.png')
encoded_img=Image.open('flower1234.png')
encoded_img.show()

# DECRYPTION

decoded_img = stepic.decode(encoded_img)
print(decoded_img)


