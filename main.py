__author__ = 'Anton Glukhov'

import time
# import gst
# pygst.require("0.10")
import gi
gi.require_version('Gst', '1.0')
# from gi.repository import GObject
from gi.repository import Gst

# GObject.threads_init()
Gst.init(None)


def play():
    player = gst.Pipeline("player")
    source1 = gst.element_factory_make("filesrc", "file-source1")
    decoder1 = gst.element_factory_make("mad", "mp3-decoder1")
    conv1 = gst.element_factory_make("audioconvert", "converter1")

    output = gst.element_factory_make("alsasink", "alsa-output")

    # Create a software mixer with "Adder"
    adder = gst.element_factory_make("adder","audiomixer")

    # Gather a request sink pad on the mixer
    sinkpad1=adder.get_request_pad("sink%d")
    # sinkpad2=adder.get_request_pad("sink%d")

    player.add(source1, decoder1, conv1, adder, output)

    player.get_by_name("file-source1").set_property("location", "/home/anton/wither.mp3")
    # player.get_by_name("file-source2").set_property("location", "/home/anton/love.mp3")

    gst.element_link_many(source1, decoder1, conv1)
    # gst.element_link_many(source2, decoder2, conv2)

    conv_src1 = conv1.get_pad("src")
    # conv_src2 = conv2.get_pad("src")

    conv_src1.link(sinkpad1)
    # conv_src2.link(sinkpad2)

    adder.link(output)

    player.set_state(gst.STATE_PLAYING)

    time.sleep(2)

    print player.query_duration(gst.FORMAT_TIME, None)

    source2 = gst.element_factory_make("filesrc", "file-source2")
    decoder2 = gst.element_factory_make("mad", "mp3-decoder2")
    conv2 = gst.element_factory_make("audioconvert", "converter2")

    sinkpad2 = adder.get_request_pad("sink%d")

    player.add(source2, decoder2, conv2)

    player.get_by_name("file-source2").set_property("location", "/home/anton/test.mp3")
    # volume = gst.element_factory_make("volume")
    # volume.set_property("volume", 0.5)

    gst.element_link_many(source2, decoder2, conv2)

    conv_src2 = conv2.get_pad("src")

    conv_src2.link(sinkpad2)

    player.set_state(gst.STATE_PLAYING)

    time.sleep(2)

    print conv_src1.is_blocked()

    source1.set_state(gst.STATE_NULL)
    conv_src1.unlink(sinkpad1)
    adder.release_request_pad(sinkpad1)
    # del(source1)

    while True:
        print source2.get_state()
        # print conv_src1.query_position(gst.FORMAT_TIME, None)
        print conv_src2.query_position(gst.FORMAT_TIME, None)
        print conv_src2.query_duration(gst.FORMAT_TIME, None)
        format = gst.Format(gst.FORMAT_TIME)
        duration_nanosecs = conv_src2.query_duration(format)[0]
        print duration_nanosecs
        # print datetime.datetime.fromtimestamp(duration_nanosecs / gst.SECOND)

        # datetime.datetime.fromtimestamp(conv_src2.query_duration(gst.FORMAT_TIME, None)).strftime('%Y-%m-%d %H:%M:%S')

        # nanosecs, format = source1.query_position(gst.FORMAT_TIME)
        # datetime.datetime(seconds=(duration / gst.SECOND))
        # print player.query_position(gst.FORMAT_TIME, None)
        # print sinkpad2.query_duration()
        time.sleep(2)
        pass


