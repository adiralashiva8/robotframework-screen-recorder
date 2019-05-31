# Screen Recorder using Robotframework

Using robotframework [SeleniumCapLibrary](https://github.com/mihaiparvu/ScreenCapLibrary) we can record screen

# how to use

Step 1: Install SeleniumCapLibrary
    > `pip install --upgrade robotframework-screencaplibrary`

Step 2: Copy `ScreenRecordListener.py` to project

Step 3: Execute test case using listener
    > `robot --listener ScreenRecordListener.py <mytest>.robot`

Screen record videos will be created for each test case