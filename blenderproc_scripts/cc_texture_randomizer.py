import blenderproc as bproc
import argparse
import os
import shutil
import random

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Copy a specified number of textures from source to destination.')
parser.add_argument('source_dir', type=str, help='The source directory containing the textures')
parser.add_argument('--num_textures', type=int, default=5, help='The number of textures to copy')

args = parser.parse_args()

# Load textures
cc_textures = bproc.loader.load_ccmaterials(args.source_dir)
dest_dir = args.source_dir + "_" + str(args.num_textures) + "r"

# Get a list of all the folder names in the source directory
folder_names = [texture.blender_obj.name for texture in cc_textures]

# Randomly select num_textures folder names from the list
selected_folder_names = random.sample(folder_names, args.num_textures)

# Create a new folder in the destination directory with a unique name
os.makedirs(dest_dir, exist_ok=True)

# Loop through the selected folder names and copy them from the source to the destination directory
for folder_name in selected_folder_names:
    source_path = os.path.join(args.source_dir, folder_name)
    dest_path = os.path.join(dest_dir, folder_name)
    shutil.copytree(source_path, dest_path)