package proxy_server_config

class ProxyServerConfig:
    def __init__(self):
        self.config = {}

    def set_eval_command(self, command):
        try:
            self.config['eval_command'] = command
        except Exception as e:
            print(f"Error setting eval command: {str(e)}")

    def get_eval_command(self):
        return self.config.get('eval_command')

    def execute_script(self, script):
        try:
            result = eval(script)
            return result
        except Exception as e:
            print(f"Error executing script: {str(e)}")
            return None