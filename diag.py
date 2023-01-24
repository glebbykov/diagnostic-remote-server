import tkinter as tk
import paramiko

class DiagnFrame(tk.Tk):
    def diagnose(self):
        host = self.host_input.get()
        user = self.username_input.get()
        password = self.password_input.get()

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(host, username=user, password=password)
            stdin, stdout, stderr = ssh.exec_command("uptime")
            uptime = stdout.read().decode("utf-8")
            print("Uptime: ", uptime.strip())

            stdin, stdout, stderr = ssh.exec_command("df -h /")
            disk_space = stdout.read().decode("utf-8")
            print("Disk Space: \n", disk_space)

            stdin, stdout, stderr = ssh.exec_command("cat /etc/os-release")
            os_version = stdout.read().decode("utf-8")
            print("OS version: \n", os_version.strip())
        except paramiko.ssh_exception.AuthenticationException as e:
            print("Failed to connect: Invalid credentials")
        except paramiko.ssh_exception.SSHException as e:
            print("Failed to connect: ", e)
        finally:
            ssh.close()

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Server Diagn Tool")

        # Create widgets
        host_label = tk.Label(self, text="Host: ")
        host_label.grid(row=0, column=0)
        self.host_input = tk.Entry(self)
        self.host_input.grid(row=0, column=1)

        username_label = tk.Label(self, text="Username: ")
        username_label.grid(row=1, column=0)
        self.username_input = tk.Entry(self)
        self.username_input.grid(row=1, column=1)

        password_label = tk.Label(self, text="Password: ")
        password_label.grid(row=2, column=0)
        self.password_input = tk.Entry(self, show="*")
        self.password_input.grid(row=2, column=1)

        diagnose_button = tk.Button(self, text="Diagnose", command=self.diagnose)
        diagnose_button.grid(row=3, column=1)
        
#def diagnose(self):
#        host = self.host_entry.get()
#        user = self.user_entry.get()
#        password = self.pass_entry.get()
#
#        ssh = paramiko.SSHClient()
#        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
#        try:
#            ssh.connect(host, username=user, password=password)
#            stdin, stdout, stderr = ssh.exec_command("uptime")
#            uptime = stdout.read().decode("utf-8")
#            print("Uptime: ", uptime.strip())
#
#            stdin, stdout, stderr = ssh.exec_command("df -h /")
#            disk_space = stdout.read().decode("utf-8")
#            print("Disk Space: \n", disk_space)
#
#            stdin, stdout, stderr = ssh.exec_command("cat /etc/os-release")
#            os_version = stdout.read().decode("utf-8")
#            print("OS version: \n", os_version.strip())
#        except paramiko.ssh_exception.AuthenticationException as e:
#            print("Failed to connect: Invalid credentials")
#        except paramiko.ssh_exception.SSHException as e:
#            print("Failed to connect: ", e)
#        finally:
#            ssh.close()

app = DiagnFrame()
app.mainloop()
