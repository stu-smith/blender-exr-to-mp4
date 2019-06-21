# blender-exr-to-mp4

Converts a ZIP of Blender EXR files into an MP4 video.

Why do we need to do this? When using Blender network rendering, the final output is a ZIP of EXR files.
Unfortunately, those EXR files are multi-channel, and cannot be easily directly converted to an MP4,
either with Blender, or with ffmpeg.

This utility handles the entire workflow: downloading ffmpeg, downloading the ZIP, extracting,
converting the EXRs to PNGs (with appropriate gamma-correction), and converting the PNGs to lossless MP4.

Current limitations:

* Windows-only;
* Only creates lossless H.264 videos;
* Fixed gamma correction.

None of the above limitations would be very difficult to fix; however I just don't have time right now.
If you do fix them, please send a pull request and I'll be very grateful!



## Installation

You will need Python 3.7 installed.

```
pip install pipenv
pipenv install
```


## Using the utility

```
pipenv run python -m src.main --url <url-of-zip> --folder <working folder>
```

Example: my Blender network render master is at `192.168.0.200`, and I want to convert job 1:

```
pipenv run python -m src.main --url http://192.168.0.200:8000/result_1.zip --folder C:\temp\job_1
```



## Acknowledgements

* The Windows OpenEXR library is taken from: https://www.lfd.uci.edu/~gohlke/pythonlibs/
* Video encoding is handled by ffmpeg: https://ffmpeg.org/
* Much of the conversion code was taken from: https://gist.github.com/drakeguan/6303065
* PNG output is handled by Pillow: https://pillow.readthedocs.io/en/stable/

