import argparse
import os
import csv

files = []

def create_file():
    with open('dataset.csv', 'w', encoding='UTF8') as f:
        write = csv.writer(f)
        row = ""
        header = ['file', 'text']
        write.writerow(header)

        files.sort()

        for file in files:
            label = file.split('_')[0].lower().strip(" ")
            row = [f'./dataset/{file}', label]

            write.writerow(row)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate csv file from audios")
    parser.add_argument('audio_dir', metavar='A', type=str,
            help="Audio's directory")

    args = parser.parse_args()
    files = os.listdir(args.audio_dir)

    print(f'Se creará un csv con {len(files)} filas')

    create_file()
