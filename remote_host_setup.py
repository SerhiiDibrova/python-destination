import paramiko
import socket

class RemoteHostSetup:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.ssh_client = None

    def set_up_remote_host(self):
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(hostname=self.host, username=self.username, password=self.password)
        except socket.error as e:
            print(f"Failed to connect to {self.host}: {e}")
            return False
        except paramiko.AuthenticationException as e:
            print(f"Authentication failed for {self.username}@{self.host}: {e}")
            return False
        return True

    def close_connection(self):
        if self.ssh_client:
            self.ssh_client.close()