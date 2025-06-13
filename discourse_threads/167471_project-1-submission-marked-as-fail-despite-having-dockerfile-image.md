# Thread URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471)

Dear TDS Team,

I have verified my submission, and my repository **does include a Dockerfile**, and the **Docker image is accessible on DockerHub**. Please find the attached screenshot as proof. Kindly review my submission again and let me know if any further action is needed.

Looking forward to your confirmation.

Best regards,  
Arnav Mehta  
(21f3002647)

image250×534 3.92 KB

  

image713×238 11 KB
The image shows a file directory listing, likely from a code editor or file explorer. It displays several files and folders within a project.

Here's a breakdown:

*   **Folders:**
    *   `..` (Indicates going up one level in the directory structure)
    *   `LLM_PROJECT1`
    *   `__pycache__` (A Python-generated folder for compiled bytecode files)
*   **Files:**
    *   `Dockerfile` (Configuration file for Docker image creation)
    *   `LICENSE` (Text file specifying the license under which the code is released)
    *   `app.py` (likely the main application file written in Python)
    *   `datagen.py` (Python file potentially for generating data)
    *   `evaluate.py` (Python file, likely for evaluation code)
    *   `requirements.txt` (Text file listing Python packages required for the project)
    *   `tasksA.py` (Python file)
    *   `tasksB.py` (Python file)

The consistent `.py` extensions indicate that this is a Python project. The `Dockerfile` suggests the project can be containerized using Docker. The presence of `requirements.txt` is standard for Python projects to manage dependencies. Overall, the contents point to a structured project, possibly for machine learning or a language model (given the folder name LLM\_PROJECT1), with defined tasks, data generation, and evaluation components.
 Here is a detailed description of the content of the image:

The image appears to be a screenshot from a website or application, possibly related to software development or image hosting. It features the following elements:

*   **Icon:** On the left side, there's a stylized cube icon with two vertical bars on one of its faces. The icon is a muted blue-grey color.
*   **Text:** To the right of the icon, the text "arnavmehta2025/llm\_project1" is displayed prominently in a white or light-colored font. Below this, it reads "By arnavmehta2025," where the name "arnavmehta2025" is underlined in blue, indicating a hyperlink. Further to the right, it says "Updated 2 days ago."
*   **Label:** Below the author and update information, there's a small dark blue label that reads "IMAGE" in white text.
*   **Social Icons:** At the bottom, there are two icons: a star and an arrow pointing downwards. The number "0" is next to the star, and the number "16" is next to the down arrow. These likely represent likes/favorites and downloads, respectively.
*   **Background:** The background is a dark, muted blue color.

In summary, the image shows information about an item (likely an image) named "llm\_project1" hosted by "arnavmehta2025." It includes its upload or update date, its designation as an "IMAGE", and its current metrics for likes and downloads.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/1](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/1)
---
@Saransh\_Saini sir what should i do?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/2](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/2)
---
@carlton Kindly have a look into this.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/3](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/3)
---
Good Morning Sir,  
Sir even I am facing a similar issue, even though sanity check for docker image on docker hub was cleared but got a mail saying ‘dockerfile’ not present in the GitHub repo while it clearly was. Sir please look into it we have given so many days to complete this project.

Looking forward to your reply.

Thank you  
Satvik Sawhney  
23f2003680

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/8](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/8)
---
So the reason for the failure is:

You had initially put your Dockerfile inside a directory called TDSP-1-main instead of being directly in your repo. (On 15th Feb 1:26AM)

Then when our automated script checked if students repos met the requirements and yours did not we immediately sent out a warning email as a opportunity for students to make the necessary corrections.

Then once you realised your mistake, on **Feb 17th at 9:11 pm IST** i.e *yesteday*, you changed your repo to put the files in the correct locations.

Then you finally posted here on Discourse with the image [quote=“21f3002647, post:1, topic:167471”]  

image250×534 3.92 KB

  
[/quote]

showing that your files are in the correct place.

We do not take into consideration modifications to your repo after the deadline because then we would have to extend that curtesy to all students.

Kind regards
The image shows a file directory structure, likely from a code editor or file explorer, displayed in a dark theme. Here's a detailed breakdown:

