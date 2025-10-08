import os

modules_dir = "modules"
engine_file = "engine/HIPA_Engine.pine"

header = """//@version=6
indicator('Hyper Integration Engine', overlay=true)

"""

modules = []
for root, dirs, files in os.walk(modules_dir):
    for file in files:
        if file.endswith('.pine'):
            modules.append(os.path.join(root, file))
modules.sort()

with open(engine_file, 'w') as out:
    out.write(header)
    for mod in modules:
        with open(mod, 'r') as f:
            out.write(f"\n// ---- MODULE: {os.path.basename(mod)} ----\n")
            out.write(f.read() + '\n')

print("Engine generated at", engine_file)
