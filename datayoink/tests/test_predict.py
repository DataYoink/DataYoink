"""
 There is no unit tests for predict_discharge_curve(), load_trained_nn(),
 and show_output_img_and_mask() becasue they require the neural network file,
 and we do not have space on Github to store the nn model file. 

"""
import numpy as np
from datayoink.predict import load_trained_nn, predict_discharge_curve
from datayoink.predict import read_img_to_BGR, show_output_img_and_mask

def test_read_img_to_BGR():
    """
    Test read_img_to_BGR() function
    """
    img_array = np.array([[0.2,0.3,0.5],
                          [0.2,0.3,0.5],
                          [0.2,0.3,0.5]])
    result = read_img_to_BGR(img_array)
    # Assert that balck and white img array is concatenated to 3 layers
    assert np.isclose(len(result.shape),3), "Unexpected result from test"
    # Assert that balck and white img array is concatenated correctly
    assert np.allclose(result[0],result[1]), "Unexpected result from test"
    assert np.allclose(result[0],result[2]), "Unexpected result from test"    
    return
