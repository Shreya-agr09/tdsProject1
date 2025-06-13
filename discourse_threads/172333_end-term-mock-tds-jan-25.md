# Thread URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333)

Mock Exam: Tools in Data Science
================================

#### The end term and the mock has been created using the TDS GPT Assistant. Since the GPT has ALL the GAs, Course Content Modules, Live Session Transcriptions (its works like RAG), it is really able to help you prepare for the end term. Use it!

Therefore you can also create your own mocks.

ChatGPT

### ChatGPT - IITM TDS Teaching Assistant

TA for IIT Madras' Data Science course, guiding students with questions.

Below are variant questions across various topics relevant to the course. These questions have been curated from the topics areas we are focussing on. Therefore it will be very similar in content to the end term.

> What it does not contain: Scenario based questions. These are complex to construct. We will address the topics for these questions in the live session.

* LLMs
* Pandas
* Git, Docker, Bash

---

### Q1: HTTP Method Semantics

Which HTTP method is **not idempotent**, meaning repeated identical requests **may** result in different outcomes each time?

* A. GET
* B. PUT
* C. POST
* D. DELETE

**Answer**: C. POST

### Q2: IDE Features

Which feature is **least likely** to be found in a standard code editor or IDE?

* A. Code formatting tools
* B. Integrated terminal
* C. Git integration
* D. Cloud hosting of Docker containers

**Answer**: D. Cloud hosting of Docker containers

### Q3: Pandas Summary Methods

You have a DataFrame with a `region` column. To get a quick summary of how many entries are in each region, which method is most useful?

* A. df.describe()
* B. df[“region”].value\_counts()
* C. df.count()
* D. df.groupby(“region”).sum()

**Answer**: B. df[“region”].value\_counts()

### Q4: Python Exception Scope

You want to safely open a file, handle any errors, and ensure the file is always closed in Python. Which pattern should you use?

* A. `try: open(...)` then `finally: close()`
* B. `open()` and then `except`
* C. `open()` and then `raise`
* D. Use `with open(...) as f:` block

**Answer**: D. Use `with open(...) as f:` block

### Q5: Chrome DevTools - Debugging

A frontend developer wants to trace JavaScript function calls step-by-step. Which **Chrome DevTools** panel should they use?

* A. Console
* B. Application
* C. Sources
* D. Elements

**Answer**: C. Sources

### Q6: Data Cleaning Tools

You are cleaning survey responses and want to automatically match similar text entries like “NYC”, “New York City”, and “newyorkcity”. Which approach/tool would be most effective?

* A. `TRIM()` in Excel
* B. Manual Find and Replace
* C. Fuzzy matching or clustering in OpenRefine
* D. COUNTIF()

**Answer**: C. Fuzzy matching or clustering in OpenRefine

### Q7: Geospatial Libraries

Which pair of Python libraries is best suited for **geospatial analysis** and **rendering static maps**?

* A. pandas and seaborn
* B. geopandas and matplotlib
* C. folium and flask
* D. sklearn and dash

**Answer**: B. geopandas and matplotlib

### Q8: Statistical Significance

A psychologist tests if a training program changes memory performance and finds a p-value of **0.08**. What can be concluded at the 0.05 significance level?

* A. The result is highly significant
* B. The null hypothesis must be rejected
* C. There is insufficient evidence to reject the null hypothesis
* D. The program is proven to work

**Answer**: C. There is insufficient evidence to reject the null hypothesis

### Q9: Purpose of Kumu

What is a key use case for a tool like **Kumu**?

* A. Animating time series
* B. Designing deep learning models
* C. Visualizing stakeholder networks and system relationships
* D. Performing statistical analysis

**Answer**: C. Visualizing stakeholder networks and system relationships

### Q10: DevTools Performance Diagnostics

To diagnose a slow webpage, you want to **analyze scripts, rendering times, and long tasks**. Which DevTools panel provides a timeline-based view?

* A. Elements
* B. Performance
* C. Network
* D. Lighthouse

**Answer**: B. Performance

### Q11: Git Configuration

Which of the following files helps configure a Git project’s name, email, and default branch?

* A. `.gitignore`
* B. `.gitattributes`
* C. `.git/config`
* D. `README.md`

**Answer**: C. `.git/config`

### Q13: Safe HTTP Method

Which HTTP method is considered **safe**, meaning it is only used for retrieval and **must not change** server state?

* A. GET
* B. DELETE
* C. PATCH
* D. POST

**Answer**: A. GET

### Q14: Deduplicating Text Entries

A dataset has entries like “IBM”, “I.B.M.”, and “International Business Machines”. What is the best tool to cluster these for cleaning?

* A. Excel TRIM
* B. OpenRefine using key collision or fingerprinting
* C. pandas merge()
* D. CONCATENATE()

**Answer**: B. OpenRefine using key collision or fingerprinting

### Q15: Geospatial + Interactive Mapping

A conservation biologist wants to visualize real-time animal tracking data on an interactive map. Which libraries would be best?

* A. geopandas and plotly
* B. folium and pandas
* C. seaborn and shapely
* D. rasterio and altair

**Answer**: B. folium and pandas

### Q16: Pandas - Filtering Unique Entries

You have a DataFrame of customer orders and want to list only those customers who ordered **once**. Which Pandas method chain is most suitable?

