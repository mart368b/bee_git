import subprocess, time

lines = []
with open('script.txt', 'r') as f:
    lines = f.readlines()

lines.reverse()

with open('line.bee', 'w') as fout:
    for line in lines:
        fout.seek(0)
        fout.truncate(0)
        fout.write(line.replace('\n', ''))
        fout.flush()

        subprocess.call(["git", "commit", "-a", "-Fline.bee"])
