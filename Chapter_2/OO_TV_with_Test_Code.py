'''
Titulo: OO TV with Test Code

Objetivo: Hacer una clase mas compleja.
'''

class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        # Some default list of channels
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0 # constante
        self.VOLUME_MAXIMUM = 10 # constante
        self.volume = int(self.VOLUME_MAXIMUM / 2) # Integer divide


    def power(self):
        self.isOn = not self.isOn # toggle

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False # Changing volume while muted unmutes
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume += 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume > self.VOLUME_MINIMUM:
            self.volume -= 1

    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex += 1
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0 # Wraps around to the first channel

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex -= 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)
        # if the newChannel is not in our list, don't do anything

    def showInfo(self):
        print()
        print('TV Status:')
        if self.isOn:
            print('\tTV is: On')
            print(f'\t Channel is: {self.channelList[self.channelIndex]}')
            if not self.isMuted:
                print(f'\t Volume is: {self.volume}')
            else:
                print(f'\t Volume is: {self.volume} (sound is muted)')
        else:
            print('\tTV is: Off')

# Main code
oTV = TV() # Create the TV object

# Turn the TV on and show the status
oTV.power()
oTV.showInfo()

# Change channel up twice, raise the volumne twice, show status
oTV.channelUp()
oTV.channelUp()
oTV.volumeUp()
oTV.volumeUp()
oTV.showInfo()

# Turn the TV off, show status, turn the TV on, show status
oTV.power()
oTV.showInfo()
oTV.power()
oTV.showInfo()

# Lower the volume, mute the sound, show status
oTV.volumeDown()
oTV.mute()
oTV.showInfo()

# Change the channel to 11, mute the sound, show status
oTV.setChannel(11)
oTV.mute()
oTV.showInfo()
