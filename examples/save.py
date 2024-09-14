"""
pip install -U israwave
wget https://github.com/thewh1teagle/israwave/releases/download/v0.1.0/israwave.onnx
wget https://github.com/thewh1teagle/israwave/releases/download/v0.1.0/nakdimon.onnx
wget https://github.com/thewh1teagle/israwave/releases/download/v0.1.0/espeak-ng-data.tar.gz
tar xf espeak-ng-data.tar.gz

python save.py israwave.onnx espeak-ng-data nakdimon.onnx "תגידו, גנבו לכם פעם את האוטו ופשוט ידעתם שאין טעם להגיש תלונה במשטרה?" output.wav
"""

from israwave import IsraWave
from nakdimon_ort import Nakdimon
import sys

if __name__ == '__main__':
    speech_model_path, espeak_data_path = sys.argv[1], sys.argv[2]
    niqqud_model_path, text, out_path = sys.argv[3], sys.argv[4], sys.argv[5]
    
    speech_model = IsraWave(speech_model_path, espeak_data_path)
    niqqud_model = Nakdimon(niqqud_model_path)
    text = niqqud_model.compute(text)
    waveform = speech_model.create(text)
    waveform.save(out_path)
