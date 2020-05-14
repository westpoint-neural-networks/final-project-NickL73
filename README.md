# Ahead of the Game: Coaching Predictability in NCAA Football

This GitHub repository houses an neural-network based application that could be used to predict which play Lincoln Riley, head coach of the Oklahoma Sooners, is about to call in an NCAA football game. In testing, we found it to have greater than 60% accuracy in correctly predicting whether Lincoln Riley would call a pass or a run play.

The models used in this application were trained in Google Colaboratory, and the notebooks can be found in the 'notebooks' folder in this repository. Alternatively, you can just go directly to the [Colab](https://colab.research.google.com/drive/1ITENEu7jQ-3Hox3Mxr-TRgueKHElmwCH#offline=true&sandboxMode=true) notebook.

This application uses data scraped from [collegefootballdata.com](collegefootballdata.com), which may contain inaccuracies beyond my control.

## Requirements
To run this application, you will need to have several Python modules loaded into your environment. If you do not already have it, you will need to [install pip](https://pip.pypa.io/en/stable/installing/) first to actually install the rest of the dependencies.

To install all of the dependencies, navigate to the project folder in a command prompt. At this point, I recommend making a new virtual Python environment, but it is not required. Next, type the following command:

`$ pip install -r requirements.txt`

 After executing this command, your Python environment should be able to execute the application.
 
 **NOTE: If you do not create a new virtual environment, some of the versions installed from the requirements.txt file may replace other versions you might have and cause conflicts in other projects. To ensure you don't break other projects, consider [creating](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) a new virtual environment.** 

## Launching the Application
Once all required dependencies have been installed, you can use the application. To launch the application, open a command prompt and navigate to the application's directory. If you're using a virtual environment, be sure to activate it at this point.

In the command prompt, type the following command to launch to the application:

`$ python app.py`

## Using the Application
Using the application is pretty self explanatory. Simply enter values corresponding to a certain situation in an Oklahoma football game and click the button to get the play prediction. The only valid entries are integers, so if you enter in anything other than a letter there would be no new prediction. To close the application, either click the red 'X' in the top right corner or kill the script from the command prompt.