from PIL import Image
import numpy as np
import cv2

# input: abcdefghijklmnopqrstuvwxyz{}_

image = Image.open("/home/tommaso/Desktop/finali/flag.png").convert("RGB")
image_np = np.array(image)

gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
_, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

blocksizes = []
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    blocksizes.append((x, y, w, h))

blocksizes = sorted(blocksizes, key=lambda b: (b[1], b[0]))

blocksizes[:5]

charsizes = {
    60: "a",
    66: "b",
    52: "c",
    67: "d",
    61: "e",
    42: "f",
    59: "g",
    68: "h",
    28: "i",
    34: "j",
    57: "k",
    29: "l",
    99: "m",
    69: "n",
    65: "o",
    70: "p",
    71: "q",
    44: "r",
    53: "s",
    39: "t",
    72: "u",
    54: "v",
    83: "w",
    56: "x",
    55: "y",
    51: "z",
    41: "{",
    40: "}",
    49: "_",
}

reverse = {w: c for w, c in charsizes.items()}

flag = ""
for _, _, w, _ in blocksizes[29:]:
    char = reverse.get(w, "?")
    flag += char

print(flag)
