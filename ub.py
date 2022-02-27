import os
import subprocess
import systimatic



class TW:

    def __init__(self):

        self.active = False

    def upload(self, path, username, password, dist="dist/*"):
        self.active = True
        records = []

        records.append("started record.")

        dist = f"{dist}".replace(" ", "")

        path = f"{path}".replace("\\\\", "/") + "/" + dist

        records.append(f"Fixed path: {path}")

        cmd = f'twine upload -u {username} -p {password} --repository-url https://upload.pypi.org/legacy/ "{path}"'

        records.append("Fixed auth values")

        return TW._cm_upload(self, cmd, records)


    def _cm_upload(self, cmd, records):
        records.append("uploading..")

        command = os.system(cmd)

        records.append(command)
        self.active = False
        try:
            if command == 0:
                records.append("Done uploading.")
                systimatic.msgbox(message="Done uploading.")

                return records, True

            else:
                records.append(f"Error while uploading / code: {command}")
                systimatic.msgbox(message=f"Error while uploading / code: {command}")

                return records, False
        except:

            records.append("Failed to show message box.")

            return records, False




    def builed(self, path, pythonversion=None, build="bdist_wheel"):

        self.active = True



        records = []

        path = path.replace("\\\\", "/")

        records.append("fixed path")

        cmd = f"python setup.py sdist {build}"

        records.append("fixed command.")

        os.chdir(path)

        records.append(f"changed location to {os.getcwd()}")

        records.append("running builed command..")
        command = os.system(cmd)
        try:
            if command == 0:
                records.append("Done building.")
                systimatic.msgbox(message="Done building.")
                self.active = False

                return records, True

            else:
                records.append(f"Error while building / code: {command}")
                systimatic.msgbox(message=f"Error while building / code: {command}")
                self.active = False

                return records, False
        except:
            records.append("Failed to show message box.")
            self.active = False

            return records, False
