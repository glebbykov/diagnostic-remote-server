# Server Diagnosis Tool
This is a simple GUI application that allows you to diagnose your server's uptime, the volume of the root disk space, and OS version.

The application looks like this:
[An example of the output](https://user-images.githubusercontent.com/122178014/214346924-20a7a297-0821-41d9-9429-07b2f6b5b00e.PNG)

## Getting Started!

To get started, you'll need to have Python 3 and the following libraries installed:

+ tkinter
+ paramiko
+ GUI for OS (if necessary)

If you have CentOS 7 and no GUI is configured, use the environment_for_centos7.sh script located in the current repository.

Clone the repository and run the following command:

python3 diagnosis.py

## Using the Tool

Once the application is running, you'll be prompted to enter the following information:

+ Host: The IP address or hostname of the server you want to diagnose
+ Username: The username to use when connecting to the server via SSH
+ Password: The password to use when connecting to the server via SSH

Once you've entered this information, click the "Diagnose" button to connect to the server and retrieve the diagnostic information. The results will be displayed in a new window.

## Saving the Results

You can save the results by clicking the "Save Result" button. The results will be saved in a text file with the format of hostname_date_time.txt in the same directory where the script is running.

## Note

The script uses the paramiko library to establish the SSH connection and run commands on the server. If your server requires key-based authentication, this script will not work. To quickly enable password authentication for a user, use this script: https://github.com/glebbykov/pass_on.git

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
This script is just a simple example and it can be improved by adding more functionalities and error handling. Feel free to fork the repository and add your own improvements!






