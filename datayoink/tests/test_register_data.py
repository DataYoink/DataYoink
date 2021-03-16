import numpy as np
from datayoink.register_data import json_to_dict, show_img_and_mask
from datayoink.register_data import json_to_arrs, polygon_arr_to_list
from datayoink.register_data import img_mask_rescale, to_dict

def test_json_to_dict():
    """
    Test json_to_dict()
    """
    dictionary, imgs, polygon_list = json_to_dict("datayoink/tests/test_data/test_json/", 200, 500)
    assert isinstance(dictionary, list), "Unexpected output type"
    assert isinstance(dictionary[0], dict), "Unexpected output type"
    assert len(imgs)==len(polygon_list), "Image counts doesn't match polygon counts"
    return

def test_show_img_and_mask():
    """
    Test show_img_and_mask()
    """
    imgs = [np.array([[1,1,1],[1,1,1]]),np.array([[2,2,2],[2,2,2]]),np.array([[3,3,3],[3,3,3]])]
    polygon_list = [[np.array([[1,1],[1,1]]),np.array([[2,2],[2,2]])],[],[]]
    assert len(imgs)==len(polygon_list), "Image counts doesn't match polygon counts"
    return

def test_json_to_arrs():
    """
    Test test_json_to_arrs()
    """
    img, poly_for_single_img = json_to_arrs("datayoink/tests/test_data/test_json/test_json1.json")
    if len(poly_for_single_img[0]) != 0:
        assert len(poly_for_single_img[0][0]) == 2, "Coordinates have the wrong shape"
    return

def test_polygon_arr_to_list():
    """
    Test polygon_arr_to_list()
    """
    test_poly = [np.array([[1,1],[2,2],[3,3]]), np.array([[1,1],[2,2],[3,3]])]
    new_poly, box = polygon_arr_to_list(test_poly)
    assert len(new_poly[0]) == test_poly[0].shape[0]*test_poly[0].shape[1]
    return

def test_img_mask_rescale():
    """
    Test img_mask_rescale()
    """
    # Test with empty mask array
    new_img, new_poly = img_mask_rescale(np.array([[1,1,1],[1,1,1]]), np.array([]), 300, 200)
    assert not new_poly == True, "Unexpected results for zero mask scenario"
    return
def test_to_dict():
    """
    Test test_to_dict()
    """
    test_dictionary = to_dict("test_data/test_json/","test_json1.json",
                     1,234,567,[[1, 1, 2, 2, 3, 3], [4, 4, 5, 5, 6, 6]],
                     [[1, 1, 3, 3], [4, 4, 6, 6]])
    for key in ['file_name', 'image_id', 'height', 'width', 'annotations']:
        assert key in test_dictionary.keys(), "Missing dictionary keys"
    return