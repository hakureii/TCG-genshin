import subprocess
import json
import os

def run_ai(prompt: str):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(current_dir, 'index.js')

    env = os.environ.copy()
    env['PROMPT'] = prompt

    command = ['node', script_path]

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, env=env, text=True, check=True)
        return bytes(result.stdout, "utf-8").decode("unicode_escape")

    except subprocess.CalledProcessError as e:
        return f"Error: {e}"
