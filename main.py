import os
import sys
from pydub import AudioSegment


def transfer_any_audio_types(filepath, input_audio_type, output_audio_type):
    song = AudioSegment.from_file(filepath, input_audio_type)
    filename = filepath.split(".")[0]
    song.export(f"{filename}.{output_audio_type}", format=f"{output_audio_type}")


def transfer_all_files(files_path, output_audio_type="mp3"):
    for file_path in os.listdir(files_path):
        modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
        datapath = os.path.join(modpath, files_path + file_path)
        input_audio = os.path.splitext(datapath)
        if ".DS_Store" in input_audio[0]:
            continue
        song = AudioSegment.from_file(datapath, input_audio[-1].split(".")[-1])
        print(f"converting {input_audio[0]}")
        song.export(f"{input_audio[0]}.{output_audio_type}".replace("origin", "converted"), format=output_audio_type)
        print(f"{input_audio[0]} converted")


if __name__ == '__main__':
    transfer_all_files("./origin/")
