package script_executor

import sys

class ScriptExecutor:
    def __init__(self):
        self.variables = {}

    def set_variable(self, name, value):
        self.variables[name] = value

    def call_procedure(self, procedure_name, *args, **kwargs):
        # Implement calling a procedure with the given arguments
        pass

    def eval(self, script: str) -> None:
        try:
            exec(script, globals(), self.variables)
        except Exception as e:
            print(f"Error executing script: {e}", file=sys.stderr)

    def execute_script(self, script: str) -> None:
        self.eval(script)