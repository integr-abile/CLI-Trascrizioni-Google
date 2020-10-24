import argparse
from pydub import AudioSegment
import sys
import os
import pdb
import requests
import base64
import json

def pathToBase64(path):
    f = open(path,'rb')
    file_data = f.read()
    return base64.b64encode(file_data)

def languageCodeFromAbbr(lang_abbr):
    if lang_abbr == 'it':
        return 'it-IT'
    elif lang_abbr == 'eng':
        return 'en-US'
    else:
        return 'it-IT' #default

g_transcription_google_url = "https://speech.googleapis.com/v1/speech:recognize?key=AIzaSyAVi14pKukZ8bqNqIaEqCEgr93mmyRMn_E"

slice_time_msec = 60 * 1000
audiofilepart_paths = []
tmp_audiofileparts_dir = "tmp_audio"

parser = argparse.ArgumentParser()
parser.add_argument("fileaudio_path_wav",help="Path del file audio .wav che si vuole trascrivere")
parser.add_argument("--lang", help="Lingua del file audio da trascrivere (it, eng). Default: italiano",default="it-IT")
args = parser.parse_args()

audiofile_path = args.fileaudio_path_wav
audiofile_name = os.path.basename(audiofile_path)
print(f"input -> {audiofile_name}")
audiofile_name_parts = audiofile_name.split(".")
if len(audiofile_name_parts) <= 1:
    sys.stderr.write("Assicurarsi di aver passato un nome file valido")
    sys.exit()

if len(audiofile_name_parts) > 1 and audiofile_name_parts[1] != "wav":
    sys.stderr.write("Il file di input dev'essere in formato WAV")
    sys.exit()

try:
    rec = AudioSegment.from_wav(audiofile_path)
    print(rec)

    if rec.duration_seconds > 60:
        if os.path.exists(tmp_audiofileparts_dir) == False:
            os.mkdir(tmp_audiofileparts_dir)
        rec_copy = rec
        part = 0
        while rec_copy.duration_seconds > 0:
            part_audio = rec_copy[:slice_time_msec] if rec_copy.duration_seconds > 60 else rec_copy[:]
            part_path = f"{tmp_audiofileparts_dir}/p{part}.wav"
            part_audio.export(part_path,format="wav")
            audiofilepart_paths.append(part_path)
            rec_copy = rec_copy[len(part_audio):] #ms
            part += 1
        part = 0
    else: #audio in input di durata < 1 minuto
        audiofilepart_paths.append(audiofile_path)
    
    base64EncodedFiles = map(pathToBase64,audiofilepart_paths)
    # pdb.set_trace()
    # pdb.set_trace()
    for idx,fileBase64 in enumerate(base64EncodedFiles):
        requestPayload = """
        {"config":{"encoding":"LINEAR16","sampleRateHertz":%d,"languageCode":"%s"},
                            "audio":{"content":"%s"}
                        }
        """ % (rec.frame_rate,languageCodeFromAbbr(args.lang),fileBase64.decode('UTF-8'))
        # pdb.set_trace()
        jsonPayload = json.loads(requestPayload)
        # pdb.set_trace()
        req = requests.post(g_transcription_google_url,data=requestPayload,headers={'Content-Type':'application/json'})
        # print(req.text)
except FileNotFoundError:
    sys.stderr.write("File non trovato")
    sys.exit()













