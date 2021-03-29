import os
import shutil

wav_root = '../wav/'
METHOD = ['natural', 'world', 'nsf', 'qppwg', 'usfgan']
SPK = ['bdl', 'clb', 'rms', 'slt']
N_SET = 15
N_DATA_PER_SPK = 4

for n_set in range(N_SET):
    file_paths = []
    for method in METHOD:
        os.makedirs(f'wav/set{n_set + 1}/{method}', exist_ok=True)
        files = []
        for spk in SPK:
            for n_data in range(N_DATA_PER_SPK):
                data_number = n_set * N_DATA_PER_SPK + n_data + 474
                file_path = f'{method}/{spk}_arctic_b{data_number:0>4}.wav'
                new_file_path = shutil.copyfile(wav_root + file_path, f'wav/set{n_set + 1}/' + file_path)
                files += [new_file_path]
                if method != 'natural':
                    for scale in [2.00, 0.50]:
                        file_path = f'{method}/{spk}_arctic_b{data_number:0>4}_f{scale:.2f}.wav'
                        new_file_path = shutil.copyfile(wav_root + file_path, f'wav/set{n_set + 1}/' + file_path)
                        files += [new_file_path]
        with open(f'wav/set{n_set + 1}/{method}.list', mode='w') as f:
            for file_path in sorted(files):
                f.write(file_path + '\n')