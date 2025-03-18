import subprocess

proc = subprocess.run("bash main.sh --stdout", shell=True, text=True, capture_output=True)

print(proc.stdout.strip() if proc.stdout else proc.stderr.strip())
