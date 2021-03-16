import os
from datayoink.img_rescale import img_rescale

def test_img_rescale():
    test_new_img = img_rescale("datayoink/tests/test_data/test_png.png",100,100)
    # Make sure the rescale image directory is created
    assert os.path.exists("scaled_input_image") == True, "Failed to create rescaled image folder"
    return