* A. df.groupby(“customer”).sum()
* B. df[“customer”].value\_counts() == 1
* C. df.drop\_duplicates()
* D. df[“customer”].nunique()

**Answer**: B. df[“customer”].value\_counts() == 1

### Q17: Purpose of Kumu in System Design

How does Kumu help in system design or stakeholder mapping?

* A. Organizing spreadsheets
* B. Identifying leverage points in complex systems through visual maps
* C. Rendering line graphs
* D. Sending notifications

**Answer**: B. Identifying leverage points in complex systems through visual maps

### Q18: Python Exception - Multiple Handlers

Which structure allows Python to handle different types of exceptions separately?

* A. `try`…`finally`
* B. `if`…`else`
* C. Multiple `except` blocks
* D. Nested `try` blocks

**Answer**: C. Multiple `except` blocks

### Q19: Understanding Statistical Power

If a study has **low statistical power**, what is most likely to occur?

* A. False positive (Type I error)
* B. False negative (Type II error)
* C. Confounding
* D. Multicollinearity

**Answer**: B. False negative (Type II error)

### Q20: Git Basics - Staging Area

Which Git command moves modified files to the **staging area**?

* A. git push
* B. git add
* C. git fetch
* D. git init

**Answer**: B. git add

### Q21: Chrome DevTools - Local Storage

Where can you inspect **local storage** items (e.g. tokens, preferences) in Chrome DevTools?

* A. Console
* B. Application > Local Storage
* C. Elements
* D. Sources

**Answer**: B. Application > Local Storage

### Q22: Chrome DevTools - JS Performance

Which DevTools feature helps measure execution time of scripts and CPU usage?

* A. Console
* B. Network
* C. Performance
* D. Application

**Answer**: C. Performance

### Q23: Excel Data Import - Scientific Notation Issue

You import a CSV file where product IDs like `"1E10"` are being interpreted as scientific notation in Excel. What is the best way to preserve these IDs as text?

* A. Format the column as General
* B. Use `=TEXT(A1, "0")` after import
* C. Set column format to Text during import or Text-to-Columns
* D. Change regional settings

**Answer**: C. Set column format to Text during import or Text-to-Columns

---

### Module: Everyday Tools

**Q1: Spreadsheet Functions**

You have a dataset in Excel where column A contains full names in the format “Last Name, First Name”. Which function can you use to extract the first name into a separate column?

* A. `=LEFT(A1, FIND(",", A1)-1)`
* B. `=RIGHT(A1, LEN(A1) - FIND(",", A1))`
* C. `=MID(A1, FIND(",", A1)+2, LEN(A1))`
* D. `=SPLIT(A1, ",")`

**Answer**: C — The `MID` function extracts text from the middle of a string. By finding the position of the comma and adding 2 (to skip the comma and space), it extracts the first name. Option A extracts the last name, Option B results in an error due to incorrect syntax, and Option D is not a valid Excel function.

---

### Module: Data Sourcing

**Q2: Web Scraping Ethics**

When performing web scraping to collect data, which of the following practices is considered unethical?

* A. Respecting the website’s `robots.txt` file.
* B. Sending requests at a rate that mimics human browsing behavior.
* C. Scraping data from a website that requires login without permission.
* D. Citing the source of the data collected.

**Answer**: C — Scraping data from a website that requires login without permission violates the site’s terms of service and user privacy. Options A, B, and D are ethical practices that respect the website’s policies and data ownership.

---

### Module: Data Preparation

**Q3: Handling Missing Data**

In a dataset, you notice that several entries in the “Age” column are missing. Which method is generally **not** appropriate for handling these missing values?

* A. Replacing missing values with the mean age.
* B. Deleting rows with missing age values.
* C. Replacing missing values with a fixed age, such as 0.
* D. Leaving the missing values as they are without any action.

**Answer**: D — Leaving missing values unaddressed can lead to errors in analysis and modeling. Options A, B, and C are common strategies for handling missing data, depending on the context and the extent of the missingness.

---

### Module: Data Analysis

**Q4: Statistical Measures**

Which of the following statistical measures is **not** sensitive to extreme values (outliers) in a dataset?

* A. Mean
* B. Median
* C. Standard Deviation
* D. Range

**Answer**: B — The median represents the middle value of a dataset and is not affected by outliers. In contrast, the mean, standard deviation, and range can be significantly influenced by extreme values.

---

### Module: Large Language Models

**Q5: Tokenization in NLP**

In Natural Language Processing, what is the primary purpose of tokenization?

* A. To translate text from one language to another.
* B. To split text into individual words or subwords.
* C. To encrypt text for secure communication.
* D. To summarize large texts into shorter versions.

**Answer**: B — Tokenization involves breaking down text into smaller components, such as words or subwords, which can then be processed by language models. This is a fundamental step in NLP tasks.

---

### Module: Geospatial and Network Analysis

**Q6: Geographic Coordinate Systems**

Which of the following coordinate systems is commonly used to represent locations on Earth’s surface?

* A. Cartesian Coordinate System
* B. Polar Coordinate System
* C. Geographic Coordinate System (Latitude and Longitude)
* D. Cylindrical Coordinate System

**Answer**: C — The Geographic Coordinate System uses latitude and longitude to specify locations on Earth’s surface. This system is widely used in geospatial analysis.

