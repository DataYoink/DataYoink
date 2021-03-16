import pandas as pd
import numpy as np


def get_axis_info(xcoordinatemin, xcoordinatemax, xpixelmax, ycoordinatemin, ycoordinatemax, ypixelmax, origin,
                  max_points, units):
    """
    Collects information provided by the user into a convenient dictionary form to be used in the csv
    conversion process.
    :param xcoordinatemin: float, smallest value along the x axis in input image (location of origin)
    :param xcoordinatemax: float, largest value along the x axis in input image
    :param xpixelmax: array of length 2, location in pixels of xcoordinatemax point
    :param ycoordinatemin: float, smallest value along the y axis in input image (location of origin)
    :param ycoordinatemax: float, largest value along the y axis in input image
    :param ypixelmax: array of length 2, location in pixels of xcoordinatemax point
    :param origin: array of length 2 with the pixel location of the origin:
                   origin[0] is the pixel location along x axis (integer distance from left side of image)
                   of the xcoordinatemin.
                   origin[1] is the pixel location along y axis (integer distance from top edge of image)
                   of the ycoordinatemin
    :param max_points: int, maximum number of xy points desired in output for each curve
    :param units: array with length 2, with units of each axis (x first) of the input image
    :return axis_info_dict: a dictionary with the following fields: pixel_origin, x_scale, y_scale, step,
                            units, y_pixel_range, and x_pixel_range.
    """
    # this code assumes that ypixelmin_true < ypixelmax_true, which is not the case for the input,
    # so a small correction is made
    ypixelmin_true = ypixelmax[1]
    ypixelmax_true = origin[1]
    xpixelmin = origin[0]
    xpixelmax = xpixelmax[0]
    x_scale = get_x_scale(xcoordinatemin, xcoordinatemax, xpixelmin, xpixelmax)
    y_scale = get_x_scale(ycoordinatemin, ycoordinatemax, ypixelmin_true, ypixelmax_true)
    pixel_origin = (xpixelmin, ypixelmax_true)  # assumes that y pixel max is the smaller y value
    axis_info_dict = {'pixel_origin': pixel_origin,
                      'x_scale': x_scale,
                      'y_scale': y_scale,
                      'step': get_step(max_points, xpixelmin, xpixelmax),
                      'units': (units[0], units[1]),
                      'y_pixel_range': (ypixelmin_true, ypixelmax_true),
                      'x_pixel_range': (xpixelmin, xpixelmax)}
    return axis_info_dict


def get_step(max_points, xpixelmin, xpixelmax):
    """
    Converts the maximum desired points along the x axis into a step size in pixels
    :param max_points: int, user defined maximum desired points along the x axis
    :param xpixelmin: int, minimum pixel location along the x axis
    :param xpixelmax: int, maximum pixel location along the x axis
    :return step: int, distance between x values in the output
    """
    # step = length of x axis in pixels / max_points
    step = int(np.ceil((xpixelmax - xpixelmin) / max_points))
    return step


def get_x_scale(xcoordinatemin, xcoordinatemax, xpixelmin, xpixelmax):
    """
    Establishes the scaling from pixels to x axis units. Can also be used for the y scaling, with all 'x'
    in input variables replaced with their 'y' counterparts
    :param xcoordinatemin: number, minimum x (or y) value (from input image)
    :param xcoordinatemax: number, maximum x ( or y) value (from input image)
    :param xpixelmin: int, minimum pixel location along the x (or y) axis
    :param xpixelmax: int, maximum pixel location along the x ( or y) axis
    :return x_scale: a value with units (pixels/coordinate unit) used to scale distances along the x (or y) axis
    """
    # the x pixel and x coordinate count up in the same direction
    pixel_range = xpixelmax - xpixelmin
    coordinate_range = xcoordinatemax - xcoordinatemin
    x_scale = pixel_range / coordinate_range
    return x_scale


def pixel_to_coords(pixel_loc, axis_info_dict):
    """
    Converts a pixel location to coordinates on the xy axis
    :param pixel_loc: tuple, (x,y) location of a single pixel starting from the top left
    :param axis_info_dict: dict, result of the get_axis_info function
    :return (coord_x, coord_y): tuple with the x and y coordinates of the pixel in same units as input image
    """
    # pixel_loc is a tuple (x,y) of pixel location starting from top left
    x_pixel_loc = pixel_loc[0]
    coord_x = x_pixel_to_coords(x_pixel_loc, axis_info_dict)

    # get signed distance from pixel to origin in x and y(pixel units):
    pixel_distance_y = axis_info_dict['pixel_origin'][1] - pixel_loc[1]

    # pixels / (pixel/coord) = coord
    coord_y = pixel_distance_y / axis_info_dict['y_scale']
    coords = (coord_x, coord_y)
    return coords


def x_pixel_to_coords(x_pixel_loc, axis_info_dict):
    """
    Converts the pixel location on the x axis to coordinates
    :param x_pixel_loc: int, distance in pixels of a single pixel from the left side of the image
    :param axis_info_dict: dict, result of the get_axis_info function
    :return coord_x: tuple with the x and y coordinates of the pixel in same units as input image
    """
    pixel_distance_x = x_pixel_loc - axis_info_dict['pixel_origin'][0]
    coord_x = pixel_distance_x / axis_info_dict['x_scale']
    return coord_x


