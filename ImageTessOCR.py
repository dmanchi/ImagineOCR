__author__ = 'deepak'
__project__ = 'OCRProject'

from PIL import Image
#from pytesseract import *
import pytesseract

class ImageRead:
    def __init__(self, pic):
        self.pic = pic

    def ImgRead(self):
        #print pytesseract.image_to_string(Image.open(self.pic))
        #print pytesseract.image_to_string(Image.open(self.pic), boxes=True)
        print "Running Pytesseract"
        img = Image.open(self.pic)
        for i in range(1, 360):
            imgnew = img.rotate(i)
            text = pytesseract.image_to_string(imgnew, lang='eng', boxes=True)
            w = open('/Users/deepak/Pictures/TesserOutput' + str(i) + '.txt','w')
            if len(text):
                w.write(text)
            w.close()