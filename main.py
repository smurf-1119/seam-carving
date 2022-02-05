'''
Author: zhuqipeng
Date: 2021-10-30 16:47:59
version: 3.5
LastEditTime: 2021-10-31 23:33:43
LastEditors: zhuqipeng
Description: 
FilePath: \Final Project\seam-carving\main.py
'''
from seam_carving import SeamCarver

import os



def image_resize_without_mask(filename_input, filename_output, new_height, new_width):
    obj = SeamCarver(filename_input, new_height, new_width)
    obj.save_result(filename_output)


def image_resize_with_mask(filename_input, filename_output, new_height, new_width, filename_mask):
    obj = SeamCarver(filename_input, new_height, new_width, protect_mask=filename_mask)
    obj.save_result(filename_output)


def object_removal(filename_input, filename_output, filename_mask):
    obj = SeamCarver(filename_input, 0, 0, object_mask=filename_mask)
    obj.save_result(filename_output)



if __name__ == '__main__':
    """
    Put image in in/images folder and protect or object mask in in/masks folder
    Ouput image will be saved to out/images folder with filename_output
    """

    folder_in = './in_data/'
    folder_out = './out_data/'

    filename_input = '1.png'
    filename_output = 'image_result1.jpg'
    # filename_mask = 'mask.jpg'
    new_height = 187
    new_width = 230

    input_image = os.path.join(folder_in, "images", filename_input)
    # input_mask = os.path.join(folder_in, "masks", filename_mask)
    output_image = os.path.join(folder_out, filename_output)

    image_resize_without_mask(input_image, output_image, new_height, new_width)
    # image_resize_with_mask(input_image, output_image, new_height, new_width, input_mask)
    # object_removal(input_image, output_image, input_mask)








