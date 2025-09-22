# GIF to PNG Sequence

A simple command-line tool for extracting all frames of an animated gif and saving them as a PNG sequence in a ZIP archive.

## Usage

1. Clone the repo.
2. Place your gif in the same directory as _gif_to_png_zip.py_
3. Browse to the directory in terminal.
4. Run the script:
    [MacOS:] python3 gif_to_png_zip.py
    [Windows:] python gif_to_png_zip.py

The script will:
1. Create a new directory called **frames/**
2. Extract all frames from the GIF to and save them as a PNG sequence in the **frames/**
3. Compress the **frames/** to create **frames.zip**

## Use Cases
- Animation research and analysis.
- A stepping stone tool on the way to a fork of **gif_shuffler** that includes PNG sequence as an i/o option.
