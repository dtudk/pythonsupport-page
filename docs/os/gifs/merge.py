import hashlib
import sys
from pathlib import Path

import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

cwd = Path()

tmpdir = cwd / "tmp"
hash_file = cwd / "hashes.yml"
commands_out = sys.argv[1]

def read_yaml(file: Path):
    """Read a yaml file, and return the dictionary"""
    return yaml.load(open(file, 'r'), Loader=Loader)


def write_yaml(content: dict, file: Path):
    """Write a dictionary to a yaml file"""
    with open(file, 'w') as fh:
        yaml.dump(content, fh, Dumper=Dumper)

def sortdict(d):
    return dict(sorted(d.items(), key=lambda item: item[0]))

def merge(d1, d2):
    d = {**d1}
    for key, value in d2.items():
        if isinstance(value, dict):
            value = merge(d.get(key, {}), value)
        d[key] = value
    return sortdict(d)

# Populate the hash table
hashes = {}
if hash_file.is_file():
    hashes = read_yaml(hash_file)

# Read the default configuration
def_config = read_yaml(cwd / "config.yml")
commands = open(commands_out, 'w')

for path in cwd.glob("*/*.yml"):
    if not path.is_file():
        continue
    if path.is_relative_to(tmpdir):
        continue
    if path.name in ("config.yml", "hashes.yml"):
        continue

    config = read_yaml(path.parent / "config.yml")

    # get a path object relative to cwd (strips segments behind)
    top_path = path.relative_to(cwd)
    top_path_str = str(top_path)

    # Merge dictionaries
    yml = merge(merge(def_config, config),
                read_yaml(path))

    # check whether we need to do anything
    content = yaml.dump(yml, Dumper=Dumper)
    current_hash = hashlib.md5(content.encode("utf-8")).hexdigest()
    old_hash = hashes.get(top_path_str, current_hash + "never")

    # Correct the output files
    stem = path.stem
    out = tmpdir / '_'.join(top_path.parts)
    gif = path.with_suffix(".gif")
    if old_hash == current_hash and gif.is_file():
        print(f"Skipping {top_path_str} as it already exists with same hash")
        continue
    elif top_path_str in hashes and gif.is_file():
        print(f"Running {top_path_str} even if it exists, hashes are different: {old_hash} != {current_hash}")
    elif gif.is_file():
        print(f"Running {top_path_str} as the hash is not found.")
    else:
        print(f"Running {top_path_str} as the file is not found.")

    hashes[top_path_str] = current_hash
    # We do not have the same hash, or the file does not exist
    write_yaml(yml, out)
    commands.write(f"terminalizer render -o {gif} {out}\n")

commands.close()

# Store the hashes, to be re-used
write_yaml(sortdict(hashes), hash_file)
