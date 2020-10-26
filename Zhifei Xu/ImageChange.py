
# Saturday, 24 October 2020
# Professor Leon Tabak
# CSC355 Open Source Development
# Zhifei Xu




#The Colorsys module, one of the built-in modules in Python,
# provides an interface for bi-directional conversion between RGB and YIQ/HLS/HSV color patterns.
# It provides six functions, three for converting RGB to YIQ/HLS/HSV,
# and three for converting YIQ/HLS/HSV to RGB.
# website: https://docs.python.org/3.6/library/colorsys.html
# https://blog.csdn.net/jy692405180/article/details/72758054/
import colorsys

from PIL import Image
from PIL import ImageDraw, ImageOps, ImageEnhance, ImageFilter


target_hue=0

class imageChange:
    def enhance_Color(photo,int):
        enhance_color = ImageEnhance.Color(photo)

        enhance = enhance_color.enhance(int)

        enhance.show()
        return enhance

    def enhance_Brightness(photo,int):
        enhance_brightness = ImageEnhance.Brightness(photo)

        enhance = enhance_brightness.enhance(int)

        enhance.show()
        return enhance

    def enhance_Contrast(photo,int):

        enhance_contrast = ImageEnhance.Contrast(photo)

        enhance = enhance_contrast.enhance(int)

        enhance.show()
        return enhance

    def enhance_Sharpness(photo,int):

        enhance_sharpness = ImageEnhance.Sharpness(photo)

        enhance = enhance_sharpness.enhance(int)

        enhance.show()
        return enhance

    def filter_Contour(photo):
        #  perform contour filtering on the image
        filter_contour = photo.filter(ImageFilter.CONTOUR)


        filter_contour.show()
        return filter_contour

    def filter_Detail(photo):
        filter_detail = photo.filter(ImageFilter.DETAIL)

        filter_detail.show()
        return filter_detail

    def filter_Blur(photo):
        filter_blur = photo.filter(ImageFilter.BLUR)

        filter_blur.show()
        return filter_blur

    def filter_Smooth(photo):
        filter_smooth = photo.filter(ImageFilter.SMOOTH)

        filter_smooth.show()
        return filter_smooth

    def filter_Sharpen(photo):
        filter_sharpen = photo.filter(ImageFilter.SHARPEN)

        filter_sharpen.show()
        return filter_sharpen

    def filter_Emboss(photo):
        filter_emboss = photo.filter(ImageFilter.EMBOSS)

        filter_emboss.show()
        return filter_emboss

    def filter_GaussianBlur(photo, int):
        filter_gaussianBlur = photo.filter(ImageFilter.GaussianBlur(int))

        filter_gaussianBlur.show()
        return filter_gaussianBlur

    def convert_RGB_to_HSV(photo):

        print("original_photo mode", photo.mode)
        print("original_photo size", photo.size)

        # Converts the image to RGB color
        change_photo = photo.convert("RGBA")

        print("change_photo mode", change_photo.mode)
        print("change_photo size", change_photo.size)


        # Separate RGB color values
        change_photo.load()
        r, g, b, a = change_photo.split()

        result_r, result_g, result_b, result_a = [], [], [], []

        # Each pixel is processed in turn
        for pixel_r, pixel_g, pixel_b, pixel_a in zip(r.getdata(), g.getdata(), b.getdata(), a.getdata()):

            # translate between RGB and HSV value of each pixel
            h, s, v = colorsys.rgb_to_hsv(pixel_r / 255., pixel_b / 255., pixel_g / 255.)
            # Change the hue value of the image
            target_hue = h
            rgb = colorsys.hsv_to_rgb(target_hue, s, v)
            pixel_r, pixel_g, pixel_b = [int(x * 255.) for x in rgb]

            # Save the results for each pixel
            result_r.append(pixel_r)
            result_g.append(pixel_g)
            result_b.append(pixel_b)


        r.putdata(result_r)
        g.putdata(result_g)
        b.putdata(result_b)


        # Merged each pixel to a new image
        new_photo = Image.merge('RGB', (r, g, b))

        new_photo.show()
        return new_photo








