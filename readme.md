# Screen Recorder using Robotframework

Using robotframework [SeleniumCapLibrary](https://github.com/mihaiparvu/ScreenCapLibrary) we can record screen

---
## How to use in my project

**Step 1**: Install SeleniumCapLibrary (For latest changes and fixes which are not part of current release)
 > `pip install git+https://github.com/mihaiparvu/ScreenCapLibrary.git`
 
**Step 2**: Copy `ScreenRecordListener.py` to project

**Step 3**: Execute test case using listener
 > `robot --listener ScreenRecordListener.py <mytest>.robot`

Screen record videos will be created for each test case

---
## TODO

 - Append video to log.html
    > Will implement once [this](https://github.com/mihaiparvu/ScreenCapLibrary/issues/25) issue got resolved