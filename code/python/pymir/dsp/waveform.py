import matplotlib
matplotlib.use('Agg')
import librosa
from librosa.core import load
import matplotlib.pyplot as plt
import numpy as np

def main():
    y, sr = load('/data/audio/autum_leaves_take1.wav', duration=10)
    plt.figure()
    plt.subplot(1, 1, 1)
    librosa.display.waveplot(y, sr=sr)
    plt.title('Monophonic')
    plt.savefig('wave.png')
 
    D = librosa.logamplitude(np.abs(librosa.stft(y))**2, ref_power=np.max)
    plt.subplot(1, 2, 1)
    librosa.display.specshow(D, y_axis='linear')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Linear-frequency power spectrogram')
    plt.savefig('spectrogram.png')

if __name__ == '__main__':
    main()
