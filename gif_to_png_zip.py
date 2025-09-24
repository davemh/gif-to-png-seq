from PIL import Image
import os
import zipfile

def gif_to_png_zip(gif_path, out_dir="frames", zip_name="frames.zip"):
    # Ensure output directory exists
    os.makedirs(out_dir, exist_ok=True)

    # Open the source GIF
    img = Image.open(gif_path)
    frame = 0
    filenames = []

    # Extract all GIF frames and save them as sequentially-numbered PNG files
    try:
        while True:
            img.seek(frame)
            filename = os.path.join(out_dir, f"frame_{frame:04d}.png")
            img.save(filename)
            filenames.append(filename)
            print(f"Saved {filename}")
            frame += 1
    except EOFError:
        pass  # no more frames

    # Compress the PNG sequence into a ZIP archive
    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in filenames:
            zipf.write(file, os.path.basename(file))
    print(f"Created {zip_name} with {len(filenames)} frames.")

# Allow script to be run directly, or module to be loaded without execution, from the same file.

if __name__ == "__main__":
    gif_to_png_zip("input.gif")
