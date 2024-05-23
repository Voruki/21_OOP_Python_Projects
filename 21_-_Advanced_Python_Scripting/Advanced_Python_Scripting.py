import os
import json
import shutil
from subprocess import PIPE, run
import sys

# Constants
GAME_DIR_PATTERN = "game"
GAME_CODE_EXTENSION = ".go"
GAME_COMPILE_COMMAND = ["go", "build"]

def find_all_game_paths(source):
    """
    Finds all directories containing 'game' in their names within the source directory.
    Returns a list of these directories' paths.
    """
    game_paths = []
    for root, dirs, files in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(root, directory)
                game_paths.append(path)
        break  # Only check the top-level directory
    return game_paths

def get_name_from_paths(paths, to_strip):
    """
    Generates new directory names by stripping a specified pattern from the original directory names.
    """
    new_names = [os.path.basename(path).replace(to_strip, "") for path in paths]
    return new_names

def create_dir(path):
    """
    Creates a directory if it does not already exist.
    """
    if not os.path.exists(path):
        os.makedirs(path)

def copy_and_overwrite(source, dest):
    """
    Copies a directory and its contents from source to destination, overwriting the destination if it exists.
    """
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(source, dest)

def make_json_metadata_file(path, game_dirs):
    """
    Creates a JSON file with metadata about the game directories.
    """
    data = {
        "gameNames": game_dirs,
        "numberOfGames": len(game_dirs)
    }
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def compile_game_code(path):
    """
    Compiles the game code located in the specified path.
    """
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(GAME_CODE_EXTENSION):
                command = GAME_COMPILE_COMMAND + [file]
                run_command(command, path)
                return
        break

def run_command(command, path):
    """
    Runs a shell command in a specified directory and prints the result.
    """
    cwd = os.getcwd()
    os.chdir(path)
    result = run(command, stdout=PIPE, stderr=PIPE, text=True)
    print("Compile result:", result.stdout, result.stderr)
    os.chdir(cwd)

def main(source, target):
    """
    Main function that coordinates finding, copying, and compiling game directories.
    """
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

    game_paths = find_all_game_paths(source_path)
    new_game_dirs = get_name_from_paths(game_paths, "_game")

    create_dir(target_path)

    for src, new_dir in zip(game_paths, new_game_dirs):
        dest_path = os.path.join(target_path, new_dir)
        copy_and_overwrite(src, dest_path)
        compile_game_code(dest_path)

    json_path = os.path.join(target_path, "metadata.json")
    make_json_metadata_file(json_path, new_game_dirs)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("You must pass a source and target directory - only.")
    source, target = sys.argv[1:]
    main(source, target)
