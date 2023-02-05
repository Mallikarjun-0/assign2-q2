#Imports
import jsonlines
from PIL import Image
import os
import numpy as np

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms=None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''

        self.annotation_file = annotation_file
        self.transforms = transforms
        f = jsonlines.open(annotation_file)
        data = []
        for line in f.iter():
            data.append(line)
        self.f = f
        self.data = data


    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        #lines = iter(self.f)
        len = 0
        for line in self.data:
             len+=1
        return len

    
    def __getann__(self, idx):
        '''
            return the data items for the index idx as an object
        '''
        return self.data[idx]        

    def __transformitem__(self, path):
        '''
            return transformed PIL Image object for the image in the given path
        '''
        im = Image.open(path)
        for transform in self.transforms:
            image = transform
            im = image.__call__(im)
        return im


if __name__ == "__main__":
    data = Dataset('/home/sai_/CS29006_SW_Lab_Spr2023/Python_DS_Assignment_Question_02/data/annotations.jsonl')
    line = data.__getann__(2)
    print((line['file_name']))
    #print(file[0])