import numpy as np
from datayoink.coordconverter import get_axis_info, get_step, get_x_scale, pixel_to_coords, closest,\
                                     unify_x, get_pixels_2d, create_pixel_dict, create_coordinate_dict, get_start_end


def test_get_axis_info():
    """
    Tests the get_axis_info function
    """
    # the output is a dictionary with the fields: pixel_origin, x_scale, y_scale, step, and units
    axis_info_dict = get_axis_info([1], [5], [20], [250], [10], [25], [30, 280], 30, ['volts', 'amps'])
    assert isinstance(axis_info_dict, dict), 'axis_info_dict is not a dictionary'
    for field in ['step', 'pixel_origin', 'x_scale', 'y_scale', 'units', 'y_pixel_range', 'x_pixel_range']:
        assert field in axis_info_dict.keys(), 'axis_info_dict is missing fields'
    return


def test_get_step():
    """
    Tests the get_step function
    """
    step1 = get_step(19, 10, 200)
    step2 = get_step(18, 10, 200)
    step3 = get_step(16, 10, 200)
    # the step size * the number of points should be close to the length of the axis
    # step size is an integer
    for step in [step1, step2, step3]:
        assert isinstance(step, int), 'the step size is not an integer'
    # the length of the axis/ step size should be close to but less than the max points
    assert np.isclose(190 / step1, 19), 'length of axis/step size not ~< max points'
    assert ((190 / step2) < 18) and ((190 / step2) > 17), 'length of axis/step size not ~< max points'
    assert ((190 / step3) < 16) and ((190 / step3) > 15), 'length of axis/step size not ~< max points'
    return


def test_get_x_scale():
    """
    Tests the get_x_scale function
    """
    x_scale = get_x_scale(1, 5, 20, 250)
    # x_scale * coordinate range should equal pixel range
    assert np.isclose(x_scale * (5 - 1), (250 - 20)), 'the x scaling is incorrect'
    assert np.isclose(x_scale, 57.5), 'the x scaling is incorrect'

    x_scale = get_x_scale(-1, -5, 20, 250)
    assert np.isclose(x_scale * (-5 + 1), (250 - 20)), 'the x scaling is incorrect'
    assert np.isclose(x_scale, -57.5), 'the x scaling is incorrect'
    return


def test_pixel_to_coords():
    """
    Tests the pixel_to_coords function (and by extension the x_pixel_to_coords function)
    """
    axis_info_dict1 = {'pixel_origin': (20, 100), 'y_scale': 5.3, 'x_scale': 20.5}
    axis_info_dict2 = {'pixel_origin': (20, 100), 'y_scale': -0.2, 'x_scale': 0.005}
    # the output coordinates should be within the coordinate ranges for each axis
    # given a scale and a location, test a few cases (+-0)
    coords1 = pixel_to_coords((20, 100), axis_info_dict1)  # (0,0)
    coords2 = pixel_to_coords((20, 100), axis_info_dict2)  # (0,0)
    coords3 = pixel_to_coords((55, 33), axis_info_dict1)  # (1.707317, 12.641509)
    coords4 = pixel_to_coords((55, 33), axis_info_dict2)  # (7000, -335)
    coords5 = pixel_to_coords((55, 105), axis_info_dict2)  # (1.707317, 25)

    assert np.isclose(coords1[0], 0), 'pixel to coordinate conversion is incorrect'
    assert np.isclose(coords1[1], 0), 'pixel to coordinate conversion is incorrect'
    assert np.isclose(coords2[0], 0), 'pixel to coordinate conversion is incorrect'
    assert np.isclose(coords2[1], 0), 'pixel to coordinate conversion is incorrect'
    assert np.isclose(coords3[0], 1.707317), 'pixel to coordinate conversion is incorrect'
    assert np.isclose(coords3[1], 12.64150943), 'pixel to coordinate conversion is incorrect'
    assert np.isclose(coords4[0], 7000), 'pixel to coordinate conversion is incorrect'
    assert np.isclose(coords4[1], -335), 'pixel to coordinate conversion is incorrect'
    assert np.isclose(coords5[1], 25), 'pixel to coordinate conversion is incorrect'
    return


def test_closest():
    """
    Tests the closest function
    """
    lst = [0, 2, 1, 3, 4, 5, 6]
    # val is equidistant to two values in list, first one in list is chosen
    assert closest(lst, 1.5) == 2, 'closest value is incorrect'
    assert closest(lst, 3.5) == 3, 'closest value is incorrect'
    # val is equal to one value in list
    assert closest(lst, 2) == 2, 'closest value is incorrect'
    # val is closer to one in particular
    assert closest(lst, 1.8) == 2, 'closest value is incorrect'
    return


