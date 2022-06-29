#!/usr/bin/python3
import time
from git import Repo


def GitAuto():
    repo = Repo("./")
    repo.git.add(all=True)
    repo.git.commit('-m', 'Auto Commit by GitAuto.py')
    repo.git.push()

def main():
    day = 10
    Previousday = time.time()
    while (1):
        if (time.time() - Previousday > day):
            with open("GitAuto.txt", "a") as f:
                f.write("Another day, another commit\n")
            GitAuto()
            Previousday = time.time()

main()