import soundfile as sf
import numpy as np
import argparse
import os

arr_audios = []
arr_noises = []
arr_prefix = []

def create_audio(arr_main, arr_bg):
    if arr_main.shape[0] > arr_bg.shape[0]:
        diff = abs(arr_main.shape[0] - arr_bg.shape[0])
        arr_bg = np.concatenate((arr_bg, np.zeros((diff, 2))))
    elif arr_main.shape[0] < arr_bg.shape[0]:
        diff = arr_bg.shape[0] - arr_main.shape[0]
        arr_bg = arr_bg[:-diff]

    return np.add(arr_main, arr_bg)

def write_file(arr_out, aud_path, path, name, samplerate, i, sufix):
    out_name = os.path.splitext(f'{aud_path}/{name}')[0].split('/')[-1]
    sf.write(f'{path}/{out_name}_{sufix}_{i}.wav', arr_out, samplerate)
    print(f'Archivo {out_name}_{sufix}_{i}.wav creado.')

def creating_audios(aud_path, no_path, out_path, name):
    for audio in arr_audios:
        ind = 0
        for noise in arr_noises:
            arr_au, samplerate_au = sf.read(f'{aud_path}/{audio}')
            arr_no, _ = sf.read(f'{no_path}/{noise}')

            arr_out = create_audio(arr_au, arr_no)
            write_file(arr_out, aud_path, out_path, audio,
                        samplerate_au, ind, name)
            ind += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add noise to wav audios.')
    parser.add_argument('noise_dir', metavar='N', type=str,
                        help="Noise's audio directory")
    parser.add_argument('audio_dir', metavar='A', type=str,
                        help="Audio's to add noise directory")
    parser.add_argument('output_dir', metavar='R', type=str,
                        help="Audio's output directory")

    args = parser.parse_args()
    arr_prefix = os.listdir(args.audio_dir)
    arr_noises = os.listdir(args.noise_dir)

    for ad in arr_prefix:
        arr_audios = os.listdir(f'{args.audio_dir}/{ad}')
        creating_audios(f'{args.audio_dir}/{ad}', args.noise_dir, args.output_dir, ad)

