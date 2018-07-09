# IPE Style Sheets

This repository contains a collection of IPE style sheets,
such as to add extra color palettes for different corporate identities
for which I had to work, etc.

## How to add a style sheet to an IPE document

1. First of all, you should already have installed
   [the IPE Extensible Drawing Editor](http://ipe.otfried.org/)
   from its website. Of course, you will also need LaTeX installed
   in your machine in order to use IPE.
2. To add a new style sheet into a document, select from the menu
   `Edit > Style sheets` (or hit the shortcut `Ctrl + Shift + S`),
   then browse for a new `.isy` style sheet by clicking `Add`.
3. Occasionally, you will need to force updating the style sheets
   by selecting the menu `Edit > Update style sheets`
   (shortcut: `Ctrl + Shift + U`), then re-run the LaTeX build via
   `File > Run Latex` (shortcut: `Ctrl + L`).

## Available style sheets

### Basic style sheets

Each style sheet in [basic](basic/) directory contains a basic
functionality which would help writing IPE documents easier.

- **[colors](basic/colors/)**: Contains definitions of different color palettes
- **[presentations](basic/presentations)**: Contains page layout templates for presentations
- **[fonts](basic/fonts/)**: Contains font configuration with LaTeX


### Corporate Identities

Style sheets for each corporate identity are located in its respective
subdirectory under the main [corporates](corporates/) directory.
In most cases, there is at least one style sheet which defines a color
palettes for an organization for the sake of consistency.

**Warning:** I am denying all responsibilities regarding any inaccuracies
of any information or any assets in these files inside
[corporates](corporates/) directory provided by me. I am also
_not_ claiming any rights to the designs or trademarks presented in these
files; they are provided only for convenience. Please make sure that you
have the right to use these assets first.
