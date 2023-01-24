import tkinter as tk
import paramiko

class DiagnFrame(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Server Diagn Tool")

        # Create widgets
        host_label = tk.Label(self, text="Host: ")
        host_label.pack()
        self.host_input = tk.Entry(self)
        self.host_input.pack()

        username_label = tk.Label(self, text="Username: ")
        username_label.pack()
        self.username_input = tk.Entry(self)
        self.username_input.pack()

        password_label = tk.Label(self, text="Password: ")
        password_label.pack()
        self.password_input = tk.Entry(self, show="*")
        self.password_input.pack()

        diagnose_button = tk.Button(self, text="Diagnose", command=self.diagnose)
        diagnose_button.pack()

    def diagnose(self):
        host = self.host_input.get()
        user = self.username_input.get()
        password = self.password_input.get()

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(host, username=user, password=password)
            stdin, stdout, stderr = ssh.exec_command("uptime")
            self.uptime = stdout.read().decode("utf-8")

            stdin, stdout, stderr = ssh.exec_command("df -h /")
            self.disk_space = stdout.read().decode("utf-8")

            stdin, stdout, stderr = ssh.exec_command("cat /etc/os-release | grep 'PRETTY_NAME'| cut -d'=' -f2")
            os_version = stdout.read().decode("utf-8")
            os_version = os_version.strip().split("\n")
            self.os_version = " ".join([i.strip().strip('"') for i in os_version])

            self.result_window = tk.Toplevel(self)
            self.result_window.title("Diagnostic Result")

            host_label = tk.Label(self.result_window, text="Host: " + host.strip())
            host_label.pack()

            uptime_label = tk.Label(self.result_window, text="Uptime: " + self.uptime.strip())
            uptime_label.pack()

            disk_space_label = tk.Label(self.result_window, text="Disk Space: \n" + self.disk_space)
            disk_space_label.pack()

            os_version_label = tk.Label(self.result_window, text="OS version: " + self.os_version)
            os_version_label.pack()

            save_button = tk.Button(self.result_window, text="Save Result", command=self.save_result)
            save_button.pack()

        except paramiko.ssh_exception.AuthenticationException as e:
            print("Failed to connect: Invalid credentials")
        except paramiko.ssh_exception.SSHException as e:
            print("Failed to connect: ", e)
        finally:
            ssh.close()

        # Create widgets
        host_label = tk.Label(self, text="Host: ")
        host_label.pack()
        self.host_input = tk.Entry(self)
        self.host_input.pack()

        username_label = tk.Label(self, text="Username: ")
        username_label.pack()
        self.username_input = tk.Entry(self)
        self.username_input.pack()

        password_label = tk.Label(self, text="Password: ")
        password_label.pack()
        self.password_input = tk.Entry(self, show="*")
        self.password_input.pack()

        diagnose_button = tk.Button(self, text="Diagnose", command=self.diagnose)
        diagnose_button.pack()

    def save_result(self):
        host = self.host_input.get()
        uptime = self.uptime.strip()
        disk_space = self.disk_space.strip()
        os_version = self.os_version.strip()

        with open("diagnostic_result.txt", "w") as f:
            f.write("Host: " + host + "\n")
            f.write("Uptime: " + uptime + "\n")
            f.write("Disk Space: " + disk_space + "\n")
            f.write("OS version: " + os_version + "\n")

app = DiagnFrame()
app.mainloop()