---

### Module: Data Visualization

**Q7: Effective Data Visualization**

When creating a bar chart to compare the sales performance of different products, which practice should be avoided?

* A. Ordering bars from highest to lowest value.
* B. Using different colors for each bar without a legend.
* C. Starting the y-axis at zero.
* D. Labeling each bar with its exact value.

**Answer**: B — Using different colors for each bar without a legend can confuse the audience, as they may assume the colors represent different categories. Consistency and clarity are key in effective data visualization.

---

### Module: Everyday Tools

**Q8: VS Code Feature Use**

You are editing a Python script in Visual Studio Code and want to quickly find and edit all occurrences of a variable name in the current file. What feature should you use?

* A. Git integration
* B. Debug panel
* C. **Multi-cursor editing**
* D. Terminal commands

**Answer**: C — Multi-cursor editing allows you to place multiple cursors in a file and edit text in multiple locations at once. It is useful for refactoring variable names or repeated patterns.

---

### Module: Data Sourcing

**Q9: Data API Identification**

Which of the following data sources is most likely to provide structured data accessible via an API?

* A. A scanned PDF document
* B. A screenshot of a chart
* C. **The World Bank data portal**
* D. A newspaper article

**Answer**: C — The World Bank data portal provides structured datasets accessible via APIs. The other options involve unstructured or image-based content not suitable for direct data access.

---

### Module: Data Preparation

**Q10: Data Type Conversion in Excel**

You imported a CSV file into Excel, and one of the columns containing numbers is treated as text. What is the easiest way to convert it into numeric format?

* A. Use the CONCAT function
* B. Format the column as Text
* C. **Use the VALUE() function**
* D. Use SUBSTITUTE()

**Answer**: C — The VALUE function converts text that appears as numbers into actual numeric values. This is useful when data is imported with formatting issues.

---

### Module: Data Analysis

**Q11: Outlier Detection**

You are analyzing a dataset of employee salaries. Which visualization is best for quickly identifying outliers?

* A. Line chart
* B. **Box plot**
* C. Histogram
* D. Pie chart

**Answer**: B — A box plot clearly shows the spread of data and highlights outliers as individual points beyond the whiskers.

---

### Module: Large Language Models

**Q12: Prompt Engineering Strategy**

To get consistent, structured responses from a language model when extracting key information, which approach is most effective?

* A. Ask the model to “summarize” the text
* B. Use open-ended questions
* C. **Use system messages and JSON schema formatting**
* D. Provide only one-word inputs

**Answer**: C — System messages and structured output formats like JSON schemas guide the model to generate reliable and consistent structured responses.

---

### Module: Geospatial and Network Analysis

**Q13: Network Centrality**

In a social network graph of coworkers, which metric best identifies the person who connects the most groups together?

* A. Degree centrality
* B. Closeness centrality
* C. **Betweenness centrality**
* D. Eigenvector centrality

**Answer**: C — Betweenness centrality measures how often a node appears on shortest paths between other nodes, highlighting connectors or “bridges” in the network.

---

### Module: Data Visualization

**Q14: Choosing the Right Chart**

You want to show how the composition of a marketing budget changes across three years. Which visualization is most appropriate?

* A. Pie charts for each year
* B. Scatter plots
* C. **Stacked bar chart**
* D. Line chart

**Answer**: C — A stacked bar chart shows parts of a whole across different categories and time periods, making it easier to compare budget composition over years.
Here's a detailed description of the image:

**Content:**

The image features a stylized, abstract symbol against a black background.

**Symbol Description:**

*   **Shape:** The symbol resembles a geometric knot or interlocking loops. It's a six-petaled, rounded shape.
*   **Appearance:** The symbol is depicted with a glowing, white outline, creating a contrast with the black background. The white outline gives it a luminous or ethereal quality.

**Background:**

*   The background is completely black, which emphasizes the symbol and makes it stand out.

**Possible Interpretation:**

The symbol is the logo of OpenAI.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/1](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/1)
---


Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/2](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/2)
---
@carlton @Jivraj  
any link for last term’s end term question answer

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/4](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/4)
---
quizpractice.space

### Practise End Term Quiz Question Papers

Practice with IITM's online BS degree question papers and quizzes to improve your preparation.
Here's a detailed description of the content in the image:

The image shows two capital letters, "Q" and "P", presented in a stylized, somewhat blurred fashion. The letters appear to be rendered with a gradient effect, transitioning from white to gray, suggesting a light source is illuminating them from the front. The background is a dark gray or black color, providing a contrast that makes the letters stand out. The style of the font is simple and sans-serif, with a slight pixelated or blocky appearance due to the image quality or rendering. The letters are positioned close to each other and fill most of the frame.
 Here's a detailed description of the image, focusing on key elements that would be helpful for answering questions about it:

**Overall Impression:**

The image displays a website interface, presumably a practice exam platform. It's divided into two main sections:

*   **Left:** A branding/promotional area with the company's logo and name.
*   **Right:** A screenshot of the website showing an active practice test.

**Left Section (Branding/Promotion):**

*   **Logo:** The logo includes "QP" inside of a black square.
*   **Text:**
    *   "Practice Previous Question Papers" (prominently displayed).
    *   "IITM Online BS Degree"
    *   "www.quizpractice.space" (website address)
