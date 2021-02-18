from paramiko import SSHClient
import paramiko
from jc.parsers import df, who, ps


class SSH:
    def __init__(self,hostname, username):
        self._ssh = SSHClient()
        self._ssh.load_system_host_keys()
        self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._ssh.connect(hostname=hostname, username=username, timeout=10)

    def __del__(self):
        """ Called when the instance is about to be destroyed. 
        The connection has to be closed here.
        """
        if self._ssh:
            self._ssh.close()


    def cmd_disk_usage(self):
        cmd_str = 'df -hT'
        stdin,stdout,stderr = self._ssh.exec_command(cmd_str)
        if stderr.channel.recv_exit_status() != 0:
            print(stderr.read())
        else:
            output_cmd = stdout.read()
            return df.parse(output_cmd.decode("utf-8"))

    def cmd_users_connected(self):
        cmd_str = 'who'
        stdin,stdout,stderr = self._ssh.exec_command(cmd_str)
        if stderr.channel.recv_exit_status() != 0:
            print(stderr.read())
        else:
            output_cmd = stdout.read()
            return who.parse(output_cmd.decode("utf-8"))


    def cmd_proccess_running(self):
        cmd_str = 'ps -aux'
        stdin,stdout,stderr = self._ssh.exec_command(cmd_str)
        if stderr.channel.recv_exit_status() != 0:
            print(stderr.read())
        else:
            output_cmd = stdout.read()
            return ps.parse(output_cmd.decode("utf-8"))

    def cmd_cpu_usage(self):
        cmd_str = "top -b -n 2 -d1 | grep \"Cpu(s)\" | awk '{print $2}' | awk -F. '{print $1}'"
        stdin,stdout,stderr = self._ssh.exec_command(cmd_str)
        if stderr.channel.recv_exit_status() != 0:
            print(stderr.read())
        else:
            output_cmd = stdout.readlines()
            output_for_format = []
            for index, out in enumerate(output_cmd, start=0):
                cpu_name = 'cpu_' + str(index)
                output_for_format.append({'cpu': cpu_name ,'value_percent': out.replace('\n','')})
        return output_for_format


    def mem_usage(self):
        cmd_str = "free | grep Mem |awk '{print $3/$2 * 100.0}'"
        stdin,stdout,stderr = self._ssh.exec_command(cmd_str)
        if stderr.channel.recv_exit_status() != 0:
            print(stderr.read())
        else:
            output_cmd = stdout.read().decode("utf-8")
            return {'mem_usage_percent': output_cmd.replace('\n','')}


    def exec_cmd(self,cmd):
        stdin,stdout,stderr = self._ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            print(stderr.read())
        else:
            return stdout.read()




if __name__ == '__main__':
    pass