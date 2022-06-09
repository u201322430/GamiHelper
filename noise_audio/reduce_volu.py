import soundfile as sf
import numpy as np
import sys

if __name__ == '__main__':
    reduce_vol = float(sys.argv[1]) # Cantidad a reducir el volumen
    name_output = sys.argv[2] # Nombre del archivo de salida
    file = sys.argv[3] # Nombre del archivo al cual se le bajara el volumen

    inp, samplerate = sf.read(file)

    print(f"Average {file}:", np.average(inp))

    def my_func(x):
        if type(x) != type(0):
            return x/reduce_vol

    out = np.apply_along_axis(my_func, -2, inp)

    print(f"Average ouput:", np.average(out))

    sf.write(name_output, out, samplerate)