*   **Graphics:** There's an emoji of a graduate with a graduation cap.

**Right Section (Website Interface):**

*   **Browser Window:**  Clearly shown is a browser window, indicating the platform is web-based.
*   **URL:** The URL in the address bar is "quizpractice.space/question-paper/practise/1/8edb1ffc-4da0-4b43-8c2a-02eb5c3f184b".
*   **Header:**  The header includes the "QP" logo, links to "Home," "About," and "Privacy Policy."
*   **Exam Information:**
    *   Subject: "CT"
    *   Details: "2023 Oct: IIT M DIPLOMA AN2 EXAM QPD2"
*   **Exam Mode Toggle:** "Exam Mode" and "Practise" are presented as tabs, with "Practise" currently selected.
*   **Question Menu:** A series of numbered buttons (1 through 18) indicating the questions in the exam.  Question 3 is highlighted.
*   **Timer:**  A countdown timer displays "00:09."  There are also pause and restart buttons.
*   **Controls:** A "Submit Exam" button.
*   **Question Display:**
    *   "Question 3: 640653668426"
    *   "Match the following expressions on the left side with the appropriate match."
    *   A list of expressions (a. 2 == 2 or 2 > 3, b. 2 == 2 and 2 > 3, c. 2 = 3, d. 2 + '2', e. 2 < 3) and potential answers (1. Invalid expression, 2. True, 3. False, 4. 4, 5. '22').
    *   Radio buttons with multiple choice options (various combinations of pairings between the expressions and answers).
*   **Footer:** "Question 4: 640653668437" with a "View Details" button.

**Key Features & Details:**

*   **Practice Test Platform:** The image promotes a website for practicing previous question papers.
*   **IITM Online BS Degree:** The website is associated with the IITM Online BS Degree program.
*   **Programming/Logic Questions:** The expressions in Question 3 suggest the exam tests programming logic or basic coding principles.
*   **Interactive Interface:** The presence of buttons, radio buttons, and a timer indicates the website is interactive.

Let me know if you would like me to focus on a specific aspect of the image!
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/5](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/5)
---
So here is more questions in the form of a little quiz (shared by someone in the group,DM for Credit )

gkmfrombs.github.io

### Quiz from PDF

That has 350 questions if you don’t want to go through all of them(it’s pretty time consuming)  
in that case just do this PDF.(This pdf contains all the questions that is a bit conceptual i would say and some questions which i failed to do  )

accounts.google.com

### Google Drive: Sign-in

Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).

(If you know context to the pdf’s name,we are friends )

Thank you,  
Kindeeesstt Regards,(hopefully the last post on discourse for TDS),  
Tushar Jalan
Here's a detailed description of the image:

**Content:**

The image features a bright yellow emoji face. It's a cheerful, loving expression. Here's a breakdown:

*   **Face:** Round, yellow face, which is the standard color for emojis.

*   **Eyes:** The eyes are closed with simple, curved lines, suggesting a happy, content expression.

*   **Mouth:** The mouth is represented by a wide, gently curved line, indicating a warm, happy smile.

*   **Cheeks:** There are light pink blushes on each cheek, enhancing the feeling of affection or love.

*   **Hearts:** Three red hearts surround the face. One heart is positioned to the upper right and the two others at the lower-left and lower right corners of the face. These hearts are a strong indicator of love, affection, or gratitude.

Overall, the emoji conveys feelings of love, affection, happiness, and warmth.
 Here's a detailed description of the image:

**Content:**

The image features a single element: a yellow emoji face. This emoji is commonly known as the "Smiling Face with Tear" emoji.

**Key Features:**

*   **Shape:** The emoji is circular, representing a typical smiley face.
*   **Color:** The face is bright yellow.
*   **Facial Features:**
    *   Eyes: It has two small, dark brown oval eyes.
    *   Mouth: It has a simple, curved black line representing a smile.
    *   Tear: A single, prominent blue teardrop is located below and to the left of the mouth. It appears to be falling down the cheek.

**Overall Impression:**

The emoji conveys a mixed emotion: happiness or amusement combined with a hint of sadness or emotional release. It suggests a situation where someone is laughing or smiling through tears, or perhaps acknowledging a bittersweet feeling.
 Here's a detailed description of the image:

**Content:** The image shows a single emoji.

**Emoji Description:**

*   **Shape:** The emoji is a round, yellow face.
*   **Expression:** The face is smiling broadly. It has two small, curved eyes and a wide grin revealing a set of white teeth. The overall expression conveys happiness, cheerfulness, and perhaps even amusement or glee.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/6](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/6)
---
Thank you for your efforts  
Thanks

Edit: Opened in incognito and it worked.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/7](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/7)
---
Hi @carlton please upload the recording of Thursday’s TDS session on the YouTube playlist

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/8](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/8)
---
@carlton sir i have done the 350 questions . i am able to answer 80% of the questions on my own, correctly. will end term also be similar to these questions? are pyqs any helpful ?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/9](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/9)
---
Live Session - TDS - 2025/04/10 20:00 GMT+05:30 - Recording - Google Drive

Access recording through this gdrive link

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/10](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/10)
---
Thank you for the questions sir.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/11](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/11)
---
Mock Exam: Tools in Data Science
================================

