"""Python serial number generator.
The class Serial Generator is hoing to generate a serial number beginning from teh starting number the user provides
"""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=1):
        self.start = start
        self.next_num = start

    def generate(self):
        """
        The generate function returns the initial numbel on the start
        On all other instances it will start giving the next number  in a sequence of 1 on 1
        """
        if self.next_num == self.start:
            self.next_num = self.next_num + 1
            return self.start
        else:
            next_num = self.next_num
            self.next_num = self.next_num + 1
            return next_num

    def reset(self):
        """
        The reset function returns the "net_num" to the starting number, reseting the sequence
        """
        self.next_num = self.start
