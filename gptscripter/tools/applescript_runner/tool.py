from subprocess import Popen, PIPE
from griptape.core import BaseTool, action
from schema import Schema

class AppleScriptRunner(BaseTool):
    @action(config={
            "name": "run_applescript",
            "description": "Can be used to complete one task at a time by running AppleScript code. Can play music by song name. Can create notes. Can create calendar events. Can send messages. Can open apps. Can do math.",
            "schema": Schema(
                str,
                description="The AppleScript code to execute. Must be valid AppleScript."
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