**Folders (Directories):**

*   `..`: Indicates the parent directory.
*   `LLM_PROJECT1`:  A folder likely containing project-related files. The name suggests it's related to a Large Language Model project.
*   `__pycache__`:  A standard Python directory used for storing compiled bytecode files.

**Files:**

*   `Dockerfile`:  A text file containing instructions for building a Docker image.
*   `LICENSE`:  A text file defining the terms and conditions under which the software can be used, distributed, and modified.
*   `app.py`:  A Python file, likely the main application script.
*   `datagen.py`:  A Python file, possibly responsible for data generation or preprocessing.
*   `evaluate.py`:  A Python file, probably used for evaluating the performance of a model.
*   `requirements.txt`:  A text file listing the Python packages (dependencies) required to run the project.
*   `tasksA.py`:  A Python file, likely containing functions or code related to a specific set of tasks labeled 'A'.
*   `tasksB.py`:  A Python file, likely containing functions or code related to a specific set of tasks labeled 'B'.

In summary, the directory structure appears to be a Python project with dependencies, a Dockerfile for containerization, and various Python scripts for the main application, data generation, evaluation, and task management. The presence of "LLM" in the project folder's name suggests it's related to developing or working with a large language model.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/9](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/9)
---
@carlton sir  
Yes, I corrected my repo at 9:11 PM IST, but I had actually written and submitted my query much earlier at 4 PM. At that time, I wasn’t entirely sure if this was the actual issue, but it looks like it was.

I understand that the deadline had already passed, and I only saw the email later. I had two GATE papers on the 15th and an interview on the 16th, so I was extremely busy and couldn’t check my emails sooner. However, I had raised my concern well before making the correction, so I’d really appreciate it if my submission could still be considered

Kind regards,  
Arnav Mehta  
21f3002647
Certainly! Here's a breakdown of the image content:

**Description:**

*   The image shows a yellow emoji representing a sad or unhappy face.
*   The emoji has a circular yellow face.
*   It features two dark brown, round eyes and a downturned black line forming a sad frowning mouth.

This emoji is commonly used to express feelings of sadness, disappointment, or unhappiness.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/10](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/10)
---
Sir, please consider it we have spent a lot of time, in my case just the d in Dockerfile was small that too on remote repository. On my local repository it was Dockerfile only I even have a published docker image as verified by you autated script only. The name of the file on remote repository did not change even after commit it through my local repo, once I read the mail in morning it was only then I realised it wasn’t changed on GitHub repo.

Sir I understand the deadline has passed and I am not asking for a resubmission, I am just asking to consider the already submitted work, just that. It would be really helpful. I just have one commit on my repo that too “Rename dockerfile to Dokerfile” . Sir please attest consider what we have already submitted. I have made no changes as you can verify it too.

Sir it is a humble request to please consider it.

Warm Regards,  
Satvik Sawhney  
23f2003680

Screenshot 2025-02-18 at 1.53.10 PM1889×467 54 KB
Here's a detailed description of the content in the image:

The image presents a list of files and folders within a directory structure, likely in a code repository or file management system. It has a dark theme.

**File/Folder List:**

*   **Business (Folder):** Description states "Reconfigured taskB8 taskB9 taskB10" with modification date "2 days ago".
*   **Operations (Folder):**  Description states "Reconfigured taskA8 taskA9 taskA10" with modification date "2 days ago".
*   **app (Folder):** Description states "Updated Dockerfile and requirements.txt" with modification date "2 days ago".
*   **Dockerfile (File):**  Description states "Rename dockerfile to Dockerfile" with modification date "yesterday".
*   **LICENSE (File):**  Description states "MIT License" with modification date "3 days ago".
*   **README.md (File):** Description states "Project Structure" with modification date "3 days ago".

To the right of the modification dates are some icons:
*   A law scale icon
*   A waveform icon
*   A star icon
*   An eye icon
*   A "connected components" icon
*   The beginning of the word "Re"

**General Observations:**

*   The image gives a snapshot of a code repository or project directory and recent commits.
*   The modification dates provide a sense of the activity within the directory.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/11](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/11)
---
Dear TDS Team,

