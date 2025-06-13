# Thread URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485](https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485)

Sir,

The License file is present in the github repository however i received a mail that said that it was absent.  

image1145×673 33.8 KB

  

image633×336 7.1 KB

Sir I thought that the ‘LICENSE’ file had to be renamed to ‘MIT LICENSE’.  
Can you please look into it. Thankyou!
The image is a screenshot of a Git repository browser, likely GitHub, GitLab, or Bitbucket.  It shows the contents of a repository named `tds_project-1`.

Here's a breakdown of the visible information:

* **Repository Name:** `tds_project-1` (marked as public)
* **Branch:** The repository is currently on the `main` branch, with one other branch present.
* **Tags:** No tags are present.
* **Commit History:** The right-hand side shows a summary of the six most recent commits, including the commit hash (`c61a6ef`), the commit message, and the time of the commit.  The commits include actions like creating a LICENSE file, renaming it to MIT LICENSE, and final submissions.  The timeline of the commits shows activities spanning over the past two months, with one commit made "now".
* **Files and Folders:** The left-hand side lists the files and folders within the repository, including:
    * `_pycache_` (a folder containing compiled Python bytecode)
    * `venv` (a virtual environment folder)
    * `Dockerfile` (indicates the project is designed to be containerized using Docker)
    * `LICENSE` (the original license file)
    * `MIT LICENSE` (the renamed license file)
    * `app.py` (likely the main application file)
    * `requirements.txt` (listing project dependencies)
    * `test.txt` (a test file)
* **Commit Details:** Each file or folder on the left has a corresponding commit message and timestamp on the right, indicating when and why that file was modified.

The interface is dark-themed, typical of many modern code hosting platforms.  The screenshot provides a snapshot of the repository's file structure and its recent activity.
 The image contains text output showing the results of a project evaluation. The top line warns that failure to meet minimum requirements will result in the submission not being evaluated.

The core of the image details the prerequisite evaluations for Project 1.  Each line checks for the presence and validity of different components:

* **Is Docker image present in dockerhub AND is public:** PASS (successful)
* **Is Github repo present AND public:** PASS (successful)
* **Is Dockerfile present in root of github repo:** PASS (successful)
* **Is MIT license present at root of github repo:** FAIL (unsuccessful)

Despite three prerequisites passing, the overall `Prerequisites` result is `FAIL` because one requirement (MIT license) failed.  The final line displays the project score as 0, likely due to the failure of the prerequisites.  The `Dockerfile` is highlighted in gray, possibly indicating it is a specific file name or term of importance.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/1](https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/1)
---
Hi @22f3000585

Standard MIT License naming criteria is to be named as LICENSE or LICENSE.md(all caps).

Adding a license to a repository - GitHub Docs

Kind regards

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/3](https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/3)
---
image931×108 3.89 KB

  
Sir, this is why i renamed it to ‘MIT LICENSE’.  
Sir can you please consider it. Thank you!
Here's a description of the image:

The image contains a text snippet, seemingly from an automated email or system message.  The main content explains that a submission to a system (likely a code submission or project evaluation) has failed.

The key details are:

* **Failed Submission:** The message clearly states that the submission resulted in a "FAIL".
* **GitHub Link:**  A GitHub repository link is provided: `https://github.com/22f3000585/tds_project-1.git`. This indicates the location of the submitted code.
* **Reasons for Failure:** The reasons for the failure are listed below the main statement:
    * `No such repo`: The provided GitHub repository does not exist.
    * `No "MIT" in LICENSE`:  A license file (LICENSE) was not found, or if found, it didn't contain the MIT license.
    * `No Dockerfile`: A Dockerfile, crucial for containerization, is missing.

The text `No` before "such repo",  "MIT", and "Dockerfile" is highlighted in a pale yellow. This highlights the missing elements as the main causes of failure.

The overall impression is that the submission failed because of basic project setup issues: the repository doesn't exist, there's a missing license, and it lacks a Dockerfile for deployment.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/4](https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/4)
---
Same here. I also added and saved the file as MIT license because of the following message. I request you to please consider evaluating the project.  

