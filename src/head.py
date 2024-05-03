import os, discord, requests, json
from io import BytesIO
from PIL import Image, ImageSequence

def getAsset(path):
    base_url = "https://raw.githubusercontent.com/hakureii/TCG-genshin-assets/main/"
    return base_url + path

def getToken():
    return os.environ["TOKEN"]

def getIntents():
    return discord.Intents.all()

def getAssetList():
    with open("src/assets.json") as file:
        assets = json.load(file)
    return assets

def resizeImage(image_url):
    new_size = (int(9 * 27), int(16 * 27))
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    frames = []
    for frame in ImageSequence.Iterator(image):
        resized_frame = frame.resize(new_size, resample=Image.LANCZOS)
        frames.append(resized_frame)
    output = BytesIO()
    frames[0].save(output, format="GIF", save_all=True, append_images=frames[1:])
    output.seek(0)
    return output

def getColor(name:str):
    with open("src/colors.json") as file:
        colours = json.load(file)
    return int(colours[name.lower()][1:], 16)

