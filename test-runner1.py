#!/usr/bin/env python3

import sys
import subprocess

if len(sys.argv) != 3:
    sys.exit(f"Usage: {sys.argv[0]} <object_path> <intergace>")

object_path = sys.argv[1]
interface = sys.argv[2]

subprocess.run(
    [
        "mate-terminal",
        "-e",
        f"/bin/bash -c \"echo -e 'Hello from runner for test-interface1!\n{object_path = }\n{interface = }' && cat\"",
    ]
)
