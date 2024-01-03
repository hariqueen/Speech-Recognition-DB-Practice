import os
import wave
import shutil
import text_processing as tp

__all__ = ["process_data", "process_each_file"]

def process_data(source_folders, db_folders):
    for folder in db_folders:
        wav_folder = os.path.join(folder, 'wav')
        etc_folder = os.path.join(folder, 'etc')

        with open(os.path.join(etc_folder, 'DURINFO'), 'w') as durinfo_file, \
             open(os.path.join(etc_folder, 'LANG'), 'w') as lang_file, \
             open(os.path.join(etc_folder, 'PROMPTS'), 'w') as prompts_file:

            for i in range(1, 501):
                source_file_number = 33000 + i + (1000 * (folder.index(folder) // 2))
                process_each_file(i, source_file_number, source_folders, folder, wav_folder, etc_folder, durinfo_file, lang_file, prompts_file)

def process_each_file(i, source_file_number, source_folders, folder, wav_folder, etc_folder, durinfo_file, lang_file, prompts_file):
    wav_filename = f'broadcast_{source_file_number:08}.wav'
    new_wav_filename = f'{i:05}.wav'
    txt_filename = f'broadcast_{source_file_number:08}.txt'
    source_folder = source_folders[folder.index(folder) // 2]

    try:
        shutil.copy(os.path.join(source_folder, wav_filename), os.path.join(wav_folder, new_wav_filename))
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {os.path.join(source_folder, wav_filename)}")

    try:
        with wave.open(os.path.join(wav_folder, new_wav_filename), 'rb') as wav_file:
            frames = wav_file.getnframes()
            rate = wav_file.getframerate()
            duration = frames / float(rate)
            durinfo_file.write(f'{folder}/wav/{i:05}.wav\t{duration:.2f}\n')
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {os.path.join(wav_folder, new_wav_filename)}")

    try:
        with open(os.path.join(source_folder, txt_filename), 'r') as txt_file:
            text = txt_file.read().strip()
            lang_file.write(f'{folder}/wav/{i:05}.wav\t{tp.create_lang_text(text)}\n')
            prompts_file.write(f'{folder}/wav/{i:05}.wav\t{tp.create_prompts_text(text)}\n')
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {os.path.join(source_folder, txt_filename)}")
