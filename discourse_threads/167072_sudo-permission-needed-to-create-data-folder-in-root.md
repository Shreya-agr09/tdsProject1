# Thread URL: [https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072](https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072)

@Jivraj @carlton sir please help

When I am downloading the data folder after processing datagen.py , it is trying to download in root folder and it is facing permission error . how can we overcome this ?  
needs sudo permission all the time…  

image2100×216 100 KB
Here's a detailed description of the image content:

**Overall Impression:**

The image is a screenshot of a terminal window, likely running a Linux or Unix-like operating system.  It shows the command-line interface, displaying user input and system output.

**Textual Elements:**

1.  **Username and Hostname:**

    *   `vikramjncasr@ANJANEYA` is likely the username (`vikramjncasr`) and the hostname (`ANJANEYA`) of the system.  This is a standard format for the command prompt in many Linux/Unix shells.
2.  **Current Directory:**

    *   `: /mnt/c/IIT_Madras/TDS_Project_1$`  This indicates that the user's current working directory is `/mnt/c/IIT_Madras/TDS_Project_1`. This suggests that the user is potentially working on a project within a directory structure on their system.  The `c` likely indicates a drive letter, and the path is likely on a Windows Subsystem for Linux (WSL) environment.
3.  **Commands and Output:**

    *   `ls /` This is the primary command being executed. `ls` is the list command, and the `/` argument means "list the contents of the root directory".
    *   The output of the `ls /` command is a list of directories located in the root directory:
        *   `bin`
        *   `boot`
        *   `etc`
        *   `init`
        *   `lib.usr-is-merged`
        *   `lost+found`
        *   `mnt`
        *   `proc`
        *   `run`
        *   `sbin.usr-is-merged`
        *   `srv`
        *   `tmp`
        *   `var`
        *   `bin.usr-is-merged`
        *   `dev`
        *   `home`
        *   `lib`
        *   `lib64`
        *   `media`
        *   `opt`
        *   `root`
        *   `sbin`
        *   `snap`
        *   `sys`
        *   `usr`

**Color Coding:**

*   It appears there is a syntax highlighting applied for the `init` and `tmp` folder names.
*   The command prompt elements (username, hostname, current directory) have distinct colors, likely defined by the shell's configuration.
*   The output of the `ls` command (directory names) are typically displayed in a different color than the command itself.

**In summary, the image shows a user executing the `ls /` command in a terminal, displaying the contents of the root directory on their system.**
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072/1](https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072/1)
---
Hi Vikram,

This is because (if you watched the session, or examined the code, you would have realised that) datagen.py was designed to run inside your docker container. And datagen.py (or a similar named file which we will not tell you ahead of time and will be provided as the query parameter in task A1) will normally be called by evaluate.py  
Inside the docker container, permission for the data folder is set by the Dockerfile  
which then allows your application to access the root folder inside your docker image and create the /data folder.

So the workflow is like this (for your internal testing only… please follow the Project page for deliverables and evaluation to submit project successfully):

1. You create your application server that serves 2 endpoints on localhost:8000
2. You create a docker image that runs this application server.
3. You run the docker image using podman as described in the project page.
4. For mimicking the testing conditions. You need two files:  
   evaluate.py and datagen.py to be in the same folder where you are running these two scripts.
5. Run evalute.py using uv.

If your docker image is correctly configured and your application is correctly configured, then all the tasks run by evaluate.py will correctly tell you if the application is producing the right result for each task.

Hope that gives clarity.

Kind regards

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072/2](https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072/2)
---
@Jivraj @carlton sir please help

When I am downloading the data folder after processing datagen.py , it is trying to download in root folder and it is facing permission error . how can we overcome this ?  
needs sudo permission all the time…  

image2100×216 100 KB
Here is a detailed description of the image content:

The image appears to be a screenshot of a terminal window, likely running in a Linux or Unix-like environment. The terminal prompt indicates a user named "vikramjncasr" logged in as "ANJANEYA" on a system with a working directory of "/mnt/c/IIT_Madras/TDS_Project_1".

The command "ls /" has been executed. This command lists the contents of the root directory ("/"). The output lists standard directories found on a Unix-like system, including:

*   bin
*   boot
*   etc
*   init
*   lib.usr-is-merged
*   lost+found
*   mnt
*   proc
*   run
*   sbin.usr-is-merged
*   srv
*   tmp
*   var
*   bin.usr-is-merged
*   dev
*   home
*   lib
*   lib64
*   media
*   opt
*   root
*   sbin
*   snap
*   sys
*   usr

The terminal prompt reappears below the output of the "ls" command, indicating that the system is ready for further commands. The text "Professional Corner" appears at the top left. Overall, the image depicts a standard Linux/Unix environment.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072/1](https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072/1)
---
Hi Vikram,

This is because (if you watched the session, or examined the code, you would have realised that) datagen.py was designed to run inside your docker container. And datagen.py (or a similar named file which we will not tell you ahead of time and will be provided as the query parameter in task A1) will normally be called by evaluate.py  
Inside the docker container, permission for the data folder is set by the Dockerfile  
which then allows your application to access the root folder inside your docker image and create the /data folder.

So the workflow is like this (for your internal testing only… please follow the Project page for deliverables and evaluation to submit project successfully):

1. You create your application server that serves 2 endpoints on localhost:8000
2. You create a docker image that runs this application server.
3. You run the docker image using podman as described in the project page.
4. For mimicking the testing conditions. You need two files:  
   evaluate.py and datagen.py to be in the same folder where you are running these two scripts.
5. Run evalute.py using uv.

If your docker image is correctly configured and your application is correctly configured, then all the tasks run by evaluate.py will correctly tell you if the application is producing the right result for each task.

Hope that gives clarity.

Kind regards

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072/2](https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072/2)
---
