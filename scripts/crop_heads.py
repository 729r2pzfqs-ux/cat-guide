#!/usr/bin/env python3
"""Crop cat breed images to head shots (top-center square crop)"""

from PIL import Image
import os

INPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../catfinder.app/images/breeds")
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../catfinder.app/images/heads")

os.makedirs(OUTPUT_DIR, exist_ok=True)

count = 0
for img_file in sorted(os.listdir(INPUT_DIR)):
    if not img_file.endswith(('.webp', '.png', '.jpg', '.jpeg')):
        continue
    
    img_path = os.path.join(INPUT_DIR, img_file)
    img = Image.open(img_path)
    w, h = img.size
    
    # Square crop from top-center (captures head)
    # Use 70% of width as the crop size, focused on top
    size = int(min(w, h * 0.75))
    left = (w - size) // 2
    top = 0
    
    img_cropped = img.crop((left, top, left + size, top + size))
    
    # Resize to consistent 400x400
    img_cropped = img_cropped.resize((400, 400), Image.LANCZOS)
    
    # Save as webp for consistency
    base_name = os.path.splitext(img_file)[0]
    output_path = os.path.join(OUTPUT_DIR, f"{base_name}.webp")
    img_cropped.save(output_path, 'WEBP', quality=85)
    print(f"✓ {base_name}.webp")
    count += 1

print(f"\nDone! Cropped {count} images to {OUTPUT_DIR}/")
