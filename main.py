#!/usr/bin/python3
from PIL import Image

print("PIL imported")
from os import listdir, environ

print("listdir imported")
from os.path import isfile, join

print("isfile imported\n")
import datetime

INPUTPATH = f"{environ['APPDATA']}/PrismLauncher/instances/1.20.1/.minecraft/journeymap/data/mp/146~56~112~60~19132/overworld/day/"
print("input path set: {}\n".format(INPUTPATH))

filelist = [f for f in listdir(INPUTPATH) if isfile(join(INPUTPATH, f))]
print("filelist created: {}\n".format(filelist))

img = Image.open(INPUTPATH + filelist[0])
print("image opened: {}".format(filelist[0]))
TILE_WIDTH, TILE_HEIGHT = img.size
print("tile size: {}x{}\n".format(TILE_WIDTH, TILE_HEIGHT))

setX = set()
setY = set()

bigX = 0
print("bigX set to 0")
bigY = 0
print("bigY set to 0")
smallX = 0
print("smallX set to 0")
smallY = 0
print("smallY set to 0\n")

for f in filelist:
    print("checking {}".format(f))
    coord = f.split(".")
    print("coord: {}".format(coord))
    ints = coord[0].split(",")
    print("ints: {}".format(ints))
    x = int(ints[0])
    print("x: {}".format(x))
    y = int(ints[1])
    print("y: {}".format(y))

    setX.add(x)
    setY.add(y)

dictX = {i: j for i, j in zip(range(len(setX)), sorted(list(setX)))}
print("dictX created: {}".format(dictX))
dictY = {i: j for i, j in zip(range(len(setY)), sorted(list(setY)))}
print("dictY created: {}\n".format(dictY))

bigX = max(setX)
print("bigX set to {}".format(bigX))
bigY = max(setY)
print("bigY set to {}".format(bigY))
smallX = min(setX)
print("smallX set to {}".format(smallX))
smallY = min(setY)
print("smallY set to {}\n".format(smallY))

print("\nimage map spans from ({},{}) to ({},{})\n".format(smallX, smallY, bigX, bigY))

bigimg = Image.new("RGB", (TILE_HEIGHT * (len(setX)), TILE_WIDTH * (len(setY))))
print(
    "bigimg created: {}x{}\n".format(
        TILE_HEIGHT * (bigX + abs(smallX)), TILE_WIDTH * (bigY + abs(smallY))
    )
)

print("starting stitch\n")

for i in range(len(setX)):
    for j in range(len(setY)):
        x = dictX[i]
        y = dictY[j]
        if "{},{}.png".format(x, y) in filelist:
            print("found {},{}.png".format(x, y))
            img = Image.open(INPUTPATH + "{},{}.png".format(x, y))
            print("opened {},{}.png".format(x, y))
            bigimg.paste(
                im=img,
                box=((i) * TILE_HEIGHT, (j) * TILE_WIDTH),
            )
            print("pasted {},{}.png".format(x, y))

print(f"saving {datetime.datetime.now().strftime('%Y-%m-%d')}.png")
bigimg.save(f"{datetime.datetime.now().strftime('%Y-%m-%d')}.png")
print(f"saved {datetime.datetime.now().strftime('%Y-%m-%d')}.png")