#!/usr/bin/env python3
import subprocess, sys, os

# Use the uv-managed Python directly
python_path = r"C:\Users\hanyu\AppData\Roaming\uv\python\cpython-3.12-windows-x86_64-none\python.exe"
if not os.path.exists(python_path):
    python_path = sys.executable  # fallback

subprocess.run([python_path, "end_to_end_test.py"], check=False)
