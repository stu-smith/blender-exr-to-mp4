import os
from .command_line import CommandLine
from .output import Output
from .windows_processor import WindowsProcessor
from .converter import Converter


def main():
    command_line = CommandLine()

    url_format = command_line.url_format
    start_num_exr = command_line.start_num
    end_num_exr = command_line.end_num
    working_dir = command_line.folder
    channels = command_line.channels
    fps = command_line.fps

    Output.title('Starting EXR to MP4 conversion')
    Output.info('EXR URL format: ' + url_format)
    Output.info('EXR indexes   : ' + str(start_num_exr) + '...' + str(end_num_exr))
    Output.info('Working folder: ' + working_dir)
    Output.info('Channels      : ' + ','.join(channels))
    Output.info('FPS           : ' + str(fps))

    pngs_dir = os.path.join(working_dir, 'pngs')
    exrs_dir = os.path.join(working_dir, 'exrs')

    if not os.path.exists(pngs_dir):
        os.makedirs(pngs_dir)
    if not os.path.exists(exrs_dir):
        os.makedirs(exrs_dir)

    processor = WindowsProcessor(working_dir)

    processor.ensure_ffmpeg()

    Output.title('Downloading EXRs')

    for exr_i in range(start_num_exr, end_num_exr + 1):
        exr_url = url_format % exr_i
        exr_filename = processor.get_exr_filename(exr_i)
        processor.ensure_download_file(exr_url, os.path.join(exrs_dir, exr_filename))

    Output.title('Converting EXR files')

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

    Output.title('Encoding video')
    processor.encode_to_video(fps)

    Output.title('Process complete!')
    Output.info('Done.')
    Output.info('')


if __name__ == '__main__':
    main()
