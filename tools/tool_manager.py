# coding=utf-8
import os
from time import sleep

from core import WiriftTool
from core import WiriftToolsCollection


class UpdateTool(WiriftTool):
    TITLE = "Update Tool or System"
    DESCRIPTION = "Update Tool or System"

    def __init__(self):
        super(UpdateTool, self).__init__([
            ("Update System", self.update_sys),
            ("Update WiriftTool", self.update_ht)
        ], installable = False, runnable = False)

    def update_sys(self):
        os.system("sudo apt update && sudo apt full-upgrade -y")
        os.system(
            "sudo apt-get install tor openssl curl && sudo apt-get update tor openssl curl")
        os.system("sudo apt-get install python3-pip")

    def update_ht(self):
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/wirifttool/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/wirifttool/;"
                  "mkdir wirifttool;"
                  "cd wirifttool;"
                  "git clone https://github.com/wirifit/wirifttool.git;"
                  "cd wirifttool;"
                  "sudo chmod +x install.sh;"
                  "./install.sh")


class UninstallTool(WiriftTool):
    TITLE = "Uninstall WiriftTool"
    DESCRIPTION = "Uninstall WiriftTool"

    def __init__(self):
        super(UninstallTool, self).__init__([
            ('Uninstall', self.uninstall)
        ], installable = False, runnable = False)

    def uninstall(self):
        print("wirifttool started to uninstall..\n")
        sleep(1)
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/wirifttool/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/wirifttool/;")
        print("\nWiriftTool Successfully Uninstalled..")
        print("Happy Hacking..!!")
        sleep(1)


class ToolManager(WiriftToolsCollection):
    TITLE = "Update or Uninstall | WiriftTool"
    TOOLS = [
        UpdateTool(),
        UninstallTool()
    ]
