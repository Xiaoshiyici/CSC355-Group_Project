from PIL import Image
from PIL import ImageDraw, ImageOps, ImageEnhance, ImageFilter
import sys

from Kaiyu_Wang.ImageSlice import read_image
from Zhifei_Xu.ImageChange import imageChange
from Mingyuan_Gao.blend_image import blendImages


def main():
    # change the image path when you run this code on other computers.
    image1path1 ="/Users/rwkm/PycharmProjects/CSC355-Group_Project/Images/Image_1.jpg"
    image1path2 ="/Users/rwkm/PycharmProjects/CSC355-Group_Project/Images/Image_2.jpg"

    read_image(image1path1,image1path2)

    # change the image path when you run this code on other computers.
    image1part1 = Image.open("/Users/rwkm/PycharmProjects/CSC355-Group_Project/Images/output1a.jpg")
    image1part2 = Image.open("/Users/rwkm/PycharmProjects/CSC355-Group_Project/Images/output1b.jpg")
    image2part1 = Image.open("/Users/rwkm/PycharmProjects/CSC355-Group_Project/Images/output2a.jpg")
    image2part2 = Image.open("/Users/rwkm/PycharmProjects/CSC355-Group_Project/Images/output2b.jpg")

    # we modify our image to different color,
    photo_1 = imageChange.enhance_Color(image1part1, 5)
    modified1 = imageChange.filter_Contour(photo_1)

    photo_2 = imageChange.enhance_Brightness(image1part2, 5)
    modified2 = imageChange.filter_Detail(photo_2)

    photo_3 = imageChange.enhance_Contrast(image2part1, 5)
    modified3 = imageChange.filter_Blur(photo_3)

    photo_4 = imageChange.enhance_Sharpness(image2part2, 5)
    modified4 = imageChange.convert_RGB_to_HSV(photo_4)


    # show the final image after blend
    blendImages(modified1, modified2, 2)
    blendImages(modified3, modified4, 4)




if __name__ == "__main__":
    main()