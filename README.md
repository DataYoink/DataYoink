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

To fully utilize DataYoink and the corresponding examples, clone this repository and from the root directory run:
```
conda env create -f datayoink.yml
```

This will install all packages necessary for DataYoink except for Detectron2.

To install Detectron2, make sure to be in the newly created DataYoink environment.

In the active environment, run:

```
ipython kernel install --user --name=DataYoink
````
This creates a unique kernel for DataYoink.

##### Installing Detectron2

Note: gcc & g++ ≥ 5.4 are required to install and utilize Detectron2. [ninja](https://ninja-build.org/) is recommended for faster build. After having them, run:

```
python -m pip install 'git+https://github.com/facebookresearch/detectron2.git'
# (add --user if you don't have permission)

# Or, to install it from a local clone:
git clone https://github.com/facebookresearch/detectron2.git
python -m pip install -e detectron2

# Or if you are on macOS
CC=clang CXX=clang++ ARCHFLAGS="-arch x86_64" python -m pip install ......
```
To rebuild detectron2 that's built from a local clone, use rm -rf build/ **/*.

or

follow [INSTALL.md](https://github.com/facebookresearch/detectron2/blob/master/INSTALL.md) provided by facebookresearch


### DataYoink tutorial

The ```examples``` folder contains jupyter notebooks with demos of how to use different
aspects of the DataYoink package:
- ```Demo_Using_Pretrained_Mask``` gives detailed steps for how to use DataYoink and Detectron2
to extract coordinate points from an image and save them in an excel file. Remember to download the [pretrained neural network](https://drive.google.com/file/d/1nTSYiEJO9sQXS6oMbRplGWmQ0AjRs9ss/view?usp=sharing) and [configuration file](https://drive.google.com/file/d/1fYthIcfHDZEA9ygazq0KYYi7ha-I8u55/view?usp=sharing).
- ```Demo_Resize_and_Register_Training_Dataset``` gives an overview of how to train a similar
neural network using your own set of training images and create the output files from
Detectron2 requred for use in the DataYoink coordinate extraction tool.

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
|   |   ChristinaNotebook.ipynb
|   |   Dataset_Cleanup.ipynb
|   |   Demo_load_NN_from_pkl.ipynb
|   |   DorisNotebook.ipynb
|   |   Input_image_resize.ipynb
|   |   KevNotebook.ipynb
|   |   KevNotebook_Copy.ipynb
|   |   KevinDetectron2.ipynb
|   |   plot.jpg
|
+---examples
|   |   __init__.py
|   |   Demo_Using_Pretrained_Mask.ipynb
|   |   Demo_Resize_and_Register_Training_Dataset.ipynb
|   |   Demo_load_NN_from_pkl.ipynb
|   |   Test_color_1solid.png
|   |   Test_color.png
|   |   Test_bw_1solid.png
|   |   Test_bw.png
|   |
|   +---pyfiles_for_demos
|   |   |   coordconverter.py
|   |   |   img_rescale.py
|   |   |   pointclassifier.py
|   |   |   predict.py
|   |   |   register_data.py
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
+---dist
|   |   DataYoink-1.0.0-py3-none-any.whl
|   |   DataYoink-1.0.0.tar.gz
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

- DataYoink discharge curve predition neural network currently requires input images to be of the ```.png``` format.
- DataYoink functions for creating training dataset dictionary require .json annotations created by ```labelme```.


### Have any issues or suggestions?
We'd love to hear your input! We are planning to release version 2 later this year
with support for different types of plots, a more accurate model, and less reliance
on user input with the goal of making this a flexible tool that can be applied with
the push of a button. If there are any features that you would like to see in version 2
or suggestions for improving the current features, please let us know by submitting
an issue on github.

