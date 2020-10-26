#Mingyuan Gao
#Professor Leon Tabak
#blend image

from PIL import Image

def blendImages(firstPhoto, secondPhoto, int):
    #Convert the first photo to RGBA
    firstPhoto = firstPhoto.convert("RGBA")
    #Convert the second photo to RGBA
    secondPhoto = secondPhoto.convert("RGBA")
    #To reset the first photo's size
    resizedFirstPhoto = firstPhoto.resize((600,600))
    #To reset the second photo's size
    resizedSecondPhoto = secondPhoto.resize((600,600))
    #to blend two reseted photo
    blendedImage = Image.blend(resizedFirstPhoto, resizedSecondPhoto, int)
    #show the result
    blendedImage.show()
    return


#
# def main():
#     print("test")
#
#
#     firstPhoto = Image.open("blackimagesflower-wall.jpg")
#     secondPhoto = Image.open("brightimagesflower-wall.jpg")
#     blendImages(firstPhoto, secondPhoto, 0.7)
#
# if __name__ == "__main__":
#     main()
# tos
#     firstTwoBlendedImage = Image.blend(resizedFirstPhoto, resizedSecondPhoto, int)
#     #to blend second two reseted photos
#     secondTwoBlendedImage = Image.blend(resizedThirdPhoto, resizedFourthPhoto, int)
#     #to blend two blended photos
#     finalBlendedImage = Image.blend(firstTwoBlendedImage, secondTwoBlendedImage, int)
#     #show the result
#     finalBlendedImage.show()
#     return
#
# def main():
#     print("test")
#
#
#     firstPhoto = Image.open("blackimagesflower-wall.jpg")
#     secondPhoto = Image.open("brightimagesflower-wall.jpg")
#     thirdPhoto = Image.open("brightencontrastimagesflowers-wall.jpg")
#     fourthPhoto = Image.open("coloredimagesflowers-wall.jpg")
#     blendImages(firstPhoto, secondPhoto, thirdPhoto, fourthPhoto, 0.7)
#
# if __name__ == "__main__":
#     main()
