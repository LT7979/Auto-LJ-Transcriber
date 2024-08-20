Place all of your .wav files to be transcribed in a folder named "wavs". The folder name is just an example but that
is where the python script assumes they are. Folder structure should look like:

/Some_Directory
    | transcibe_LJ.py  
    | wavs/
        | audio000.wav
        | audio001.wav
        | ...

from here you can start the open-ai whisper API.
In this example I use Docker to run it. Installation and Documentation for the Whisper API can be found at
https://github.com/ahmetoner/whisper-asr-webservice

running the whisper API container:

sudo docker run -d --gpus all -p 9000:9000 -e ASR_MODEL=base -e ASR_ENGINE=openai_whisper onerahmet/openai-whisper-asr-webservice:latest-gpu

once the service is running, make sure you are in the directory of your transcribe_LJ.py script. and run it:

python3 transcribe_LJ.py

after it runs, a file named transcribed.csv will be created. feel free to rename it to something like metafile_dataset.csv

REMEMBER TO DELETE THE EMPTY LINE AT THE BEGINNING OF THE transcribed.csv FILE OR ELSE IT WONT WORK!!!

CONGATS YOU DID IT! Have fun training!
