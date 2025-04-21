import tomllib
import subprocess
import sys
from pathlib import Path

class RiddleRunner:
    def __init__(self, toml_file):
        self.toml_file = Path(toml_file)
        if not self.toml_file.exists():
            raise FileNotFoundError(f"File not found: {self.toml_file}")
        self.config = self.load_config()

    def load_config(self):
        with self.toml_file.open("rb") as f:
            return tomllib.load(f)

    def run(self):
        commands = self.config.get("commands")
        if not commands or not isinstance(commands, list):
            raise ValueError("Missing or invalid 'commands' list in riddle.toml")
        for cmd in commands:
            if not isinstance(cmd, str):
                raise TypeError(f"Invalid command type: {cmd} (expected string)")
            print(f"Running: {cmd}")
            result = subprocess.run(cmd, shell=True)
            if result.returncode != 0:
                raise RuntimeError(f"Command failed: {cmd}")

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != "run":
        print("Usage: python riddle.py run riddle.toml")
        sys.exit(1)
    runner = RiddleRunner(sys.argv[2])
    runner.run()
