#!/usr/bin/env python3
"""
Process cat breed images: rename, convert to WebP, create head crops
"""

import os
import subprocess
from pathlib import Path

# Number to breed name mapping (from CAT_BREEDS.md)
BREEDS = {
    1: "Persian",
    2: "Maine Coon",
    3: "Ragdoll",
    4: "British Shorthair",
    5: "Siamese",
    6: "Abyssinian",
    7: "Bengal",
    8: "Sphynx",
    9: "Scottish Fold",
    10: "Birman",
    11: "Russian Blue",
    12: "Norwegian Forest Cat",
    13: "Burmese",
    14: "Oriental Shorthair",
    15: "Devon Rex",
    16: "Cornish Rex",
    17: "Exotic Shorthair",
    18: "Himalayan",
    19: "American Shorthair",
    20: "Tonkinese",
    21: "Ragamuffin",
    22: "Savannah",
    23: "Siberian",
    24: "Balinese",
    25: "Turkish Angora",
    26: "Turkish Van",
    27: "Somali",
    28: "Chartreux",
    29: "Ocicat",
    30: "Egyptian Mau",
    31: "Singapura",
    32: "Manx",
    33: "Japanese Bobtail",
    34: "American Curl",
    35: "Selkirk Rex",
    36: "LaPerm",
    37: "Korat",
    38: "Bombay",
    39: "Havana Brown",
    40: "Burmilla",
    41: "Toyger",
    42: "Pixie-Bob",
    43: "Cymric",
    44: "American Bobtail",
    45: "Nebelung",
    46: "Snowshoe",
    47: "Chausie",
    48: "Sokoke",
    49: "Australian Mist",
    50: "Peterbald",
    51: "Donskoy",
    52: "Kurilian Bobtail",
    53: "American Wirehair",
    54: "European Shorthair",
    55: "Brazilian Shorthair",
    56: "Khao Manee",
    57: "Lykoi",
    58: "Munchkin",
    59: "Highlander",
    60: "Serengeti",
    61: "Thai",
    62: "Chantilly-Tiffany",
    63: "York Chocolate",
    64: "Colorpoint Shorthair",
    65: "Javanese",
    66: "Oriental Longhair",
    67: "British Longhair",
    68: "Asian",
    69: "Tiffanie",
    70: "RagaMuffin",
    71: "California Spangled",
    72: "Dragon Li",
    73: "Suphalak",
    74: "Aphrodite Giant",
    75: "Cyprus",
}

def name_to_slug(name):
    """Convert breed name to URL slug"""
    return name.lower().replace(' ', '-').replace('(', '').replace(')', '')

def process_images(source_dir, dest_breeds_dir, dest_heads_dir):
    """Process all images: convert to WebP and create head crops"""
    
    source_path = Path(source_dir)
    breeds_path = Path(dest_breeds_dir)
    heads_path = Path(dest_heads_dir)
    
    breeds_path.mkdir(parents=True, exist_ok=True)
    heads_path.mkdir(parents=True, exist_ok=True)
    
    processed = 0
    missing = []
    
    for num, name in BREEDS.items():
        src_file = source_path / f"{num}.png"
        slug = name_to_slug(name)
        
        if not src_file.exists():
            missing.append(f"{num}: {name}")
            continue
        
        # Convert to WebP for breeds/
        breed_dest = breeds_path / f"{slug}.webp"
        subprocess.run([
            'cwebp', '-q', '80', str(src_file), '-o', str(breed_dest)
        ], capture_output=True)
        
        # Create head crop (square from top)
        tmp_cropped = f"/tmp/cat-crop-{num}.png"
        tmp_head = f"/tmp/cat-head-{num}.png"
        
        # Crop to square from top
        subprocess.run([
            'sips', '-c', '1024', '1024', str(src_file), '--out', tmp_cropped
        ], capture_output=True)
        
        # Resize to 400x400
        subprocess.run([
            'sips', '-Z', '400', tmp_cropped, '--out', tmp_head
        ], capture_output=True)
        
        # Convert head to WebP
        head_dest = heads_path / f"{slug}.webp"
        subprocess.run([
            'cwebp', '-q', '80', tmp_head, '-o', str(head_dest)
        ], capture_output=True)
        
        # Cleanup
        if os.path.exists(tmp_cropped):
            os.remove(tmp_cropped)
        if os.path.exists(tmp_head):
            os.remove(tmp_head)
        
        print(f"  ✓ {num}. {name} → {slug}.webp")
        processed += 1
    
    print(f"\n✅ Processed {processed} images")
    if missing:
        print(f"\n⚠️ Missing {len(missing)} images:")
        for m in missing:
            print(f"  - {m}")

if __name__ == '__main__':
    import sys
    
    source = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/Downloads/catfinder-images/Catfinder")
    breeds_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../cat-finder/images/breeds")
    heads_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../cat-finder/images/heads")
    
    print(f"Processing cat images from: {source}")
    print(f"Breeds output: {breeds_dir}")
    print(f"Heads output: {heads_dir}\n")
    
    process_images(source, breeds_dir, heads_dir)
