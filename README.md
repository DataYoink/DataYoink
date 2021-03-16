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
|   LICENSE <br />
|   README.md <br />
|   requirements.txt <br />
|   setup.py <br />
|   datayoink.yml <br />
|   .gitignore <br />
|<br />
+---docs <br />
|   |   ComponentChart.pdf <br />
|   |   Use_Cases.md <br />
|   |<br />
|   \---dev <br />
|           ChristinaNotebook.ipynb <br />
|<br />
+---examples <br />
|   |   Demo_Using_Pretrained_Mask.ipynb<br />
|   |   Demo_Resize_and_Register_Training_Dataset.ipynb<br/>
|   |   Demo_load_NN_from_pkl.ipynb<br/>
|   |<br/>
|   +---pyfiles_for_demos<br/>
|   |   |   coordconverter.py<br/>
|   |   |   img_rescale.py<br/>
|   |   |   pointclassifier.py<br/>
|   |   |   predict.py<br/>
|   |<br/>
|   +---discharge_curve_json<br/>
|   |   |   discharge_curve (1).json<br/>
|   |   |   ...<br/>
|   |<br/>
|   +---discharge_curve_image<br/>
|   |   |   discharge_curve (1).png<br/>
|   |   |   ...
|   |<br/>
|<br/>
\---datayoink<br/>
    |   __init__.py<br/>
    |   coordconverter.py<br/>
    |   img_rescale.py<br/>
    |   predict.py<br/>
    |   register_data.py<br/>
    |<br/>
    \---tests<br/>
        |   __init__.py
        |   predict_function_and_test.ipynb<br/>
        |   test_register_data.ipynb<br/>
        |   test_coordconverter.py<br/>
        |   test_img_rescale.py<br/>
        |   test_predict.py<br/>
        |   test_register_data.py<br/>
        |<br/>
        \---test_data<br/>
            |   test_config.pkl<br/>
            |   test_png.png<br/>
            |   test_predict.pkl<br/>
            |<br/>
            \---test_json<br/>
                    test_json1.json<br/>
                    test_json2.json<br/>


```
### Input Requirements


### Have any issues or suggestions?
We'd love to hear your input! We are planning to release version 2 later this year
with support for different types of plots, a more accurate model, and less reliance
on user input with the goal of making this a flexible tool that can be applied with
the push of a button. If there are any features that you would like to see in version 2
or suggestions for improving the current features, please let us know by submitting
an issue on github.