Screenshot 2025-04-02 at 4.49.23 PM1776×228 15.5 KB
The image contains a text-based message, likely part of an email or online submission platform feedback. Here's a breakdown of the text:

* **`No "MIT" in LICENSE;No Dockerfile`**: This line indicates that the submission is missing a MIT license and a Dockerfile. These are common components in software projects.

* **`Please ensure that your submission passes the above checklist for it to be even considered for scoring.`**: This statement clearly explains that a checklist (not shown in the image) must be completed for the submission to be evaluated.

* **`Note: We've only considered your latest submissions, as we permitted students to submit more than once.`**: This clarifying note explains that multiple submissions were allowed, but only the most recent one was assessed.  The word "latest" is underlined for emphasis.


The overall context suggests this is feedback concerning a graded assignment or project submission where specific criteria were not met.  The sender is informing the submitter of the reasons for a potential low score or non-consideration.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/5](https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/5)
---
@24ds2000125 @22f3000585

I completely appreciate that you feel these are minor issues.

But the team has decided that we cannot allow students to make changes to their repos. Because someone else might have another minor issue they want to fix. We have to apply the rule uniformly.

Unfortunately we cannot allow submissions that fail the prerequisites.  
Changing it now will not suddenly make it eligible.

These things do matter when done at scale. Its an important lesson Anand wants students to understand. These “minor” things matter.

Its a bit like assembling a rocket and forgetting the checklist for the pilot. Minor detail, costs Rs 2, but the rocket cannot leave without it.

We had a significant discussion about it internally. For the sake of fairness to everyone who got it right, we cannot allow edits after the Project deadline. It makes the prerequisites meaningless, especially when it was clearly stressed upon in the sessions and the Project page.

I know you will feel very disappointed but it is the decision the team has made and I have shared the reasons why.

Kindest regards

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/6](https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/6)
---
Sir,  
Thankyou for your prompt reply to my query.  
I wanted to let you know that i had made change of ‘LICENSE’ to ‘MIT LICENSE’ on the 16th of Feb itself as that was the day that i had received the mail and because I saw that the submission date had been extended by one day(i.e the 16th of Feb itself).  
I completely understand what you are trying to convey but that was the sole reason i made that change on the 16th.  
I completely respect your decision but if there is even a slight possibility that you consider it (only because I did it on the 16th) I would highly appreciate it.  
Thankyou!

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/7](https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/7)
---
One thing we are doing is looking at the latest commit before the 18th of Feb. So if it was correct before the 18th of Feb then we will consider it and evaluate it, but it has to be precisely what is expected. If so, then your submission will be evaluated by building the image from the docker manifest in the github present at the version before the 18th.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/8](https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/8)
---
Well noted sir. Thanks a lot!

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/9](https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/9)
---
Sir, I received the mail today -  

image652×156 5.43 KB

  
Sir, I had already added the LICENSE and changed it to’MIT LICENSE’ due to this reason before the deadline itself.  

image836×101 18.2 KB

  
Sir,the rest of my prerequistes are working well.Can you please check as due to this my project has also not been evaluated.The MIT LICENSE file was already present in the github repo as I submitted my project’s github repo in the google form that was provided.  

image1113×487 20.2 KB

  
Sir can you please check.  
Thankyou
The image contains a text-based log of a pre-requisites check.  The log is formatted as a list of checks and their results.  Each check has a description and a numerical result: 1 indicates success (pass) and 0 indicates failure (fail).

The checks are:

1. **Docker repo exists and is public:** This checks if a Docker repository exists and is publicly accessible.  The timestamp is also validated. Result: 1 (pass).

2. **Github repo exists and is public:** This checks if a Github repository exists and is publicly accessible.  The timestamp is also validated. Result: 1 (pass).

3. **Github repo check - LICENSE or LICENSE.md file exists:** This check verifies the presence of either a `LICENSE` or `LICENSE.md` file, indicating the presence of an MIT license. Result: 0 (fail).