#### The end term and the mock has been created using the TDS GPT Assistant. Since the GPT has ALL the GAs, Course Content Modules, Live Session Transcriptions (its works like RAG), it is really able to help you prepare for the end term. Use it!

Therefore you can also create your own mocks.

ChatGPT

### ChatGPT - IITM TDS Teaching Assistant

TA for IIT Madras' Data Science course, guiding students with questions.

Below are variant questions across various topics relevant to the course. These questions have been curated from the topics areas we are focussing on. Therefore it will be very similar in content to the end term.

> What it does not contain: Scenario based questions. These are complex to construct. We will address the topics for these questions in the live session.

* LLMs
* Pandas
* Git, Docker, Bash

---

### Q1: HTTP Method Semantics

Which HTTP method is **not idempotent**, meaning repeated identical requests **may** result in different outcomes each time?

* A. GET
* B. PUT
* C. POST
* D. DELETE

**Answer**: C. POST

### Q2: IDE Features

Which feature is **least likely** to be found in a standard code editor or IDE?

* A. Code formatting tools
* B. Integrated terminal
* C. Git integration
* D. Cloud hosting of Docker containers

**Answer**: D. Cloud hosting of Docker containers

### Q3: Pandas Summary Methods

You have a DataFrame with a `region` column. To get a quick summary of how many entries are in each region, which method is most useful?

* A. df.describe()
* B. df[“region”].value\_counts()
* C. df.count()
* D. df.groupby(“region”).sum()

**Answer**: B. df[“region”].value\_counts()

### Q4: Python Exception Scope

You want to safely open a file, handle any errors, and ensure the file is always closed in Python. Which pattern should you use?

* A. `try: open(...)` then `finally: close()`
* B. `open()` and then `except`
* C. `open()` and then `raise`
* D. Use `with open(...) as f:` block

**Answer**: D. Use `with open(...) as f:` block

### Q5: Chrome DevTools - Debugging

A frontend developer wants to trace JavaScript function calls step-by-step. Which **Chrome DevTools** panel should they use?

* A. Console
* B. Application
* C. Sources
* D. Elements

**Answer**: C. Sources

### Q6: Data Cleaning Tools

You are cleaning survey responses and want to automatically match similar text entries like “NYC”, “New York City”, and “newyorkcity”. Which approach/tool would be most effective?

* A. `TRIM()` in Excel
* B. Manual Find and Replace
* C. Fuzzy matching or clustering in OpenRefine
* D. COUNTIF()

**Answer**: C. Fuzzy matching or clustering in OpenRefine

### Q7: Geospatial Libraries

Which pair of Python libraries is best suited for **geospatial analysis** and **rendering static maps**?

* A. pandas and seaborn
* B. geopandas and matplotlib
* C. folium and flask
* D. sklearn and dash

**Answer**: B. geopandas and matplotlib

### Q8: Statistical Significance

A psychologist tests if a training program changes memory performance and finds a p-value of **0.08**. What can be concluded at the 0.05 significance level?

* A. The result is highly significant
* B. The null hypothesis must be rejected
* C. There is insufficient evidence to reject the null hypothesis
* D. The program is proven to work

**Answer**: C. There is insufficient evidence to reject the null hypothesis

### Q9: Purpose of Kumu

What is a key use case for a tool like **Kumu**?

* A. Animating time series
* B. Designing deep learning models
* C. Visualizing stakeholder networks and system relationships
* D. Performing statistical analysis

**Answer**: C. Visualizing stakeholder networks and system relationships

### Q10: DevTools Performance Diagnostics

To diagnose a slow webpage, you want to **analyze scripts, rendering times, and long tasks**. Which DevTools panel provides a timeline-based view?

* A. Elements
* B. Performance
* C. Network
* D. Lighthouse

**Answer**: B. Performance

### Q11: Git Configuration

Which of the following files helps configure a Git project’s name, email, and default branch?

* A. `.gitignore`
* B. `.gitattributes`
* C. `.git/config`
* D. `README.md`

**Answer**: C. `.git/config`

### Q13: Safe HTTP Method

Which HTTP method is considered **safe**, meaning it is only used for retrieval and **must not change** server state?

* A. GET
* B. DELETE
* C. PATCH
* D. POST

**Answer**: A. GET

### Q14: Deduplicating Text Entries

A dataset has entries like “IBM”, “I.B.M.”, and “International Business Machines”. What is the best tool to cluster these for cleaning?

* A. Excel TRIM
* B. OpenRefine using key collision or fingerprinting
* C. pandas merge()
* D. CONCATENATE()

**Answer**: B. OpenRefine using key collision or fingerprinting

### Q15: Geospatial + Interactive Mapping

A conservation biologist wants to visualize real-time animal tracking data on an interactive map. Which libraries would be best?

* A. geopandas and plotly
* B. folium and pandas
* C. seaborn and shapely
* D. rasterio and altair

**Answer**: B. folium and pandas

### Q16: Pandas - Filtering Unique Entries

You have a DataFrame of customer orders and want to list only those customers who ordered **once**. Which Pandas method chain is most suitable?

* A. df.groupby(“customer”).sum()
* B. df[“customer”].value\_counts() == 1
* C. df.drop\_duplicates()
* D. df[“customer”].nunique()

**Answer**: B. df[“customer”].value\_counts() == 1

