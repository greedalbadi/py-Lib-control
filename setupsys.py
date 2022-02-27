



def getversion(path):
    try:
        file = open(f"{path}\\\\setup.py", "r")

        for line in file.read().splitlines():

            if "version=" in line:

                version = line.split("=")[1].replace("'", "").replace(",", "").replace(" ", "")

                break

        return version
    except:
        return False



def setversion(path, version):
    print("S")
    file = open(f"{path}\\\\setup.py", "r")

    lines = []

    for line in file.read().splitlines():

        lines.append(line)



    file.close()


    open(f"{path}\\\\setup.py", "w").close()

    file = open(f"{path}\\\\setup.py", "a")

    for line in lines:

        if "version=" in line:
            line = f"  version='{version}',".replace(" ", "")
        file.write(line + "\n")
    del lines
    file.close()
    return True
