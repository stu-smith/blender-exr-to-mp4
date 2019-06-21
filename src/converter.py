import numpy
import OpenEXR
import Imath
from PIL import Image

from .output import Output

# Portions of this cod takern from:
# https://gist.github.com/drakeguan/6303065


class Converter(object):

    @staticmethod
    def convert(input_path, output_path, channels):
        Output.info('Converting: ' + input_path + '...')

        exr = OpenEXR.InputFile(input_path)
        header = exr.header()
        pixel_type = Imath.PixelType(Imath.PixelType.FLOAT)

        available_channels = header['channels']

        for channel in channels:
            if not channel in available_channels:
                Output.info('Cannot find channel [' + channel + '].')
                Output.info('Available channels are:')

                for available_channel in available_channels:
                    Output.info('  ' + available_channel)

                Output.fatal(
                    'Use --channels <R>,<G>,<B> to choose which channels to read.'
                )

        dw = header['dataWindow']
        size = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)

        rgb = [numpy.fromstring(exr.channel(
            c, pixel_type), dtype=numpy.float32) for c in channels]

        for i in range(3):
            rgb[i] = numpy.where(
                rgb[i] <= 0.0031308,
                (rgb[i] * 12.92) * 255.0,
                (1.055 * (rgb[i] ** (1.0 / 2.4)) - 0.055) * 255.0
            )

        rgb8 = [Image.frombytes(
            'F', size, c.tostring()).convert('L') for c in rgb]

        Image.merge('RGB', rgb8).save(output_path, 'PNG')
