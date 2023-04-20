from subprocess import Popen, PIPE
from griptape.core import BaseTool, action
from schema import Schema

class AppleScriptRunner(BaseTool):
    @action(config={
            "name": "run_applescript",
            "description": "Can be used to run AppleScript code to accomplish different tasks (for example,  play music by song name, create notes, create calendar events, send messages, open apps, do math, etc.).",
            "schema": Schema(
                str,
                description="Valid executable AppleScript code"
            )
        })
    def run_applescript(self, value: bytes) -> str:
        p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        stdout, stderr = p.communicate(value.decode())

        if len(stdout.strip()) == 0:
            if len(stderr.strip()) == 0:
                return "Success."
            return stderr
        return "Success."