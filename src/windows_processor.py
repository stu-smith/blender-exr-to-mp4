import os
import tempfile
import zipfile
from urllib.request import Request, urlopen

from .output import Output


class WindowsProcessor(object):
    def __init__(self, working_dir):
        self._working_dir = working_dir

        if not os.path.exists(self._working_dir):
            os.makedirs(self._working_dir)

    def ensure_ffmpeg(self):
        ffmpeg_url = self.get_ffmpeg_url()
        temp = tempfile.gettempdir()

        self.ensure_download_file(ffmpeg_url, 'ffmpeg.zip', temp)
        self.ensure_unzip('ffmpeg.zip', 'ffmpeg', temp)

    def get_ffmpeg_url(self):
        return 'https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-4.1.3-win64-static.zip'

    def get_exr_filename(self, num):
        return'input-%d.exr' % num

    def ensure_download_file(self, url, file, dir=None):
        Output.title('Ensuring ' + file + '...')
        Output.info('Need: ' + url)

        if not dir:
            dir = self._working_dir

        path = os.path.join(dir, file)

        Output.info('At  : ' + path)

        if os.path.isfile(path):
            Output.checkpoint('Already exists, no work to do.')
        else:
            Output.info('Does not exist, need to download...')
            req = Request(url, headers={'User-Agent': 'blender-exr-to-mp4'})

            data = urlopen(req).read()

            with open(path, 'wb') as f:
                f.write(data)

            Output.checkpoint('Download complete.')

    def ensure_unzip(self, zip_file, folder, dir):
        Output.title('Ensuring ' + folder + '...')

        if not dir:
            dir = self._working_dir

        zip_path = os.path.join(dir, zip_file)
        folder_path = os.path.join(dir, folder)

        Output.info('Need: ' + folder_path)
        Output.info('From: ' + zip_path)

        if os.path.exists(folder_path):
            Output.checkpoint('Already exists, no work to do.')
        else:
            Output.info('Does not exist, need to extract...')

            zip_ref = zipfile.ZipFile(zip_path, 'r')
            zip_ref.extractall(folder_path)
            zip_ref.close()

            Output.checkpoint('Extract complete.')

    def encode_to_video(self, fps):
        temp = tempfile.gettempdir()
        cmd = '{} -r {} -i "{}" -c:v libx264 -preset veryslow -crf 0 -y "{}"'.format(
            os.path.join(temp, 'ffmpeg',
                         'ffmpeg-4.1.3-win64-static', 'bin', 'ffmpeg.exe'),
            fps,
            os.path.join(self._working_dir, 'pngs', 'input-%d.png'),
            os.path.join(self._working_dir, 'output.mp4')
        )

        Output.info('Running: ' + cmd)

        os.system(cmd)
