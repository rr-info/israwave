# israwave

Mission to create a Hebrew TTS model as powerful and user-friendly as WaveNet

## Features

- Generate sentence in less than 1ms on CPU
- Powerful text processor by espeak-ng
- Support for SSML (soon)

## Play with it!

You can play with it on [HuggingFace Space](https://huggingface.co/spaces/thewh1teagle/tts-with-israwave)

## Samples

https://github.com/user-attachments/assets/3212a800-406f-4d79-8aa1-d814eed815d6

## Setup

```console
python -m venv israwave
cd israwave
source bin/activate     # on linux
scripts\activate.bat    # on windows
pip install -U israwave
# for windows:  [`wget` can be found here](https://eternallybored.org/misc/wget/1.21.4/64/wget.exe)
wget https://github.com/thewh1teagle/israwave/releases/download/v0.1.0/israwave.onnx
wget https://github.com/thewh1teagle/israwave/releases/download/v0.1.0/nakdimon.onnx
wget https://github.com/thewh1teagle/israwave/releases/download/v0.1.0/espeak-ng-data.tar.gz
tar xzf espeak-ng-data.tar.gz
```

You also need [`israwave.onnx`](https://github.com/thewh1teagle/israwave/releases/download/v0.1.0/israwave.onnx), [`espeak-ng-data`](https://github.com/thewh1teagle/israwave/releases/download/v0.1.0/espeak-ng-data.tar.gz), and [`nakdimon.onnx`](https://github.com/thewh1teagle/israwave/releases/download/v0.1.0/nakdimon.onnx). Please see examples.

## Examples

See [examples](examples)

### examples usage:
(assuming "play.py" or "save.py" are copied to the virtual environment root dir)
```
source bin/activate     # for linux.  On windows: scripts\activate.bat   
python play.py israwave.onnx espeak-ng-data nakdimon.onnx "דוגמא להשמעה מיידית"
python save.py israwave.onnx espeak-ng-data nakdimon.onnx "דוגמא לשמירת קובץ שמע" output.mp3
```


## Dataset

The model trained on [saspeech gold standard](https://openslr.org/134/).

## Thanks

Thanks to [Kan11](https://www.kan.org.il/) and [Shaul](https://www.kan.org.il/authors/%D7%A9%D7%90%D7%95%D7%9C-%D7%90%D7%9E%D7%A1%D7%98%D7%A8%D7%93%D7%9E%D7%A1%D7%A7%D7%99/) for providing the dataset.

Thanks to [elazarg](https://github.com/elazarg) for sharing the [Nakdimon](https://github.com/elazarg/nakdimon) diacritics model, which was instrumental in our project.

For [mush42](https://github.com/mush42) for their excellent TTS training recipe.