### Q17: Purpose of Kumu in System Design

How does Kumu help in system design or stakeholder mapping?

* A. Organizing spreadsheets
* B. Identifying leverage points in complex systems through visual maps
* C. Rendering line graphs
* D. Sending notifications

**Answer**: B. Identifying leverage points in complex systems through visual maps

### Q18: Python Exception - Multiple Handlers

Which structure allows Python to handle different types of exceptions separately?

* A. `try`…`finally`
* B. `if`…`else`
* C. Multiple `except` blocks
* D. Nested `try` blocks

**Answer**: C. Multiple `except` blocks

### Q19: Understanding Statistical Power

If a study has **low statistical power**, what is most likely to occur?

* A. False positive (Type I error)
* B. False negative (Type II error)
* C. Confounding
* D. Multicollinearity

**Answer**: B. False negative (Type II error)

### Q20: Git Basics - Staging Area

Which Git command moves modified files to the **staging area**?

* A. git push
* B. git add
* C. git fetch
* D. git init

**Answer**: B. git add

### Q21: Chrome DevTools - Local Storage

Where can you inspect **local storage** items (e.g. tokens, preferences) in Chrome DevTools?

* A. Console
* B. Application > Local Storage
* C. Elements
* D. Sources

**Answer**: B. Application > Local Storage

### Q22: Chrome DevTools - JS Performance

Which DevTools feature helps measure execution time of scripts and CPU usage?

* A. Console
* B. Network
* C. Performance
* D. Application

**Answer**: C. Performance

### Q23: Excel Data Import - Scientific Notation Issue

You import a CSV file where product IDs like `"1E10"` are being interpreted as scientific notation in Excel. What is the best way to preserve these IDs as text?

* A. Format the column as General
* B. Use `=TEXT(A1, "0")` after import
* C. Set column format to Text during import or Text-to-Columns
* D. Change regional settings

**Answer**: C. Set column format to Text during import or Text-to-Columns

---

### Module: Everyday Tools

**Q1: Spreadsheet Functions**

You have a dataset in Excel where column A contains full names in the format “Last Name, First Name”. Which function can you use to extract the first name into a separate column?

* A. `=LEFT(A1, FIND(",", A1)-1)`
* B. `=RIGHT(A1, LEN(A1) - FIND(",", A1))`
* C. `=MID(A1, FIND(",", A1)+2, LEN(A1))`
* D. `=SPLIT(A1, ",")`

**Answer**: C — The `MID` function extracts text from the middle of a string. By finding the position of the comma and adding 2 (to skip the comma and space), it extracts the first name. Option A extracts the last name, Option B results in an error due to incorrect syntax, and Option D is not a valid Excel function.

---

### Module: Data Sourcing

**Q2: Web Scraping Ethics**

When performing web scraping to collect data, which of the following practices is considered unethical?

* A. Respecting the website’s `robots.txt` file.
* B. Sending requests at a rate that mimics human browsing behavior.
* C. Scraping data from a website that requires login without permission.
* D. Citing the source of the data collected.

**Answer**: C — Scraping data from a website that requires login without permission violates the site’s terms of service and user privacy. Options A, B, and D are ethical practices that respect the website’s policies and data ownership.

---

### Module: Data Preparation

**Q3: Handling Missing Data**

In a dataset, you notice that several entries in the “Age” column are missing. Which method is generally **not** appropriate for handling these missing values?

* A. Replacing missing values with the mean age.
* B. Deleting rows with missing age values.
* C. Replacing missing values with a fixed age, such as 0.
* D. Leaving the missing values as they are without any action.

**Answer**: D — Leaving missing values unaddressed can lead to errors in analysis and modeling. Options A, B, and C are common strategies for handling missing data, depending on the context and the extent of the missingness.

---

### Module: Data Analysis

**Q4: Statistical Measures**

Which of the following statistical measures is **not** sensitive to extreme values (outliers) in a dataset?

* A. Mean
* B. Median
* C. Standard Deviation
* D. Range

**Answer**: B — The median represents the middle value of a dataset and is not affected by outliers. In contrast, the mean, standard deviation, and range can be significantly influenced by extreme values.

---

### Module: Large Language Models

**Q5: Tokenization in NLP**

In Natural Language Processing, what is the primary purpose of tokenization?

* A. To translate text from one language to another.
* B. To split text into individual words or subwords.
* C. To encrypt text for secure communication.
* D. To summarize large texts into shorter versions.

**Answer**: B — Tokenization involves breaking down text into smaller components, such as words or subwords, which can then be processed by language models. This is a fundamental step in NLP tasks.

---

### Module: Geospatial and Network Analysis

**Q6: Geographic Coordinate Systems**

Which of the following coordinate systems is commonly used to represent locations on Earth’s surface?

* A. Cartesian Coordinate System
* B. Polar Coordinate System
* C. Geographic Coordinate System (Latitude and Longitude)
* D. Cylindrical Coordinate System

**Answer**: C — The Geographic Coordinate System uses latitude and longitude to specify locations on Earth’s surface. This system is widely used in geospatial analysis.

---

### Module: Data Visualization

**Q7: Effective Data Visualization**

When creating a bar chart to compare the sales performance of different products, which practice should be avoided?

