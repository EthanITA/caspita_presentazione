import os
from subprocess import run

try:
    working_proj_dir = os.path.join(os.path.dirname(__file__))
    os.startfile(os.path.join(working_proj_dir, "pagina presentazione.lnk"))
    run(["wsl", "-d", "Ubuntu-20.04", "bash", "-c", "-i", "tv"])
except Exception as e:
    print(e)
    input()
