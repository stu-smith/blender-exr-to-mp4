import argparse

from .output import Output


class CommandLine(object):

    def __init__(self):
        parser = argparse.ArgumentParser()

        parser.add_argument(
            '--url-format',
            required=True,
            help='Specifies the format of the URLs for the EXR files.'
        )

        parser.add_argument(
            '--start-num',
            required=True,
            help='Specifies the index of the first EXR file.'
        )

        parser.add_argument(
            '--end-num',
            required=True,
            help='Specifies the index of the last EXR file.'
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

        self.url_format = args.url_format
        self.start_num = int(args.start_num)
        self.end_num = int(args.end_num)
        self.folder = args.folder
        self.channels = args.channels.split(',')
        self.fps = int(args.fps)

        if len(self.channels) != 3:
            Output.fatal(
                '--channels must be a comma-separated list of three channels.'
            )
