from robot.libraries.BuiltIn import BuiltIn

class ScreenRecordListener:

    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        self.PRE_RUNNER = 0

    def start_suite(self, data, result):

        if self.PRE_RUNNER == 0:
            BuiltIn().import_library('ScreenCapLibrary')
            self.screencaplib = BuiltIn().get_library_instance('ScreenCapLibrary')
            #BuiltIn().import_library('OperatingSystem')
            #self.operatingsystemlib = BuiltIn().get_library_instance('OperatingSystem')
            #self.outputdir = BuiltIn().get_variable_value("${OUTPUT_DIR}")

            self.PRE_RUNNER = 1

        self.test_count = len(data.tests)

    def start_test(self, data, test):
        if self.test_count != 0:
            self.test_case_name = ''.join([x.replace(' ', '_') for x in str(test)])
            self.screencaplib.start_video_recording(name=str(self.test_case_name))
    
    def end_test(self, data, test):
        if self.test_count != 0:
            self.screencaplib.stop_video_recording()

            # write a logic that when test is passed remove passed test case video
            #if str(test.status) == 'PASS':
            #    self.operatingsystemlib.remove_file(str(self.outputdir) + "/" + str(self.test_case_name) + "_1.webm")