I have verified my submission, and my repository **does include a Dockerfile**, and the **Docker image is accessible on DockerHub**. Please find the attached screenshot as proof. Kindly review my submission again and let me know if any further action is needed.

Looking forward to your confirmation.

Best regards,  
Arnav Mehta  
(21f3002647)

image250×534 3.92 KB

  

image713×238 11 KB
The image shows a file directory structure in a dark-themed interface, likely a code editor or file explorer. Here's a breakdown of the content:

*   **Folders:**
    *   ".." (likely the parent directory)
    *   "LLM\_PROJECT1"
    *   "\_\_pycache\_\_"
*   **Files:**
    *   "Dockerfile"
    *   "LICENSE"
    *   "app.py"
    *   "datagen.py"
    *   "evaluate.py"
    *   "requirements.txt"
    *   "tasksA.py"
    *   "tasksB.py"

The file extensions ".py" indicate that "app.py," "datagen.py," "evaluate.py," "tasksA.py," and "tasksB.py" are Python files. "requirements.txt" is a common file for specifying Python dependencies. "Dockerfile" suggests that the project is intended to be containerized using Docker. "LICENSE" indicates a license file.
 Here's a detailed description of the image:

The image shows a dark-themed UI element likely from a website or application that hosts or displays software projects.

*   **Icon:** On the left is a stylized icon resembling a cube or a box. The lines are bold and blue-grey in color, contrasting with the dark background.

*   **Project Name:** To the right of the icon, the text "arnavmehta2025/llm\_project1" is prominently displayed. The first part "arnavmehta2025" might indicate the username or organization name, while "llm\_project1" represents the project's name.

*   **Author and Update Info:** Below the project name, in smaller font, it says "By arnavmehta2025". The username is a hyperlink (as seen by the underlining). Next to it, "Updated 2 days ago" indicates the project was last updated recently.

*   **Type Label:** There is a small, dark blue box that contains the word "IMAGE" in white text.

*   **Metrics:** At the bottom, there are two icons:
    *   A star icon, followed by "0", suggesting the project has zero stars.
    *   A download icon with a downward arrow, followed by "16", indicating the project has been downloaded 16 times.

In summary, the image is a UI element displaying information about a software project ("llm\_project1") created by "arnavmehta2025", which was updated 2 days ago and has 0 stars and 16 downloads. The project is tagged as an "IMAGE".
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/1](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/1)
---
@Saransh\_Saini sir what should i do?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/2](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/2)
---
@carlton Kindly have a look into this.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/3](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/3)
---
Good Morning Sir,  
Sir even I am facing a similar issue, even though sanity check for docker image on docker hub was cleared but got a mail saying ‘dockerfile’ not present in the GitHub repo while it clearly was. Sir please look into it we have given so many days to complete this project.

Looking forward to your reply.

Thank you  
Satvik Sawhney  
23f2003680

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/8](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/8)
---
So the reason for the failure is:

You had initially put your Dockerfile inside a directory called TDSP-1-main instead of being directly in your repo. (On 15th Feb 1:26AM)

Then when our automated script checked if students repos met the requirements and yours did not we immediately sent out a warning email as a opportunity for students to make the necessary corrections.

Then once you realised your mistake, on **Feb 17th at 9:11 pm IST** i.e *yesteday*, you changed your repo to put the files in the correct locations.

Then you finally posted here on Discourse with the image [quote=“21f3002647, post:1, topic:167471”]  

image250×534 3.92 KB

  
[/quote]

showing that your files are in the correct place.

We do not take into consideration modifications to your repo after the deadline because then we would have to extend that curtesy to all students.

Kind regards
Here is a detailed description of the content of the image:

The image shows a file directory or file explorer view, likely within a software development environment.  The background is a dark blue/grey.  There are a mix of files and folders.

The following are the files and folders listed in the directory:

