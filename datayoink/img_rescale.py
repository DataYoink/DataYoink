import PIL
from PIL import Image
import numpy as np
import detectron2
import detectron2.data.transforms as T
import matplotlib
import matplotlib.pyplot as plt

def img_rescale(PNG_img, height, width):
    """
    This function rescales an image to designated height and width,
    returns new img as np array, and save the resacled image as
    .png file in the directory ./scaled_input_image as scaled_PNG_img.
    
    Inputs:
        img - .png image files
        height - expected height after conversion in unit of pixels
        width - expected width after conversion in unit of pixels
    
    Output:
        new_img - an nd array of the rescaled image 
    """
    if not os.path.exists("scaled_input_image"):
        os.mkdir("scaled_input_image") # new directory to store the scaled images
    img = Image.open(PNG_img) 
    img_array = np.array(img)
    scale = T.ScaleTransform(np.shape(img_array)[0],np.shape(img_array)[1], height, width)
    new_img = scale.apply_image(img_array, "bilinear")
    print("original image shape:",img_array.shape,"is scaled to new image shape",new_img.shape)
    img2save = Image.fromarray(new_img)
    img2save.save("./scaled_input_image/scaled_"+PNG_img)
    #plt.imshow(new_img)
    return new_img