def closest(lst, val):
    """
    Finds the closest number in a list to a value. If there is a tie, the first value in the list is selected.
    :param lst: list, a list of numbers
    :param val: any number
    :return: the value in list 'lst' that is closest to val
    """
    lst = np.asarray(lst)
    idx = (np.abs(lst - val)).argmin()
    return lst[idx]


def unify_x(pixel_lst, axis_info_dict):
    """
    Fits the y values in the input list to an evenly spaced list of x axis values
    :param pixel_lst: list, a list of tuples (x, y), each with the xy location of a pixel starting
                            from the top left of the image
    :param axis_info_dict: dict, result of the get_axis_info function
    :return unified_pixel_lst: a list of (x, y) pixels, similar to input list
    """
    # get the number of pixels between each desired coordinate pt based on scale
    # create bins of pixels and avg the values between them
    pixel_lst.sort()

    # step is a global variable based on user input
    step = axis_info_dict['step']
    x_pixels = [i[0] for i in pixel_lst]
    x_vals = list(range(min(x_pixels), max(x_pixels), step))

    # create dictionary of point and closest standard x val
    closest_dict = {}
    for point in pixel_lst:
        key = closest(x_vals, point[0])
        if key in closest_dict.keys():
            closest_dict[key].append(point)
        else:
            closest_dict[key] = [point]

    # iterate through keys to average all y values in each set
    for key in closest_dict:
        y_vals = [i[1] for i in closest_dict[key]]
        y_val = sum(y_vals) / len(y_vals)
        closest_dict[key] = y_val

    # for all the missing dict keys, make a line between nearest values and fill it in
    existing_keys = list(closest_dict.keys())
    existing_keys.sort()
    for x in x_vals:
        if x not in existing_keys:
            # find the index of first existing x greater than x
            i = 0
            while existing_keys[i] < x and i < (len(x_vals) + 1):
                i += 1

            x2 = existing_keys[i]  # existing x just above missing x
            y2 = closest_dict[x2]
            x1 = existing_keys[i - 1]  # existing x just below missing x
            y1 = closest_dict[x1]

            # find line between bounds
            m = (y1 - y2) / (x1 - x2)
            b = (x1 * y2 - x2 * y1) / (x1 - x2)

            # solve for y of x
            y = m * x + b
            closest_dict[x] = y

        else:
            continue

    # turn dictionary into a list of tuples
    unified_pixel_lst = list(closest_dict.items())
    unified_pixel_lst.sort()

    return unified_pixel_lst


def get_pixels_2d(pixel_array_2d):
    """
    Identifies pixels in a 2d slice of the pred_masks array belonging to a single instance
    :param pixel_array_2d: a 2D numpy array of shape (H,W) with only boolean values, where
                           H and W are the height and width of the input image in pixels
    :return pixel_lst: a list of (x, y) pixels belonging to the same instance
    """
    result = np.where(pixel_array_2d)
    pixel_lst = list(zip(result[1], result[0]))  # gives the x then the y in the tuple
    return pixel_lst


def create_pixel_dict(pred_masks):
    """
    Creates a dictionary of pixels belonging to each instance
    :param pred_masks: a 3D tensor of shape (N, H,W) with only boolean values, where
                           H and W are the height and width of the input image in pixels
                           and N is the number of unique instances
    :return pixel_dict: a dict with keys of the form 'curve_N', where N starts at 1,
                        and values that are each lists of (x, y) pixels belonging to the same instance
    """
    # initialize dict
    pixel_dict = {}

    pixel_array_3d = np.array(pred_masks)
    for N in range(len(pixel_array_3d)):
        pixel_array_2d = pixel_array_3d[N]
        pixel_lst = get_pixels_2d(pixel_array_2d)

        # add the list of pixels for this N to the pixel dict
        instance_id = 'curve_' + str(N + 1)
        pixel_dict[instance_id] = pixel_lst
    return pixel_dict


def create_coordinate_dict(pixel_dict, axis_info_dict):
    """
    Creates a dictionary of coordinate locations of pixels belonging to each instance
    :param pixel_dict: a dict with keys of the form 'curve_N', where N starts at 1,
                        and values that are each lists of (x, y) pixels belonging to the same instance
    :param axis_info_dict: dict, result of the get_axis_info function
    :return coordinate_dict: a dict with keys of the form 'curve_N', where N starts at 1,
                        and values that are each lists of (x, y) positions belonging to the same instance
    """
    # initialize dict
    coordinate_dict = {}

    for ID in pixel_dict.keys():
        pixel_lst = pixel_dict[ID]

        # get unified x axis:
        # add an if statement to handle user specifying either step size (in coordinates) or number of points
        unified_pixel_lst = unify_x(pixel_lst, axis_info_dict)

        # convert pixels to coordinates
        coordinate_lst = []
        for pixel_loc in unified_pixel_lst:
            coordinate_lst.append(pixel_to_coords(pixel_loc, axis_info_dict))

        # add the list of coordinates for this ID to the coordinate dict
        coordinate_dict[str(ID)] = coordinate_lst
    return coordinate_dict