4. **Github repo check - Dockerfile exists:** This checks if a `Dockerfile` exists in the Github repository. Result: 1 (pass).


There's a minor typo in the last line. "Gihub" should be "Github".
 Here's a description of the image:

The image shows a snippet of text, likely from an automated code submission review or build system. 


The text states:

"We see that your submission [link to github repo] has a result of FAIL due to the below reasons:"

Below this, a list of reasons for the failure is given:

"No such repo; No "MIT" in LICENSE; No Dockerfile"

This indicates that the submission failed because:

1. **The repository linked does not exist.**
2. **A file named `LICENSE` containing the MIT license is missing.**
3. **A `Dockerfile` is missing.**

The highlighted words ("No such repo," "No "MIT"", and "No Dockerfile") suggest that these were automatically detected as missing items, implying the system is checking for the presence of these specific files or conditions.
 The image shows a screenshot of a Git commit history, likely from a platform like GitHub or GitLab.  The top line shows the commit ID (`22f3000585`) and a message indicating the creation of a LICENSE file.  Next to it, the user `c61a6ef` and the time of the last commit (5 days ago) are visible, along with a commit count (6).

The rest of the image details the changes made in each commit, showing the file(s) affected and a brief description of the change.  It lists several files, including:

* `_pycache_` (a directory likely containing compiled Python bytecode)
* `venv` (a virtual environment directory)
* `Dockerfile` (a file defining a Docker container)
* `LICENSE` (an initial license file, later renamed)
* `MIT LICENSE` (the renamed license file)
* `app.py` (the main application file)
* `requirements.txt` (a file listing project dependencies)
* `test.txt` (a test file)


For each file, the description of the commit mentions either a "Final Submission" or "First submission," indicating stages of development.  The timestamps reveal that most modifications were done approximately 2 months ago, except for the final commit updating the LICENSE file.  The visual style is dark, common for many code hosting platforms.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/10](https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/10)
---
Sir,

The License file is present in the github repository however i received a mail that said that it was absent.  

image1145×673 33.8 KB

  

image633×336 7.1 KB

Sir I thought that the ‘LICENSE’ file had to be renamed to ‘MIT LICENSE’.  
Can you please look into it. Thankyou!
This image shows a screenshot of a Git repository's file structure and commit history within a code hosting platform, likely GitHub or GitLab. 


Here's a breakdown of the visible elements:

* **Repository Name:** The repository is named `tds_project-1` and is marked as public.

* **Branch and Tags:** It shows one branch (`main`) and zero tags.

* **Commit History:** The rightmost column displays a concise history of six commits, showing the commit message and timestamp ("2 months ago" or "now").  Each file change is linked to a specific commit.

* **File Structure:** The left-hand column displays the files and directories within the repository.  Notable files include:
    * `_pycache_`: A directory containing compiled Python bytecode.
    * `venv`: A virtual environment directory.
    * `Dockerfile`: A file for building Docker images.
    * `LICENSE`: A license file (initially created, then renamed).
    * `MIT LICENSE`: The renamed license file (MIT License).
    * `app.py`: Likely the main application file.
    * `requirements.txt`: A file listing project dependencies.
    * `test.txt`: A test file.

* **Commit Messages:** The middle column lists concise descriptions of each commit action, such as "Final Submission," "First submission," "Create LICENSE," and "Rename LICENSE to MIT LICENSE."

* **Top Bar:** The top bar contains standard UI elements like "Pin," "Unwatch," "Go to file," and "Add file."  There's also a code view toggle.

* **Commit ID:** `c61a6ef` is shown as the most recent commit hash.


In short, the image provides a quick overview of a project's file structure, its commit history, and the evolution of the project's licensing. The use of a virtual environment (`venv`) and a `Dockerfile` suggests a structured project setup for software development.
 The image contains a text-based report showing the results of a project evaluation. 


Here's a breakdown of the content:

* **Top Warning:** A prominent warning message states that failure to meet minimum requirements will prevent submission evaluation.

* **Project 1 Prerequisite Evaluations:** This section lists several checks performed on the project submission, with a "PASS" or "FAIL" status for each:
    * `Is Docker image present in dockerhub AND is public: PASS`
    * `Is Github repo present AND public: PASS`
    * `Is Dockerfile present in root of github repo: PASS`
    * `Is MIT license present at root of github repo: FAIL`

* **Overall Status:** Based on the individual checks, the overall prerequisites evaluation is marked as `Prerequisites: FAIL`.

* **Project Score:** Consequently, the project receives a score of `Project 1 Score: 0`.

The crucial element is the failure to include an MIT license, which caused the overall project evaluation to fail despite passing other checks.  The `Dockerfile` is highlighted in grey, likely to emphasize its importance.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/1](https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/1)
---
Hi @22f3000585

Standard MIT License naming criteria is to be named as LICENSE or LICENSE.md(all caps).

Adding a license to a repository - GitHub Docs

Kind regards

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/3](https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/3)
---
image931×108 3.89 KB

  
Sir, this is why i renamed it to ‘MIT LICENSE’.  
Sir can you please consider it. Thank you!
Here's a description of the image:

The image shows a text snippet, likely from an automated email or system message. 


The text explains that a submission to a system (likely a code submission platform) has failed. The reasons for the failure are listed below:

* **"No such repo"**:  The repository linked (a GitHub repository, judging by the URL) could not be found.
* **"No "MIT" in LICENSE"**: The repository didn't contain a license file with the MIT license.
* **"No Dockerfile"**:  The repository lacked a `Dockerfile`, which is necessary for containerized applications.

The GitHub URL is partially visible: `https://github.com/22f3000585/tds_project-1.git`. This is likely the location where the code was supposed to be.  The highlighted words ("No," "MIT," and "No") are visually emphasized, possibly by being in a different color or font style than the surrounding text.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/4](https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/4)
---
Same here. I also added and saved the file as MIT license because of the following message. I request you to please consider evaluating the project.  

Screenshot 2025-04-02 at 4.49.23 PM1776×228 15.5 KB
The image contains a text message, likely an automated email response or a portion of one.  The message is formatted simply, with three distinct sections:

1. **Header:** "No "MIT" in LICENSE;No Dockerfile"  This line indicates a missing MIT license and Dockerfile in a submission.

2. **Checklist Requirement:** "Please ensure that your submission passes the above checklist for it to be even considered for scoring." This emphasizes that the submission must meet certain criteria to be evaluated. The "above checklist" is not visible in the image.

3. **Submission Note:** "Note: We've only considered your latest submissions, as we permitted students to submit more than once." This clarifies that only the most recent submission from a student will be considered, acknowledging that multiple submissions were allowed.

The overall message suggests that the submission under review had a problem and that the submitter should check a missing checklist to ensure their work meets requirements for evaluation.  The message is likely part of an automated grading or review process.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/5](https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/5)
---
@24ds2000125 @22f3000585

I completely appreciate that you feel these are minor issues.

But the team has decided that we cannot allow students to make changes to their repos. Because someone else might have another minor issue they want to fix. We have to apply the rule uniformly.

Unfortunately we cannot allow submissions that fail the prerequisites.  
Changing it now will not suddenly make it eligible.

These things do matter when done at scale. Its an important lesson Anand wants students to understand. These “minor” things matter.

Its a bit like assembling a rocket and forgetting the checklist for the pilot. Minor detail, costs Rs 2, but the rocket cannot leave without it.

We had a significant discussion about it internally. For the sake of fairness to everyone who got it right, we cannot allow edits after the Project deadline. It makes the prerequisites meaningless, especially when it was clearly stressed upon in the sessions and the Project page.

I know you will feel very disappointed but it is the decision the team has made and I have shared the reasons why.

