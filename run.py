#!/usr/bin/env python3
"""Quick launcher — runs the DeDollar Stock Monitor"""
import subprocess, sys, webbrowser, time, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Starting DeDollar Stock Monitor...")
print("Open: http://localhost:5000")
webbrowser.open("http://localhost:5000")
subprocess.run([sys.executable, "server.py"])
