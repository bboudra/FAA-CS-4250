__author__ = 'redragonx/daemoniclegend'

# future home for keyboard inputs
import plane_controller.plane_controller
import re

class User_keypad():

    bullshitVar = None
    pattern = re._compile("\d{4}\#")

    def keypad_input(self, codeIn):
        new_code = codeIn
        re.match("\d{4}\#" , new_code)
        if len(new_code) == 5:
            if re.match("\d{4}\#" , new_code):
                plane_controller.plane_controller.update_transponder_code(new_code)
                return 'Success'
        else:
            return 'Fail'



    def __init__(self):
        pass
