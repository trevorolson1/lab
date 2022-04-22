class Television:
    """
    A class representing the Television Objects
    """

    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self, chan=MIN_CHANNEL, vol=MIN_VOLUME, stat=False):
        self.chan = chan
        self.vol = vol
        self.stat = stat
        """
        Constructor to create the initial state of the Television object
        :param chan: Television Channel.
        :param vol: Television Volume.
        :param stat: Television power status.
        """

    def power(self):
        if self.stat == False:
            self.stat = True
        else:
            self.stat = False
        """
        Method to turn the Television on or off.
        """
        pass

    def channel_up(self):
        if self.stat == True:
            if self.chan == self.MAX_CHANNEL:
                self.chan = self.MIN_CHANNEL
            else:
                self.chan += 1

        """
        Method to change channel up, loops to minimum channel if at maximum channel.
        """
        pass

    def channel_down(self):
        if self.stat == True:
            if self.chan == self.MIN_CHANNEL:
                self.chan = self.MAX_CHANNEL
            else:
                self.chan -= 1
        """
        - Method to change channel down, loops to max channel if at min channel.
        """
    def volume_up(self):
        if self.stat == True:
            if self.vol == self.MAX_VOLUME:
                return
            else:
                self.vol += 1
        """
        Method to turn the volume up, if at max volume, the volume value does not change.
        """

    def volume_down(self):
        if self.stat == True:
            if self.vol == self.MIN_VOLUME:
                return
            else:
                self.vol -= 1
        """
        Method to turn volume down, if at min volume, the volume value does not change.
        """

    def __str__(self):
        """
        Method to return the TV status using the format shown.
        :return: TV Status
        """
        return "TV status: Is on = {}, Channel = {}, Volume = {}".format(self.stat, self.chan, self.vol)  # TV status: Is on = True, Channel = 0, Volume = 0


