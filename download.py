from PIL import Image
import requests
from io import BytesIO

class Download(object):
    '''
        A class for helping in dowloading the required images from the given url to the specified path
    '''

    def __call__(self, path, url):
        '''
            Arguments:
            path: download path with the file name
            url: required image URL
        '''
        img = requests.get(url)
        with open(path,'wb') as f:
            f.write(img.content)

if __name__ == '__main__':
    image = Download()
    image.__call__("/home/sai_/Downloads/1.jpg","http://farm5.staticflickr.com/4127/5172389204_31214fdc50_z.jpg")

