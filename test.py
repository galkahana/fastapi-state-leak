from subprocess import Popen

if __name__ == "__main__":
    procs = [Popen("poetry run python -m test-single", shell=True) for i in range(50)]
    for p in procs:
        p.wait()
