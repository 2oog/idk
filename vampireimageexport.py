from PIL import Image
import json

path = 'D:/vampire/'

j = json.loads(open(path + "items.json", 'r').readlines()[0])
img = Image.open(path + "items.png")

for jpix in j['textures'][0]['frames']:
    img.crop( 
        (
            jpix['frame']['x'], 
            jpix['frame']['y'],
            jpix['frame']['x'] + jpix['frame']['w'],
            jpix['frame']['y'] + jpix['frame']['h']
        ) 
    ).save(path + 'img/' + jpix['filename'])