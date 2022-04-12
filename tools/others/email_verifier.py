# coding=utf-8
from core import WiriftTool
from core import WiriftToolsCollection


class KnockMail(WiriftTool):
    TITLE = "Knockmail"
    DESCRIPTION = "KnockMail Tool Verify If Email Exists"
    INSTALL_COMMANDS = [
        "git clone https://github.com/heywoodlh/KnockMail.git",
        "cd KnockMail;sudo pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd KnockMail;python3 knockmail.py"]
    PROJECT_URL = "https://github.com/heywoodlh/KnockMail"


class EmailVerifyTools(WiriftToolsCollection):
    TITLE = "Email Verify tools"
    TOOLS = [KnockMail()]
    
