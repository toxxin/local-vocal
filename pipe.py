import gst

__author__ = 'Anton Glukhov'

from track import Track

class Pipe():

    uid = 0

    tracks = []

    def __init__(self):
        pipe = gst.Pipeline("pipe")

        # Create a software mixer with "Adder"
        self.adder = gst.element_factory_make("adder","audiomixer")

        self.output = gst.element_factory_make("alsasink", "alsa-output")

        pass

    def add(self, track):

        sinkpad1 = self.adder.get_request_pad("sink%d")

        self.volume = gst.element_factory_make("volume")
        pass

    # def

    def play(self):
