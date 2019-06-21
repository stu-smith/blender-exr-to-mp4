import argparse

from .output import Output


class CommandLine(object):

    def __init__(self):
        parser = argparse.ArgumentParser()

        parser.add_argument(
            '--url',
            required=True,
            help='Specifies the URL of the ZIP containing the EXR files.'
        )

        parser.add_argument(
            '--folder',
            required=True,
            help='Specifies the working folder where the conversion will take place.'
        )

        parser.add_argument(
            '--channels',
            required=False,
            default='Combined.Combined.R,Combined.Combined.G,Combined.Combined.B',
            help='Specifies the three channels that will be used to extract RGB information.'
        )

        parser.add_argument(
            '--fps',
            required=False,
            default='24',
            help='Specifies the video frame-rate.'
        )

        args = parser.parse_args()

        self.url = args.url
        self.folder = args.folder
        self.channels = args.channels.split(',')
        self.fps = args.fps

        if len(self.channels) != 3:
            Output.fatal(
                '--channels must be a comma-separated list of three channels.'
            )