*   `..` (This usually indicates navigating to the parent directory).  It's depicted as a folder icon.
*   `LLM_PROJECT1` (Folder icon)
*   `__pycache__` (Folder icon)
*   `Dockerfile` (File icon)
*   `LICENSE` (File icon)
*   `app.py` (File icon)
*   `datagen.py` (File icon)
*   `evaluate.py` (File icon)
*   `requirements.txt` (File icon)
*   `tasksA.py` (File icon)
*   `tasksB.py` (File icon)

The filenames ending in `.py` suggest these are Python source code files. `requirements.txt` is a common file for specifying Python package dependencies. `Dockerfile` is related to containerization, and `LICENSE` indicates a license file for the project. The folder names `LLM_PROJECT1` and the filenames suggest that this project is probably related to the development of an LLM model, or Large Language Model, and the files `evaluate.py`, `datagen.py`, `tasksA.py` and `tasksB.py` provide supporting functions for the model.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/9](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/9)
---
@carlton sir  
Yes, I corrected my repo at 9:11 PM IST, but I had actually written and submitted my query much earlier at 4 PM. At that time, I wasn’t entirely sure if this was the actual issue, but it looks like it was.

I understand that the deadline had already passed, and I only saw the email later. I had two GATE papers on the 15th and an interview on the 16th, so I was extremely busy and couldn’t check my emails sooner. However, I had raised my concern well before making the correction, so I’d really appreciate it if my submission could still be considered

Kind regards,  
Arnav Mehta  
21f3002647
Here's a detailed description of the image:

**Content:**

The image shows a single emoji: a sad face.

**Features:**

*   **Shape:** The emoji is a perfect circle.
*   **Color:** The background of the face is a bright, light yellow.
*   **Facial Features:**
    *   Eyes: It has two small, round, dark brown or black eyes. The eyes lack any distinct highlights or pupils, giving them a slightly flat, sad appearance.
    *   Mouth: The mouth is a downturned curve or frown, also in a dark brown or black color. It is simple and suggests sadness or disappointment.

**Overall Impression:**

The image clearly conveys the emotion of sadness or unhappiness. The simplicity of the emoji makes it easily recognizable and understandable.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/10](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/10)
---
Sir, please consider it we have spent a lot of time, in my case just the d in Dockerfile was small that too on remote repository. On my local repository it was Dockerfile only I even have a published docker image as verified by you autated script only. The name of the file on remote repository did not change even after commit it through my local repo, once I read the mail in morning it was only then I realised it wasn’t changed on GitHub repo.

Sir I understand the deadline has passed and I am not asking for a resubmission, I am just asking to consider the already submitted work, just that. It would be really helpful. I just have one commit on my repo that too “Rename dockerfile to Dokerfile” . Sir please attest consider what we have already submitted. I have made no changes as you can verify it too.

Sir it is a humble request to please consider it.

Warm Regards,  
Satvik Sawhney  
23f2003680

Screenshot 2025-02-18 at 1.53.10 PM1889×467 54 KB
Here is a detailed description of the image:

The image is a screenshot of a file directory structure, likely from a code repository like GitHub or GitLab, presented in a dark mode interface. Here's a breakdown of the elements:

**Directory Structure:**
- **Folders:**
    - "Business"
    - "Operations"
    - "app"

- **Files:**
    - "Dockerfile"
    - "LICENSE"
    - "README.md"

**Commit Messages/Descriptions:**
- For "Business": "Reconfigured taskB8 taskB9 taskB10"
- For "Operations": "Reconfigured taskA8 taskA9 taskA10"
- For "app": "Updated Dockerfile and requirements.txt"
- For "Dockerfile": "Rename dockerfile to Dockerfile"
- For "LICENSE": "MIT License"
- For "README.md": "Project Structure"

**Dates:**
- Folders "Business," "Operations," and "app" were last modified "2 days ago."
- "Dockerfile" was last modified "yesterday."
- "LICENSE" and "README.md" were last modified "3 days ago."

**Icons:**
- Each folder has a folder icon.
- Each file has a document icon indicating the type of file.

**Overall Impression:**
The image shows a repository with a mix of folders and files, giving context to changes made within the past few days. The commit messages provide a glimpse into the work being done, such as reconfiguring tasks and updating dependencies.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/11](https://discourse.onlinedegree.iitm.ac.in/t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/11)
---
