from __future__ import absolute_import

from unittest import TestCase

from plotly import exceptions
from plotly.graph_objs import Frames


class FramesTest(TestCase):

    def test_instantiation(self):

        native_frames = [{}, {'data': []}, 'foo', {'data': [], 'layout': {}}]

        Frames(native_frames)
        Frames()

    def test_string_frame(self):
        frames = Frames()
        frames.append({})
        frames.append('foobar')
        self.assertEqual(frames[1], 'foobar')
        self.assertEqual(frames.to_string(),
                         "Frames([\n"
                         "    Figure(\n"
                         "        data=Data()\n"
                         "    ),\n"
                         "    'foobar'\n"
                         "])")

    def test_non_string_frame(self):
        frames = Frames()
        frames.append({})

        with self.assertRaises(exceptions.PlotlyListEntryError):
            frames.append([])

        with self.assertRaises(exceptions.PlotlyListEntryError):
            frames.append(0)
