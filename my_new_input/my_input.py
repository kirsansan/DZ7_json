"""the simple class for inputting and check strings"""


class InputAndCheckString:

    input_string: str = ""
    is_correct: bool = False
    is_empty: bool = True

    def __init__(self, input_string: str = ""):
        self.input_string = input_string
        self.is_correct = False
        self.is_empty = self.verify_empty()

    def verify_empty(self) -> bool:
        """check that string is empty or not"""
        if self.input_string == "":
            self.is_correct = False
            self.is_empty = True
            return True
        else:
            self.is_correct = True
            self.is_empty = False
            return False

    def verify_correct(self) -> bool:
        """check for something characteristic of string. for instance including only dots and minuses
        we will check and letter in string and if we will find anything else
        except minuses, spaces and dots  then we will return with False result
        """
        for letter in self.input_string:
            if letter not in ". -":
                self.is_correct = False
                return False
        self.is_correct = True
        return True

    def input_while_correct(self, in_comment: str):
        """I am going request you while you enter non-empty string
           in old version also all strings was rebuild to lowercase
        """
        self.input_string = ""
        self.is_correct = False
        while not self.is_correct:
            # print(in_comment)
            self.input_string = input(in_comment)
            self.verify_empty()  # it can change is_correct flag
            # self.input_string = self.input_string.lower()

    def input_empty(self, in_comment: str):
        """I am going request you while you enter EMPTY string
           don't ask me why customer want entering Enter only. It is a part of SOW
        """
        # self.input_string = ""
        self.is_empty = False
        while not self.is_empty:
            print(in_comment)
            self.input_string = input()
            self.verify_empty()  # it can change is_empty flag


# Block for self-testing
if __name__ == '__main__':
    test_input_string = InputAndCheckString("....1234")
    print(test_input_string.verify_correct())  # wait for False

    test_input_string.input_string = "   .- -- . "
    print(test_input_string.verify_correct())  # wait for True
