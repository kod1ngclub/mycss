from pathlib import Path

def Echo(text):
    print(f"| {text}")

def DuSize(path):
    file = Path(path)
    if not file.is_file(): raise RuntimeError(f"Fail to catch file {path}")

    size_b = file.stat().st_size
    size_kb = size_b / 1024

    rep = f"{round(size_kb, 2)}kb"
    return rep

def Cat(path):
    file = Path(path)
    if not file.is_file(): raise RuntimeError(f"Fail to catch file {path}")

    Echo(f"Catched file {path} [{DuSize(path)}]")
    
    liens = []
    with open(path, "r") as target:
        lines = target.readlines()
    
    return lines

def Touch(path, data):
    with open(path, "w") as target:
        for line in data: target.write(line)
    
    Echo(f"Created file {path}")

def Unindent(data):
    return [line.lstrip() for line in data]

NEWLINE = "\n"
EMPTY = ""

def Unnewline(data):
    return [line.replace(NEWLINE, EMPTY) for line in data]

def Pipe(data, funcs):
    store = []
    store = data

    for func in funcs:
        store = func(store)
    
    return store

MAIN_CSS = Cat("style/main.css")

FLEX_CSS = Cat("style/flex.css")
GRID_CSS = Cat("style/grid.css")
VIEW_CSS = Cat("style/view.css")

FONT_CSS = Cat("style/font.css")
TEXT_CSS = Cat("style/text.css")
COLOR_CSS = Cat("style/color.css")

MARGIN_CSS = Cat("style/margin.css")
PADDING_CSS = Cat("style/padding.css")

BORDER_CSS = Cat("style/border.css")
OUTLINE_CSS = Cat("style/outline.css")

entire = []

entire.extend(MAIN_CSS)

entire.extend(FLEX_CSS)
entire.extend(GRID_CSS)
entire.extend(VIEW_CSS)

entire.extend(COLOR_CSS)
entire.extend(FONT_CSS)
entire.extend(TEXT_CSS)

entire.extend(MARGIN_CSS)
entire.extend(PADDING_CSS)

entire.extend(BORDER_CSS)
entire.extend(OUTLINE_CSS)

OUT = "my.css"

Touch(OUT, Pipe(entire, [
    Unnewline,
    Unindent
]))

Echo(f"Done! [{DuSize(OUT)}]")