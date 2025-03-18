import subprocess

proc = subprocess.run("curl neofetch.sh | bash", shell=True, text=True, capture_output=True)

print(proc.stdout.strip() if proc.stdout.strip() else proc.stderr.strip())
