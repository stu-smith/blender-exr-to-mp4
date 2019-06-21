# blender-exr-to-mp4

Converts a ZIP of Blender EXR files into an MP4 video.

Why do we need to do this? When using network rendering, the final output is a ZIP of EXR files.
Unfortunately, those EXR files are multi-channel, and cannot be easily converted to an MP4,
either with Blender, or with ffmpeg.

Currently this utility is Windows-only.

I have included a custom WHL file from: https://www.lfd.uci.edu/~gohlke/pythonlibs/

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