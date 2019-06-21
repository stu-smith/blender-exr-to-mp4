import os
from .command_line import CommandLine
from .output import Output
from .windows_processor import WindowsProcessor
from .converter import Converter


def main():
    command_line = CommandLine()

    zip_url = command_line.url
    working_dir = command_line.folder
    channels = command_line.channels

    Output.title('Starting EXR to MP4 conversion')
    Output.info('ZIP URL       : ' + zip_url)
    Output.info('Working folder: ' + working_dir)
    Output.info('Channels      : ' + ','.join(channels))

    processor = WindowsProcessor(working_dir)

    processor.ensure_ffmpeg()
    processor.ensure_download_file(zip_url, 'exrs.zip')
    processor.ensure_unzip('exrs.zip', 'exrs')

    Output.title('Converting EXR files')

    pngs_dir = os.path.join(working_dir, 'pngs')
    exrs_dir = os.path.join(working_dir, 'exrs')

    if not os.path.exists(pngs_dir):
        os.makedirs(pngs_dir)

    exr_files = os.listdir(exrs_dir)

    Output.info('Found {} EXR files for processing.'.format(len(exr_files)))

    for exr_file in exr_files:
        exr_path = os.path.join(exrs_dir, exr_file)
        png_path = os.path.join(
            pngs_dir, os.path.splitext(exr_file)[0] + '.png')

        if os.path.isfile(png_path):
            Output.info('Already done {}, skipping...'.format(exr_file))
        else:
            Output.info('Processing {}...'.format(exr_file))

            Converter.convert(
                os.path.join(exr_path),
                png_path,
                channels
            )

    Output.title('Process complete!')
    Output.info('Done.')
    Output.info('')


if __name__ == '__main__':
    main()