def testmultipipeline():

    player1 = gst.Pipeline("player1")
    source1 = gst.element_factory_make("filesrc", "file-source")
    decoder1 = gst.element_factory_make("mad", "mp3-decoder")
    conv1 = gst.element_factory_make("audioconvert", "converter")
    sink1 = gst.element_factory_make("alsasink", "alsa-output")

    player1.add(source1, decoder1, conv1, sink1)
    gst.element_link_many(source1, decoder1, conv1, sink1)

    player1.get_by_name("file-source").set_property("location", "/home/anton/love.mp3")
    player1.set_state(gst.STATE_PLAYING)

    time.sleep(1)

    player2 = gst.Pipeline("player2")
    source2 = gst.element_factory_make("filesrc", "file-source")
    decoder2 = gst.element_factory_make("mad", "mp3-decoder")
    conv2 = gst.element_factory_make("audioconvert", "converter")
    sink2 = gst.element_factory_make("alsasink", "alsa-output")

    player2.add(source2, decoder2, conv2, sink2)
    gst.element_link_many(source2, decoder2, conv2, sink2)

    player2.get_by_name("file-source").set_property("location", "/home/anton/love.mp3")
    player2.set_state(gst.STATE_PLAYING)

    time.sleep(1)

    player3 = gst.Pipeline("player3")
    source3 = gst.element_factory_make("filesrc", "file-source")
    decoder3 = gst.element_factory_make("mad", "mp3-decoder")
    conv3 = gst.element_factory_make("audioconvert", "converter")
    sink3 = gst.element_factory_make("alsasink", "alsa-output")

    player3.add(source3, decoder3, conv3, sink3)
    gst.element_link_many(source3, decoder3, conv3, sink3)

    player3.get_by_name("file-source").set_property("location", "/home/anton/love.mp3")
    player3.set_state(gst.STATE_PLAYING)

    time.sleep(1)

    player4 = gst.Pipeline("player4")
    source4 = gst.element_factory_make("filesrc", "file-source")
    decoder4 = gst.element_factory_make("mad", "mp3-decoder")
    conv4 = gst.element_factory_make("audioconvert", "converter")
    sink4 = gst.element_factory_make("alsasink", "alsa-output")

    player4.add(source4, decoder4, conv4, sink4)
    gst.element_link_many(source4, decoder4, conv4, sink4)

    player4.get_by_name("file-source").set_property("location", "/home/anton/love.mp3")
    player4.set_state(gst.STATE_PLAYING)

    time.sleep(1)

    player5 = gst.Pipeline("player5")
    source5 = gst.element_factory_make("filesrc", "file-source")
    decoder5 = gst.element_factory_make("mad", "mp3-decoder")
    conv5 = gst.element_factory_make("audioconvert", "converter")
    sink5 = gst.element_factory_make("alsasink", "alsa-output")

    player5.add(source5, decoder5, conv5, sink5)
    gst.element_link_many(source5, decoder5, conv5, sink5)

    player5.get_by_name("file-source").set_property("location", "/home/anton/love.mp3")
    player5.set_state(gst.STATE_PLAYING)


def testmixtune():
    player = gst.Pipeline("player")
    sink = gst.element_factory_make("alsasink", "alsa-output")

    # Create a software mixer with "Adder"
    adder = gst.element_factory_make("adder","audiomixer")
    player.add(adder)

    # Gather a request sink pad on the mixer
    sinkpad1=adder.get_request_pad("sink%d")
    sinkpad2=adder.get_request_pad("sink%d")

    buzzer1 = gst.element_factory_make("audiotestsrc","buzzer1")
    buzzer1.set_property("freq",1000)
    player.add(buzzer1)

    buzzersrc1=buzzer1.get_pad("src")
    buzzersrc1.link(sinkpad1)

    buzzer2 = gst.element_factory_make("audiotestsrc","buzzer2")
    buzzer2.set_property("freq",500)
    player.add(buzzer2)

    buzzersrc2=buzzer2.get_pad("src")
    buzzersrc2.link(sinkpad2)

    player.add(sink)
    adder.link(sink)


def testtune():
    pipeline = gst.Pipeline("mypipeline")

    audiotestsrc = gst.element_factory_make("audiotestsrc", "audio")
    pipeline.add(audiotestsrc)

    sink = gst.element_factory_make("alsasink", "sink")
    pipeline.add(sink)

    audiotestsrc.link(sink)

    pipeline.set_state(gst.STATE_PLAYING)

    while True:
        pass


def play_10():
    pipe = Gst.Pipeline()
    # source = Gst.ElementFactory()
    src = Gst.ElementFactory.make("filesrc", "src")
    decoder = Gst.ElementFactory.make("mad", "mp3-decoder1")
    conv = Gst.ElementFactory.make("audioconvert", "converter1")
    volume = Gst.ElementFactory.make("volume", "volume")
    output = Gst.ElementFactory.make("alsasink", "alsa-output")

    [pipe.add(k) for k in [src, decoder, conv, volume, output]]

    # pipe.add(src)
    # pipe.add(decoder)
    # pipe.add(conv)
    # pipe.add(volume)
    # pipe.add(output)
    src.set_property("location", "/home/anton/wither.mp3")
    volume.set_property("volume", 0.2)

    src.link(decoder)
    decoder.link(conv)
    conv.link(volume)
    volume.link(output)

    pipe.set_state(Gst.State.PLAYING)

    time.sleep(1)
    volume.set_property("volume", 0.6)
    time.sleep(1)
    volume.set_property("volume", 0.7)
    time.sleep(1)
    volume.set_property("volume", 0.8)
    time.sleep(1)
    volume.set_property("volume", 0.9)
    time.sleep(1)
    volume.set_property("volume", 1.0)

    for i in range(0,10):


    while True:
        pass




if __name__ == "__main__":
    play_10()