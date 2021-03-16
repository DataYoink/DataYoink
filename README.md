# DataYoink <br />
DataYoink is a plot digitizer for battery discharge plots from scientific literature. Aided by the
Detectron2 software system from FAIR and powered by the PyTorch deep learning framework, DataYoink identies unique
curves on any battery discharge plot and saves the data to an easily interpretable excel file. 

Version 1 (current) utilizes a jupyter notebook-based user interface which prompts the user for basic information
about the plot area, which can be paired with our pre-trained neural network to quickly and easily extract points
from battery discharge plots. Examples have also been included for users who wish to train their own neural network.

Version 2 (in development) will improve on Version 1 by replacing the user interface with a fully automated
framework, making DataYoink much easier to run on large sets of images. Version 2 will also see improvements
to model accuracy and support expanded to a variety of different plot types (including dQ/dV)


=======

### Software dependencies
- Detectron2 (requires Linux or macOS)
- Pytorch >1.6
- OpenCV is optional but recommended if visualiztion is needed

### How to install 


### DataYoink tutorial


### Organization of repo <br />
```
|   LICENSE
|   README.md
|   requirements.txt
|   setup.py
|   datayoink.yml
|   .gitignore
|
+---docs
|   |   ComponentChart.pdf
|   |   Use_Cases.md
|   |
|   \---dev
|           ChristinaNotebook.ipynb
|
+---examples
|   |   Demo_Using_Pretrained_Mask.ipynb
|   |   Demo_Resize_and_Register_Training_Dataset.ipynb
|   |   Demo_load_NN_from_pkl.ipynb
|   |
|   +---pyfiles_for_demos
|   |   |   coordconverter.py
|   |   |   img_rescale.py
|   |   |   pointclassifier.py
|   |   |   predict.py
|   |
|   +---discharge_curve_json
|   |   |   discharge_curve (1).json
|   |   |   ...
|   |
|   +---discharge_curve_image
|   |   |   discharge_curve (1).png
|   |   |   ...
|   |
|
\---datayoink
    |   __init__.py
    |   coordconverter.py
    |   img_rescale.py
    |   predict.py
    |   register_data.py
    |
    \---tests
        |   __init__.py
        |   predict_function_and_test.ipynb
        |   test_register_data.ipynb
        |   test_coordconverter.py
        |   test_img_rescale.py
        |   test_predict.py
        |   test_register_data.py
        |
        \---test_data
            |   test_config.pkl
            |   test_png.png
            |   test_predict.pkl
            |
            \---test_json
                    test_json1.json
                    test_json2.json


```
### Input Requirements


### Have any issues or suggestions?
We'd love to hear your input! We are planning to release version 2 later this year
with support for different types of plots, a more accurate model, and less reliance
on user input with the goal of making this a flexible tool that can be applied with
the push of a button. If there are any features that you would like to see in version 2
or suggestions for improving the current features, please let us know by submitting
an issue on github.

