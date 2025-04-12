# mycss

Lightweight sets of CSS for old-school design

## Getting started

1. Clone this!
2. Use following command to build a minimalised file

```bash
python3 make.py
# -> my.css
```

## How to use classnames

> If you want to read more, go to `example`

### Padding

- `p-x-1` padding 30px at left and right
- `p-x-2` padding 20px at left and right
- `p-x-3` padding 10px at left and right
- `p-y-1` padding 30px at top and bottom
- `p-y-2` padding 20px at top and bottom
- `p-y-3` padding 10px at top and bottom

### Margin

- `m-auto` margin auto
- `m-x-1` margin 30px at left and right
- `m-x-2` margin 20px at left and right
- `m-x-3` margin 10px at left and right
- `m-y-1` margin 30px at top and bottom
- `m-y-2` margin 20px at top and bottom
- `m-y-3` margin 10px at top and bottom

### Flex

- `flex-row` horizental flex with space-between
- `flex-row-start` horizental flex with flex-start
- `flex-row-end` horizental flex with flex-end
- `flex-col` vertical flex with flex-start

### Grid

- `grid4`
  - Over 1200px, split by 4
  - From 900px to 1200px, split by 3
  - From 600px to 900px, split by 2
  - Under 600px, split by 1
- `grid3`
  - Over 1200px, split by 3
  - From 900px to 1200px, split by 2
  - From 600px to 900px, split by 1
  - Under 600px, split by 1

### View

- `view-doc`
  - Over 1200px, width `65%`
  - From 900px to 1200px, width `80%`
  - From 600px to 900px, width `95%`
  - Under 600px, width `95%`
- `view-side`
  - Over 1200px, split by 2 to 8
  - From 900px to 1200px, split by 3 to 7
  - From 600px to 900px, split by 1 (vertically aligned)
  - Under 600px, split by 1 (vertically aligned)

### Font

- `f-size-1` font-size as `2.5rem`
- `f-size-2` font-size as `2rem`
- `f-size-3` font-size as `1.5rem`
- `f-bold` font-weight as bold
- `f-italic` font-style as italic

### Border

- `b-none`
- `b-groove` border-style as groove
- `b-groove-hover` On hover, border-style as groove
- `b-groove-active` On active, border-style as groove
- `b-groove-focus` On focus, border-style as groove
- `b-ridge` border-style as ridge
- `b-ridge-hover` On hover, border-style as ridge
- `b-ridge-active` On active, border-style as ridge
- `b-ridge-focus` On focus, border-style as ridge
- `b-inset` border-style as inset
- `b-inset-hover` On hover, border-style as inset
- `b-inset-active` On active, border-style as inset
- `b-inset-focus` On focus, border-style as inset
- `b-outset` border-style as outset
- `b-outset-hover` On hover, border-style as outset
- `b-outset-active` On active, border-style as outset
- `b-outset-focus` On focus, border-style as outset
- `b-guard-left` Add border-like guard at left
- `b-guard-right` Add border-like guard at right
- `b-guard-top` Add border-like guard at top
- `b-guard-bottom` Add border-like guard at bottom
- `b-size-1` border-size as `1rem`
- `b-size-2` border-size as `0.5rem`
- `b-size-3` border-size as `0.2rem`

## Color

- `color-dark` color as `black`
- `color-shadow` color as `grey`
- `color-light` color as `whitesmoke`
- `bcolor-dark` background-color as `black`
- `bcolor-shadow` background-color as `grey`
- `bcolor-light` background-color as `whitesmoke`
- `acolor-dark` accent-color as `black`
- `acolor-shadow` accent-color as `grey`
- `acolor-light` accent-color as `whitesmoke`

## Etc

- `outline`
  - no outline
  - Even on focus, no outline