def test_unify_x():
    """
    Tests the unify_x function
    """
    axis_info_dict = {'step': 3}
    pixel_lst = [(20, 100), (20, 90), (21, 91), (22, 85), (22, 83), (23, 80), (24, 81), (24, 83), (25, 80), (29, 50),
                 (29, 45), (30, 30), (30, 10)]
    pixels_y = [i[1] for i in pixel_lst]
    pixels_x = [i[0] for i in pixel_lst]
    unified_pixel_lst = unify_x(pixel_lst, axis_info_dict)
    unified_x = [i[0] for i in unified_pixel_lst]
    unified_y = [i[1] for i in unified_pixel_lst]
    x_spaces = np.diff(unified_x)
    # the x values in the list of tuples are all stepsize apart
    assert np.allclose(x_spaces, 3), 'the spacing between x values is incorrect'
    # the x values are unique
    assert len(set(unified_x)) == len(unified_x), 'the x values are not unique'
    # y values are all between the min and max pixel
    for y in unified_y:
        assert (y <= max(pixels_y)) and (y >= min(pixels_y)), 'unified y value is outside of expected bounds'
    # same for x values
    for x in unified_x:
        assert (x <= max(pixels_x)) and (x >= min(pixels_x)), 'unified x value is outside of expected bounds'
    return


def test_get_pixels_2d():
    """
    Tests the get_pixels_2d function
    """
    # create an array with a few trues and many falses, check positions in output match
    test_array = np.array([[False,  True, False,  False, False, False, False],
                           [False, False,  False,  True, False, False, False],
                           [False,  False, False, False, False,  True, False],
                           [True, False, False,  False, False, False, True],
                           [False, False,  False, False, False, False, False]])
    pixel_lst = get_pixels_2d(test_array)
    expected_pixel_lst = [(1, 0), (3, 1), (5, 2), (0, 3), (6, 3)]
    assert set(expected_pixel_lst) == set(pixel_lst), 'unexpected values in 2d pixel list'
    return


def test_create_pixel_dict():
    """
    Tests the create_pixel_dict function
    """
    pred_masks = np.array([[[False,  True, False,  True, False, False, False],
                            [False, False, False, False, False,  True,  True],
                            [False,  True, False, False, False, False, False],
                            [False,  True,  True, False, False, False, False],
                            [False, False,  True, False, False, False, False]],

                           [[True, False, False, False, False,  True,  True],
                            [True, False, False, False,  True, False, False],
                            [False, False, False, False, False,  True, False],
                            [False, False,  True, False,  True, False, False],
                            [False, False, False, False,  True, False, False]]])
    pixel_dict = create_pixel_dict(pred_masks)
    # check that the keys are 'curve_' and then a unique number that matches the shape of pred_masks
    assert list(pixel_dict.keys()) == ['curve_1', 'curve_2'], 'incorrect keys in pixel_dict'
    # the values are not the same for each one (not repeated)
    assert set(pixel_dict['curve_1']) != set(pixel_dict['curve_2']), 'curves in pixel_dict are not unique'
    return


def test_create_coordinate_dict():
    """
    Tests the create_coordinate_dict function
    """
    pred_masks = np.array([[[False,  True, False,  True, False, False, False],
                            [False, False, False, False, False,  True,  True],
                            [False,  True, False, False, False, False, False],
                            [False,  True,  True, False, False, False, False],
                            [False, False,  True, False, False, False, False]],

                           [[True, False, False, False, False,  True,  True],
                            [True, False, False, False,  True, False, False],
                            [False, False, False, False, False,  True, False],
                            [False, False,  True, False,  True, False, False],
                            [False, False, False, False,  True, False, False]]])
    pixel_dict = create_pixel_dict(pred_masks)
    axis_info_dict = {'pixel_origin': (0, 4), 'y_scale': 5.3, 'x_scale': 20.5, 'step': 1}
    coordinate_dict = create_coordinate_dict(pixel_dict, axis_info_dict)
    # the keys of the coordinate dict are the same as that of the pixel dict
    assert set(coordinate_dict.keys()) == set(pixel_dict.keys()), 'keys of coordinate and pixel dicts dont match'
    return


def test_get_start_end():
    """
    Tests the get_start_end function
    """
    pred_masks = np.array([[[False,  True, False,  True, False, False, False],
                            [False, False, False, False, False,  True,  True],
                            [False,  True, False, False, False, False, False],
                            [False,  True,  True, False, False, False, False],
                            [False, False,  True, False, False, False, False]],

                           [[True, False, False, False, False,  True,  True],
                            [True, False, False, False,  True, False, False],
                            [False, False, False, False, False,  True, False],
                            [False, False,  True, False,  True, False, False],
                            [False, False, False, False,  True, False, False]]])
    pixel_dict = create_pixel_dict(pred_masks)
    axis_info_dict = {'pixel_origin': (0, 4), 'y_scale': 5.3, 'x_scale': 20.5, 'step': 1}
    start_end_dict = get_start_end(pixel_dict, axis_info_dict)
    # the keys of the output dict are the same as the input
    assert set(start_end_dict.keys()) == set(pixel_dict.keys()), 'keys of start_end and pixel dicts dont match'
    for key in start_end_dict.keys():
        # the end is larger than (or equal to) the start
        assert start_end_dict[key][1] >= start_end_dict[key][0], 'starting x value greater than end value'
        # the start and end are between the coordinate ranges (hard to test without using all other functions)
    return
