import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play

load_dotenv()
def text_to_audio(folder):
    elevenlabs = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
    )

    save_file_path = f"user_uploads/{folder}/audio.mp3"
    
    with open(os.path.join(f"user_uploads/{folder}/",'desc.txt')) as f:
        text = f.read()
    audio = elevenlabs.text_to_speech.convert(
        text=text,
        voice_id="JBFqnCBsd6RMkjVDRZzb",  # "George" - browse voices at elevenlabs.io/app/voice-library
        model_id="eleven_v3",
        output_format="mp3_44100_128",
    )
    
    
    
    
    with open(save_file_path,"wb") as f:
        for chunk in audio:
            f.write(chunk)
    
    print("Audio file created successfully!")

    return save_file_path



def generate_reel(folder):
    pass

if __name__ == "__main__":
    with open("done.txt","r") as f:
        done_folders = f.readlines()
    done_folders = [f.strip() for f in done_folders]
    user_uploads = os.listdir("user_uploads")
    print("done_folders:",done_folders)
    print("all_folders:",user_uploads)
    for folder in user_uploads:
        if folder in done_folders:
            text_to_audio(folder)
            generate_reel(folder)
            # with open("done.txt","a") as f:
            #     f.write(folder +'\n')
        
    