* A. Ordering bars from highest to lowest value.
* B. Using different colors for each bar without a legend.
* C. Starting the y-axis at zero.
* D. Labeling each bar with its exact value.

**Answer**: B — Using different colors for each bar without a legend can confuse the audience, as they may assume the colors represent different categories. Consistency and clarity are key in effective data visualization.

---

### Module: Everyday Tools

**Q8: VS Code Feature Use**

You are editing a Python script in Visual Studio Code and want to quickly find and edit all occurrences of a variable name in the current file. What feature should you use?

* A. Git integration
* B. Debug panel
* C. **Multi-cursor editing**
* D. Terminal commands

**Answer**: C — Multi-cursor editing allows you to place multiple cursors in a file and edit text in multiple locations at once. It is useful for refactoring variable names or repeated patterns.

---

### Module: Data Sourcing

**Q9: Data API Identification**

Which of the following data sources is most likely to provide structured data accessible via an API?

* A. A scanned PDF document
* B. A screenshot of a chart
* C. **The World Bank data portal**
* D. A newspaper article

**Answer**: C — The World Bank data portal provides structured datasets accessible via APIs. The other options involve unstructured or image-based content not suitable for direct data access.

---

### Module: Data Preparation

**Q10: Data Type Conversion in Excel**

You imported a CSV file into Excel, and one of the columns containing numbers is treated as text. What is the easiest way to convert it into numeric format?

* A. Use the CONCAT function
* B. Format the column as Text
* C. **Use the VALUE() function**
* D. Use SUBSTITUTE()

**Answer**: C — The VALUE function converts text that appears as numbers into actual numeric values. This is useful when data is imported with formatting issues.

---

### Module: Data Analysis

**Q11: Outlier Detection**

You are analyzing a dataset of employee salaries. Which visualization is best for quickly identifying outliers?

* A. Line chart
* B. **Box plot**
* C. Histogram
* D. Pie chart

**Answer**: B — A box plot clearly shows the spread of data and highlights outliers as individual points beyond the whiskers.

---

### Module: Large Language Models

**Q12: Prompt Engineering Strategy**

To get consistent, structured responses from a language model when extracting key information, which approach is most effective?

* A. Ask the model to “summarize” the text
* B. Use open-ended questions
* C. **Use system messages and JSON schema formatting**
* D. Provide only one-word inputs

**Answer**: C — System messages and structured output formats like JSON schemas guide the model to generate reliable and consistent structured responses.

---

### Module: Geospatial and Network Analysis

**Q13: Network Centrality**

In a social network graph of coworkers, which metric best identifies the person who connects the most groups together?

* A. Degree centrality
* B. Closeness centrality
* C. **Betweenness centrality**
* D. Eigenvector centrality

**Answer**: C — Betweenness centrality measures how often a node appears on shortest paths between other nodes, highlighting connectors or “bridges” in the network.

---

### Module: Data Visualization

**Q14: Choosing the Right Chart**

You want to show how the composition of a marketing budget changes across three years. Which visualization is most appropriate?

* A. Pie charts for each year
* B. Scatter plots
* C. **Stacked bar chart**
* D. Line chart

**Answer**: C — A stacked bar chart shows parts of a whole across different categories and time periods, making it easier to compare budget composition over years.
Here's a detailed description of the image:

**Overall Impression:** The image features a logo or symbol set against a black background. The design is abstract and appears to be stylized.

**Key Features:**

*   **Symbol/Logo:** The central element is a geometric symbol resembling a stylized knot or a complex flower. It consists of interconnected, curved lines that loop around a central point.
*   **Color:** The symbol is white, contrasting sharply with the black background.
*   **Style:** The design is clean and modern. The lines have a smooth, almost glowing quality. The edges are slightly blurred, giving it a soft appearance.
*   **Shape:** The overall shape of the symbol is roughly circular, though the individual elements are more curvilinear.

**Based on the visual cues, I can infer the following:**

*   **Likely a Corporate Logo:** This type of design is commonly used for branding purposes.
*   **Modern and Abstract:** The abstract nature of the symbol suggests a focus on innovation and forward-thinking.

Without additional context, it's difficult to determine the exact meaning or purpose of the logo.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/1](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/1)
---


Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/2](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/2)
---
@carlton @Jivraj  
any link for last term’s end term question answer

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/4](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/4)
---
quizpractice.space

### Practise End Term Quiz Question Papers

Practice with IITM's online BS degree question papers and quizzes to improve your preparation.
Here's a detailed description of the image:

**Content:**

The image features two letters, "Q" and "P", presented in a stylized, slightly blurred font. They appear to be uppercase. 

**Color and Visual Style:**

*   The letters are white or light grey.
*   The background is black.
*   The edges of the letters are not perfectly sharp, giving the image a soft or slightly out-of-focus look. This could be due to a blur effect or image quality.

**Potential Interpretation:**

Without additional context, the image could represent:

*   A logo or an abbreviation.
*   A text sample in a specific font.
*   A visual representation of a two-letter code or identifier.

**Possible Information Missing**

* It is difficult to determine the size of letters related to the overall image
* The font cannot be identified without greater resolution.
 Here's a detailed description of the image content:

**Overall Layout:**

*   The image shows a website screenshot juxtaposed with some branding elements. On the left, there's a white background with the text "Practice Previous Question Papers" and the website address "www.quizpractice.space." On the right side of the image is a screenshot of a web page containing an online quiz or exam.

