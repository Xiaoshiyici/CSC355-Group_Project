# Import PIL module
from PIL import Image

# Import sys module for sys.argv(to get filename)
import sys
# Get filenames from argument
def read_image(filename1, filename2):
# Open the image files
    image1 = Image.open(filename1)
    image2 = Image.open(filename2)
    width, height = image1.size[0], image1.size[1] # Get image size
    image2 = image2.resize((width, height), Image.ANTIALIAS)

# Save the output images
    image1.crop((0, 0, width, height / 2)).save('/Users/rwkm/PycharmProjects/CSC355-Group_Project/Images/output1a.jpg')
    image1.crop((0, height / 2, width, height)).save('/Users/rwkm/PycharmProjects/CSC355-Group_Project/Images/output1b.jpg')
    image2.crop((0, 0, width, height / 2)).save('/Users/rwkm/PycharmProjects/CSC355-Group_Project/Images/output2a.jpg')
    image2.crop((0, height / 2, width, height)).save('/Users/rwkm/PycharmProjects/CSC355-Group_Project/Images/output2b.jpg')







