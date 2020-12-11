A = [
    ["Blå - Pantone 287 EC", (0, 61, 115)],
    ["Blå (mørk) - Pantone 289 EC", (0, 37, 70)],
    ["Lilla - Pantone 2665 EC", (101, 90, 159)],
    ["Lilla (mørk) - Pantone 5265 EC", (40, 28, 65)],
    ["Cyan - Pantone Process Cyan EC", (55, 160, 203)],
    ["Cyan (mørk) - Pantone 3025 EC", (0, 62, 92)],
    ["Turkis - Pantone 326 EC", (0, 171, 164)],
    ["Turkis (mørk) - Pantone 567 EC", (0, 69, 67)],
    ["Grøn - Pantone 376 EC", (139, 173, 63)],
    ["Grøn (mørk) - Pantone 574 EC", (66, 88, 33)],
    ["Gul - Pantone 7408 EC", (250, 187, 0)],
    ["Gul (mørk) - Pantone 455 EC", (99, 75, 3)],
    ["Orange - Pantone 144 EC", (238, 127, 0)],
    ["Orange (mørk) - Pantone 463 EC", (95, 52, 8)],
    ["Rød - Pantone 485 EC", (226, 0, 26)],
    ["Rød (mørk) - Pantone 490 EC", (91, 12, 12)],
    ["Magenta - Pantone Process Magenta EC", (226, 0, 122)],
    ["Magenta (mørk) - Pantone 229 EC", (95, 0, 48)],
    ["Grå - Pantone Cool Gray 7 EC", (135, 135, 135)],
    ["Grå (mørk) - Pantone 11 C", (75, 75, 74)]
]

for title, (r, g, b) in A:
    print("<color name=\"%s\" value=\"%.5f %.5f %.5f\"/>" % (title, r/255, g/255, b/255))