**Branding Elements (Left Side):**

*   The left side has a logo with the letters "QP."
*   The text "Practice Previous Question Papers" is prominently displayed.
*   "IITM Online BS Degree" is mentioned.
*   The website address "www.quizpractice.space" is given.

**Website Screenshot (Right Side):**

*   The website is dark-themed (likely dark mode).
*   The website address "quizpractice.space" is visible in the browser's address bar.
*   There are navigation links labeled "Home," "About," and "Privacy Policy."
*   **Exam Details:**
    *   Subject: CT
    *   Exam: 2023 Oct: IIT M DIPLOMA AN2 EXAM QPD2
*   **Exam Mode:** There is a toggled button that lets you switch between "Exam Mode" and "Practise". The "Practise" button is currently selected.
*   **Question Menu:** There's a numbered grid of buttons from 1 to 18, indicating questions in the quiz/exam.
*   **Timer:** The timer reads "00:09." There are play and restart icons beneath it.
*   **Controls:** There's a "Submit Exam" button.
*   **Question 3:**
    *   It includes the question ID "640653668426".
    *   The question is a matching question where expressions on the left need to be matched with options on the right.
    *   Expressions: a. 2==2 or 2>3, b. 2==2 and 2>3, c. 2=3, d. 2+'2', e. 2<3
    *   Matching Options: 1. Invalid expression, 2. True, 3. False, 4. 4, 5. '22'
    *   Multiple-choice options are provided for matching.
*   **Question 4:**  Visible at the bottom with the ID "640653668437." A "View Details" button is available.

**Overall, the image promotes the "quizpractice.space" website for practicing previous question papers, specifically highlighting a Computer Technology (CT) diploma exam (IIT M DIPLOMA AN2 EXAM QPD2).**
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/5](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/5)
---
So here is more questions in the form of a little quiz (shared by someone in the group,DM for Credit )

gkmfrombs.github.io

### Quiz from PDF

That has 350 questions if you don’t want to go through all of them(it’s pretty time consuming)  
in that case just do this PDF.(This pdf contains all the questions that is a bit conceptual i would say and some questions which i failed to do  )

accounts.google.com

### Google Drive: Sign-in

Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).

(If you know context to the pdf’s name,we are friends )

Thank you,  
Kindeeesstt Regards,(hopefully the last post on discourse for TDS),  
Tushar Jalan
Here's a detailed description of the image:

**Content:**

The image is a digital depiction of a yellow emoji face with hearts surrounding it.

**Features:**

*   **Emoji Face:** The central element is a classic yellow emoji face, smiling warmly. It has closed, crescent-shaped eyes and a gentle, closed-lip smile. There are visible blush marks on the cheeks.

*   **Hearts:** Three red hearts are positioned around the emoji's face. One is near the top right, another on the lower left, and the third on the lower right. This arrangement suggests a sense of being embraced by love or strong affection.

*   **Color:** The dominant colors are yellow (for the face) and red (for the hearts), creating a cheerful and emotionally warm feel.

*   **Overall Impression:** The image conveys feelings of love, happiness, affection, and contentment.
 Here's a detailed description of the image:

**Content:**

The image depicts a yellow circular emoji with a small, curved smile and two dark brown, oval-shaped eyes. To the left of the smile, a single, large, light blue teardrop is positioned, originating from just below the left eye.

**Key Features:**

*   **Shape:** Circular face.
*   **Color:** Predominantly yellow.
*   **Facial Features:**
    *   Smiling mouth (curved line).
    *   Two oval eyes.
    *   Single teardrop.

**Overall Impression:**

The emoji seems to portray a mixed emotion. The smile suggests happiness or contentment, while the teardrop suggests sadness, relief, or other emotional release. The combination of these elements likely communicates a feeling that is bittersweet or rueful.
 Okay, here's a detailed description of the image:

**Content:**

The image shows a single emoji.

**Description of the Emoji:**

*   It's a yellow, circular smiley face.
*   The eyes are represented by two simple, curved shapes resembling closed or squinting eyes.
*   The mouth is wide open, displaying a full set of white teeth.
*   The overall expression conveys a sense of great happiness, joy, or amusement.

**Possible Interpretations:**

Based on the features, the emoji is most likely representing:

*   **A wide grin:** Indicating extreme happiness.
*   **Laughter:** Suggesting something is very funny.
*   **Joyful expression:** Simply portraying a state of being very pleased.

Let me know if you have any other questions about the image!
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/6](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/6)
---
Thank you for your efforts  
Thanks

Edit: Opened in incognito and it worked.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/7](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/7)
---
Hi @carlton please upload the recording of Thursday’s TDS session on the YouTube playlist

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/8](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/8)
---
@carlton sir i have done the 350 questions . i am able to answer 80% of the questions on my own, correctly. will end term also be similar to these questions? are pyqs any helpful ?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/9](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/9)
---
Live Session - TDS - 2025/04/10 20:00 GMT+05:30 - Recording - Google Drive

Access recording through this gdrive link

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/10](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/10)
---
Thank you for the questions sir.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/11](https://discourse.onlinedegree.iitm.ac.in/t/end-term-mock-tds-jan-25/172333/11)
---
