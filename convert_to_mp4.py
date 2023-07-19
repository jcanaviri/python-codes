import os
import subprocess


def convert_to_mp4(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Input file {input_file} does not exist")
        return

    # Check if ffmpeg is installed
    try:
        subprocess.run(["ffmpeg", "-version"], check=True)
    except FileNotFoundError:
        print("ffmpeg not found, please install ffmpeg")
        return

    # Run the conversion command
    cmd = ["ffmpeg", "-i", input_file, "-codec", "copy", output_file]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print("Conversion failed")


convert_to_mp4(
    f"Guillermo.Del.Toros.Pinocchio.2022.mkv", f"Guillermo.Del.Toros.Pinocchio.2022.mp4"
)