Kindest regards

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/6](https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/6)
---
Sir,  
Thankyou for your prompt reply to my query.  
I wanted to let you know that i had made change of ‘LICENSE’ to ‘MIT LICENSE’ on the 16th of Feb itself as that was the day that i had received the mail and because I saw that the submission date had been extended by one day(i.e the 16th of Feb itself).  
I completely understand what you are trying to convey but that was the sole reason i made that change on the 16th.  
I completely respect your decision but if there is even a slight possibility that you consider it (only because I did it on the 16th) I would highly appreciate it.  
Thankyou!

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/7](https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/7)
---
One thing we are doing is looking at the latest commit before the 18th of Feb. So if it was correct before the 18th of Feb then we will consider it and evaluate it, but it has to be precisely what is expected. If so, then your submission will be evaluated by building the image from the docker manifest in the github present at the version before the 18th.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/8](https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/8)
---
Well noted sir. Thanks a lot!

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/9](https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/9)
---
Sir, I received the mail today -  

image652×156 5.43 KB

  
Sir, I had already added the LICENSE and changed it to’MIT LICENSE’ due to this reason before the deadline itself.  

image836×101 18.2 KB

  
Sir,the rest of my prerequistes are working well.Can you please check as due to this my project has also not been evaluated.The MIT LICENSE file was already present in the github repo as I submitted my project’s github repo in the google form that was provided.  

image1113×487 20.2 KB

  
Sir can you please check.  
Thankyou
The image contains a text output showing a pre-requisites check.  The check has four components:

1. **Docker repo check:**  Verifies that a Docker repository exists and is public, with a creation timestamp before February 18th. The result is `1`, indicating a pass.

2. **Github repo check:** Similar to the Docker check, it verifies the existence and public status of a GitHub repository, also requiring a timestamp before February 18th. The result is `1`, a pass.

3. **Github repo license check:** This checks for the existence of either a `LICENSE` or `LICENSE.md` file, indicating an MIT License. The result is `0`, indicating a fail.

4. **Github repo Dockerfile check:** This confirms the presence of a `Dockerfile` in the GitHub repository. The result is `1`, a pass.

The header indicates that `1` signifies a successful check, and `0` represents failure.  There's a minor typo in the last line ("Gihub" instead of "Github").
 This image shows a snippet of text from what appears to be an automated build or submission process.  The message indicates a failure ("FAIL") for a submission made to a system. The submission's location is identified by a GitHub repository link: `https://github.com/22f3000585/tds_project-1.git`.

The reasons for the failure are listed below:

* **No such repo:** The system couldn't find the specified GitHub repository.
* **No "MIT" in LICENSE:** The repository is missing a LICENSE file with the MIT license.
* **No Dockerfile:**  A Dockerfile, necessary for building container images, is absent from the repository.


These three reasons are likely the cause of the build or submission's failure.  The highlighted words "No" and "MIT" indicate the parts of the error message that are critical.
 The image shows a code repository commit history, likely from a platform like GitHub or GitLab.  The top line shows the repository ID (`22f3000585`) and the initial commit message ("Create LICENSE").  The author (`c61a6ef`) and the time since the last commit ("5 days ago") are also displayed, along with a count of commits ("6 Commits").

The main part of the image lists the files changed in each commit.  Each row includes:

* **File or directory name:**  This could be a Python file (`app.py`), a requirements file (`requirements.txt`), a test file (`test.txt`), a Dockerfile, a license file (`LICENSE`, `MIT LICENSE`), a virtual environment directory (`venv`), or a cache directory (`_pycache_`).

* **Commit message:**  A short description of the change made in that commit, such as "Final Submission", "First submission", or "Rename LICENSE to MIT LICENSE".

* **Time since commit:** This shows how long ago each commit was made ("2 months ago" or "5 days ago").

The image is dark-themed, with light-colored text for easy readability.  The file icons clearly indicate the type of file (folders, text files).  The information presented gives a concise overview of the repository's recent activity.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/10](https://discourse.onlinedegree.iitm.ac.in/t/project-1-discrepancy-regarding-mit-license/171485/10)
---