def get_start_end(pixel_dict, axis_info_dict):
    """
    Creates a dictionary of coordinate locations of first and last points for each instance
    :param pixel_dict: a dict with keys of the form 'curve_N', where N starts at 1,
                        and values that are each lists of (x, y) pixels belonging to the same instance
    :param axis_info_dict: dict, result of the get_axis_info function
    :return pixel_dict: a dict with keys of the form 'curve_N', where N starts at 1,
                        and values that are tupeles: (x_start, x_end) with first and last x values
                        of points for each instance
    """
    # initialize dict
    start_end_dict = {}

    for ID in pixel_dict.keys():
        pixel_lst = pixel_dict[ID]

        # get start and end, assumes x is in the first position
        start = x_pixel_to_coords(min(pixel_lst)[0], axis_info_dict)
        end = x_pixel_to_coords(max(pixel_lst)[0], axis_info_dict)
        # add the start and end tuple for this ID to the pixel dict
        start_end_dict[str(ID)] = (start, end)
    return start_end_dict


def create_output_dict(pred_masks, axis_info_dict):
    """
    Creates a dictionary of the output info for each instance (coordinates, start/end values, and units)
    :param pred_masks: a 3D tensor of shape (N, H,W) with only boolean values, where
                           H and W are the height and width of the input image in pixels
                           and N is the number of unique instances
    :param axis_info_dict: dict, result of the get_axis_info function
    :return output_dict: a dictionary with keys 'coordinates' and 'start_end', which each refer to the dictionaries
                        created by create_coordinate_dict and get_start_end, and a key 'units' with value of type
                        tuple containing the x and y coordinate units
    """
    pixel_dict = create_pixel_dict(pred_masks)
    output_dict = dict()
    output_dict['coordinates'] = create_coordinate_dict(pixel_dict, axis_info_dict)
    output_dict['start_end'] = get_start_end(pixel_dict, axis_info_dict)
    output_dict['units'] = axis_info_dict['units']
    return output_dict


def write_results_to_excel(output_dict, filename):
    """
    Saves the results stored in the output dictionary in an excel file with name 'filename', and one sheet per instance
    and one sheet with start and end locations on the x axis for each instance
    :param output_dict: a dictionary with keys 'coordinates' and 'start_end', which each refer to the dictionaries
                        created by create_coordinate_dict and get_start_end, and a key 'units' with value of type
                        tuple containing the x and y coordinate units
    :param filename: a string with the desired name of the output excel file
    """
    excel_filename = str(filename) + '.xlsx'
    writer = pd.ExcelWriter(excel_filename, engine='xlsxwriter')
    x_units = output_dict['units'][0]
    y_units = output_dict['units'][1]

    # a summary of the start and end of the x axis for each ID
    starts = []
    ends = []
    ids = []
    for ID in output_dict['start_end'].keys():
        ids.append(ID)
        start = output_dict['start_end'][ID][0]
        end = output_dict['start_end'][ID][1]
        starts.append(start)
        ends.append(end)
    df = pd.DataFrame(list(zip(ids, starts, ends)),
                      columns=['ID', 'x start, ' + str(x_units), 'x end, ' + str(x_units)])
    df.to_excel(writer, sheet_name='starts_ends', index=False)

    # the actual data in xy form, one ID per sheet
    for ID in output_dict['coordinates'].keys():
        x = [output_dict['coordinates'][ID][i][0] for i in range(len(output_dict['coordinates'][ID]))]
        y = [output_dict['coordinates'][ID][i][1] for i in range(len(output_dict['coordinates'][ID]))]
        column_titles = ['x, ' + str(x_units), 'y, ' + str(y_units)]
        df = pd.DataFrame(list(zip(x, y)), columns=column_titles)
        df.to_excel(writer, sheet_name=str(ID), index=False)
    writer.save()
    return


def datayoink_to_excel(detect_output, axis_info_dict, filename='image'):
    """
    Converts the detectron2 prediction output to a list of coordinate values and saves them in
    an excel file (.xlsx) with a name based on filename and one sheet per instance and one sheet
    with start and end locations on the x axis for each instance.
    :param detect_output: the output of detectron2 with an 'instances' field containing information about
                          predicted masks
    :param axis_info_dict: dict, result of the get_axis_info function
    :param filename: the base filename for the output excel file
    """
    n_images = len(detect_output)
    if n_images > 1:
        for image in range(n_images):
            pred_masks = detect_output[image]['instances'].pred_masks
            output_dict = create_output_dict(pred_masks, axis_info_dict)
            filename_n = filename + '_' + str(image)
            write_results_to_excel(output_dict, filename_n)
    elif n_images == 1:
        pred_masks = detect_output['instances'].pred_masks
        output_dict = create_output_dict(pred_masks, axis_info_dict)
        filename_n = filename
        write_results_to_excel(output_dict, filename_n)
    return
