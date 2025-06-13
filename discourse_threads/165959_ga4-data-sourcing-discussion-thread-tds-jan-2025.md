# Thread URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959)

Please post any questions related to Graded Assignment 4 - Data Sourcing.

Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.

Deadline: Sunday, February 9, 2025 6:29 PM

@Jivraj @Saransh\_Saini @carlton

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/1](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/1)
---


Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/2](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/2)
---
Screenshot 2025-02-01 132301331×314 12.3 KB

  
what is the error here?? sir @Jivraj
Here's a description of the image:

The image shows a code snippet and an error message related to JSON data. 


**The JSON data:** The main part displays a JSON object, likely part of a larger dataset. The object has the following key-value pairs:

* `"id"`: `"tt7144296"` (a string, possibly a movie or show ID)
* `"title"`: `"1. Kiss and Kill"` (a string, the title)
* `"year"`: `2017` (a number, the year)
* `"rating"`: `2.9` (a number, a rating)

There's a trailing comma after the `"rating"` key-value pair which is syntactically incorrect in standard JSON.  Most JSON parsers will ignore or reject this.

**The Error Message:** Below the JSON data, an error message is shown:

* `Error: Expected: 2.9 Actual: 2.9`

This indicates a test or validation process where the expected value of `2.9` for the `"rating"` field matched the actual value.  Even though the values match, the trailing comma in the JSON likely caused a prior error in parsing or processing that is not displayed here.

**Overall:** The image suggests a snippet from a testing or debugging process where JSON data is being checked. The error message, despite showing a match, highlights a syntax problem within the provided JSON snippet.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/3](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/3)
---
I have the Same doubt.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/5](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/5)
---
@22f3001315 @21f3002277 @24ds2000024 – please try again after reloading the page. The new error message will be clearer, like this:

```
Error: At [0].rating: Values don't match. Expected: "7.4". Actual: 7.4

```

FYI, we expect all values as strings, not numbers. That’s because the year can sometimes be a range for a TV series (e.g. 2021 - 2024) and the rating can sometimes be missing.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/6](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/6)
---
In Question 2, it is specifically said to filter the movies however, the evaluator is expecting a TV show there. Should we also include TV shows now?

edit: This is an everchanging dataset, so will our answers be saved, as, this json might not be in this order tomorrow?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/7](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/7)
---
@23f2000237 A good point. Yes, please include *all* titles. I’ve reworded the question accordingly. Thanks.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/8](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/8)
---
Q3. How to handle the error ? @Jivraj

TypeError: Cannot read properties of null (reading ‘0’)

```
http://127.0.0.1:8000/api/outline?country=Russia

{"outline":"## Contents\n# Russia\n## Etymology\n## History\n### Early history\n### Kievan Rus'\n### Grand Duchy of Moscow\n### Tsardom of Russia\n### Imperial Russia\n#### Great power and development of society, sciences, and arts\n#### Great liberal reforms and capitalism\n#### Constitutional monarchy and World War\n### Revolution and civil war\n### Soviet Union\n#### Command economy and Soviet society\n#### Stalinism and modernisation\n#### World War II and United Nations\n#### Superpower and Cold War\n#### Khrushchev Thaw reforms and economic development\n#### Period of developed socialism or Era of Stagnation\n#### Perestroika, democratisation and Russian sovereignty\n### Independent Russian Federation\n#### Transition to a market economy and political crises\n#### Modern liberal constitution, international cooperation and economic stabilisation\n#### Movement towards a modernised economy, political centralisation and democratic backsliding\n#### Invasion of Ukraine\n## Geography\n### Climate\n### Biodiversity\n## Government and politics\n### Political divisions\n### Foreign relations\n### Military\n### Human rights\n### Corruption\n### Law and crime\n## Economy\n### Transport and energy\n### Agriculture and fishery\n### Science and technology\n#### Space exploration\n### Tourism\n## Demographics\n### Language\n### Religion\n### Education\n### Health\n## Culture\n### Holidays\n### Art and architecture\n### Music\n### Literature and philosophy\n### Cuisine\n### Mass media and cinema\n### Sports\n## See also\n## Notes\n## References\n## Sources\n## Further reading\n## External links"}


```

error resolved

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/9](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/9)
---
in my output which is correct  
there are two \n instead of one .

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/11](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/11)
---
it should one(for newline), my code is working now

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/12](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/12)
---
Dear Sir,  
I was at 2/10 yesterday. After pasting JSON file of IMDB & reloading as suggested My marks updated to 3/10. Kindly confirm if I have got whole of IMDB question.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/13](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/13)
---
Q4. How to handle the error ? @Jivraj

Error: At 2025-02-05: Values don’t match

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/14](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/14)
---
There is no submit button is available in below screen. Is it fine to save the link url only. Please clarify (unless we click submit button the log of Graded Assignment 4 remains red)  

image1920×1080 337 KB
Here's a description of the image:

The image shows a computer screen displaying a web page within a Chrome browser window. 


**Browser Window and Tabs:** The browser window shows several tabs at the top, including one titled "Graded Assignment 4: IITM On," indicating the page's focus is on a graded assignment from the Indian Institute of Technology Madras. Another tab shows a URL related to online course material ("seek.onlinedegree.iitm.ac.in/...").


**Web Page Content:** The main content of the web page is divided into two main sections.

* **Left Section (Navigation Panel):** This is a dark gray sidebar containing a course navigation menu.  Items include "Modules," "Grades," and a list of modules ("Course Introduction," "Module 1: Development Tools," "Module 2: Deployment Tools," "Module 3: Large Language Models," "Project 1," "Module 4: Data Sourcing," and "Graded Assignment 4"). This structure strongly suggests an online learning platform.

* **Right Section (Assignment Details):** This section displays details about a "Graded Assignment 4." It provides:
    * The due date and time.
    * Instructions stating that multiple submissions are allowed, with only the final submission being graded.
    * Troubleshooting advice for students experiencing access issues (e.g., disabling ad blockers, checking browser settings, ensuring Javascript is enabled).
    * A specific instruction to use the student's ID when accessing the assignment to have their score counted.
    * A direct link to access the assignment: `https://exam.sanand.workers.dev/tds-2025-01-ga4`.

**System Tray:** The bottom right corner displays the system clock and date (06:00 03-02-2025), along with language settings (ENG).


**Overall:** The screenshot clearly displays an online learning environment where a student is reviewing details for a graded assignment. The information presented helps the student understand the assignment, its submission process, and possible troubleshooting steps if they encounter problems accessing it.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/15](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/15)
---
I have a doubt regarding the bonus mark. Suppose someone were to get 10/10 in the assignment, would their mark be recored as 11/10 or just 10?  
(Assuming they have interacted in this thread)

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/16](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/16)
---
Anyone scoring 10/10 on GA4 and replying with a *relevant* message on this thread will get 11/10
That's an emoji! 


Specifically, it's a digital image of a yellow smiley face emoji. 


Here's a breakdown of its features:

* **Shape:** A perfect or near-perfect circle.
* **Color:**  Bright, golden yellow.
* **Eyes:** Two small, dark brown, almost black, circular dots. They are relatively close together.
* **Mouth:** A small, slightly upturned line, indicating a subtle smile. It's not a wide, exaggerated grin, but a gentle, contented expression.
* **Overall Impression:** The emoji conveys a feeling of calm happiness, contentment, or mild amusement.  It's not overly expressive, but pleasant and approachable.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/17](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/17)
---
For me I just made filter of rating between 2 and 7 in site and typed in console as per video. with that data got in console worked fine.  
copy the coding and save in place use it for data extract when finally submit

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/18](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/18)
---
For question 2 getting Error: At [8].title: Values don’t match. Expected: “9. Un matrimonio di troppo”. Actual: “9. You’re Cordially Invited” But this movie is not found when searched by name  

image1414×295 19 KB
Here's a description of the image:

The image shows a screenshot of a search interface, likely from a website or application for searching media (books, movies, etc.). 


Here's a breakdown of the visible elements:

* **Left Side (Search Filters):** This section displays search filters allowing users to refine their search results.  There are expandable sections indicated by small upward-pointing triangles. The visible filters are:
    * **Title name:** A text input field where the user has entered "Un matrimonio di troppo" (Italian for "A marriage too much").
    * **Title type:** A filter with a dropdown (not expanded).

* **Right Side (No Results):** This section displays a large "No results found" message, indicating that the search query did not yield any matches. A greyed-out magnifying glass icon with a cross over it visually emphasizes the lack of results. Below the message is a helpful instruction: "Please adjust your filters or start a new search."

* **Top (Header):** At the top, there is the heading "Search filters" on the left and a button labeled "Expand all" with a downward arrow, suggesting the possibility to expand more filters not currently visible.

The overall appearance is clean and minimalist, with a consistent use of white space and simple design elements. The language suggests the platform might be international or cater to users who speak Italian. The main issue highlighted is the absence of results matching the search criteria.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/19](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/19)
---
how to get the BBC weather API key?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/20](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/20)
---
Just a quick query on the Bonus mark.

Would this be added to the final grade? Say for example, Someone get a full score in the first 4 assignments. So the total comes up to 39.5/39.5, and would be converted to 0.15 or 15 marks. Would the bonus mark be additional to that 15 or would the score change to 40.5/39.5 and then get normalised to 15?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/21](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/21)
---
@JoelJeffrey It will be added to the GA4 marks, not the final grade. So, it’s roughly worth 0.15% on the total - not a full 1% on the total.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/22](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/22)
---
Please post any questions related to Graded Assignment 4 - Data Sourcing.

Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.

Deadline: Sunday, February 9, 2025 6:29 PM

@Jivraj @Saransh\_Saini @carlton

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/1](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/1)
---


Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/2](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/2)
---
Screenshot 2025-02-01 132301331×314 12.3 KB

  
what is the error here?? sir @Jivraj
The image shows a code snippet and an error message.

The main part of the image displays JSON data representing a movie or TV show entry.  The data includes:

* **`id`**:  "tt7144296" (likely a unique identifier, possibly from IMDb)
* **`title`**: "1. Kiss and Kill"
* **`year`**: 2017
* **`rating`**: 2.9

The JSON is slightly malformed; there's a closing curly brace `}` at the very beginning, which is syntactically incorrect.  It should be placed at the end.

Below the JSON data, there's an error message:

* **`Error: Expected: 2.9 Actual: 2.9`**  This suggests a test or assertion checking the value of the `rating` field. The test passed because the expected and actual values are the same.  The error message is likely unrelated to the syntax issue in the JSON itself.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/3](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/3)
---
I have the Same doubt.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/5](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/5)
---
@22f3001315 @21f3002277 @24ds2000024 – please try again after reloading the page. The new error message will be clearer, like this:

```
Error: At [0].rating: Values don't match. Expected: "7.4". Actual: 7.4

```

FYI, we expect all values as strings, not numbers. That’s because the year can sometimes be a range for a TV series (e.g. 2021 - 2024) and the rating can sometimes be missing.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/6](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/6)
---
In Question 2, it is specifically said to filter the movies however, the evaluator is expecting a TV show there. Should we also include TV shows now?

edit: This is an everchanging dataset, so will our answers be saved, as, this json might not be in this order tomorrow?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/7](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/7)
---
@23f2000237 A good point. Yes, please include *all* titles. I’ve reworded the question accordingly. Thanks.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/8](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/8)
---
Q3. How to handle the error ? @Jivraj

TypeError: Cannot read properties of null (reading ‘0’)

```
http://127.0.0.1:8000/api/outline?country=Russia

{"outline":"## Contents\n# Russia\n## Etymology\n## History\n### Early history\n### Kievan Rus'\n### Grand Duchy of Moscow\n### Tsardom of Russia\n### Imperial Russia\n#### Great power and development of society, sciences, and arts\n#### Great liberal reforms and capitalism\n#### Constitutional monarchy and World War\n### Revolution and civil war\n### Soviet Union\n#### Command economy and Soviet society\n#### Stalinism and modernisation\n#### World War II and United Nations\n#### Superpower and Cold War\n#### Khrushchev Thaw reforms and economic development\n#### Period of developed socialism or Era of Stagnation\n#### Perestroika, democratisation and Russian sovereignty\n### Independent Russian Federation\n#### Transition to a market economy and political crises\n#### Modern liberal constitution, international cooperation and economic stabilisation\n#### Movement towards a modernised economy, political centralisation and democratic backsliding\n#### Invasion of Ukraine\n## Geography\n### Climate\n### Biodiversity\n## Government and politics\n### Political divisions\n### Foreign relations\n### Military\n### Human rights\n### Corruption\n### Law and crime\n## Economy\n### Transport and energy\n### Agriculture and fishery\n### Science and technology\n#### Space exploration\n### Tourism\n## Demographics\n### Language\n### Religion\n### Education\n### Health\n## Culture\n### Holidays\n### Art and architecture\n### Music\n### Literature and philosophy\n### Cuisine\n### Mass media and cinema\n### Sports\n## See also\n## Notes\n## References\n## Sources\n## Further reading\n## External links"}


```

error resolved

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/9](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/9)
---
in my output which is correct  
there are two \n instead of one .

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/11](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/11)
---
it should one(for newline), my code is working now

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/12](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/12)
---
Dear Sir,  
I was at 2/10 yesterday. After pasting JSON file of IMDB & reloading as suggested My marks updated to 3/10. Kindly confirm if I have got whole of IMDB question.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/13](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/13)
---
Q4. How to handle the error ? @Jivraj

Error: At 2025-02-05: Values don’t match

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/14](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/14)
---
There is no submit button is available in below screen. Is it fine to save the link url only. Please clarify (unless we click submit button the log of Graded Assignment 4 remains red)  

image1920×1080 337 KB
The image shows a screenshot of a computer screen displaying an online course page. 


Here's a breakdown of the visible content:

* **Top Browser Bar:** A typical browser window is visible at the top, showing the URL of an IIT Madras online course assignment (`seek.onlinedegree.iitm.ac.in/courses/...`). The title bar indicates "Graded Assignment 4".

* **Left Sidebar:** A navigation menu is on the left, listing modules of the course including "Course Introduction," "Module 1: Development Tools," "Module 2: Deployment Tools," "Module 3: Large Language Models," "Project 1," "Module 4: Data Sourcing," and finally "Graded Assignment 4". The sections are collapsible. "Modules" and "Grades" are headings in the sidebar.

* **Main Content Area:** This area displays the details of "Graded Assignment 4". The key information includes:
    * **Due Date:** Clearly stated as "2025-02-09, 23:59 IST".
    * **Multiple Submissions:**  The student is allowed to submit multiple times before the deadline.
    * **Troubleshooting:** A section provides guidance on common access problems, suggesting disabling ad blockers, allowing cookies and JavaScript, using Chrome browser, disabling browser extensions, and checking anti-virus settings. It also mentions that corporate network policies may interfere.  The student is told to use their student ID to access the assignment.
    * **Assignment Link:**  A direct link to the assignment is provided: `https://exam.sanand.workers.dev/tds-2025-01-ga4`.

* **Bottom Taskbar:** A Windows taskbar is visible at the bottom of the screen, showing standard icons and the time and date.

In short, the image captures a student's view of an online graded assignment in an IIT Madras course, including instructions, a deadline, troubleshooting tips, and the assignment access link.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/15](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/15)
---
I have a doubt regarding the bonus mark. Suppose someone were to get 10/10 in the assignment, would their mark be recored as 11/10 or just 10?  
(Assuming they have interacted in this thread)

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/16](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/16)
---
Anyone scoring 10/10 on GA4 and replying with a *relevant* message on this thread will get 11/10
That's a digital image of a simple, smiling emoticon. 


Here's a breakdown of its features:

* **Shape:** It's a perfect or nearly perfect circle.
* **Color:** The main body is a bright, yellowish-orange.
* **Features:**
    * **Eyes:** Two small, dark brown, nearly circular dots are positioned symmetrically on either side of the center.  They are relatively small compared to the overall size of the face.
    * **Mouth:** A simple, slightly curved line forms a subtle smile.  It's a thin line and doesn't extend far up the sides of the face.  The curve is gentle, indicating a pleasant, calm expression rather than a wide, enthusiastic grin.

The overall style is reminiscent of classic emoticons and emoji designs, prioritizing simplicity and clarity to convey a positive emotion.  The image is likely generated digitally, showing a slightly pixelated or soft texture depending on the viewing scale.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/17](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/17)
---
For me I just made filter of rating between 2 and 7 in site and typed in console as per video. with that data got in console worked fine.  
copy the coding and save in place use it for data extract when finally submit

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/18](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/18)
---
For question 2 getting Error: At [8].title: Values don’t match. Expected: “9. Un matrimonio di troppo”. Actual: “9. You’re Cordially Invited” But this movie is not found when searched by name  

image1414×295 19 KB
Here's a description of the image:

The image shows a screenshot of a search interface, likely from a database or online catalog.  The left side displays search filters.  The top-left corner shows "Search filters" in a bold, slightly larger font size.  Next to it, there’s a small button that says "Expand all" with a downward-pointing arrow, suggesting there might be more filter options that can be expanded.

Below, there are two filter fields:

* **Title name:** This field has a text input box where "Un matrimonio di troppo" is typed.  This suggests a search for this particular title.  Small upward-pointing arrows next to this and the next field indicate they're expandable.

* **Title type:** This field is empty, indicating that no specific title type has been selected.

The right side of the image displays a large, greyed-out magnifying glass icon with a cross over it. This symbol usually signifies "no results found". Below this icon, the text "No results found" is prominently displayed in bold black letters.  A smaller line of text underneath instructs the user to "Please adjust your filters or start a new search".

The overall appearance suggests a clean and simple search interface, with the "No results found" message clearly indicating the outcome of the current search parameters. The presence of the Italian phrase "Un matrimonio di troppo" hints at the language or content focus of the database.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/19](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/19)
---
how to get the BBC weather API key?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/20](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/20)
---
Just a quick query on the Bonus mark.

Would this be added to the final grade? Say for example, Someone get a full score in the first 4 assignments. So the total comes up to 39.5/39.5, and would be converted to 0.15 or 15 marks. Would the bonus mark be additional to that 15 or would the score change to 40.5/39.5 and then get normalised to 15?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/21](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/21)
---
@JoelJeffrey It will be added to the GA4 marks, not the final grade. So, it’s roughly worth 0.15% on the total - not a full 1% on the total.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/22](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/22)
---
you can go and login using your email id in this below mentioned link

https://home.openweathermap.org/api\_keys

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/23](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/23)
---
Error: At [10].year: Values don’t match. Expected: "2025– ". Actual: “2025–”

Can someone help me with this?  
Thanks

Edit: Resolved

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/24](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/24)
---
Q8 I got the Error: No executed job step matches 23f2003853@ds.study.iitm.ac.in. the .yml file contains the following  
" name: Daily Commit

on:  
schedule:  
- cron: ‘0 12 \* \* \*’ # Runs daily at 12:00 PM UTC  
workflow\_dispatch: # This allows manual trigger

jobs:  
commit:  
runs-on: ubuntu-latest

```
steps:
- name: Checkout repository
  uses: actions/checkout@v2

- name: Make a dummy change with email 23f2003853@ds.study.iitm.ac.in in the commit
  run: |
    echo "This is a daily commit" > daily_commit.txt
    git config --global user.email "23f2003853@ds.study.iitm.ac.in"
    git config --global user.name "23f2003853"
    git add daily_commit.txt
    git commit -m "Daily commit from 23f2003853@ds.study.iitm.ac.in"
    git push"

```

@Jivraj can help me to fix the issue

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/25](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/25)
---
Have a step with your email id as its name. (Instead of checkout repository)  
Also make sure you give read and write permission so it commits without any error

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/26](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/26)
---
name: Daily Commit

on:  
schedule:  
- cron: ‘0 0 \* \* \*’ # Runs once a day at midnight UTC  
workflow\_dispatch: # Allows manual triggering of the workflow

jobs:  
commit:  
runs-on: ubuntu-latest

```
steps:
- name: Checkout repository
  uses: actions/checkout@v3

- name: Make daily commit by 23f3000264@ds.study.iitm.ac.in
  run: |
    echo "Daily commit by 23f3000264@ds.study.iitm.ac.in" >> daily_commit.txt
    git add index.html
    git commit -m "Daily commit"
    git push
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

```

sir this is my code and im getting a error in this  

image703×137 9.75 KB
The image shows a screenshot of a user interface element, likely from a software application or a web page.  The primary focus is a text input field where a user is asked to enter a GitHub repository URL.  The format for the URL is explicitly given as `https://github.com/USER/REPO`.

The user has entered the following URL: `https://github.com/dakshagarwal76/daily-update`.

Below the input field, an error message is displayed: `Error: No executed job step matches 23f3000264@ds.study.iitm.ac.in`.  This suggests that the provided repository URL is not associated with the expected job step identified by the alphanumeric string.  The error message points to a mismatch between the provided GitHub repository and some internal identifier (likely a job ID or similar) within the system.

The overall appearance is of a dark-themed interface, with the text input field highlighted in a light color against the dark background, suggesting visual clarity and contrast. The error message is highlighted in a distinct reddish-pink color, typically used to indicate errors or warnings.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/27](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/27)
---
dont remove the space after year- for example “year”: "2023- "

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/28](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/28)
---
Please anyone help me in doing q1 , my doubt is when i open the website Advanced search , i have click on movies and then do the coding part if not how to select titles of the movies as there is no movies on the page.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/29](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/29)
---
In q4 i got this error someone pls expalin “Error: At root: Property name mismatch”

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/31](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/31)
---
```
Student marks - Group 100

| Maths | Physics | English | Economics | Biology |
| ----- | ------- | ------- | --------- | ------- |
| 48    | 51      | 15      | 47        | 65      |
| 74    | 70      | 23      | 17        | 70      |
| 81    | 50      | 59      | 45        | 51      |
| 80    | 63      | 43      | 99        | 28      |
| 85    | 72      | 82      | 79        | 14      |
| 76    | 50      | 15      | 55        | 13      |
| 21    | 86      | 25      | 14        | 64      |
| 54    | 72      | 98      | 30        | 96      |
| 15    | 24      | 67      | 19        | 35      |
| 68    | 82      | 16      | 70        | 67      |
| 64    | 94      | 42      | 26        | 10      |
| 31    | 79      | 98      | 21        | 24      |
| 90    | 32      | 88      | 39        | 56      |
| 36    | 72      | 79      | 86        | 96      |
| 91    | 61      | 57      | 28        | 23      |
| 81    | 40      | 95      | 74        | 30      |
| 60    | 31      | 66      | 36        | 83      |
| 81    | 16      | 67      | 25        | 90      |
| 40    | 96      | 57      | 84        | 47      |
| 53    | 92      | 10      | 10        | 82      |
| 33    | 40      | 20      | 68        | 95      |
| 95    | 48      | 69      | 24        | 42      |
| 93    | 84      | 79      | 33        | 17      |
| 40    | 81      | 39      | 31        | 60      |
| 31    | 44      | 96      | 78        | 54      |
| 58    | 21      | 98      | 58        | 44      |
| 47    | 22      | 91      | 77        | 46      |
| 61    | 93      | 75      | 25        | 79      |
| 18    | 19      | 47      | 20        | 58      |
| 77    | 51      | 28      | 14        | 97      |

```

This is the piece of markdown that is being generated for the last question of ga4.Even after using the prettier of the mentioned version i am getting incorrect answer.  
Anyone like to help.  
@Jivraj @carlton @s.anand

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/33](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/33)
---
For Q10, I am extracting the text first using PyMuPDF (fitz) and then using markdownify to convert it to markdown and finally prettier. However despite trying changing it from PyMuPDF to other text extraction libraries, I end up getting

> Incorrect. Try Again

errors

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/34](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/34)
---
I think you have used the wrong document, because, this is the marks list for Q9

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/35](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/35)
---
which tool you are using ?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/36](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/36)
---
HOW TO GET BBC API KEY  

image1888×868 75.5 KB
This image shows a programming exercise or coding challenge within a web-based interface. Let's break down the visible elements:

**Top Section:**

* **Header:** Displays "Due Sun, 9 Feb, 2025, 11:59 pm IST" indicating a deadline.  "Score: 1/10" shows the current score, and buttons "Check all" and "Save" are present.

* **Instructions:**  The core of the exercise is laid out in three numbered steps:
    1. **API Integration and Data Retrieval:** This step details fetching location data from a BBC Weather API using GET requests.
    2. **Weather Data Extraction:**  This involves retrieving weather forecast data using the `locationId` obtained in the previous step.
    3. **Data Transformation:**  This is the key transformation step where the code needs to extract `issueDate` and `enhancedWeatherDescription` and organize them into a JSON object. The structure of the JSON object is exemplified.

* **Example JSON Output:** A sample JSON output is shown, demonstrating the desired format:  A JSON object where dates (`issueDate`) are keys, and weather descriptions (`enhancedWeatherDescription`) are values.

**Bottom Section:**

* **Question:**  "What is the JSON weather forecast description for Tel Aviv?" This is the question the user needs to answer by writing code.

* **Answer Box:** A text box is provided for the user to enter the JSON code representing the weather forecast for Tel Aviv, based on the instructions and the example output.

* **Error Message:** A "SyntaxError: Unexpected end of JSON input" is visible, indicating an error in the user's code input. This suggests that the user hasn't correctly formatted their JSON response.


**Overall:**

The task is to write code that interfaces with the BBC Weather API, retrieves weather data for Tel Aviv, and then formats that data into a specific JSON structure. The error message highlights that the user's attempt at creating the JSON has failed due to a syntax issue.  The user needs to fix their code to produce valid JSON matching the example provided.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/37](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/37)
---
in the bbc question what should be starting and the ending date

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/38](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/38)
---
you dont need the key you need that file used in 2 lecture videos just look for it.
That's a pixel art depiction of a thumbs-up gesture. 


Here's a breakdown of its features:

* **Style:** The image is clearly pixel art, meaning it's composed of individual squares of color to create the image.  The resolution is low, giving it a blocky appearance.

* **Color:** The dominant color is a yellowish-gold, used for the entire hand. There's subtle shading variation within the hand to give it a slightly three-dimensional look, but it's minimal due to the pixel art style.

* **Shape and Form:** The hand is depicted in a simplified, cartoonish way. The fingers are not individually detailed; they are more suggestive of a clenched fist with a thumb extended upwards. 


* **Meaning:** The thumbs-up gesture universally signifies approval, agreement, or positivity.  This image functions as a visual representation of that positive sentiment.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/39](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/39)
---
Please find below the screen shot showing the committed with step name my iitm email id  

image1366×768 79.8 KB

  
But the answer says  

image602×164 21 KB

  
Please help to fix the issue
Here's a description of the image:

The image shows a screenshot of a computer screen displaying a GitHub Actions workflow run. 


Here's a breakdown of the visible information:

* **Browser Window:** The top shows a Chrome browser window with the GitHub URL clearly visible.  It indicates a workflow run (`/workflows/actions/runs/13154595741/workflow`).

* **Workflow Run Details:** The left side shows the summary of the workflow run, including:
    * The workflow name (`23f2003853@ds.study.iitm.ac.in`) and run number (#13).
    * A checkmark indicating successful completion of the `daily-commit` job.
    * Sections for Summary, Jobs, Run details, and Usage.
    * A button to view the Workflow file, which is expanded to show the code.

* **Workflow File Code:** The central and right part of the image displays the YAML code of the workflow file.  This code defines:
    * The workflow name.
    * A schedule (`cron: '0 10 * * *'`), indicating a daily run at 10:00 AM UTC.
    * Manual triggering capability (`workflow_dispatch`).
    * Permissions to write contents.
    * The `daily-commit` job which runs on `ubuntu-latest` and includes steps such as checkout using the `actions/checkout@v3` action.

* **Bottom of Screen:** The bottom of the screenshot shows the Windows taskbar, the system clock (showing the time and date), the weather, language settings, and the "Activate Windows" message, indicating the operating system is not activated.

In summary, the image provides a detailed view of a GitHub Actions workflow run, showing both the overall status and the specific YAML code that defines its behavior.  The code suggests a workflow that runs daily to perform some action (likely a commit) on a repository.
 The image shows a screen capture of a web page, likely part of a GitHub Actions workflow setup or verification process.

Here's a breakdown of the content:

* **Instructions:** The top section provides instructions for setting up and verifying a GitHub workflow:
    * The workflow's YAML file must be located in the `.github/workflows/` directory.
    * After creation, the workflow should be triggered and allowed to complete.
    * Verification involves checking that the workflow is the most recent action in the repository and that it creates a commit within 5 minutes of its run.

* **Repository URL Input:**  A text input field prompts the user to enter their repository URL.  The placeholder text indicates the expected format: `https://github.com/USER/REPO`.  The user has entered `https://github.com/23f2003853/workflows`.

* **Error Message:** A red error message appears below the input field: "Error: No executed job step matches 23f2003853@dsstudy.itm.ac.in". This suggests the provided repository URL or the workflow within it is not functioning as expected, or the workflow hasn't run yet.


* **"Check" Button:** A blue button labeled "Check" is present at the bottom, presumably to submit the repository URL for verification and possibly trigger the workflow if it isn't already running.


* **Overall Context:** The image strongly suggests a problem with a user's GitHub Actions workflow. The error message indicates that no matching job steps were found. The user needs to either fix their workflow YAML file, correctly trigger the workflow, or provide the correct repository URL.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/40](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/40)
---
Still the issue is there. Have posted screen shot.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/41](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/41)
---
what Mr. Sakthivel S said is correct. could you tell me what tool did you use to convert .md file. I have done as per links in question and used chatgpt also. but nothing is correct

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/42](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/42)
---
Please give the solution if you got any…have you been able to solve the bbc weather question?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/43](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/43)
---
@s.anand @carlton  
In question 8 i got error  
“Enter your repository URL (format: https://github.com/USER/REPO):  
https://github.com/Ansh205/github-actions  
Error: No workflow runs found”  
But i have successfully commited  

Screenshot 2025-02-05 1932331462×642 38.4 KB
The image shows a screenshot of a workflow monitoring interface, likely from a CI/CD (Continuous Integration/Continuous Deployment) platform like GitHub Actions or GitLab CI.  Here's a breakdown of the content:

**Header:**

* **"All workflows"**:  This is the main title, indicating the page displays all active workflows.
* **"Showing runs from all workflows"**:  A subtitle clarifying that the data shown represents all runs from all workflows.
* **Search Bar**: A search bar with the placeholder text "Filter workflow runs" allows filtering workflow runs based on various criteria.

**Main Section:**

* **"4 workflow runs"**:  This indicates the number of workflow runs currently displayed.
* **Workflow Run Entries**: The main body consists of four separate workflow run entries. Each entry contains:
    * **Status Icon**: A green checkmark (✓) for successful runs and a red 'x' (✕) for failed runs.
    * **Workflow Name**:  "Daily Commit Workflow" is the name of the workflow in all cases.
    * **Workflow Run Details**: A description of the run, e.g., "Daily Commit Workflow #4: Manually run by Ansh205," indicating the run number and the user who initiated it manually.
    * **Branch**: The branch the workflow ran on ("main" in all cases in this image).
    * **Time Since Run**: Displays when the run completed ("5 minutes ago," "37 minutes ago," etc.) and duration.
    * **Three Dots Icon**: Three vertical dots ( ... ) likely represent a menu for more options related to each run.

**Column Headers:**

At the top, there are column headers:

* **"Event"**:  Likely indicates how the workflow was triggered (manual, scheduled, etc.).
* **"Status"**: The success or failure status of the workflow run.
* **"Branch"**: The Git branch the workflow operated on.
* **"Actor"**:  The user or system that initiated or triggered the workflow run.


In summary, the image displays a clean and organized view of recent workflow runs, providing crucial information about their success, timing, user, branch, and the ability to filter the data. The consistent "Daily Commit Workflow" name suggests a recurring workflow that executes after every commit.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/45](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/45)
---
Just follow the links and notebooks given in the references.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/46](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/46)
---
@Jivraj @carlton  
sir i have submitted my GA3 but its showing not submitted why?  

Untitled design1414×2000 314 KB
The image shows a screenshot of a web browser displaying an online assessment or exam. 


Here's a breakdown of the visible content:

* **Top Bar:** A standard browser address bar is visible at the very top, showing a URL (partially obscured) related to an online learning platform (possibly a university's learning management system). The title bar indicates a deadline ("Ended Wed 3 Feb 2025, 11:59 GMT").

* **Header:** The main header states "TDS 2025 Jan GA3 - Large Language Models," indicating a course, assignment, and topic related to large language models.

* **Instructions:** A section provides instructions for the assessment.  These instructions include advice about reading material, checking answers multiple times, resubmissions, and permitted resources/tools.  There's a specific note about multiple browser windows.

* **Discussion Forum:** A button or link invites the user to "Join the discussion on Discourse."

* **Login Information:**  A small line indicates the user's logged-in status with a partially visible user ID.

* **Recent Saves:** Shows recent saves made by the user (time and score information partially visible).

* **Module 3: Large Language Models:** A section heading marks the current module.

* **Assignment Details:**  This section details a graded assignment, its due date (Feb 5, 2025), and the student's current submission status ("Not Submitted").

* **Scoreboard:**  A table displays placeholders for the user's score, peer average, and median score for the assignment.  All three fields show hyphens, indicating the assignment has not yet been submitted and scored.

The overall appearance suggests an academic online assessment platform, likely used for a course or program related to large language models in the field of technology or data science.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/47](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/47)
---
@s.anand Sir no submit button is available. On the top of it say submission is required. Could you clarify us  

image690×388 46.5 KB
Here's a description of the image:

The image is a screenshot of a computer screen showing a web browser displaying an online course assignment. 


Here's a breakdown of the visible content:

* **Top Browser Bar:** Shows the URL of the assignment page, indicating it's hosted by IIT Madras' online degree program.  Standard browser controls (back, forward, refresh, etc.) are also visible, along with a star (bookmark), a bell (notifications), and a profile icon.  The title bar indicates the page is a "Graded Assignment 4".

* **Left Sidebar:** Contains a navigation menu for the online course. This menu lists:
    * Modules: "Course Introduction", "Module 1: Development Tools", "Module 2: Deployment Tools", "Module 3: Large Language Models", "Project 1", "Module 4: Data Sourcing", and "Graded Assignment 4".  These are selectable items, as indicated by arrows next to them.
    * Grades: A section labeled "Grades" is also present.
    * Calc: A section labeled "Calc" is visible at the bottom, suggesting a calculator or spreadsheet-like tool.

* **Main Content Area:** This is the largest section and displays the details of the "Graded Assignment 4". The text includes:
    * **Due Date:** Clearly states the due date and time.
    * **Submission Policy:** Explains that multiple submissions are allowed before the deadline, with only the final submission being graded.
    * **Troubleshooting:** Provides a list of potential issues that might prevent access to the assignment, such as ad blockers, cookie blockers, browser extensions, and network restrictions. It also specifies that Chrome is the recommended browser.
    * **Student ID Requirement:** Emphasizes the need to use the student ID when accessing the assignment; otherwise, the grade will not be considered.
    * **Assignment Link:** Provides a direct link to access the graded assignment itself.


* **Bottom Taskbar:** A standard Windows taskbar is visible at the bottom, showing open applications and the system clock.


In essence, the screenshot displays instructions and crucial information regarding a graded assignment within an online course offered by the Indian Institute of Technology Madras.  The emphasis is on providing clear instructions, troubleshooting steps, and the link to access the actual assignment.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/48](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/48)
---
what’s your directory structure, is it (.github/workflows/<filename.yaml>) and public

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/49](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/49)
---
As per instruction we need to create a directory in that we should have .yml file. But I tried with there were two issues (1) Github has not allowed to run the file (as there was no menu is available to run manually) (I checked with Copolit AI it says it is not correct to have cron jobs in a directory, I am not sure) (2) when I submit the url to iitm I got the following error  

image602×135 24.8 KB

  
I removed the directory and submitted the same url I got the following error  

image1122×184 5.81 KB

  
I do not know what to do next. Can TA help us
Here's a description of the image:

The image shows a section of a webpage, likely a form or interactive tutorial. The primary content is a set of instructions, with a section for user input.

**Instructions:** The instructions guide the user through steps relating to a GitHub workflow:

1. **Location:** The workflow should reside in the `.github/workflows/` directory.
2. **Post-creation steps:** After creating the workflow, the user must trigger it, wait for completion, ensure it's the most recent action in the repository, and verify a commit is created within 5 minutes of the run.
3. **Repository URL Input:** A text field prompts the user to enter their repository URL, providing a format example (`https://github.com/USER/REPO`).  The user has entered `https://github.com/23f2003853/workflows`.

**Error Message:**  A red error message at the bottom indicates a `YAMLParseError`. The error specifies that implicit keys need to be on a single line, pointing to the start of an HTML doctype (`<!DOCTYPE html>`) which is unexpected in the YAML file used for the workflow. This suggests that the user is likely providing an incorrect input or has an incorrectly formatted workflow definition file.

**Overall:** The image captures a common scenario of debugging a GitHub workflow. The error message directly points to a syntax error, and the provided instructions indicate the steps required for a successful workflow execution.
 The image shows a section of a webpage, likely a form for checking GitHub repository workflows. 


Here's a breakdown of the content:

* **Instructional Text:** At the top, it says "Enter your repository URL (format: https://github.com/USER/REPO):". This clearly indicates the expected input format.

* **Input Field:** Below the instruction, there's a text input field. The URL "https://github.com/23f2003853/workflows" is entered in this field. A red border around the field suggests an error.  An exclamation mark icon (①) appears near the right end of the input field, also indicating an error.

* **Error Message:** Below the input field, an error message is displayed: "Error: No executed job step matches 23f2003853@ds.study.iitm.ac.in". This explains that the entered repository doesn't contain any executed workflow steps that match the expected pattern (presumably tied to the `23f2003853@ds.study.iitm.ac.in` part).

* **"Check" Button:** At the bottom, a blue button labeled "Check" is present. This button is likely used to submit the repository URL and trigger the workflow check.

In summary, the user has inputted a GitHub repository URL, but the system has returned an error indicating it cannot find any matching executed job steps within that repository, based on a specific identifier.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/50](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/50)
---
The submission is on the Actual assignment page like for all the previous GAs in TDS. This is the **ONLY** valid submission button for GA1, GA2, GA3, GA4, GA5.

Screenshot 2025-02-06 at 10.43.15 am1390×1146 113 KB
Here's a description of the image:

The image shows a webpage, likely an online exam or quiz. 


**Top Section (Browser Bar and Navigation):**

* A standard browser address bar is visible at the top, showing a URL that includes "exam.sanand.workers.dev/tds-2025-01-ga4," suggesting a specific exam or test. 
* Standard browser navigation buttons (back, forward, refresh) are present.


**Header:**

* A blue header bar displays "[Admin] Due Sun, 9 Feb, 2025, 11:59 pm IST Score: 0". This indicates an exam deadline, time zone, and the current score (zero).
* Two buttons are in the header: "Check all" and "Save". The "Save" button is highlighted, suggesting the user's focus.


**Main Content:**

* Large text displays "TDS 2025 Jan GA," which seems to be the title or identifier of the exam.
* Below this is the heading "Instructions," followed by a numbered list of guidelines for taking the test:
    * These instructions include advice on checking answers, saving progress, handling browser issues, and permitted resources.  The words "Check" and "Save" are highlighted within the instructions, indicating the corresponding buttons above.

**Overall:**

The screenshot clearly points to an online test interface. The "Save" button's highlighted status suggests the user is likely in the process of completing or reviewing the test and saving their work. The instructions emphasize regular saving to prevent data loss.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/51](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/51)
---
try with this

* name: Set up Git user (23f2003853@ds.study.iitm.ac.in)  
  run: |  
  git config --global user.name “GitHub Actions Bot”  
  git config --global user.email “23f2003853@ds.study.iitm.ac.in”

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/52](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/52)
---
Thank you for your help , my repo was not public before and can you also help me in g4 i got this “Error: At root: Property name mismatch”

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/53](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/53)
---
In g4 which Question have that error you are getting

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/54](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/54)
---
In the last two question of the ga,it is mentioned including both groups.so what is the meaning of this .  

image1622×601 85.5 KB

  
@Jivraj @carlton
The image contains a text description of a data analysis task.  Here's a breakdown:

**The Task:**

The core task is to calculate the total Biology marks for students who achieved 17 or more marks in Physics, specifically those belonging to groups 43-66 (inclusive). This requires several steps:

1. **Data Extraction:** Obtain the student marks data from a PDF file (`q-extract-tables-from-pdf.pdf`) using PDF parsing libraries (Tabula, Camelot, or PyPDF2).  The data should be converted into a usable format (CSV, Excel, or DataFrame).

2. **Data Cleaning and Preparation:** Convert the marks data into a numerical format to enable accurate calculations.

3. **Data Filtering:** Identify the subset of students who meet the criteria: 17 or more marks in Physics and belonging to groups 43-66.

4. **Calculation:** Sum the Biology marks for the filtered students.

**Context and Benefits:**

The task is presented within the context of EduAnalytics, a system that automates this process for Greenwood High School. The benefits of automation are listed:

* **Identify Performance Trends:** Quickly identify areas needing improvement or where students excel.
* **Allocate Resources Effectively:** Direct resources to areas and subjects that require attention.
* **Enhance Reporting Efficiency:** Reduce manual data processing time.
* **Support Data-Driven Strategies:** Use accurate data to improve educational strategies and outcomes.


**The Question:**

The final question explicitly asks for the total Biology marks based on the specified criteria.  This is the ultimate goal of the four-step data analysis process.

In short, the image presents a well-defined data analysis problem, outlining the necessary steps and highlighting the overall benefits of automating the process.  The final question directly asks for the answer produced by completing those steps.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/55](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/55)
---
Hi Tushar,

If you looked at the PDF you might have realised that students have been grouped. The question gives you a range for the groups 43-66. Including both groups implies both group 43 and 66 are included in your calculation.

kind regards

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/56](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/56)
---
Question 4 "  
Sample output

{  
“25-02-04”: “Sunny intervals and light winds”,  
“25-02-05”: “Light rain and light winds”,

}  
Error: At root: Property name mismatch"

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/57](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/57)
---
Hi, even i’m facing the same issue,  

image1564×715 34.2 KB

  

image1916×882 65.1 KB

  

image1605×320 26.5 KB

@Jivraj  
@Saransh\_Saini  
@carlton  
Can anyone please help to fix this issue and submit this correctly.
This image shows a GitHub Actions workflow run.  Here's a breakdown of the key elements:

* **Top Bar:**  The top bar displays the repository name (`DigvijaysinhChudasamaliTM / TDS_GA_4`), a search bar, and standard GitHub navigation tabs (Code, Issues, Pull requests, Actions, Projects, Wiki, Security, Insights, Settings).

* **Workflow Run Details:** The main section shows details about a specific workflow run titled "Daily Commit #10".

    * **Summary:** A summary section shows that the workflow was triggered manually 16 hours ago by the user `DigvijaysinhChudasamaliTM`  branch `main`.  It shows the workflow completed successfully (`Success`) and took 18 seconds.

    * **Jobs:**  A single job, "daily-commit," is listed and shows a green checkmark, indicating successful completion.

    * **Run Details:**  This section provides access to more detailed information regarding resource usage and the workflow file itself.

    * **Workflow File:** This shows the name of the workflow file (`daily-commit.yml`) and its trigger (`on: workflow_dispatch`).


* **Right Sidebar:** This area displays information about the workflow run, including the job status, total duration, and artifacts (which are none in this case, represented by "-").

* **Overall:** The visual style is consistent with the dark theme often used in GitHub.  The green checkmarks indicate successful completion of both the overall workflow run and the individual job. The image clearly illustrates a successful automated process within a GitHub repository.
 The image shows a GitHub repository's `.yml` file, a workflow definition file for automating daily commits. 


Here's a breakdown of the key information visible:

* **Repository:** The repository belongs to user `DigvijaysinhChudasamaliTM` and is named `TDS_GA_4`. The specific file displayed is within the `github/workflows` directory and is named `daily-commit.yml`.

* **Workflow Name:** The workflow is named "Daily Commit".

* **Schedule:**  The `cron` expression `'0 0 * * *'` indicates that the workflow runs daily at midnight UTC.

* **Manual Trigger:** The workflow also allows manual triggering via the `workflow_dispatch` keyword.

* **Steps:** The workflow consists of these steps:
    * **Checkout repository:** Uses the `actions/checkout` action to check out the repository's code.
    * **Set up Git configuration:** Configures the Git user email and name. The email is set to a GitHub Actions generic email.
    * **Create a file with a daily commit message:** Creates a file (`daily-commit.txt`) containing a message indicating an automated daily commit.
    * **Commit changes:** Commits the changes made.

* **File Structure (left panel):** The left panel displays the repository's file structure, showing the location of the `daily-commit.yml` file and a related `daily-commit.txt` file.

* **Recent Activity (top right):** Shows the last update made to the `daily-commit.yml` file, indicating the time it was last modified (17 hours ago).

* **Code Editor (right panel):** The main area shows the code of the `daily-commit.yml` file, including comments explaining each section.  The line numbers are clearly visible.

* **Top Bar:** This shows the standard GitHub interface elements, including navigation links (Code, Issues, Pull requests, etc.), a search bar, and the user's profile icon.

In essence, this screenshot showcases a GitHub Actions workflow designed to automatically create and commit a simple text file to a repository every day. This is a common practice for keeping a repository active and for various automated tasks.
 The image shows a dark-themed interface, possibly a web page or application, with instructions and an input field. 


Here's a breakdown of the content:

**Instructions:**

* **"After creating the workflow:"** This heading introduces a set of steps.
* Three bullet points outline the steps to follow:
    * Trigger the workflow and wait for completion.
    * Ensure the workflow appears as the most recent action in the repository.
    * Verify that a commit is created within 5 minutes of the workflow run.
* **"Enter your repository URL (format: https://github.com/USER/REPO)"** This prompts the user to input a GitHub repository URL.

**Input Field:**

* A text input field displays a GitHub repository URL: `https://github.com/DigvijaysinhChudasamalITM/TDS_GA_4`.  This is likely the user's input.
* A small red circle with a white 'i' inside suggests an information icon, possibly offering more details on the input field.

**Error Message:**

* **"Error: No executed job step matches 21f2000588@ds.study.iitm.ac.in"** This error message indicates a problem; a job step with that specific identifier was not found. This suggests the workflow may have failed or encountered an issue during execution.


In summary, the image depicts a user attempting to execute a workflow on a GitHub repository, encountering an error due to a missing job step. The error message and instructions provide context for the issue.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/58](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/58)
---
21f3002277:

> Set up Git user (23f2003853@ds.study.iitm.ac.in)

Still the same error appears
That's a digital image showing a single, uppercase letter "V" in white against a solid bright blue background. 


The "V" is sans-serif, meaning it lacks the small decorative strokes or feet at the ends of the letterforms. It's relatively simple and straightforward in its design.  The image is likely a profile picture or avatar, perhaps used online in a forum or social media platform. The bright blue is a common choice for brand colors.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/59](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/59)
---
Thanks for providing clarification Sir

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/60](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/60)
---
I am also facing same issue can’t resolve.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/61](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/61)
---
@Jivraj @carlton @Saransh\_Saini  
In ques 4 Scrap the BBC Weather API,  
I scraped the locationId for my city (i.e Mumbai)

and post that also mapped each `issueDate` to its corresponding `enhancedWeatherDescription` .

The sample output mentioned was:  
The output would look like this:

```
{
  "2025-01-01": "Sunny with scattered clouds",
  "2025-01-02": "Partly cloudy with a chance of rain",
  "2025-01-03": "Overcast skies",
  // ... additional days
}

```

And My Output after scraping (And as explained by professor in Video 2 BBC weather was)

{  
“2025-02-05”: “A clear sky and light winds”,  
“2025-02-06”: “A clear sky and light winds”,  
“2025-02-07”: “A clear sky and light winds”,  
“2025-02-08”: “A clear sky and light winds”,  
“2025-02-09”: “A clear sky and light winds”,  
“2025-02-10”: “A clear sky and light winds”,  
“2025-02-11”: “A clear sky and light winds”,  
“2025-02-12”: “A clear sky and light winds”,  
“2025-02-13”: “A clear sky and light winds”,  
“2025-02-14”: “A clear sky and light winds”,  
“2025-02-15”: “A clear sky and light winds”,  
“2025-02-16”: “A clear sky and light winds”,  
“2025-02-17”: “A clear sky and light winds”,  
“2025-02-18”: “A clear sky and light winds”,  
“2025-02-19”: “A clear sky and light winds”  
}

But it’s giving Error::  
Error: At root: Different number of properties

Can you please help how to fix this issue.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/62](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/62)
---
Issue resolved for me after following below step  
After creating the workflow:

* Trigger the workflow and wait for it to complete
* Ensure it appears as the **most recent action** in your repository
* Verify that it creates a commit during or within 5 minutes of the workflow run

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/63](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/63)
---
In place of “name: Setup up GIT config” change to “name: add commit {your\_email}”

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/64](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/64)
---
use this Google Colab with the city name to get the Json Body just change the date format.

@23f2004752

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/65](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/65)
---
@carlton @Jivraj could you please help me with this?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/66](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/66)
---
On running this colab with city = Mumbai,

I’m gettingh this error: Error: At root: Property name mismatch

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/67](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/67)
---
it’s getting,

```
{
    "2025-02-06": "Sunny and a gentle breeze",
    "2025-02-07": "Sunny and a gentle breeze",
    "2025-02-08": "Sunny and a gentle breeze",
    "2025-02-09": "Sunny and a gentle breeze",
    "2025-02-10": "Sunny and a gentle breeze",
    "2025-02-11": "Sunny and a gentle breeze",
    "2025-02-12": "Sunny and a moderate breeze",
    "2025-02-13": "Sunny and a gentle breeze",
    "2025-02-14": "Sunny and a gentle breeze",
    "2025-02-15": "Sunny and a gentle breeze",
    "2025-02-16": "Sunny and a gentle breeze",
    "2025-02-17": "Sunny and a gentle breeze",
    "2025-02-18": "Sunny and a gentle breeze",
    "2025-02-19": "Sunny and a gentle breeze"

}

```

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/68](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/68)
---
can tell me in your .yml which are all place did you use your iitm email id. Because I got the error No executed job step matches 23f2003853@ds.study.ittm.ac.in. My commit was completed in 11 seconds

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/69](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/69)
---
@s.anand @carlton @Jivraj  
Is there any way to crack this , I tired multiple time no improvement.  
Also what does this " It is *very hard* to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. Reformatting with Prettier helps standardize the output format for comparison." mean.  

image1327×743 41.6 KB
This image shows a computer screen displaying a coding exercise.  The instructions ask the user to:

1. **Convert a PDF to Markdown:** Extract the text and formatting from a provided PDF (`q-pdf-to-markdown.pdf`) into Markdown.
2. **Format the Markdown:** Use the Prettier code formatter (version 3.4.2) to standardize the Markdown.
3. **Submit:** Submit the formatted Markdown file.

The instructions emphasize the importance of preserving the structure and formatting from the original PDF as much as possible.  The "Impact" section explains how automating this process benefits EduDocs Inc. by enhancing productivity, improving quality, supporting scalability, and facilitating easier integration with various digital platforms.

Below the instructions, there's a text input box where the user is supposed to enter the formatted Markdown.  An attempt has been made, resulting in the lines:

`Ater vulnero solio tabula.`
`Auctus benigne coaegresco defetiscor delinquo.`
`Talio balbus cultura vae. Sint deripio tener adfectus agnitio aro cruentus arbustum. Abstergo alii sollers.`

The system responded with "Incorrect. Try again."  A final note explains the inherent difficulty in perfectly converting PDFs to Markdown and highlights the use of Prettier for standardization.  A small warning icon (a circled "i") is visible next to the user's incorrect response.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/70](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/70)
---
Same problem please help me too if you get it right.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/71](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/71)
---
Yes followed all these steps, and still the error is being seen,

Error: No executed job step matches 21f2000588@ds.study.iitm.ac.in

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/72](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/72)
---
Yes true,

Here’s the output:  
{  
“2025-02-05”: “Sunny and a gentle breeze”,  
“2025-02-06”: “Sunny and a gentle breeze”,  
“2025-02-07”: “Sunny and a gentle breeze”,  
“2025-02-08”: “Sunny and a gentle breeze”,  
“2025-02-09”: “Sunny and a gentle breeze”,  
“2025-02-10”: “Sunny and a gentle breeze”,  
“2025-02-11”: “Sunny and a moderate breeze”,  
“2025-02-12”: “Sunny and a gentle breeze”,  
“2025-02-13”: “Sunny and a gentle breeze”,  
“2025-02-14”: “Sunny and a gentle breeze”,  
“2025-02-15”: “Sunny and a gentle breeze”,  
“2025-02-16”: “Sunny and a gentle breeze”,  
“2025-02-17”: “Sunny and a gentle breeze”,  
“2025-02-18”: “Sunny and a gentle breeze”  
}

But unfortunately this error persists,

Error: At root: Property name mismatch

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/73](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/73)
---
Now re-check you answer. May it will give link where the issue exists. if it gives url browsers the link and address.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/74](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/74)
---
Yes true same happened with me.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/75](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/75)
---
re-check your answer again it may give an url. check the url

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/76](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/76)
---
Now on rechecking, the error message has changed to – “TypeError: Failed to fetch”

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/77](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/77)
---
No its giving such error:  

image1729×278 15.2 KB
The image shows a screenshot of a web interface, likely part of a software development tool or a similar application. 


Here's a breakdown of the visible content:

* **Top Section (Instructions):**  The top partially visible text seems to be instructions, possibly advising the user to verify a commit or action within a certain timeframe.  The full text isn't clear.

* **Repository URL Input:** A prominent input field asks the user to "Enter your repository URL".  Example formatting (using `https://github.com/USER/REPO`) is provided as a hint.  A URL is already entered into the field: `https://github.com/DigvijaysinhChudasamalITM/TDS_GA_4`.  A small, circular icon (possibly indicating an error or warning) is visible to the right of the input box.

* **Error Message:** Below the input field, an error message is displayed: "TypeError: Failed to fetch". This indicates that the application failed to retrieve information from the entered repository URL.

* **"Check" Button:** A blue button labeled "Check" is visible at the bottom.  This button likely attempts to validate the entered repository URL.

The overall appearance suggests a dark theme is used in the interface.  The error message is crucial; it clearly indicates that there's a problem connecting to or retrieving data from the specified GitHub repository. The likely cause is an issue with the repository URL itself, network connectivity, or permissions.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/78](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/78)
---
Here’s the action’s:  

image1921×467 45.4 KB
The image shows a screenshot of the GitHub Actions interface.  Here's a breakdown of the content:

**Left-hand Panel (Actions):** This section lists various options within GitHub Actions.  The items include:

* **All workflows:** This is selected, indicating the display shows all workflows.
* **Daily Commit:** A workflow named "Daily Commit" is listed.
* **Management, Caches, Attestations, Runners, Usage metrics, Performance metrics:** These are other options available within the Actions section.  They likely pertain to managing, monitoring, and analyzing the workflow executions.

**Right-hand Panel (All workflows):** This area displays the workflow runs.

* **All workflows:** The title indicates this section shows data for all workflows.
* **Showing runs from all workflows:** A subtitle clarifying the scope of the displayed data.
* **Help us improve GitHub Actions:** A feedback request box prompting users to help improve GitHub Actions.
* **15 workflow runs:**  The number of workflow runs currently displayed.
* **Two "Daily Commit" entries:** Two recent workflow runs for the "Daily Commit" workflow are listed.  Both were manually run by a user named "DigvijayainChudasamaTM".  They include timestamps ("13 minutes ago"), their status (both show a checkmark indicating successful completion), and the branch ("main") they ran on.


**Top Right Corner:**

* **Filter workflow runs:** A search bar allowing users to filter the displayed workflow runs based on specific criteria.
* **Give feedback:** A button to provide feedback to GitHub about Actions.


In essence, the image shows a typical view of a user's GitHub Actions page displaying recently run workflows and offering various management and feedback options. The focus is on the two recent successful runs of a workflow called "Daily Commit".
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/79](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/79)
---
Check you Github account and browse Action for your repo. then check All Work flows. Ensure the first item is schedule triggered confirmation

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/80](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/80)
---
What you meant by " Ensure the first item is schedule triggered confirmation"? You meant the latest one should be this right?

image1920×889 82 KB
The image is a screenshot of a GitHub Actions workflow page. 


Here's a breakdown of the visible content:

* **Top Bar:** Shows the repository name (`DigvijaysinhChudasamaliTM/TDS_GA_4`), standard GitHub navigation options (Code, Issues, Pull requests, Actions, Projects, Wiki, Security, Insights, Settings), and a search bar.

* **Left Sidebar:** Contains a navigation menu for GitHub Actions, including:
    * **Actions:**  A heading, with a "New workflow" button.
    * **All workflows:** A list that's currently selected, showing sub-items that are hidden, except for "Daily Commit".
    * **Management:** A section header,  with sub-items (Caches, Attestations, Runners, Usage metrics, Performance metrics) that are collapsed.

* **Main Content Area:** Displays the workflow runs.
    * **"All workflows" heading:** Displays the message "Showing runs from all workflows".
    * **GitHub Actions Feedback Request:** A banner asking for feedback to improve GitHub Actions.
    * **Workflow Run List:** A table-like view shows 15 recent workflow runs of a workflow named "Daily Commit."  Each run displays:
        * **Status:**  A green checkmark (success) or a red cross (failure).
        * **Run Number:** ("Daily Commit #15", etc.)
        * **Trigger:** Indicates whether it was manually triggered ("Manually run by...") or scheduled.
        * **Timestamp:** Shows when the run started.
        * **Duration:** Shows how long the run took.
    * **Filter Bar:**  A search bar ("Filter workflow runs") to filter the workflow runs.


* **Right Side:** Contains a "Give feedback" button near the top.  The workflow run list shows columns for Event, Status, Branch, and Actor.

The overall appearance suggests a dark theme is selected in the GitHub interface. The screenshot is likely taken to illustrate or troubleshoot a specific workflow's activity.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/81](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/81)
---
check this type of screen  

image1000×286 16.8 KB
The image shows a screenshot of a GitHub Actions page. 


Here's a breakdown of the content:

* **Top Section (Feedback Request):** A banner at the top invites the user to provide feedback on GitHub Actions. It includes a button labeled "Give feedback" and a close button (X).

* **Middle Section (Workflow Runs Summary):** This section displays a summary indicating there are 71 workflow runs.

* **Bottom Section (Specific Workflow Run):** This section details a specific workflow run:

    * **Workflow Run ID:** `23f2003853@ds.study.iitm.ac.in` is highlighted, indicating the user or system responsible for the run.  A more detailed ID, `23f2003853@ds.study.iitm.ac.in #23`, is shown below.  This shows it's run #23 by that user/system.
    * **Branch:** The branch is identified as "main".
    * **Time:** The run happened 23 minutes ago.
    * **Duration:** The run took 19 seconds.
    * **Status:** The green checkmark indicates successful completion of this particular workflow run.
    * **Action Buttons:** Three vertical dots (...) suggest further options related to this workflow run.


* **Headers (Event, Status, Branch, Actor):** These headers are visible in a table-like structure, suggesting that the bottom section displays data for each workflow run, though only one is fully visible in this image.


In short, the image captures a GitHub Actions dashboard showing summary information of workflow runs and inviting user feedback.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/82](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/82)
---
use name:email inside yml page

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/84](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/84)
---
Yep done, thank you!
That's a digital image of a smiling emoticon, specifically a yellow smiley face emoji. 


Here's a breakdown of its features:

* **Shape and Color:** The emoji is a perfect circle, predominantly bright yellow.

* **Facial Features:** It has two dark brown, oval-shaped eyes that are relatively small in proportion to the face.  A large, open-mouthed smile is prominent, showing a pink tongue and white, slightly uneven teeth. The mouth is a wide curve, expressing strong happiness or laughter.

* **Style:** The style is consistent with common emoji designs, with soft shading and a slightly glossy appearance giving a three-dimensional effect, though rendered in a pixelated style.  The lines are not crisp, reflecting the limitations of the pixel format.

The overall impression is one of cheerful exuberance. There is no text present.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/85](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/85)
---
```
Depopulo amoveo curo.
Concego creatinue ancilla vesper conicio cinimatico eribro.  
Custodia anica arbustum coniceto suma corporis aduno commenoro curiositas augero.  
Uredo thesis ancilla alter eun tener vomito praesentium templum.  
Magni deprimo celebre.

### Bellum pelor cornu vorax perspiciatis.

Labore elus umerus voluntarius.  
Vicissitudo cilíctum cicuta campana.  
Desino perspiciatis comodo.

### amarttudo tabesco crinis amissio

tui qui decumbo vobis  
audacia charismatubineus contigo  
aro eum talio elus  
coniuratio cubo ab vere  
validus tam patria deficio  
agnosco spectaculumcoerceo  
spectaculum vulpes valetudo  
minima cado suffragium  
asperiores thesaurus cometes  
vesica amplus cimentarius  
volum curiositas cornu

## Paupertrucido confido triduana ante sublime

# Consequatur comminor

Coadunatio delectus atqui placeat atque copia ventosus aer quae.  
Tatillo causa damatico validus torrena tivpinca.  
Adside nisi atavus aspiente.

[soius tam](https://tds.s-anand.net/#/markdown)

Ceno usilio desino velociter sit aut. Concedo accedo vac congregatio sperno venia sum sordeo animi tametsi. Accusamus suppellex turpis dedecor uliam vaco venusit:

- tu! amicitia ante suppellex studio
- utor debilito suasoria odio
- antea desino despecto magni

[coadunatio voco](https://tds.s-anand.net/#/markdown)

[incidunt aliquam](https://tds.s-anand.net/#/markdown)

Tametsitenuis conscendo.

- tempore vorner aestas commentoro
- absconditus coruscus

## Blanditiis tabula animi succedo

Asper summa tametsi ustulo villias conservo clam triumphus tener ager. Audax conforto adopto vesco arbustum deorsum terror impedit iure. Adsum atrox caries acc

Beatae ducimus aperio amarttudo caries

- cinis solvo unde unde arbustum
- canis civitas viro
- thorax pax demens
- arbustum suficco thorax testimonium ex.
- vinliter sumptus

Explicabo defico adfectus.

Comedo cattus justo tamdiu tumultus confido thesaurus coadunatio volutabrum. Succedo tabula audax copia vinculum.

**cogo audio suffragium**

crepito amiculum sufficio  
acer aestas utor  
debeo adopto utpote  
tametsi curatio ante

## Maxime vulgo depulso decipio atrox

## Career debeo

**conatus cui admoneo**

theatum pauper tego
pecco caeous vulgo
cursim desino arceo
balbus comminor et 

```

In the question no. 10, I have tried numerous time to get it right markdown content but it was incorrect all the time.

I have tried these steps:

```
import pymupdf4llm
md_text = pymupdf4llm.to_markdown("/content/q-pdf-to-markdown.pdf")

import pathlib
pathlib.Path("output.md").write_bytes(md_text.encode())

```

Then i run this in bash

```
prettier --write output.md

```

And what i got frankly telling was far from this, I did some manual touchups, and this what i have now. This is the best version i could come up with. Saw the preview, it does matches with the pdf.

#Can someone please advise me a better approach?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/87](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/87)
---
hey, can you help me in doing this i can’t able to do this.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/89](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/89)
---
@24ds3000090

We will be changing this question. Even we found it hard

Kind regards
That's an emoji! 


Specifically, it's a yellow, round emoticon with a wide, open mouth showing teeth and a pink tongue. The eyes are closed in a smiling expression. A single, light-blue droplet of sweat is shown on the right side of the face. The overall style is consistent with modern emoji designs, appearing smooth and slightly glossy.  The image is digitally rendered and pixelated, characteristic of emoji images.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/90](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/90)
---
@JoelJeffrey

We will be changing this question. Even we found it pretty hard

Kind regards
That's an emoji! 


Specifically, it's a yellow emoticon with a wide, open, laughing mouth, closed eyes, and a single drop of sweat on its right temple (from the viewer's perspective). The expression conveys a feeling of nervous or slightly uncomfortable laughter, perhaps suggesting amusement mixed with anxiety or exertion.  The style is consistent with common emoji designs found on smartphones and other digital platforms. There's no text present.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/91](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/91)
---
sir in the weather question could you provide from where do we get the bbc api because i have searched a lot and havent been able to find it

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/92](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/92)
---
https://tds.s-anand.net/#/bbc-weather-api-with-python

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/93](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/93)
---
try manually inspecting the output of the api and compare it with your script output.  
Or else try refreshing the browser and check.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/94](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/94)
---
@carlton  
Previously i got correct on q2 but now i am getting the error when i refresh the page “TypeError: Cannot read properties of null (reading ‘textContent’)”

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/95](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/95)
---
Please try city=“Mumbai” as a string literal.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/96](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/96)
---
Q4 BBC Weather

I don’t understand why I am getting

> Error: At root: Different number of properties

Is it because of different dates? Shall I match the dates?

@carlton Please guide. Thank you.

BBC weather565×781 30.5 KB
The image shows a coding challenge or exercise. 


Here's a breakdown of the image's content:

**Task Description:**

The top section describes a task involving three steps:

1. **API Integration and Data Retrieval:** Fetching weather data from the BBC Weather API using a location ID and API key.
2. **Weather Data Extraction:** Retrieving the forecast data.
3. **Data Transformation:** Extracting the `issueDate` and `enhancedWeatherDescription` and creating a JSON object where `issueDate` is the key and `enhancedWeatherDescription` is the value.

**Example Output:**

A sample JSON output is provided, showing the desired format:  a JSON object where dates are keys and weather descriptions are values.

**The Challenge:**

The main part of the challenge asks to provide the JSON weather forecast description for "Osaka". A JSON object is already partially filled in.

**Error Message:**

The attempt resulted in an "Error: At root: Different number of properties" message. This indicates the user's JSON object doesn't have the same number of key-value pairs as expected or required by the system.  The error suggests the JSON is not correctly formatted or is missing data according to the specifications.

**Input and Output Areas:**

There are text boxes for writing and checking the JSON code (the user enters their answer in the lower text box). A "Check" button allows the user to submit their answer.

**In short:** The image presents a programming problem requiring the user to retrieve and format weather data from an API into a specific JSON structure.  The error message highlights an issue with the submitted JSON's structure.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/97](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/97)
---
thema coruscus
--------------

* cupiditate celebrer
* argentum alius voro soluta
* sto decor capto suffoco acs tempus deludo deleo ventus odio

Sordeo tergo beatae coniecto ambitus carus. Vae tamdiu debilito verto confugo  
territo acies vos patria. Versus surgo degero vester tersus paulatim chirographum

| abeo | super | valetudo adhuc |
| --- | --- | --- |
| conatus | comptus | spiculum summisse |
| alienus | addo | demergo conturbo |
| uberrime | subseco | altus & ea |
| apto | cursus | infit & summa |

* tabula necessitatibus beneficium concido
* adhaero tepesco ars
* adnuo beatae
* cursim ahsens culpa animi aestivus

Solium vulgus commodo claro curriculum valens
---------------------------------------------

Aut ipsum spiritus tantillus vacuus adsum crebro animus pel paulatim. Tunc vallum  
torqueo aequus valens triduana illo. Uredo cursus fuga vir.

Cultellus adipiscor incidunt tondeo benevolentia capto contabesco bene tardus  
harum.

Bos subnecto beatae abeo vulnus terra verus balbus

* arguo via vallum usus aliquid
* tempus balbus videlicet acquiro

attonbitus tardus versus cuppedia  
derelinctuo curatio stalla solen  
comburo commodo caveo at  
deporto aliquid thymum  
confero sortitus ago  
triduana umquam acies

Beneficium doloremque aspernatur dolor dolorum despecto attonbitus unus alienus  
Capto optio dolores.  
Commodi sono denuo molestiae terebro  
Benigne anser vulgus brevis coaegresco vinum debeo.  
Cras aut ullam error terreo absque aro adstringo sublime thymum

Triumphuslaudantium curto certus
--------------------------------

Callide stabilis subito claudeo occaecati depono. Turba thymum bis deludo una.  
Sumo consuasor necessitatibus vix solitudo dolorum dolorem vinco inflammatio

* apparatus spero sulum desino ultra
* nauner necessitatibus bos calculus nlaceat
* animadverto defessus triumphus
* acquiro artificiose minima sortitus terminatio

Aegrus tot tot aetas. Clinís volva tamen sumptus. Solutio deludo suscipio deputo  
demens vero audeo annus alo accendo.

I am getting error: Incorrect. Try again.  
@Jivraj @carlton can you please explain the reason for this error

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/98](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/98)
---
Hi Mishkat

Please refer to this post.

GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025] Tools in Data Science

> @JoelJeffrey
> We will be changing this question. Even we found it pretty hard 
> Kind regards

Kind regards
That's a close-up headshot of a man. 


Here's a description:

* **The Man:** He appears to be of South Asian or Middle Eastern descent, with dark hair, brown eyes, and olive skin. He's wearing rectangular, dark-framed glasses. His expression is pleasant and somewhat neutral, almost a slight smile. He has short, neatly styled hair. 

* **Clothing:** He's wearing a purple collared shirt, which looks like a polo shirt or a similar style.

* **Background:** The background is a plain, pale yellow or beige wall, providing a simple, uncluttered backdrop that focuses attention on the subject.

* **Image Quality:** The image quality is somewhat low-resolution; it's a little blurry and pixelated, especially noticeable in the skin tones and details of the clothing.  It's likely a smaller image that's been enlarged.

There is no text in the image.  The image itself is primarily a portrait suitable for use as a profile picture or in a directory.
 That's an emoji! 


Specifically, it's a yellow circle emoticon with a wide, open-mouth laugh, closed eyes, and a single, light-blue droplet of sweat on its temple. The overall expression conveys a feeling of nervous laughter or a laugh that is so intense it's causing the emoji to sweat.  The style is consistent with modern emoji designs, showing a glossy, three-dimensional effect.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/99](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/99)
---
@s.anand Sir the question 10 of the Graded Assignment 4 is very tough I have tried everything from custom python codes using different libraries to online converted and also formatted using prettier. Please sir guide me how to do the question.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/100](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/100)
---
Yep figured that, and after matching the data solved the error and got that question correct.  
Though thank you.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/101](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/101)
---
@s.anand Sir I have done the question 2 of the graded assignment but I am very curious to know why the answers language gets periodically change. Is there some kind of backend code which is responsible for that or is something else ?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/102](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/102)
---
Yes we’ll were facing this issue.

@carlton sir mentioned yesterday that they will change the question.

"We will be changing this question. Even we found it hard

Kind regards"

So need to worry about that question for now.
That's an emoji! 


Specifically, it's a cartoon-style yellow emoticon with a wide, open-mouthed laugh. The eyes are closed in a way that suggests happy laughter. There's a single, light-blue droplet of sweat next to the emoji, suggesting the laughter might be nervous or intense. The overall style is similar to many commonly used emoji on smartphones and computers.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/103](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/103)
---
OK, that is good to hear, you won’t believe that yesterday I was trying this question for 2 hours literally, it can be more also.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/104](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/104)
---
I was stuck at that question for 2 days, I tried multiple ways but was not able to format the content with prettier as expected, every time I was getting the error “Incorrect. Try again.”

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/105](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/105)
---
On popular demand, I’ve made Q10 of GA4 easier (converting from PDF to Markdown). The question remains the same, but the check is more liberal and the error messages are more helpful. Please give it a shot now.

(FYI, one person *did* solve it. A colleague, not someone from the IITM DS program.)

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/106](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/106)
---
Hello Sir, i tried but unfortunately after extracting the contents and formatting the contents and submitting it, it’s showing various errors like Missing links, Missing tables…

But on checking the file i wasn’t able to find any single table in the contents in that case what could be done to fix these errors?

@Jivraj @carlton @Saransh\_Saini

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/107](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/107)
---
same issue with me as well

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/108](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/108)
---
Sir I checked the pdf file, there is only one place unorder list is given and the same is available in my answer. But the system throws error Missing List (I tried with other symbols \* and + also) . Please inform me where I made mistake  

image1108×271 5.87 KB
Here's a description of the image:

The image shows a screenshot of a code editor or similar environment.  The main focus is a rectangular area displaying a list of Latin words or phrases, each preceded by a hyphen.  The words are:

* cuppedia tamquam facilis confugo
* conservo depereo
* consectetur arx
* aeternus celebrer

Underneath this list, the message "Error: Missing lists" appears. This suggests that the software or tool used to process the data (presumably a Markdown parser) is unable to render the input data as a properly formatted list.

The top of the image contains the question: "What is the markdown content of the PDF, formatted with prettier@3.4.2?". This indicates the image is a result of trying to render some Markdown content from a PDF using a specific version of the `prettier` code formatter.  The `prettier@3.4.2` part refers to a specific version of this code beautifier.

The wavy red underlines under the Latin phrases in the list seem to highlight a problem detected by the software, likely related to the list formatting error. The presence of an exclamation mark icon near the right edge of the central area reinforces this idea of an error or warning being present.

In short, the image showcases a Markdown formatting error specifically related to creating an unordered list.  The error is caught by the system, and this is clearly shown in the output.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/109](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/109)
---
this is table. Check it  

image313×136 5.2 KB
The image contains a table with three columns and four rows.  Each column is headed by a Latin word:  `capitulus`, `deleniti`, and `pariatur`. Below each heading are four Latin words, apparently intended as example vocabulary words or a related word list. 


Here's a breakdown of the content:

* **Column 1 (capitulus):** voluptate, quaerat, vestigium, ait
* **Column 2 (deleniti):** barba, cedo, trans, alioqui
* **Column 3 (pariatur):** bellum, cursus, sortitus, verumtamen


The text is neatly formatted and appears to be a section from a Latin vocabulary list, exercises, or a similar educational resource.  The font is sans-serif and straightforward, and the layout is clean and easy to read.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/110](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/110)
---
Q 10 - PDF to Markdown.

Why it is saying

> Incorrect. Try again?

Do I need to add CSS?

`Carbo ventosus tametsi patior. Recusandae ciminatio alienus nisi ventosus apud. Theatrum abutor aperio spargo vestrum virga placeat adulescens. Deripio alveus creator omnis tabula patria cupiditate in virga speculum. Acidu`s alienus vehemens vapulus.`

**earum clamo collum**  
curtus careo curatio  
tendo sunt culpo  
Suus sit magni traho tempora.

Depraedor vae dedecor conturbo. Curia vigor vinco terebro alii tantum clam. Modi veniam alveus clementia sumo iusto adfero truculenter.

| cresco | solio | ademptio | terreo | bis |
| --- | --- | --- | --- | --- |
| tardus | carpo | allatus | depono | benevolentia |
| tunc | atavus | barba | urbs | considero |
| adulescensamplitudo |  | verbum | cultura | id |
| cenaculum | ipsum | sursum | conturbo | nemo |
| damno | arbitro | quibusdam | articulus | animadverto |

* ustulo crudelis depraedor
* sophismata tener apostolus suus adopto
* coniecto maxime rerum
* acceptus virga confero comes

cresco vomito

deputo ceno

Cuppedia uberrime socius atque paens
====================================

Sto theca testimonium aestus debitis
====================================

valde vulgus

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/111](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/111)
---
I checked many times. For me it says “Incorrect. Try again.”

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/112](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/112)
---
Ya i know, i added tables, list, blockquote, code, tables have all been added still it’s showing errors. Not sure where am I going wrong.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/113](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/113)
---
Please refer video and document relating to Question 1 of Assignment 3. There it is mentioned how to mark bold, table etc., use those marks

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/114](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/114)
---
I have added all those and pasted the markdown and it appears as above.

```
`` Carbo ventosus tametsi patior.
Recusandae ciminatio alienus nisi ventosus apud.
Theatrum abutor aperio spargo vestrum virga placeat adulescens.
Deripio alveus creator omnis tabula patria cupiditate in virga speculum.
Acidu`s alienus vehemens vapulus. ``

**earum clamo collum**
curtus careo curatio
tendo sunt culpo
Suus sit magni traho tempora.

Depraedor vae dedecor conturbo. Curia vigor vinco terebro alii tantum clam. Modi veniam alveus clementia sumo iusto adfero truculenter.

| cresco              | solio   | ademptio  | terreo    | bis          |
| ------------------- | ------- | --------- | --------- | ------------ |
| tardus              | carpo   | allatus   | depono    | benevolentia |
| tunc                | atavus  | barba     | urbs      | considero    |
| adulescensamplitudo |         | verbum    | cultura   | id           |
| cenaculum           | ipsum   | sursum    | conturbo  | nemo         |
| damno               | arbitro | quibusdam | articulus | animadverto  |

- ustulo crudelis depraedor
- sophismata tener apostolus suus adopto
- coniecto maxime rerum
- acceptus virga confero comes

[cresco vomito](;;;)

[deputo ceno](;;;)

# Cuppedia uberrime socius atque paens

# Sto theca testimonium aestus debitis

[valde vulgus](;;;)


```

Below is the screenshot of provided PDF. That font colour strains my eyes. Any particular reason for that PDF?

image541×439 20.9 KB
Here's a description of the image:

The image shows a page filled with Latin text, seemingly a collection of words and short phrases, possibly from a vocabulary list, exercises, or a short text with annotations.  The text is written in a serif typeface, common in classical texts.


**Key Features:**

* **Latin Text:** The predominant feature is a large quantity of Latin words and phrases, organized in columns or short groupings in some sections.  Some lines are longer than others.  Punctuation varies, but includes periods, commas, and occasional bullet points.

* **Highlighted Words/Phrases:**  Several words and short phrases are underlined, appearing to be possibly vocabulary words or key terms.  They are highlighted in a blue-ish color, making them stand out against the black text on the off-white background. Examples include: `cresco vomito`, `deputo ceno`, `valde vulgus`.

* **Organization:** The text is not consistently organized. Some sections appear to be lists of words (like a vocabulary exercise), while others look like sentence fragments or short sentences. There's no clear title or heading provided.


**Possible Interpretations:**

The image's content suggests a language learning context. It's probable that it's part of a Latin textbook, worksheet, or study notes.  The highlighted words might indicate vocabulary words to learn or phrases to practice translating.  The varied organization suggests that this is not a published, formal text; it might be a personal or classroom resource.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/115](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/115)
---
I am getting missing link error. I checked in the pdf file also, the blue color text seems a link but its not clickable.  
Any suggestion to move nearer to the actual solution.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/116](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/116)
---
You may try like this: cresco vomito

```
[cresco vomito](;;;)

```

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/117](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/117)
---
Even I’m getting a similar error in Q2, it is expecting a foreign title whereas my search result gives only English titles.  

image1614×250 14.4 KB

  
Please help.
The image shows a snippet of code that appears to be JSON data, along with an error message.

**JSON Data:**

The JSON data is formatted as a key-value pair structure, representing information about a TV show:

* `"id"`:  `"tt8712204"` (likely an identifier)
* `"title"`: `"25. Batwoman"` (the title of the show)
* `"year"`: `"2019-2022"` (the years the show aired)
* `"rating"`: `"3.6"` (a rating out of 10, possibly)


**Error Message:**

Below the JSON data is an error message:

`Error: At [12].title: Values don't match. Expected: "13. Pideme lo que quieras". Actual: "13. Ask Me What You Want"`

This message indicates a discrepancy in the title field.  The system expected the title to be "13. Pideme lo que quieras" (Spanish for "13. Ask me whatever you want"), but the actual title provided was "13. Ask Me What You Want" (English).  This suggests a data validation or comparison issue within a larger system, possibly during data import or update.  The "[12]" might refer to a line number or index within the data source.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/118](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/118)
---
I think the idea behind this font is to make it difficult for people to manually work on the markdown file from scratch. I guess they want us to use the tools (like PyMuPDF4LLM, markitdown) they provided as resources to convert pdf into a markdown and then may be we can do some manual intervention to make it to the result as the scraping tools are not 100% accurate.

Could be another reason too. TAs’ can feel free to pitch in.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/119](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/119)
---
A post was merged into an existing topic: Tds: assignment is not submitting

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/120](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/120)
---
your last saved score (i.e.6 of your’s) will be official score and forgot about seek portal , it is not meant for this type of assignment.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/121](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/121)
---
Thank you for the update! I gave Q10 another shot, and I was able to solve it this time. The more liberal checks and improved error messages made a big difference in understanding where I was going wrong.  
Thank again.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/122](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/122)
---
Can we use hacking to get answers to some questions? Has anyone ever done it?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/123](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/123)
---
What format is required for the “missing links” here  

image1973×849 93.6 KB

Here is my markdown

```
- statua demulceo amaritudo tametsi

- tam ante

- dens spiritus

- thema succurro sollers audio

Conforto conor tum deputo caecus cervus coepi aegrotatio totam xiphias. Repudiandae ducimus acerbitas ademptio . Delectatio tamquam suus.

Centum usitas tamen cedo auctus turpis video clibanus. Correptius beatus crepusculum decens succedo alias aperte decumbo trado. Talio universe deduco caute sui u

vester undique

- subito umbra

- caritas saepe

- taceo concido bos

Tenetur exercitationem numquam ultio tyrannus aeger vindico. Subvenio ambulo vacuus. Quidem quam tactus tracto aureus cupiditas.

thema astrum

# Spero uter

Harum cometes damnatio theologus virgo aperiam velut cursim.

**venustaspeccatus adsum**

acidus quisquam torrens

clam adeptio virga

Depulso claro consectetur concedo aveho bis pectus traho nobis. Cura adicio colligo corporis eligendi soluta ducimus carus. Allatus sapiente summa atqui deludo cur


```

Terebro vallum rem velociter currus suppellex.  
Viduo damno ustilo valetudo.  
Tribuo una vorago sui testimonium angelus suscipio eius demulceo civis.

```

Delectus coniecto repellendus amoveo amissio incidunt


```

Audax teneo centum cilicium vigor venio.  
Patria credo tonsor.  
Defessus pax volup vomito creator video campana cedo vita votum.  
Laudantium victoria aer via tepidus.  
Adulescens corporis triumphus coruscus sordeo trans dolorum.

```

- doloremque cum allatus aduro

- inventore thalassinus

- aperiam tergiversatio

- contigo alienus aranea cito cogo

Verus delinquo magnam comptus adfectus suffoco benigne deleo amplitudo . Cura deleniti theologus vestigium aranea denique vester doloribus . Venio cimentarius cr

depereo subvenio

---

```
Here's a description of the image:

The image shows a code editor or a similar programming environment displaying text.  The main part of the screen shows a question and its context within a larger exercise. The question asks for the Markdown content of a PDF, formatted using a specific tool ("prettier@3.4.2").


Here's a breakdown of the visible content:

* **Top Section:**  A title "Impact" is prominently displayed, followed by a description explaining the purpose of the exercise: to contribute to EduDocs Inc.'s mission of providing high-quality, accessible educational resources by automating PDF to Markdown conversion and ensuring consistent formatting.  Four bullet points list the benefits of this automation.

* **Question Section:**  A clear question is presented: "What is the markdown content of the PDF, formatted with prettier@3.4.2?".  Below this, a code block (presumably containing the PDF's content) is shown, containing Latin phrases:  "Audax teneo centum cilicium vigor venio.", "Patria credo tonsor.", "Defessus pax volup vomito creator video campana cedo vita votum.", "Laudantium victoria aer via tepidus.", "Adulescens corporis triumphus coruscus sordeo trans dolorum."

* **Error Message:** An error message "Error: Missing links" appears below the code block.

* **Bottom Section:** An explanatory note clarifies that perfect Markdown conversion from PDFs is difficult and often requires manual corrections. The question simplifies the task by focusing only on a few basic aspects.


**Key features for answering a potential question about the image:**

* The Latin text within the code block is the crucial part of the question.
* The error message "Error: Missing links" indicates there might be additional context or data missing from the original PDF that the automatic conversion couldn't handle.
* The explanation at the bottom emphasizes that a completely accurate answer is not expected due to the inherent difficulties of PDF-to-Markdown conversion.

In short, the image presents a programming or coding challenge involving PDF to Markdown conversion, highlighting the complexities and limitations of such processes. The user is asked to interpret a partial output and understand why the outcome may not be perfect.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/124](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/124)
---
In the pdf you see some blue color font for specific words write that word in format

```
[word](#)


```

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/125](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/125)
---
1. There are only four texts which look like link texts in the pdf.  
   All four properly coded in link markdown syntax, in the preview, they appear as link texts same as in pdf.

Link text

Even after chaning all the 4 texts which appered in blue color in the pdf to link texts,  
below error is still observed.

Error: Missing links

Did anyone else face same issue ?

2. Also, no text in the pdf looks like a code block.  
   But, Missing Code error was seen and after changing one of the paragraph by using markdown code syntax that error is gone.

Appreciate any suggestions on the link error.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/126](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/126)
---
Replace actual text to expected text until you got correct

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/127](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/127)
---
same kind of error is arising with me too.Any suggestion what is wrong with it??

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/128](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/128)
---
the rating should be treated as string.  
Format is as “2.9” instead of number 2.9

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/129](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/129)
---
Yes it can be done. Got the 10th one correct by implementing breakpoint by printing the expected answer which is being used to validate the user answer in the js script.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/130](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/130)
---
i am facing a similar issue

image1746×766 56.3 KB
The image shows a coding exercise or challenge.  The top section displays an example of a JSON object representing a weather forecast. The keys are dates formatted as YYYY-MM-DD, and the values are string descriptions of the weather.  The example shows three days.


The main part of the image focuses on a text input area where the user is asked to provide a JSON weather forecast description for Shanghai. The user has entered a JSON object similar to the example, but it contains 5 days instead of 3.


Below the input area, an error message is displayed: "Error. At root: Different number of properties". This indicates that the provided JSON object has a different number of key-value pairs than what's expected or what the system is looking for.  The number of keys (days) is the issue. A "Check" button is visible, presumably to submit the answer for evaluation.  There's a small red circled "i" next to the error message and the text entry area, hinting at additional information or a pop-up explanation if clicked.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/131](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/131)
---
image1678×892 43.3 KB

  
succesfully completed GA4 with 10/10 Marks
Here's a description of the image:

The image shows a screenshot of a web page, likely an online assignment platform. 


Here's a breakdown of the visible elements:

* **Top Navigation Bar:** A dark green bar at the top displays various links and titles, including "YouTube," "Academic Calendar," "Quiz Master," an app development project, a course title ("BS-DS, Jan 2025"), and "Tools in Data Science." The URL indicates a specific assignment ("exam.sanand.workers.dev/tds-2025-01-ga4").

* **Assignment Details:**  Below the navigation bar, it shows the assignment's due date ("Due Sun, 9 Feb, 2025, 11:59 pm IST"), the student's current score ("Score: 10/10"), and buttons to "Check all" and "Save."

* **Discourse Forum Promotion:** A dark blue box encourages participation in a Discourse forum for bonus marks. It indicates that replying to a specific discussion thread ("GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]") with a relevant question or answer will earn the student an extra point.

* **Login Status:**  The page displays the user's login information, showing their email address ("23f2005275@ds.study.iitm.ac.in") and a "Logout" button.

* **Recent Saves:** A section titled "Recent saves" lists the user's previous submission attempts, showing timestamps, scores (10, 5, and 3), and a "Reload" button for each save.

Overall, the interface suggests a structured learning environment where students complete assignments and can engage in discussion forums for extra credit. The dark color scheme and clean layout contribute to a professional appearance.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/132](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/132)
---
sir how will we know if we have been awarded with the bonus mark. Will it be reflected in our ga score and the marks would be 11/10 or will it be added later

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/133](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/133)
---
In Q2. getting , able to fix most of the errors but  

image1920×1080 159 KB

Error: At [18].title: Values don’t match. Expected: “19. Graymail”. Actual: “19. The Recruit”

this kind of errors for some titles, even though i only applied Rating filter and nothing else, then why i’m getting different titles then the test cases?
Here's a description of the image:

The image shows a screenshot of a macOS computer screen displaying multiple browser windows and applications. 


**Browser Window (Left):** This is the main focus, showing a webpage seemingly from IMDb. The page displays a list of movies with their titles, year, runtime, rating, and a short synopsis. The tabs at the top indicate browsing activity related to IMDb, possibly searching for movies based on ratings.  The tabs also show other websites that might be related to work or personal projects.


**Browser Window (Right):** This window shows a browser developer console, a tool used for web development. The console displays a large amount of JSON-formatted data, likely representing movie data from the left-hand IMDb page.  This suggests the user might be scraping or analyzing this data.


**Dock (Bottom):** The macOS dock is visible at the bottom, showing various applications including Messages, Xcode, Google Chrome, and others. 


**Overall:** The screenshot suggests a user working on a project involving movie data, possibly scraping or analyzing data from IMDb using browser developer tools. The multiple browser tabs and the presence of professional development software (Xcode) in the dock hint at a developer's or data analyst's workflow. The timestamp in the upper right corner of the screen indicates the date and time the screenshot was taken.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/134](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/134)
---
Hello Sir, thank you for changing the question.

@carlton I’m getting the below error:

```
Words like https, webbed, impact are missing (or not separated as words). 

```

However, in the source PDF file itself these words are not available.

image657×106 7.78 KB
Here's a description of the image:

The image shows a dark-themed code editor or text interface displaying a list of words, seemingly Latin, each enclosed within vertical bars.  Underneath each word, there's a wavy red underline, suggesting an error or warning.  The words are: *quos*, *utrum*, *tredecim*, *valetudo*, *cras*, *videlicet*, *laudantium*, *aetas*, *canis*, and *tantum*.

At the bottom, there's a red error message that reads: "Error: Words like https, webbed, impact are missing (or not separated as words)". This indicates that the system or program is expecting or searching for words like "https," "webbed," and "impact" but cannot find them because either they aren't present in the input or aren't properly separated.  The nature of the red underlines on the Latin words suggests a potential problem with the formatting or the way those words are handled by the system, possibly a mismatch with expected vocabulary or format.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/135](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/135)
---
Copy the row name that is use to change and paste it in your answers

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/136](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/136)
---
the ranking changes from time to time. you might need to scrape the data again.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/137](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/137)
---
i am facing issue in Q7.

I am using this command : “https://api.github.com/search/users?q=location:Seattle+followers:>120&sort=created&order=desc”

and the output on evaluating is : 2011-05-07T08:30:48Z

But i am getting the error :  

image1889×848 113 KB

Can someone please help me on this ?
Here's a description of the image content:

The image shows a dark-themed coding challenge or task within an application or website interface.  The core problem is to find the creation date of the newest GitHub user in Seattle with over 120 followers using the GitHub API.

**Key Text Elements:**

* **The Challenge:**  The top section clearly states the problem: find all users in Seattle with over 120 followers using the GitHub API and determine when the newest user's profile was created.
* **Steps:** A numbered list outlines the steps to solve the problem: API integration, data processing (filtering), and sorting and formatting the date in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ).
* **Impact:** A section describes the benefits of automating this process, emphasizing targeted recruitment, competitive intelligence, efficiency, and data-driven decision-making.
* **Input Field and Response:** There's an input field where a user enters the ISO 8601 formatted date.  The user has submitted `2011-05-07T08:30:48Z`, which is marked as "Incorrect".  A small red circle with an "i" inside it is shown next to the incorrect response field.
* **Hint/Instructions:** Below the incorrect answer is a hint that helps guide the user on how to effectively use the GitHub API filters (location and followers), sorting by the 'joined' field in descending order, and fetching only the first result.  It additionally specifies to ignore users who joined after a particular date and time.

**Overall:**

The image is a screenshot of a coding challenge that tests the user's ability to interact with the GitHub API, filter data, sort data, and handle dates. The incorrect answer and the hints strongly suggest an iterative problem-solving process.  The dark background and clean layout are typical of many coding platforms or online judges.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/138](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/138)
---
I am also facing the same issue. What is the problem here?  

image1788×908 77.9 KB
The image shows a coding exercise or quiz with a score of 9/10. 


Here's a breakdown of the content:

**Instructions:** The instructions describe a three-part process:

1. **API Integration and Data Retrieval:** Fetch weather forecast data for London using the BBC Weather API.  This involves sending a GET request to obtain a location ID and using that ID in a subsequent request.

2. **Weather Data Extraction:** Retrieve the weather forecast data using the obtained `locationId`.

3. **Data Transformation:** Extract the `issueDate` and `enhancedweatherDescription` from the API response. Create a JSON object where the `issueDate` is the key, and the `enhancedweatherDescription` is the value.

**Expected Output Example:** The instructions provide an example of the desired JSON output format:

```json
{
"2025-01-01": "Sunny with scattered clouds",
"2025-01-02": "Partly cloudy with a chance of rain",
"2025-01-03": "Overcast skies",
// ... additional days
}
```

**The Question:** The question asks for the JSON weather forecast description for London, based on the given data.

**User's Answer:** The user has provided a JSON object in the answer box:

```json
{
"2025-02-17": "Sunny and light winds",
"2025-02-18": "Sunny intervals and light winds",
"2025-02-19": "Sunny and light winds",
"2025-02-20": "Light cloud and light winds",
"2025-02-21": "Light rain and a gentle breeze"
}
```

**Error Message:** An error message indicates a "Property name mismatch." This suggests an issue with the formatting or keys in the user's JSON response.  The system likely expects a different format for the date keys.


**Top Bar:** The top bar shows:

* **Due Date and Time:** Due Sun, 9 Feb, 2025, 11:59 pm IST
* **Score:** 9/10
* **Buttons:** "Check all" and "Save" buttons.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/139](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/139)
---
@21F1005510 Actually, some IMDb titles have multiple names. For example, The Recruit is also known as Graymail in India. My server checks from a different region from yours. Hence the need for manual corrections for a few titles.

**Why didn’t I pick an exercise that could be fully automated?** Because this is how real-life data sourcing is. It’s never perfect. You often need to create workflows where you’re able to quickly correct such errors in automation.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/140](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/140)
---
To evaluate the bonus mark for replying to this Discourse topic, At around the time of the deadline, we’ll close this thread, load all posts here, and run this in the Console:

```
[...new Set($$('.names a[href^="/u/"]').map(d => d.textContent))]

```

… to get the Discourse IDs who posted. Then we’ll match it to the email IDs and pass it to the operations team who will add it to the portal by 2025-02-22T18:30:00Z.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/141](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/141)
---
I am getting the error in Q4 as “Error: At root: Property name mismatch”

what could me the cause of this error? Any please help.

@carlton

image716×402 23.3 KB
The image shows a coding exercise or quiz with a question about creating a JSON object representing a weather forecast. 


Here's a breakdown of the image's content:

* **Question:** The top line asks: "What is the JSON weather forecast description for Sao Paulo?"

* **Code Input Area:** A text box contains an attempt at creating a JSON object.  The dates are used as keys, and weather descriptions are the values. The code is:

```json
{
"2025-02-08": "Partly cloudy and light winds",
"2025-02-09": "Thundery showers and a gentle breeze",
"2025-02-10": "Sunny and a gentle breeze",
"2025-02-11": "Thundery showers and light winds",
"2025-02-12": "Sunny intervals and a gentle breeze",
}
```

* **Error Message:** Below the code input area, an error message is displayed: "Error: At root: Property name mismatch". This indicates a problem with the JSON structure, likely related to the keys (dates) not being properly formatted as strings within the JSON.  Valid JSON keys must be enclosed in double quotes.

* **Check Button:** A blue button labeled "Check" is at the bottom, presumably used to submit the answer and receive feedback.


In summary, the image presents a JSON coding challenge where the user needs to correctly format the provided weather data into a valid JSON object. The error message highlights that the provided JSON is not correctly formatted.  The error is that the keys are not correctly enclosed in double quotes.  The correct format is shown in the response.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/142](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/142)
---
This is the only thing which worked for me.

@carlton Sir, can I suggest to replace the snapshot of example output which expects the year to be an integer and the ratings as to be floats (instead of actual evaluation which expects them to be strings). Also, it would help to clarify that “Movie 1” should carry the numerical prefix as reported in IMDB. The current example on the portal is:  

image1580×196 4.81 KB
The image contains a code snippet, likely representing a JSON array.  The array appears to hold data for multiple movies. Each movie object within the array has four key-value pairs:

* `"id"`: A unique alphanumeric identifier for the movie (e.g., "tt1234567").
* `"title"`: The title of the movie (e.g., "Movie 1").
* `"year"`: The release year of the movie (e.g., 2021).
* `"rating"`: The movie's rating (e.g., 5.8).

The code shows two complete movie objects and then a comment `// ... more titles` indicating that more movie objects are present in the full, unseen array. The JSON structure is properly formatted with curly braces `{}` for each object and square brackets `[]` for the array.  The background is dark, enhancing the readability of the light-blue colored code.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/143](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/143)
---
Your dot of 2.9 may be the dot from alphabet or numeric one  
Try to copy the value and then replace it

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/144](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/144)
---
Try to copy the error data  
The problem might be off dot  
check one dot is on right of m and other right of 0 in keyboard  
these two dots may represent different meanings

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/145](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/145)
---
is it resolved?  
i too am getting the same error,even if it was working fine yesterday.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/146](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/146)
---
https will be part of the link (provided ‘link’ is one of the checkpoints of evaluation)

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/147](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/147)
---
Sir, In Graded Assignment - 4 >> Q2, the year I extracted appears as “2024,” whereas the expected value on the portal is “2024–”. I have manually adjusted several values based on the expected format. This issue is specific to the year field.

I use different classes to extract values for various fields. Could there be any other element on the portal affecting this extraction?

In Q4, one of my classmates is encountering a “root property” error despite using the same extraction method as I do. Upon checking, I found that this issue occurs because the city’s time is displayed as the previous day compared to our time. The portal results seem to be based on the city’s actual time rather than IST.  
I would appreciate your guidance on these issues.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/148](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/148)
---
Good idea @23f2005138 and thanks. I fixed this. The example now reads:

```
[
  { "id": "tt1234567", "title": "Movie 1", "year": "2021", "rating": "5.8" },
  { "id": "tt7654321", "title": "Movie 2", "year": "2019", "rating": "6.2" },

```

… with the year and ratings quoted.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/149](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/149)
---
lakshaygarg654:

> In Graded Assignment - 4 >> Q2, the year I extracted appears as “2024,” whereas the expected value on the portal is “2024–”. I have manually adjusted several values based on the expected format. This issue is specific to the year field.

I guess for the year part, there are certain series having multiple seasons, for which hyphenated “years” are given.

For the particular instance - `“2024–”`, it appears another season/part is announced, thats why it is written that way.
That's a close-up headshot of a man. 


Here's a description:

* **The Man:** He appears to be of South Asian descent, with dark hair, brown eyes, and a short, neatly trimmed beard and mustache. His expression is neutral or slightly serious. He's wearing a dark-colored suit jacket over a light-colored collared shirt.

* **The Image Quality:** The photo is a fairly standard passport-style or professional headshot. The resolution isn't exceptionally high, and the background is plain and unfocused, drawing attention to the subject. There's a slight shadow visible to his right (viewer's left) indicating the light source.  A barely visible logo or marking is in the very bottom right corner. It's too small and indistinct to identify.

* **Overall:** The image is a simple, professional portrait suitable for identification purposes or professional networking.  There is no other text or objects visible besides the man himself and the indistinct mark at the bottom.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/150](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/150)
---
Thanks @21f2000709 for this information. I figure out where i made mistake. During writing console code I added to remove non numeric values in year field which i guess removed that hyphen (“–”). I will rectify that.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/153](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/153)
---
GA 4 Q2

My JSON matches the titles of the movies as in the website, but in portal it is showing error and expecting something different from what is given in the website. How to handle this ?

image501×151 37.6 KB

  

image1226×258 13.2 KB

contradiction :  
" 2. Winnie-the-Pooh: Blood and Honey" (in web page) & ( delivered by the JSON)  
" 2. Winnie the Pooh: Blood and Honey" (expected in portal ) & ( raising error statement )

Regards  
GOVADHANAN N
Here's a description of the image:

The image shows a section of a website or app interface, likely a movie or show listing. 


Here's a breakdown of the visible elements:

* **Left Side:** A poster image for the movie "Winnie-the-Pooh: Blood and Honey" is displayed. The poster features a menacing-looking Winnie-the-Pooh character. A small "+" symbol is visible in the top-left corner of the poster, suggesting an option to add the movie to a list or queue.

* **Right Side:** This section contains information about the movie:

    * **Title:**  "2. Winnie-the-Pooh: Blood and Honey" is prominently displayed, with "Winnie-the-Pooh" underlined in blue. The "2." suggests this is the second item in a list. The entire title is inside a red rectangle.
    * **Year/Runtime/Rating:** "2023 1h 24m Not Rated" indicates the movie's release year, runtime (1 hour and 24 minutes), and that it's not yet rated by any official rating board.
    * **User Rating:** "★ 2.9 (33K)" shows an average user rating of 2.9 out of 5 stars, with 33,000 ratings.
    * **Rating Options:** A star icon with the word "Rate" next to it indicates a user can provide their own rating.
    * **Metascore:** "16" is displayed within a red box, indicating a Metascore of 16 out of 100. 


In summary, the image provides a snapshot of a movie listing showing details such as the title, poster, year of release, run time, user rating, and Metascore. The prominence of the red box around the title suggests it's the primary focus of this section of the interface.
 Here's a description of the image:

The image shows a code snippet and an error message related to JSON data.

**Code Snippet:**

The JSON data represents a single object with three key-value pairs:

* `"title"`: `"25. Battlefield Earth"`
* `"year"`: `"2000"`
* `"rating"`: `"2.5"`

The JSON is structured incorrectly; there's an extra closing square bracket `]` at the end, making it invalid JSON.


**Error Message:**

The error message states:

`Error: At [1].title: Values don't match. Expected: "2. Winnie the Pooh: Blood and Honey". Actual: "2. Winnie-the-Pooh: Blood and Honey"`

This indicates a test failure.  The test expected the `title` field to have the value `"2. Winnie the Pooh: Blood and Honey"`, but the actual value was `"2. Winnie-the-Pooh: Blood and Honey"`.  The only difference is the presence of a hyphen between "Winnie" and "the" in the actual result.  This suggests a potential issue with string comparison or data formatting within the testing system.

**Highlighting:**

The error message's "Expected" and "Actual" values are highlighted in red and green boxes respectively, drawing attention to the discrepancy. The difference in the "Actual" title is highlighted in blue within the green box.

In summary, the image presents a JSON data validation or testing scenario where a minor string difference leads to a failed test, likely due to a discrepancy in the expected and actual string formatting. The extra closing square bracket also signals a problem in the JSON structure itself.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/154](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/154)
---
so just exchange it.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/155](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/155)
---
Thanks for your response.  
Many such titles have contradiction from what is expected and what is there in the website. This case the samples are 25 your approach is accepted to some extent, but on a larger sample space, need to work it right !

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/156](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/156)
---
thanks for this, was wondering why it wasn’t working!

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/157](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/157)
---
question4692×539 36.3 KB

sir, we are getting this error. My Actual output is after get request on the given api i get only one day forcast data. I have show in above image
Here's a description of the image:

The image shows a coding problem related to JSON (JavaScript Object Notation) data.

**Top Section:**  The top section displays a sample JSON object representing a weather forecast.  It's structured as a series of key-value pairs, where the keys are dates (e.g., "2025-01-01") and the values are corresponding weather descriptions (e.g., "Sunny with scattered clouds"). The `// ... additional days` indicates that more data would follow in a real-world scenario.  The JSON is properly formatted with curly braces `{}` to enclose the object, and commas `,` separating the key-value pairs.

**Middle Section:** The middle section poses a question: "What is the JSON weather forecast description for Kuala Lumpur?". It then provides a text box where the user is expected to input the answer.  The user has entered a single key-value pair: `{"2025-02-01": "Thundery showers and light winds"}`.

**Bottom Section:** The bottom section displays an error message: "Error: At root: Different number of properties".  This indicates that the JSON input provided by the user is not compatible with the expected JSON structure shown in the top section (which suggests more than one key-value pair is needed).

**In summary:** The image presents a programming exercise involving JSON data. The task is to provide a JSON snippet representing a weather forecast for Kuala Lumpur, conforming to a specific structure. The provided solution is incorrect because it does not match the expected format; it lacks the multiple entries required by the existing structure.  The error message explicitly points out the issue of a different number of properties.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/158](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/158)
---
yes replace manually until you got correct ans . Error will suggest you what to change.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/159](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/159)
---
{  
“2025-02-08”: “Light snow and light winds”,  
“2025-02-09”: “Light snow and light winds”,  
“2025-02-10”: “Light cloud and light winds”,  
“2025-02-11”: “Sunny intervals and a gentle breeze”,  
“2025-02-12”: “Sunny and light winds”,  
“2025-02-13”: “Sunny and light winds”,  
“2025-02-14”: “Light snow and a gentle breeze”,  
“2025-02-15”: “Light snow and a gentle breeze”,  
“2025-02-16”: “Sleet and a gentle breeze”,  
“2025-02-17”: “Light rain and a gentle breeze”,  
“2025-02-18”: “Light rain showers and a gentle breeze”,  
“2025-02-19”: “Drizzle and a gentle breeze”,  
“2025-02-20”: “Light rain and light winds”,  
“2025-02-21”: “Light rain and light winds”  
}  
i got this after running my python script for question 4 but, got  
Error: At root: Property name mismatch" this error message

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/160](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/160)
---
@s.anand sir,  
I don’t understand this error. In the website, the movie name doesn’t have a colon “:”, but in the result it is expecting so.

image1005×250 15.4 KB
Here's a description of the image:

The image shows a snippet of JSON data within curly braces `{}`, containing key-value pairs representing movie data. The keys are enclosed in double quotes, as are the values.  The data includes an ID ("tt8790086"), a title ("11. Kraven the Hunter"), the year (2024), and a rating (5.4).  Following the JSON, there's an error message.


The error message indicates a mismatch in the "title" field at index [10].  The expected value is "11. Kraven: The Hunter", but the actual value is "11. Kraven the Hunter".  The difference lies in the colon separating "Kraven" and "The Hunter" - the expected value uses a colon, and the actual value uses a space.  This suggests a test case failure where the data is compared against an expected value, highlighting a discrepancy in the formatting of the movie title.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/161](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/161)
---
For this question, you may use the Google Colab file referenced in the assignment. This file will provide you with the date and description. Additionally, you can generate a weather location ID for the city specified in your assignment. Using this ID, you will obtain the weather URL, which you can then use to verify the date and description.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/162](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/162)
---
here is the difference of ‘:’ in the expected ans. so make it manually correct . i did the same and got correct ans .  
and in the question also it is mentioned that may be manually you need to correct. just give a try.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/163](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/163)
---
run your console script again and match the description.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/164](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/164)
---
yes, same happened with me . correct it manually.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/165](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/165)
---
In q10 links are not accessible through pdf and also creating problems while converting to markdown

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/166](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/166)
---
image1358×1151 179 KB

Why question 4 starts failing. It was working correct yesterday. Because of it I am getting 9/10 marks.
This image shows a coding challenge or exercise, likely from an online learning platform or a coding bootcamp.  The challenge involves using the BBC Weather API to retrieve and process weather forecast data for Manila.

Here's a breakdown of the content:

**1. Introduction:** The top section provides context about AgroTech Insights, a company using weather data for agricultural planning.  It explains the need to automate the weather data retrieval and processing, highlighting the use of the BBC Weather API.

**2. Task Description:**  The "Your Task" section outlines three steps:

* **API Integration and Data Retrieval:**  This involves sending a GET request to the BBC Weather API's locator service to get a location ID for Manila, then using that ID to fetch the weather forecast data via another API endpoint.  This requires using API keys and parameters.

* **Weather Data Extraction:** Retrieving the relevant data (forecast data) from the API response.

* **Data Transformation:**  Processing the extracted data to create a JSON object.  The key of each JSON entry is the `issueDate`, and the value is the `enhancedweatherDescription`.  An example of the desired JSON output format is shown.

**3. Example Output:** A sample JSON object is provided to illustrate the expected format of the final output.  It shows date keys and corresponding weather descriptions.

**4. Question:** The final section asks for the JSON weather forecast description for Manila, given a specific date range (February 16th-20th, 2025). A sample JSON object is provided to indicate how to fill the answer.

**5. "Check" Button:** A "Check" button is present, presumably to submit the solution and check if it's correct.


In essence, the image presents a practical coding problem that requires working with APIs, JSON data, and potentially libraries for making HTTP requests (like `requests` in Python).  The challenge is designed to test the understanding of these concepts and their application in a real-world scenario.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/167](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/167)
---
The result is dynamic with changes made in the API. So try re-executing your code today and it will automatically solve. Your code is right ! Just make a re-run and things will work out
That's a digital image of a simple, smiling yellow emoji. 


Here's a breakdown of its features:

* **Shape and Color:** It's a perfectly round, bright yellow circle.  The yellow is a fairly saturated, warm tone.

* **Facial Features:** The emoji has two small, dark brown, circular pupils that are slightly spaced apart. Below the eyes is a small, gently curved, simple smile line. There are no other details, such as eyebrows, nose, or mouth.

* **Style:** The style is minimalist and cartoonish.  The edges are slightly softened, giving it a smooth, rather than pixelated appearance, although the image is clearly digitized.

The emoji conveys a feeling of simple happiness or contentment.  There is nothing else in the image besides the emoji.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/168](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/168)
---
try running the console again and it will work, make sure the data matches with the one in api as it changes regularly

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/169](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/169)
---
Thanks!.  
It is working now. I had to manually correct 5 movie titles to get it correct.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/170](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/170)
---
Screenshot 2025-02-08 at 7.41.55 PM2576×420 32.3 KB

  
What 's the solution?
Here's a description of the image:

The image shows a dark-themed code editor or IDE displaying a JSON data snippet and an error message. 


**JSON Data:**

The JSON data is partially visible and appears to represent information about a movie or show, possibly including an ID ("tt10078772"), title ("9. Flight Risk"), and year ("2025"). The last line is cut off.


**Error Message:**

Below the JSON data, an error message is displayed:  "Error: At [10] year: Values don't match. Expected: "2025-". Actual: "2025-"" This suggests that the JSON validator or parser expected the year field to contain "2025-" but received "2025" instead. The difference appears to be a missing hyphen.


**Overall:**

The image clearly indicates a problem in the JSON data's `year` field, specifically the omission of a hyphen that the system expects. The dark background and highlighting style are typical of many code editors. The small circle with a line in the top right corner of the JSON data box is likely a closing button or a way to minimize/close that part of the code editor.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/171](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/171)
---
Titles (from the output json) should be replaced by the titles which shows in the error message “Expected”. It can only be done manually. There may be multiple titles need to be translated by this method.

Please refer the instruction.  

10000952401080×183 43.8 KB
Here's a description of the image:

The image shows a small portion of a computer screen displaying a warning message and a button. 


Here's a breakdown of the content:

* **Warning Message:** The main part of the image contains a message explaining potential issues with IMDb search results. The message reads:  "IMDb search results may differ by region. You may need to manually translate titles. Results may also change periodically. You may need to re-run your scraper code." This suggests that the user is likely using a program to automatically gather data from IMDb, and the data's accuracy and consistency may require manual intervention or code updates.

* **Button:** Below the warning message, a partially visible blue button is shown, with only the word "Check" visible.  This button likely prompts the user to acknowledge the warning or perhaps initiates a process to address the mentioned issues.


The overall context strongly implies that this is a warning related to web scraping IMDb data.  The message highlights potential regional differences, language barriers, and the need for regular code updates to maintain data accuracy.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/172](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/172)
---
you can manually add space after the hyphen

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/173](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/173)
---
I face the same error, also thinking of issueDate, the value seems to be constant in every loop inside forecasts array (is it because the data is issed on that particular date) that gives same issue date key across the json outcome. Anyways the new json with same issueDate also gives the same Root error

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/174](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/174)
---
Double-check that the rating field in the JSON is indeed a float (`2.9`) and not a string (`"2.9"`) in your code.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/175](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/175)
---
That is perhaps to ensure we don’t manually write the markdown for the pdf. Converting the pdf to markdown and getting the correct output is extremely hard, I tried doing that multiple times yet wasn’t able to get that right by the original method.

But since it is mentioned that the GAA is hackable and we are allowed to do so, for some of the questions, therefore you can try solving that by establishing a breakpoint in the sources and then write the code in the console to get the expected output.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/176](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/176)
---
Write the code referencing the provided collab file and make sure to use the API key  
The output actually changes once in a while so you might need to run the code a few times before getting in right  
https://tds.s-anand.net/#/bbc-weather-api-with-python

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/177](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/177)
---
your most recently saved score will be evaluated

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/178](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/178)
---
I am getting this error again and again after running the code in collab this city `Nur-Sultan`?  

image936×343 26 KB
The image shows a Python code error message. The main error is a `NameError: name 'location_id' is not defined`. This error occurs because the variable `location_id` is used in line 35 without being previously defined or assigned a value.  Line 35 attempts to create a URL string using an f-string, and includes `{location id}` as part of the string. The code was trying to construct a URL for the BBC weather website, using a location ID which is missing.


The traceback shows that the error originates within an IPython environment (`<ipython-input-9-128760ee996a>`). The error message at the top indicates that the program could not find a location ID for Nur-Sultan, which might be relevant context for the missing `location_id` variable.  To resolve this, a value must be assigned to `location_id` before line 35 is executed, likely by fetching it from a database, API, or other source providing location IDs.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/179](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/179)
---
In the second question are we supposed to edit the JSON manually until we reach a correct answer ? I think the expected result has some difference from what shows up in the website

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/180](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/180)
---
Not able to get the missing links in Q10  
Any suggestions welcome please

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/181](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/181)
---
For question 10 I’ve tried everything. Links and headings work fine, but I’m not able to fix the “missing tables” issue (I’ve also tried using pdfplumber and tabulate). In the pdf as well, I don’t see any tables, any hints or suggestions would be very helpful. Thanks!

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/182](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/182)
---
there is no location id mentioned as it is mentioned of the different city. please check the city for which you need to find the location id and then proceed

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/184](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/184)
---
I’m getting the same error in Q4:

image1631×641 34.2 KB
This image shows a coding exercise or problem, likely from an online learning platform or coding challenge website.  Here's a breakdown of the image's content:

**Top Section:**

* **Instruction:**  The top section provides an example of the desired JSON output format for a weather forecast.  It shows a JSON object with date strings as keys and weather descriptions as values.

**Middle Section:**

* **Question:** The middle section poses the question: "What is the JSON weather forecast description for Los Angeles?". This implies the task is to provide a JSON object representing the weather forecast for Los Angeles.

* **User's Attempt:**  Below the question is a text box containing the user's attempted JSON response.  The user has provided a JSON structure, but with incorrect date formatting (`23-02-10` instead of `2025-02-10` for example) and possibly incorrect key structure that is causing an error.  All the weather descriptions are "Sunny and light winds".

* **Error Message:** A red error message below the response box states: "Error: At root: Property name mismatch".  This indicates that the JSON keys (dates) are not correctly formatted or are not what the system expects.

**Bottom Section:**

* **"Check" Button:** A button labeled "Check" is present, presumably to submit the user's response for evaluation by the system.

**Key Issues in the User's Attempt:**

1. **Incorrect Date Formatting:** The dates in the user's attempt use `DD-MM-YY` format, whereas the example uses `YYYY-MM-DD`. JSON keys, particularly dates, should conform to standard formats for consistency and easy parsing.
2. **Potential Key Structure Problem:**  The error message ("Property name mismatch") suggests a problem beyond date format.  The system might have specific naming requirements for keys, which this attempt may not be meeting.


In summary, the user needs to correct the date format in their JSON response and ensure that the keys (dates) and possibly the overall structure adhere to the specifications implied by the example and error message.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/185](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/185)
---
How to actually do the HNRSS one…i can’t find much.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/186](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/186)
---
How did u do the links? I’m unable to do links

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/187](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/187)
---
Just copy paste the expected value in place of actual value in json. Keep doing this eventually it would be the answer would be correct.

This is a format issue when the json is scrapped from the browser.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/188](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/188)
---
Request help on Q4 aboutBBC weather data, the instructions in the question tell us to use BBC broker API and get issueDate & enhancedWeatherdescription value pairs. However, it seems there are only 2 unique values of issueDate (not the expected 14 days)

Please clarify, sharing code and output below for reference.

Code:

```
import requests

url = "https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/" + getlocid('Bogota')
response = requests.get(url)
json_data=response.json()
print(f"The number of days data is {len(json_data['forecasts'])}")

weather_data = {}

for i in range(len(json_data['forecasts'])): # Use range to create an iterable sequence of indices
  issue_date = json_data['forecasts'][i]['summary']['issueDate']
  weather_description = json_data['forecasts'][i]['summary']['report']['enhancedWeatherDescription']
  weather_data[issue_date]=weather_description
  print("Iteration No. " + str(i))
  print(issue_date)
  print(weather_description)
  
print("Final Weather Data json below")
print(weather_data)

```

Output

```
The number of days data is 14
Iteration No. 0
2025-02-08T04:00:00-05:00
Light rain showers and a gentle breeze
Iteration No. 1
2025-02-08T04:00:00-05:00
Thundery showers and a gentle breeze
Iteration No. 2
2025-02-08T04:00:00-05:00
Thundery showers and a gentle breeze
Iteration No. 3
2025-02-08T04:00:00-05:00
Thundery showers and light winds
Iteration No. 4
2025-02-08T04:00:00-05:00
Light rain showers and light winds
Iteration No. 5
2025-02-08T04:00:00-05:00
Light rain showers and light winds
Iteration No. 6
2025-02-08T04:00:00-05:00
Light rain showers and light winds
Iteration No. 7
2025-02-08T04:00:00-05:00
Thundery showers and a gentle breeze
Iteration No. 8
2025-02-08T16:01:58-05:00
Thundery showers and a gentle breeze
Iteration No. 9
2025-02-08T16:01:58-05:00
Thundery showers and light winds
Iteration No. 10
2025-02-08T16:01:58-05:00
Thundery showers and a gentle breeze
Iteration No. 11
2025-02-08T16:01:58-05:00
Thundery showers and light winds
Iteration No. 12
2025-02-08T16:01:58-05:00
Thundery showers and light winds
Iteration No. 13
2025-02-08T16:01:58-05:00
Thundery showers and a gentle breeze
Final Weather Data json below
{'2025-02-08T04:00:00-05:00': 'Thundery showers and a gentle breeze', '2025-02-08T16:01:58-05:00': 'Thundery showers and a gentle breeze'}

```

Edit: For now, I have worked around with code posted by @21f3002277. But the doubt about the question remains

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/189](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/189)
---
same with me. In the project it is written that the form should be submitted but there’s no question in the portal.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/190](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/190)
---
I have got the same error as well, verified there are workflows run in my repo/actions/runs  
When I checked the reasons, it could be due to API limit exceeded in a hour, but tried even after some time but no workflows found.

image1345×424 23.7 KB
This image shows a screenshot of a GitHub Actions workflow runs page. 


Here's a breakdown of the content:

* **Header:** At the top, "All workflows" is displayed, followed by "Showing runs from all workflows". A search bar labeled "Filter workflow runs" is present in the upper right.

* **Survey:** A section titled "Help us improve GitHub Actions" invites users to provide feedback with three quick questions.  A "Give feedback" button is also present.

* **Workflow Runs Table:**  Below the survey, a table lists two workflow runs.  Each row shows:

    * **Workflow Name:** "Action runs everyday" (repeated twice).
    * **Run Details:**  A brief description of each run's status: one scheduled and one manually triggered.  Run number (#6 and #5) are shown for each run.
    * **Branch:**  The branch where the workflow ran ("main" in both cases).
    * **Run Time:** Shows "2 hours ago" for both runs.
    * **Run Duration:** The duration of the run is shown (15s and 14s respectively).
    * **Actor:**  The user who triggered the run (blank for scheduled, and Rajalakshmi12 for manual run).
    * **Status:** Both runs show a green checkmark indicating success.

* **Table Headers:** The table has headers for "Event", "Status", "Branch", and "Actor" indicating the type of event that triggered the workflow, its status, and other details.


In essence, the image displays a recent history of successful workflow runs for a particular repository on GitHub.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/191](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/191)
---
Manual correction will not work. Try to extract - from the console. I did it like that it was not working then I extracted from console then it worked

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/192](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/192)
---
Please ensure that your .yml file should have step name as your email Id. then Manually trigger the task (don’t wait till the scheduled time), ensure it was committed within 5 minutes and that commit should be top most item in all workflows. Then check it, it will work

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/193](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/193)
---
You can find some text blue in color and underline use some dumy url it will work

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/194](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/194)
---
You can find some lines having second, third words are uniformly aligned. Those are tables

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/195](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/195)
---
When I resave the questions, the previously correct questions turn wrong which is extremely frustrating and time taking. I wish there is an option which saves the correct answer and does not require us to have multiple processes running in our pc even after getting the answer right previously.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/196](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/196)
---
In Q 6 I checked all the startups link at Hacker News - Newest: "Startup"… none is greater than 81 then how to submit that link… is there something i am missing

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/197](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/197)
---
@Jivraj @carlton ,for question 3, even a random response is shown correct

image1765×472 29.1 KB

image766×237 12.2 KB
The image shows a section of a web page or application, likely part of a tutorial or test involving configuring Cross-Origin Resource Sharing (CORS).

Here's a breakdown of the content:

**Headline:** "5. Enabling CORS: Configure the web application to include appropriate CORS headers, allowing GET requests from any origin."  This sets the context – the task is to set up CORS correctly.

**Input Field:**  There's an input field with the text "http://127.0.0.1:8000" already entered.  A green checkmark next to it indicates this input is correct. This is a localhost address often used for testing web applications.

**Text Below Input:** "Correct" confirms the accuracy of the entered URL.

**Instructions:** "We'll check by sending a request to this URL with `?country=...` passing different countries."  This explains the next step: the system will test the CORS configuration by sending requests to the specified URL with different country parameters.

**Button:** A "Check" button is present, presumably to initiate the CORS test described in the instructions.

In summary, the image displays a step in a CORS configuration process where the user has correctly entered a local API endpoint URL, and is ready to proceed with a test.  The test will verify if the CORS headers are properly configured to allow requests from any origin.
 The image shows a screenshot of a web browser window, likely Jupyter Notebook or a similar environment, running on a local server (address `127.0.0.1:8000`).  Let's break down the visible elements:

* **Browser Address Bar:** Shows the local server address `127.0.0.1:8000/?country=india`. This indicates a web application running locally, possibly with a parameter specifying the country as "India".  Standard browser controls (back, forward, refresh, home) are also present.

* **Browser Tabs:**  Multiple tabs are visible at the top, including one labeled "Mathematics for Da...", another titled "BS-DS_Jan 2025 Gr...", and "Untitled1.ipynb - Co...". These suggest different notebooks or projects open within the browser.

* **Code/Output Area:** The main part of the window shows code and output.  The line "Pretty-print" appears to be a label or comment related to code execution, possibly indicating a function or method used for formatted output.  The number `44` is shown below, likely the result of a previous code execution.  The dark background suggests a dark theme is enabled in the environment.

* **Icons:** Various icons are present representing functions or file types.  There is a typical folder icon, a settings/info icon, and icons associated with the specific notebooks and projects.

In summary, the image depicts a user working with a data science or programming project (possibly involving Python given the ".ipynb" file extension) within a web-based development environment, likely running locally and configured to display information specific to India.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/198](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/198)
---
Sir I have solved Q2, But a problem arises that, At the index 11, in the IMdb website it is listed “The Recruit” but it is showing Expected: “Graymail”.  

problem621×159 42.4 KB

How to fix this?
Here's a description of the image:

The image shows a snippet of what appears to be JSON (JavaScript Object Notation) data, representing a list of movies or TV shows. Each object in the list contains the following keys:  "id" (a unique identifier), "title" (the show's title with a number prefix), "year" (release year, sometimes with a trailing hyphen suggesting an ongoing series), and "rating" (a numerical rating).  

Below the JSON data, there's an error message:

`Error: At [11].title: Values don't match. Expected: "12. Graymail". Actual: "12. The Recruit"`

This indicates a data validation or testing error. The program or script was expecting the title at index 11 to be "12. Graymail", but it found "12. The Recruit" instead.  This suggests a discrepancy in the data source. The error message pinpoints the precise location of the mismatch within the JSON structure.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/199](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/199)
---
you have to manually change for a few mismatch.

s.anand:

> @21F1005510 Actually, some IMDb titles have multiple names. For example, The Recruit is also known as Graymail in India. My server checks from a different region from yours. Hence the need for manual corrections for a few titles.
>
> **Why didn’t I pick an exercise that could be fully automated?** Because this is how real-life data sourcing is. It’s never perfect. You often need to create workflows where you’re able to quickly correct such errors in automation.
That's a close-up shot of a man's head and shoulders. 


Here's a breakdown of the image:

* **The Man:** He appears to be middle-aged, with light to medium brown skin. His hair is short and somewhat disheveled, appearing graying or light brown. He's wearing glasses, and only a portion of the frames are visible. His expression is somewhat serious or pensive, and his gaze is directed slightly away from the camera.  The lighting is dramatic, casting shadows on his face, making some features less defined. He's wearing a dark-colored garment, possibly a shirt or jacket, but details are obscured by the shadows and resolution.

* **The Background:** The background is a plain, muted brownish-red tone, relatively undifferentiated and unfocused, drawing attention solely to the man.

* **Image Quality:** The image quality is low-resolution and somewhat blurry, especially around the edges. The detail is not sharp, and some pixelation is noticeable. This makes precise identification of features challenging.


There is no text present in the image.  The focus is entirely on the portrait of the man.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/200](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/200)
---
Yes …due to the location difference the search results are different for everyone therefore you need to adjust it accordingly  
It might need around 6-7 amendments

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/201](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/201)
---
The API is returning 14 days of forecast data, as evidenced by the output However, the issueDate values are not unique for each day. Instead, they represent the time when the forecast was issued or updated.  
In your output, there are only two unique issueDate values:  
2025-02-08T04:00:00-05:00  
2025-02-08T16:01:58-05:00  
This means the forecast was updated twice on February 8, 2025, once at 04:00 AM and again at 4:01 PM (both in EST timezone) …To get a unique weather description for each day, you need to modify your approach by using the actual forecast day for each day instead.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/203](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/203)
---
While submitting solution, do I need to keep all the local servers running/local URLs like 127.0.0.0 stuff, else I am getting one question as correct & the other one mentions unable to fetch data!? So that means I need to run them in different different ports?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/204](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/204)
---
I posted this error message but now the first issue got resolved but I am still keeping it in my post so that if anyone faces same issue, they can try if they can fix it similar to how it worked for me.

Please help with the second issue.

1. For Q8, the workflow is running on Github and commiting the scraped results to the json file (which is so amazing for me btw!). But I am getting this error for my public repo.  
   How it got resolved: I set up fixed time for cron schedule instead of every 5 min. Now it works.

> Error: No daily scheduled triggers found in workflows.

2. I had all correct results for Q1 to Q7 till yesterday but it keeps giving errors even when I reload same file for some questions. Do I need to keep addressing those errors or if once correct and saved, I can ignore those?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/205](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/205)
---
image706×257 17.3 KB

  
I have tried several times but still recieving this as error. Please help
Here's a description of the image:

The image shows a code snippet and an error message.  The main part displays a JSON (JavaScript Object Notation) array containing three movie objects. Each object has an "id," "title," and "year" field. One object also includes a "rating" field.  The JSON data is incomplete, lacking closing brackets and commas where they are needed for proper JSON syntax.


The error message below the JSON data indicates a problem during data validation or comparison.  Specifically, it says:

* **Error:**  At `[0]`.id: Values don't match. Expected: `"tt20221436"`. Actual: `"tt0437179"`

This error message means that at the first element (`[0]`) of the JSON array, the value of the "id" field ("tt0437179") does not match the expected value ("tt20221436").  This suggests a data mismatch issue, possibly indicating an error in data input, retrieval, or comparison process.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/206](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/206)
---
Screenshot 2025-02-09 at 12.28.48 PM1304×943 182 KB

  
I’m able to see the markdown response for different countries for question 3, GA 4 on my browser but I’m unable to submit it probably because of network issues. Can someone help me with a fix. Thank you.
The image shows a browser's developer tools displaying errors related to a web application. The main section shows a set of instructions for developing a web application that fetches and processes data from Wikipedia.  The steps outline:

1. **API Development:** Creating an API endpoint using a framework like FastAPI.
2. **Fetching Wikipedia Content:** Retrieving HTML from a Wikipedia page based on a country parameter.
3. **Extracting Headings:** Parsing the HTML to extract headings (H1-H6).
4. **Generating Markdown Outline:** Converting the headings into a Markdown outline.
5. **Enabling CORS:** Configuring CORS headers to allow requests from any origin.

Below the instructions is a text input field where the user inputs the API endpoint URL: `http://localhost:8000/api/outline`.  A "Check" button is pressed, and the application generates an error:  `TypeError: Load failed`.

The developer tools' console reveals the core issue: repeated "Not allowed to request resource" and "Fetch API cannot load" errors, specifically targeting the API endpoint with a country parameter (e.g., `http://localhost:8000/api/outline?country=The+Bahamas`).  The errors are consistently attributed to "access control checks." This strongly suggests a CORS (Cross-Origin Resource Sharing) misconfiguration: the server is not sending the appropriate CORS headers to allow requests from the origin (the browser making the request) to the API endpoint.

In essence, the image displays a debugging session showing a common web development problem – the API is not correctly configured to handle cross-origin requests.  The error messages are the key indicators of the problem (CORS issues) and the debugging steps are implied.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/207](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/207)
---
image1701×699 64.6 KB

  
how to tackle this error as in 10 th movie year is 2025 but it is showing 2021
This image shows a screenshot of a web page or application interface, likely part of an online coding assignment or tutorial. 


Here's a breakdown of the visible content:

* **Heading:** The top section has a heading "4. Submit: Submit the JSON data in the text box below." This clearly indicates a task requiring the user to input JSON data.

* **Impact Section:** Below, a section titled "Impact" explains the purpose of the assignment. It describes how the task of providing JSON data simulates a real-world content acquisition strategy for a streaming service. The goal is to help the service make informed decisions about which titles to license, focusing on aligning with subscriber preferences.

* **JSON Data Input:** A text box labeled "What is the JSON data?" contains JSON code with the following key-value pairs:
    * `"id": "tt26584495",`
    * `"title": "10. Companion - Die perfekte Begleitung",`
    * `"year": "2025",`
    * `"rating": "7.4"`
This JSON seems to represent data for a movie or TV show, including its ID, title, year, and rating.  Note the error message below indicates that the year value is incorrect.

* **Error Message:** A red error message is shown below the JSON input: "Error: At [10] year. Values don't match. Expected: "2021-". Actual: "2021"".  This highlights an issue where the `year` field's value is different from what's expected.

* **Disclaimer:** At the very bottom, a disclaimer mentions that IMDb search results might vary by region, and users may need to manually translate titles or re-run their scraper code. This suggests that the JSON data might be obtained from scraping IMDb.


In summary, the image presents a coding task that involves submitting correctly formatted JSON data representing movie information.  The primary problem is that the provided year value is incorrect, leading to an error.  The user needs to correct the year value to match the expected format.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/208](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/208)
---
City in my question is `Nur-Sultan` .When i search `Nur-Sultan` city name in BBC weather page .its show nothing . when i search in google then show Nur Sultan become Astana . then i am going this city name "Astana ". and got location id 1526273. after i run in collab then showing error.  

WhatsApp Image 2025-02-09 at 12.42.40\_7957510c1280×720 109 KB
The image shows a screenshot of a Python code editor with a traceback error. 


Here's a breakdown of the visible elements:

* **Code:** The majority of the image displays Python code.  The code appears to be designed to fetch weather data, possibly from a BBC weather API. It involves:
    * Creating a date range.
    * Mapping dates to weather descriptions (from `daily_summary_list`, which isn't fully visible).
    * Converting the data to JSON format.
    * Attempting to fetch location data and construct a weather URL using data from the response. This is where the error occurs.

* **Error Message:** The code execution resulted in an `IndexError: list index out of range` error. The traceback indicates the error is on line 24, where the code tries to access an element within a nested list (`result['response']['results']['results'][0]['id']`).  This suggests that the list `result['response']['results']['results']` is either empty or doesn't have an element at index 0.

* **Traceback:** A traceback provides information about the execution path that led to the error. It shows the line number where the error occurred.

* **IDE/Editor:** The code is displayed within an Integrated Development Environment (IDE) or code editor.  The editor has features like line numbers, syntax highlighting, and a traceback display.  There is a "completed at" timestamp which indicates the time the error occurred.


* **System Tray:**  A portion of the system tray is visible in the bottom right corner which displays various system icons.


* **Browser Tab:** The browser bar shows a search engine's search bar and shows "Finance headline" and "India Foreign Ex" likely from news headlines.


In summary, the image shows a Python programmer encountering an `IndexError` while working on a script that processes weather data. The error likely stems from trying to access a non-existent index within a nested list returned from an API request, indicating a problem with either the API response or the way the response is being parsed.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/209](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/209)
---
this error comes, whenever you answer the other ones and click save. Please answer this question lastly, and submit immediately. it changes within a second. If it continues means, do manual correction and change according to the “expected”

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/210](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/210)
---
while searching dont put any other filter other than asked in Problem statement.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/211](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/211)
---
image1618×513 46.3 KB

  
Can anyone help me with the 10th question. Whatever I changed with the code , it is asking something. I checked that these words are not present in the pdf itself
Here's a description of the image content:

The image shows a code block containing markdown text, purportedly extracted from a PDF and then formatted using `prettier@3.4.2`.  The markdown includes:

* **A heading:** `# Pauci Audentia Sperno Eum`
* **A sentence:** `Tracto adeptio somnus. Neque tantum desidero porro est civitas caute laboriosam valetudo.` (This line has red squiggly underlines under several words, suggesting potential OCR errors or formatting issues.)
* **A subheading:** `## Key Points`
* **Two bullet points:** `- Vomito antiquus consequuntur` and `- Amplus curis subnecto` (Again, some words have red underlines indicating potential errors.)

Below the code block is an error message: `Error: Words like back, legislature, info are missing (or not separated as words)`.  This indicates that the extraction process missed or incorrectly parsed certain words. Finally, there's an explanatory note stating the difficulty of accurately converting PDFs to Markdown and that this particular question focuses only on basic aspects.

The overall appearance suggests a problem with OCR (Optical Character Recognition) during the PDF to text conversion.  The red underlines highlight the areas where the text likely needs manual correction.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/212](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/212)
---
I didn’t get any error for Astana.  
The error may be due to incorrect loops in your code that’s why it’s going out of range, check for that.

image1860×703 133 KB
Here's a description of the image:

The image shows a screenshot of a Jupyter Notebook (`.ipynb`) file, likely used for data science or programming.  The notebook is open in a dark-themed code editor (possibly VS Code or a similar IDE).

**Top Section:**

* **File Menu:** A standard file menu bar is visible, with options like "File," "Edit," "View," "Insert," "Runtime," "Tools," and "Help."
* **Notebook Title:** The notebook's title is displayed as `bbc-weather-scraping.ipynb`.
* **"Cannot save changes" Warning:** A notification indicates that changes cannot be saved, suggesting a potential issue with the file's location or permissions.
* **Code and Data Preview:** The main part of the notebook displays two sections:
    * **A table (lines 7-13):** This table contains weather data, with columns for Date, High temperature, Low temperature, and a summary of weather conditions. The dates appear to be in February 2025.
    * **Code (below the table):**  A line of Python code is visible: `df.to_json(orient='records')`. This suggests that a Pandas DataFrame (`df`) containing the weather data is being converted to a JSON (JavaScript Object Notation) format, with records oriented as the outermost JSON elements.
    * **JSON Output:**  Below the code is a large JSON output, displaying the data in a nested JSON structure that is too lengthy to fully show in the screenshot.  The output appears to represent the same weather data shown in the table above.

**Bottom Section:**

* **"Next Steps" Menu:** A menu with options to "Generate code with df," "View recommended plots," and "New interactive sheet" is at the bottom of the screen.
* **Runtime/Memory indicators:**  In the top-right corner there are indicators for RAM and Disk usage. A "Share" button is also present, indicating collaboration features.

Overall, the image shows a typical workflow in data analysis, where data is scraped (as suggested by the file name), processed (into a Pandas DataFrame), and then exported (to JSON).  The error "Cannot save changes" suggests a potential problem with the environment or setup used for the notebook.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/213](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/213)
---
It worked for me; only 4–5 values caused errors, which I fixed manually. Additionally, I corrected the console code, which now provides the correct result.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/214](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/214)
---
what is this magic trick… please elaborate …

```
Error: At [10].id: Values don't match. Expected: "tt16027074". Actual: "tt8008948"

```

i dont see that value in data …

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/215](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/215)
---
You can manually edit that. I also have to manually edit one entry to get the correct answer.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/216](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/216)
---
Hi,  
As mentioned in the question, you have to sort by “joined” so it should be “https://api.github.com/search/users?q=location:Seattle+followers:>120&sort=joined&order=desc”

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/217](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/217)
---
There are two “Vienna”. The question4 is referring to which one?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/218](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/218)
---
Manually make correction in your answer as provided in the error message. If no such words are available insert those and check

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/219](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/219)
---
check if the action is commited

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/220](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/220)
---
try copying the expected result and pasting it inside the quotations

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/222](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/222)
---
Check the log of the daily commit .

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/223](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/223)
---
Ahh, I have the same doubt too!

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/224](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/224)
---
For the links, this format worked for me:  
[ < link text > ] (#)

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/225](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/225)
---
Yes I got it now. Thank you!

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/226](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/226)
---
it should be “2.9” instead of 2.9

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/227](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/227)
---
looks like formatting or the passed conditions have some issue… can you check and verify it once and see?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/228](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/228)
---
Error: At [3].title: Values don’t match. Expected: “4. 365 Days - Noch Ein Tag”. Actual: “4. The Next 365 Days”

{“id”: “tt21106646”, “title”: “4. The Next 365 Days”, “rating”: “2.9”, “year”: “2022”}

my result , there is no any entry with “4. 365 Days - Noch Ein Tag” on IMDB

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/229](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/229)
---
I am getting missing links as error in the 10th question. How to do it?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/230](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/230)
---
Mine is giving 1/10 on running without even writing anything? This is happening for Q3? Is it just a glitch?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/231](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/231)
---
Yes happened to me too, refresh the page, mine got fixed!

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/232](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/232)
---
Check you pdf you can find a word with blue colour and underline. Give some dummy link and use link mark with the word

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/233](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/233)
---
Best way to solve Q2 is , look at the network tab in dev tools and get the url used for assessment and get data from it .

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/234](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/234)
---
u have used a apace (\_) after 2.9 which is not visible at front that’s why it is throwing error , it should be just (“2.9”) not ("2.9 ")

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/235](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/235)
---
Agreed and I have tweaked my approach to get the correct answer. But I feel the question instructions should be adjusted accordingly - the question says to get every issueDate and enhancedweatherDescription key value pair - but only 2 such pairs exist ; whereas in the final answer it is forecast date & weather description total 14 pairs.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/236](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/236)
---
Screenshot (7)1366×768 243 KB

* Open the BBC Weather website.
* Press `Ctrl + Shift + I`.
* Select the ‘Network’ menu.
* Select ‘Fetch/XHR’.
* Type ‘Karachi’ in the input field on the website. **Do not press Enter** while entering the location; just type the location. Pressing Enter might cause ‘location?api\_key=…’ to disappear.
* ‘location?api\_key=…’ will appear in the inspect menu.
* Double-click it to open a web page (https://locator-service.api.bbci.co.uk/locations?api\_key={api\_key}). This will give the API.
* Alternatively, single-clicking ‘location?api\_key=…’ will open headers where you can see the Request URL and the API key.
Here's a description of the image:

The image shows a computer screen displaying several windows and browser tabs.  The dominant window is a web browser showing the BBC Weather website.  The page displays a global map with weather icons for various cities (London, Chicago, Tbilisi, Dakar, San José, Brasilia, Mombasa), a search bar with "Karachi, Pakistan" entered, and promotional text about weather forecasts. 


To the right, the browser's developer tools are open, specifically the Network tab. This displays details of network requests made by the webpage, including request names ("locationsTapi"), status codes (200), sizes, and timings. One line clearly shows a request to a location API. 


In the bottom right, a Windows activation prompt appears ("Activate Windows" and "How can I help you?"). It also mentions that the chat messages and network requests are sent to Google and may be seen by human reviewers to improve the AI feature.

Other visible browser tabs suggest other activity (Inbox, hness.org, My Dash, Graded, TDS 2025, GA4-D, country, BBC West, locator-sc). The taskbar at the bottom shows several applications including Google Chrome and what seems to be a file explorer. The clock shows the time as 04:36 PM, 09-02-2025.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/237](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/237)
---
type 2025 instead of only using 25 for the year

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/238](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/238)
---
HOW TO DO SCRAPING USING GITHUB ACTIONS  
I’m getting no workflow runs error Sir

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/239](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/239)
---
How to resolve “Error: Incorrect latitude. Check OSM ID ending with 2077”

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/240](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/240)
---
@22f3000657

you can try this-

https://nominatim.openstreetmap.org/search?format=jsonv2&city=Chennai&country=India

change the city and country in the url

there will be a bounding\_box field: [min\_lat, max\_lat, min\_long, max\_long]

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/241](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/241)
---
#question 10  
Hi, Can anyone help me with Question 10?  
No matter how i try to post the markdown, it is always showing that either the words are missing or are different from the original. I have tried every possible way i could think of but it is not working.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/242](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/242)
---
Getting this question right is a tough nut to crack…so I would rather suggest you to do using the developer tools by inspecting the source code and putting the breakpoint followed by writing the code in the console to retrieve the expected answer

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/243](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/243)
---
Screenshot from 2025-02-09 17-40-581599×155 26.4 KB

  
Can’t seem to get this working, have tried many variations by now like including my email in each of the name sections in every possible permutation. Probably just some silly mistake I haven’t noticed yet but any help would be appreciated. On Linux Mint if that’s relevant.

main.yml:

```
name: Daily Commit Workflow

on:
  schedule:
    - cron: '10 17 * * *' 
  workflow_dispatch:

jobs:
  commit:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Add commit using 23f2001216@ds.study.iitm.ac.in
        env:
          PAT: ${{ secrets.PAT }}  # PAT stored as a secret
        run: |
          git config --global user.name "Aryan"
          git config --global user.email "23f2001216@ds.study.iitm.ac.in"

          echo "Daily commit on $(date)" >> daily-log.txt

          git add daily-log.txt
          git commit -m "Automated daily commit on $(date)"

          ls -la
          git status

          git push origin main  
          git push "https://${{ secrets.PAT }}@github.com/${{ github.repository }}.git" main

```
The image shows a screenshot of a computer screen, specifically a section of a web form or application. 


Here's a breakdown of the content:

* **Instruction:** The text "Enter your repository URL (format: https://github.com/USER/REPO):" provides clear instructions for the user.  This implies the user is expected to input a GitHub repository URL.

* **Input Field:** A text input field is displayed below the instruction. The user is supposed to type the repository URL into this field.  A partially filled-in URL "https://github.com/AryanTikam/AryanTikam" is already present within it. A small red circle with a cross inside it suggests an error.

* **Error Message:** Below the input field, an error message is shown:  "Error: Latest run does https://github.com/AryanTikam/AryanTikam/actions/runs/13225425496 not include 23f2001216@ds.study.itm.ac.in in the name". This indicates that the provided URL, while seemingly correct, is failing validation because it doesn't contain the email address "23f2001216@ds.study.itm.ac.in" in its name or perhaps another related identifier.

In short, the image displays a form with an input field for a GitHub repository URL and an error message explaining why the provided URL is deemed invalid. The likely reason for the error is a missing or incorrect identifier within the repository’s name or configuration.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/244](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/244)
---
Hi Team,

I have made the JSON from the IMDB website using JS, But do i miss any filter conditions,  

image1640×302 20.4 KB

  
I took first 25 films which 5 to 6 rating, but json seems to be different.

Could anyone please tell me what i did wrong here?
Here's a description of the image:

The image shows a code snippet within a dark-themed code editor or IDE.  The code is a JSON object, partially visible, with key-value pairs including "year," "rating," and "id." The values associated with these keys suggest data related to a movie or show.  There's an error message below the JSON indicating a mismatch in expected and actual title values, implying that a data scraping process encountered an issue. The error states that the expected title was "11. Sebastian Fitzeks Der Heimweg" but the actual value obtained was "11. The Calendar Killer."  A further message at the very bottom explains that this might be due to regional differences in IMDb search results, and suggests manual title translation or re-running the scraper. The overall context strongly suggests a debugging session involving web scraping from IMDb.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/245](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/245)
---
Solved the above issue, please ignore it.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/246](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/246)
---
Believe it or not, I solved it

image657×516 26.1 KB
Here's a description of the image:

The image shows a code editor or a similar interface with a question and answer related to Markdown formatting.

**The Question:**

The top section asks: "What is the markdown content of the PDF, formatted with prettier@3.4.2?"  This implies a PDF file was processed using the `prettier` code formatter, version 3.4.2, and the question seeks the resulting Markdown representation.

**The Answer:**

A text box below the question contains the following Markdown code, which is marked as correct:

```markdown
|adficio|chirographum|
|---|---|
|vitae|ipsam|
|spectaculum|claudeo|
|comes|celeber|
Decumbo decumbo suadeo totidem apto.
```

This Markdown creates a table with two columns and four rows followed by a plain text sentence.

**Additional Information:**

Below the answer box, there's a note stating:  "It is very hard to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. To make it easy, this question only checks a few basic things." This disclaimer explains the challenge of accurately converting PDFs to Markdown and justifies the simplicity of the question's scope.

**Overall:**

The image presents a simple Markdown formatting problem within a coding environment, emphasizing the difficulties associated with PDF-to-Markdown conversion. The given solution demonstrates a basic table and plain text, likely chosen for ease of testing and evaluation.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/247](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/247)
---
In the 10th question, how do we add headings and links to the markdown output?(getting error: Headings missing)

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/248](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/248)
---
first convert it roughly to md file then use ai and tell it to add (all the errors one by one). and slowly it will solve all the errors

yes i know it is not the correct way to convert pdf to md file but its just a way to trick the checking system.

but i have an issue it gave me error that it does not contains the word “bash, javascript, whole redesign, net, suasoria” which is not in the actual pdf, but i added it and it worked. it was just pure trial and error.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/249](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/249)
---
this is a changing dataset so make changes to your answer accordingly and you will get it correct

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/250](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/250)
---
Do the necessary changes as it is said below as it is an everchanging dataset.  
You will get the answer correct once you make the changes asked after checking.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/251](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/251)
---
check you code and do the changes like max\_latitude  
replace [0] to [1]

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/252](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/252)
---
image835×606 34.6 KB

  
sir in Q4 i am getting this error:

```
TypeError: Cannot read properties of undefined (reading 'id')

```

please help me out with it.  
Additionally even if i write anything in the code block the err remains same!

@Jivraj @carlton @s.anand sir please help me out as only this question left.  
anyone facing this issue? let me know

```

{
     "25-02-09": "Partly cloudy and a moderate breeze",
     "25-02-10": "Sunny intervals and a moderate breeze",
     "25-02-11": "Sunny and a gentle breeze",
     "25-02-12": "Light snow and a fresh breeze",
     "25-02-13": "Light snow and a fresh breeze",
     "25-02-14": "Light snow and a gentle breeze",
     "25-02-15": "Light snow and a gentle breeze",
     "25-02-16": "Light snow and a gentle breeze",
     "25-02-17": "Light snow and a gentle breeze",
     "25-02-18": "Sunny intervals and a gentle breeze",
     "25-02-19": "Light cloud and a gentle breeze",
     "25-02-20": "Light cloud and a gentle breeze",
     "25-02-21": "Sunny and a moderate breeze"
}



```
The image shows a coding interface or online code editor. The main content is focused on a JSON (JavaScript Object Notation) data structure representing a weather forecast.

**Top Section:**  A snippet of JSON code is displayed.  It shows weather descriptions for the dates January 1st, 2nd, and 3rd of 2025.  A comment `// additional days` indicates that more data follows.

**Middle Section:**  A question is posed: "What is the JSON weather forecast description for Nur-Sultan?".  Below the question is an attempt at a JSON object providing a weather forecast for various dates in February 2025. This JSON is partially correct but has a syntax error (a missing comma).  An error message ("TypeError: Cannot read properties of undefined (reading 'id')") is shown below the attempted answer.  This suggests the code is trying to access an 'id' property that doesn't exist in the JSON structure.

**Bottom Section:** A "Check" button is visible, implying this is an interactive exercise or a coding challenge where the user's JSON needs to be validated.


The image essentially presents a problem where the user is tasked with providing a correct JSON structure representing the Nur-Sultan weather forecast, fixing the syntax error. The error message offers a clue that the code used to process the JSON is likely expecting a field named 'id' which is absent in this example.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/253](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/253)
---
in my dashboard there is no submit button for ga2,3,and 4 as well and if i check for scores in grades tab for ga2 and ga3 it was given as not submitted , does everyone facing the same ?? if the submit button is visible for anyone plss guide me to rectify that.  
regards and thanks.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/254](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/254)
---
image1224×540 18.9 KB

  
it is showing correct but if i reload the page or press ctrl+c in my terminal its showing this error what should i do now ??
Here's a description of the image:

The image shows a screenshot of a web page, likely a coding tutorial or assignment. 


**Top Section:** The top section displays a dark background with a markdown-style outline of a Wikipedia page about Vanuatu. The headings include "Contents," "Vanuatu," "Etymology," "History," and "Prehistory."


**Main Section:** Below, there's a numbered list of five steps outlining a task:

1. **API Development:** Create a web API using a framework like FastAPI, with an endpoint that accepts a `country` parameter.
2. **Fetching Wikipedia Content:** Retrieve the HTML content from the Wikipedia page corresponding to the given country.
3. **Extracting Headings:** Parse the HTML to extract all headings (H1 to H6) while preserving their order.
4. **Generating Markdown Outline:** Format the extracted headings into a Markdown outline (using `#` for headings).
5. **Enabling CORS:** Configure the API to allow Cross-Origin Resource Sharing (CORS) to enable requests from any origin.


**Bottom Section:** There's a text box with a prompt: "What is the URL of your API endpoint?". Below it, a text field displays a URL: `http://127.0.0.1:8000/api/outline?country=france`. This URL likely points to a locally running API. An error message "TypeError: Failed to fetch" appears beneath the URL, indicating that the API request failed.

The overall context suggests a programming exercise involving building a web API that fetches data from Wikipedia and transforms it into a Markdown outline. The error message indicates a problem in accessing the API, potentially due to network issues or an error in the API implementation.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/255](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/255)
---
image1150×776 54.1 KB

Respected Sir,  
How can I Solve this, I’m not able to solve this one
This image shows a programming challenge involving the Hacker News RSS API.  The challenge is presented in several parts:

**Background Information:**

* **TechInsight Analytics:**  A market research firm using Hacker News as a data source to track technology trends.
* **Manual Monitoring Problem:** Manually monitoring Hacker News for specific topics and engagement is inefficient.
* **Automation Goal:**  Automate the process of identifying and extracting relevant Hacker News posts.
* **Three Tasks:** The automation needs to perform: Topic Monitoring, Engagement Filtering, and Data Extraction.

**The Challenge (Your Task):**

The core task is to write a program that uses the Hacker News RSS API to find the latest post mentioning "WebRTC" and having at least 30 points. The program must:

1. **Automate Data Retrieval:** Fetch the latest Hacker News posts using the API, filtering by topic and minimum points.
2. **Extract and Present Data:** Extract the URL (the `<link>` tag) from the most recent relevant post's XML data.
3. **Share the Result:** Submit the URL of the identified post.

**Attempt and Error:**

A user has attempted to answer by providing a URL in the input field: `https://news.ycombinator.com/item?id=41699323`. However, the system has marked this as an "Incorrect link".

**Other UI Elements:**

* A "Check" button suggests a mechanism for validating the submitted URL.
*  The text "Search Hacker News (1 mark)" suggests this is part of an assessment, possibly worth one mark.


In essence, the image presents a coding problem with clear instructions and a mechanism for checking the answer.  The user needs to write code to interact with the Hacker News RSS API to meet the specified criteria.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/256](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/256)
---
Hi,  
For the 4th question, We can get the necessary information issueDate and its description from Summary itself right? or am I seeing the stuff in the wrong place?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/257](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/257)
---
Change it manually.  
add the expected answer

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/258](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/258)
---
when you press ctrl+c it turns off the server and same goes for refresh.  
also you dont need to manually write ?country… just write till outline and turn on the server n you are good to go.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/259](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/259)
---
ok this is fine for now and its showing correct also but at the time of evaluation will my server runs??

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/260](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/260)
---
It is written in the ques to get the link in the link tag. Not the post link. Like this  

image1464×560 115 KB
The image shows a screenshot of a code editor displaying an XML file. 


Here's a breakdown of the content:

* **XML Structure:** The core of the image is an XML file, a standard format for structured data. The XML is well-formed, with opening and closing tags properly nested.  The file appears to be an RSS feed, possibly from a news aggregator like Hacker News, given the `<title>` which includes "Hacker News".

* **Key Elements:** The XML contains typical RSS elements like `<channel>`, `<item>`, `<title>`, `<link>`, `<description>`, `<pubDate>`, etc.  The `<item>` element represents a single news item.

* **Data Within the Item:** The `<title>` of the item describes "DoppelBot: Replace Your CEO with an LLM". The `<description>` includes a link to an article (`<a href=...>`) and other details like point count and comment count on a specific platform (likely Hacker News). The `<link>` element specifies a URL ("https://modal.com/docs/examples/slack-finetune").  This appears to be a link to a tutorial or documentation regarding using Slack with an LLM (Large Language Model).

* **Highlighted Link:**  The link "https://modal.com/docs/examples/slack-finetune" is highlighted, suggesting it might be the focus of interest.

* **Code Editor Environment:** The code is displayed within a dark-themed code editor. The editor shows line numbers (although they are not fully visible) and syntax highlighting (making XML tags more visually distinct).

* **Header Message:**  At the very top, there's a brief message stating, "This XML file does not appear to have any style information associated with it. The document tree is shown below." This is likely a message from the code editor or parser.


In summary, the image presents an XML representation of a news item, focusing on a specific link pointing to what seems to be a tutorial or guide on integrating Slack with a large language model. The context hints at the potential use case of LLMs in workplace automation.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/261](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/261)
---
Thank you bro, I will try this

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/262](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/262)
---
not at all. your last saved marks will be considered

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/263](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/263)
---
just replace value instead of it. same problem I also that time I check code and modify serval time I faced same error. so just ignore it and replace expected value instead of actual value in our Json.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/264](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/264)
---
extract the pdf to markdown format using chatgpt then add links,tables and one blockquote

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/265](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/265)
---
Try to use the key ‘enhancedWeatherDescription’ parsing through the summary object (or) use the BeautifulSoup to find ‘div’ with attributes of  
class: wr-day-summary

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/266](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/266)
---
Hi, please ensure that your repository is public, if private the response would be 404. If workflow runs is not found, it might be that the number of API calls to your profile/repo might have exceeded, it usually gets reset at the end of the day. Please try again after sometime)

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/267](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/267)
---
In question 1 i am getting this error

```
 {
    "id": "tt21227864",
    "title": "2. You're Cordially Invited",
    "year": "2025",
    "rating": "5.5"
  }

```

my answer is in above format i tried changing to “2024-”, "2024- " to number tried after reloading the page but still i am getting  
Error: At [11].year: Values don’t match. Expected: “2024”. Actual: "2024– "

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/268](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/268)
---
You have to manually change these thing  
from actual change to expected.  
For me, error was almost 10 times.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/269](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/269)
---
on your 11th or 12th instance change it  
write the actual value

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/270](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/270)
---
If you have submitted on the assignment site and saved it in time, then that score is the actual score and will be updated directly on the student dashboard.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/271](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/271)
---
Your answer is correct. Just add a space after the hyphen—it will resolve the problem. Or you can copy and paste from here: '2025– '.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/272](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/272)
---
image1895×975 73.4 KB

  
i wrote everything that was there in the pdf file after converting to markdown, there is no code inside the pdf file then how does it expect to have code in markdown, can anyone help
The image shows a screen capture of an online coding exercise or quiz.  Here's a breakdown of the visible content:

**Top Bar:**

* **Timer:** "03:08:26 left" indicates a time limit of 3 hours, 8 minutes, and 26 seconds remaining.
* **Score:** "Score: 7/10" shows the current score is 7 out of 10.
* **Buttons:** "Check all" and "Save" buttons suggest a process of checking answers and saving progress.

**Exercise Instructions:**

The main body of the text describes a task involving converting a PDF document to Markdown format using specific tools and techniques.  The steps are clearly outlined:

1. **Convert PDF to Markdown:** Extract the content from a provided PDF (`qpdl-co-markdown.pdf`) and convert it to Markdown, maintaining the original structure and formatting.
2. **Format Markdown:** Use Prettier version 3.4.2 to format the converted Markdown.
3. **Submit:** Submit the formatted Markdown file.

**Impact Section:**

This section explains the value and contribution of completing the exercise, highlighting benefits like increased productivity, improved quality, better scalability, and easier integration with various digital platforms.

**Coding Question:**

The core question asks for the Markdown content of the PDF file, formatted using Prettier 3.4.2.  A partially completed answer is visible, showing some correctly formatted Markdown elements:

* A link: `[tricesimus admitto](https://example.com/tricesimus-admitto)`
* Two lines of text: `Suggero comes denique argentum.` and `Desipio crudelis antea quis.`
* Another link: `[ladeptio colligo](https://example.com/adeptio-colligo)`

The answer is incomplete, marked with "Error: Missing code."

**Important Note:** The instructions acknowledge the difficulty of perfectly converting PDFs to Markdown and state that the exercise only checks a few basic aspects to simplify the process.

In summary, the image displays a structured coding challenge focused on PDF to Markdown conversion, formatting, and submission, with clear instructions, a partially completed answer, and an emphasis on the practical application and benefits of the task.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/273](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/273)
---
Yeah! His issue is genuine. Arnav’s JSON seems to be correct, yet these are some issues faced by him.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/274](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/274)
---
Yeah! even I am facing this issue. Despite lot of efforts, last question markdown seems to always incorrect. It is always throwing any sort of error for no reason.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/275](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/275)
---
The IMDB and weather questions was a pain along with the 10th question, wasted so much time @s.anand , the questions were nowhere tough, it was the problems with the evaluation part i had spend hours just to sit and correct the JSON file and no comments on the 10th question’s part.

I am fine with the academia being challenging to study not the evalation making me manually edit solutions

@Jivraj @carlton

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/276](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/276)
---
yes change manually, there are slight changes which we have to do

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/278](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/278)
---
For the 8th question, i am getting an error that tells me i have not run the action, though i manually triggered it and confirmed the commit was made. Cant figure out whats wrong.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/279](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/279)
---
for second query i am getting this result as row 4 and 5 (Screenshot)… but when testing the results it shows

```
{"id":"tt22804850","title":"3. The Sand Castle","year":"2024","rating":"4.7"},
{"id":"tt10128846","title":"4. Megalopolis","year":"2024","rating":"4.8"},
{"id":"tt2322441","title":"5. Fifty Shades of Grey","year":"2015","rating":"4.2"},
{"id":"tt4978420","title":"6. Borderlands","year":"2024","rating":"4.6"},

```

Error: At [4].title: Values don’t match. Expected: “5. Cinquanta sfumature di grigio”. Actual: “5. Fifty Shades of Grey”  

image784×492 91.3 KB
Here's a description of the image:

The image shows a screenshot of what appears to be a movie or TV show listing website or app. 


The content is divided into two distinct movie entries, each with:

* **A Poster:** A small poster image is displayed at the beginning of each entry, one for "Megalopolis" (a dramatic-looking poster showing a city scene at night) and another for "Fifty Shades of Grey" (showing a man and a woman in formal wear).

* **Title and Number:** Each movie is listed with a number (4 and 5), indicating its position in a list, and the title ("Megalopolis" and "Fifty Shades of Grey").

* **Year, Runtime, and Rating Count:** The year of release, runtime (hours and minutes), and a rating count are provided (e.g., "2024 2h 18m 15" for Megalopolis).

* **User Rating and Metascore:** A user-submitted star rating (e.g., "4.8") with the number of ratings in parentheses (e.g., "(33K)") is shown, along with a Metascore (a numerical score out of 100).  "Rate" buttons are also visible.

* **Synopsis:** A brief plot summary or description accompanies each movie.


The overall style is clean and minimalist, typical of a movie database or streaming service interface. The background is plain and the text is easy to read.  A "+" symbol is present in the top left corner of each movie's poster, likely indicating an option to add the movie to a list or queue.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/280](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/280)
---
image606×293 20.3 KB

  
sir earlier it was correct and now i submit it again after running my code it shows error. sir i have done it correct two times earlier. but now again as i click on save button it changed. these tasks are taking too much time and creating more difficulties. please look into this @s.anand @Jivraj @Saransh\_Saini
Here's a description of the image:

The image shows a snippet of code, apparently attempting to represent a JSON (JavaScript Object Notation) weather forecast for Vienna.  The code is structured as a key-value pair, where the keys represent dates (in YYYY-MM-DD format) and the values are corresponding weather descriptions.


**Key Features:**

* **JSON Structure (Attempted):** The code aims to create a JSON object.  However, it has a syntax error, as indicated by the error message.

* **Weather Data:** The data includes weather descriptions for five consecutive days in February 2025 (10th to 14th). The descriptions are textual and include elements like "Sunny," "Sunny intervals," "Light cloud," "gentle breeze," and "moderate breeze."

* **Error Message:** A crucial element is the error message: "Error: At root: Different number of properties."  This indicates a problem in the JSON structure's syntax.  In valid JSON, each key should have an associated value.  The error suggests an inconsistency or an incomplete pairing of keys and values.

* **Missing Brackets:** The JSON structure is missing closing square brackets `}`. The image only shows the opening curly bracket.

**Why it's not valid JSON:**

The error message clearly states that the JSON is malformed due to an uneven number of properties.  A common cause of this is a missing closing brace `}` or a key without a corresponding value.  The context provided by the image does not give the full JSON data structure. To be valid, it would need to be enclosed in curly braces `{}` to denote a JSON object.


In short, the image presents an incomplete and syntactically incorrect attempt at creating a JSON weather forecast.  The error message highlights the problem.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/281](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/281)
---
image2100×400 38.1 KB

Hi Team ,

Are we expecting the result to match exactly as per the benchmark of qa4.
Here's a description of the image:

The image shows a dark-themed code editor or similar interface displaying JSON data and an error message. 


**The JSON Data:**

The main part of the image shows a JSON object.  It's structured like this:

```json
{
  "title": "1. The Night Agent",
  "year": "2023-",
  "rating": "7.5"
},
{
```

The `}` and `{`, suggest that this is likely part of a larger JSON array containing multiple objects.  The `2023-` in the `year` field suggests an incomplete or potentially incorrectly formatted year value.


**The Error Message:**

Below the JSON data, there's an error message that reads:

`Error: At [8].title: Values don't match. Expected: "9. Incorrect answer jalement invités". Actual: "9. You're Cordially Invited"`

This error message indicates a problem with a title field (at index 8 of an array).  The system expected a title of "9. Incorrect answer jalement invités", but received "9. You're Cordially Invited" instead.  This likely represents a test case failure or a data validation issue within the application.

In summary, the image depicts a coding environment where a JSON object is being validated, and an error has occurred due to a mismatch in expected and actual title values in the object at index 8 of a larger JSON array.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/282](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/282)
---
just edit some of the spellings in answers manually as per errors you get n you are good to go.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/283](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/283)
---
22f3002723:

> Cinquanta sfumature di grigio

It is just a translation of the same movie… it’s not different  
Copy paste the Expected: “title” and click on check  
It’ll work
That's a digital image of a single uppercase letter "S". 


Here's a breakdown of its features:

* **Letter:** The letter "S" is in a simple, sans-serif typeface.  It's clean and straightforward, without any embellishments or flourishes.

* **Color:** The letter is white.

* **Background:** The background is a solid, muted greyish-blue color.

* **Style:** The overall style is minimalist and simple.  The letter is centered against the background.

* **Size and Proportion:** The letter occupies a significant portion of the image, suggesting it is intended to be the primary focus.  The proportions of the letter are standard.


The image likely represents a simple avatar, icon, or initial, possibly for a user profile or branding.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/284](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/284)
---
image1802×751 40 KB

Saved responses are not being displayed and also page keeps refreshing…
Here's a description of the image:

The image shows a dark-themed online quiz interface.  Several key features are present:

* **Timer:**  At the top left, "02:23:44 left" indicates a remaining time of 2 hours, 23 minutes, and 44 seconds.

* **Score:** Next to the timer, "Score: 0" displays the current score.

* **Buttons:** Buttons labeled "Check all" and "Save" suggest quiz functionality to review answers and save progress.

* **Discourse Discussion:** A prominent teal-bordered box encourages participation in a Discourse forum.  The text "Have questions? Join the discussion on Discourse" provides clear instructions.

* **Bonus Marks:** A dark green box below the Discourse box explains bonus marks are available for IITM BS students who post relevant questions or replies to a specific Discourse thread ("GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]").

* **Login Information:** The bottom section displays the user's login information, revealing that they are logged in as "23f2001305@ds.study.iitm.ac.in," and provides a "Logout" button.

* **Loading Indicator:** A loading spinner is visible at the very bottom, suggesting an asynchronous operation is possibly in progress.

* **Instructions:**  Above the Discourse sections, small text indicates that it's permissible to find answers by "hacking the code," suggesting the quiz may be designed to allow for different solution methods.

The overall design is clean and functional, using a dark background for better readability and visual appeal.  The emphasis is on encouraging student interaction through the Discourse forum.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/285](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/285)
---
@all, in q4 Actually the answer data is sync with current weather description therefore the answer changes. Make sure to update your json file before submitting.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/286](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/286)
---
try refreshing the page and re-run the script. as the data gets updated the answer also changes.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/287](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/287)
---
refer to the link post,

GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025] Tools in Data Science

> use this Google Colab with the city name to get the Json Body just change the date format.
> @23f2004752
That's a digital image showing a single, uppercase letter "V" in white, centered on a solid blue background. 


The "V" is sans-serif, meaning it lacks the small decorative strokes at the ends of the letter's lines (serifs). The letter is simple and clean in style, and it appears to be relatively large compared to the background space it occupies.  The blue background is a uniform color, likely a shade of azure or a similar vibrant blue.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/288](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/288)
---
i 'm here for the bonus marks,

But since i am here. Just want to appreciate the course and your efforts towards this.

We need more “teachers” like you, who really puts an extra effort in the course.

And i have never seen any course cool as this,

* like appreciating tweaking things, using dev console to tweak things, keep the code checks on client side (*and as S Anand’s Student i have leveraged that freedom , gave client side answer checks’s code to `o1` and it reverse engineered the minifed code, and lots of question were solved by that only, but really curious on how others are doing this*)
* keeping the cutting edge tech in course, like function calling from OpenAI.  
  ( *i have seen some students solutions, they were using regex to solve that problem* )

image1483×687 48.1 KB
That's an emoji! 


Specifically, it's a yellow circle emoticon with a wide, open-mouthed laugh. The eyes are closed in a happy expression. A single, light-blue droplet of sweat is positioned on the right side of the emoji's face. This suggests a nervous or slightly uncomfortable laughter, not entirely carefree.  The overall style is consistent with typical modern emoji designs.
 That's an emoji depicting a yellow face with a single tear rolling down its cheek. 


Here's a breakdown of its features:

* **Face Shape and Color:** The emoji is a classic, round yellow circle representing a face.

* **Eyes:** Two small, dark brown circles represent the eyes. They are simple and evenly spaced.

* **Mouth:** A small, slightly upturned curved line forms the mouth, suggesting a hint of a smile.

* **Tear:** A single, light blue teardrop is shown falling from the left eye, indicating a feeling of happiness with a touch of sadness or bittersweetness.

* **Overall Expression:** The combination of the smile and the single tear creates an ambiguous expression. It could be interpreted as bittersweet happiness, relief, or even a sense of happy melancholy.  It's not a full-blown cry face, but shows a hint of sadness mixed with positivity.
 Here's a description of the image:

The image shows a dark-themed web page or application interface. 


**Key Sections:**

* **Top Banner:** A teal-colored banner at the very top contains a speech bubble icon and the text "Have questions? Join the discussion on Discourse". This suggests a platform for asking questions and participating in discussions.

* **Bonus Marks Section:** A section below the banner explains that bonus marks are awarded for posting on "Discourse". It specifies that IITM BS students who reply to a specific discussion thread ("GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]") with a relevant question or reply will receive 1 bonus mark on a graded assignment.

* **Login Status:** A smaller section indicates that a user with the email address "2212001394@ds.study.iitm.ac.in" is logged in. A "Logout" button is provided.

* **Recent Saves Section:** This section displays a record of recent saved work or submissions. It shows three entries, each marked "Reload" and indicating the date, time, and score achieved (10, 8, and 8). The text "most recent is your official score" clarifies that the latest score is the official one.


**Overall:**

The overall appearance suggests a learning management system (LMS) or a similar educational platform, likely used by students at IITM (presumably the Indian Institute of Technology Madras) for a course involving GA4 (Google Analytics 4) and data sourcing. The emphasis on Discourse indicates the importance of online class discussions and collaboration. The dark theme makes the text easily readable against the dark background.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/290](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/290)
---
why everytime question 2 answer is showing error in json?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/291](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/291)
---
What error are you getting @Abhay222 ?

Can you post a screenshot or error details ?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/292](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/292)
---
Is it safe to skip Q4 for those who got the city named Nur-Sultan, since it has been renamed to Astana, and the answer for Astana is incorrect in the portal?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/293](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/293)
---
@s.anand  
There is possibly wrong evaluation in q6 as it is taking in 2nd latest link as the correct answer. I might be wrong, but the latest one is giving me incorrect evaluation while the 2nd latest is giving me the correct score.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/294](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/294)
---
getting the same issue Error: At [12].year: Values don’t match. Expected: "2024– ". Actual: “2024”

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/295](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/295)
---
yes this kind errors.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/296](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/296)
---
@Abhay222 @22f3002184

if you look closely the expected value is `2024-`  and actual that you are supplying is `2024`.  
Difference ? your value does have a `-` and a space at the end.  
reason ? you might be scraping it ? `trim()` or maybe using `innerText` to get tag’s text ?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/297](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/297)
---
it seems we are intended to provide country specific versions for Individual students simulating being an analyst for MNC in various locations. Clearly you got Spain and I seem to have gotten France, although it doesn’t seem to be mentioned in the question itself.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/298](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/298)
---
Thank you Tanya for pointing out this issue.  
Just tell me this, has your city changed? If yes then what was it earlier and what is it now.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/299](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/299)
---
any reply regarding this please

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/301](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/301)
---
22f2000113:

> For question 2 getting Error: At [8].title: Values don’t match. Expected: “9. Un matrimonio di troppo”. Actual: “9. You’re Cordially Invited” But this movie is not found when searched by name

the movie may have different title on IMDb (perhaps in another language) according to region which is why there isnt an exact match u can manually format it to get marks
That's a close-up shot of a simple digital avatar or icon. 


Here's a description:

* **Background:** The background is a solid, muted grayish-blue color.

* **Letter:** A large, uppercase, sans-serif "M" is centered on the background. The "M" is white and has a clean, simple, and somewhat bold font. 

* **Overall Impression:** The image is minimalistic and likely represents an initial or a placeholder for a user's profile, possibly on a website or app.  The overall color palette is very subdued and neutral.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/302](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/302)
---
GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025] Tools in Data Science

> We have removed that button, cause it was causing confusion among the students.
> If you have saved your answers on the TDS portal then you need not worry, you will be marked. The button was just there to ensure you saw the assignment on the TDS portal.
> Regards,
> TDS TA

Read this
That's a blurry, low-resolution image of a man. 


Here's what can be observed:

* **The Man:** He appears to be middle-aged, with dark hair (possibly under a cap), and a mustache. He's wearing a horizontally striped shirt, predominantly dark with lighter stripes, and blue jeans. His expression is somewhat indistinct due to the image quality.

* **The Setting:** The background is extremely out of focus, but seems to suggest an outdoor or possibly a bustling indoor location. There are indistinct shapes and colors that could be buildings, signage, or other objects, but none are clearly identifiable.

* **Image Quality:** The photo is significantly blurry and pixelated, making precise details difficult to discern. The resolution is low, and the colors are somewhat muted.


There is no discernible text in the image. The lack of clear detail makes it impossible to provide more specific information about the man, his location, or the circumstances under which the photograph was taken.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/303](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/303)
---
Try changing it manually. Some values keep changing due to change in server.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/304](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/304)
---
Alright so in Q4 of W4, We have to extract weather forecast data from bbc servers for a given city. The city I have been given Nur-Sultan is not present in the bbc data base, it appears the city is now known as Astana and is listed in the bbc database as Astana.  
Since Nur-Sultan doesn’t exist in the bbc database, all of my attempts to extract data for it were meet with failure. So I extracted the data for Astana and pasted it in the portal but that doesn’t work as well and throws the following error “TypeError: Cannot read properties of undefined (reading ‘id’)”  
What am I suppose to do? @carlton @Jivraj @Saransh\_Saini  

Screenshot 2025-02-09 1759481823×850 82.3 KB

Below is the data for Astana that I was able to extract, Since Nur-Sultan doesn’t exist in the bbc database:  
{  
“2025-02-09”: “Partly cloudy and a moderate breeze”,  
“2025-02-10”: “Sunny intervals and a moderate breeze”,  
“2025-02-11”: “Sunny and a gentle breeze”,  
“2025-02-12”: “Light snow and a fresh breeze”,  
“2025-02-13”: “Light snow and a fresh breeze”,  
“2025-02-14”: “Light snow and a gentle breeze”,  
“2025-02-15”: “Light snow and a gentle breeze”,  
“2025-02-16”: “Light snow and a gentle breeze”,  
“2025-02-17”: “Light cloud and a gentle breeze”,  
“2025-02-18”: “Sunny intervals and a gentle breeze”,  
“2025-02-19”: “Light cloud and a gentle breeze”,  
“2025-02-20”: “Light cloud and a gentle breeze”,  
“2025-02-21”: “Sunny and a moderate breeze”,  
“2025-02-22”: “Light snow and a moderate breeze”  
}
The image shows a coding challenge or exercise. 


Here's a breakdown of the key elements:

* **Top Bar:** Displays a timer (06:00:20 left), a score (3/10), and buttons labeled "Check all" and "Save".  This suggests a timed, graded coding assessment.

* **Instructions (Steps 1-3):** These outline the task:
    1. Use the BBC Weather API to get the location ID for Nur-Sultan using a GET request.
    2. Use the obtained location ID to get the weather forecast from another API endpoint (weather broker API) via a GET request.
    3. Transform the API response into a JSON object. The keys should be the `issueDate`, and the values should be the `enhancedWeatherDescription`.

* **Example Output:** A JSON snippet is provided to show the expected format of the final output.

* **Coding Challenge:** The main part of the image is a text box where the user is expected to provide the JSON weather forecast description for Nur-Sultan.  A partially completed JSON object is visible, showing several entries with dates and weather descriptions.

* **Error Message:** At the bottom, a JavaScript error message appears: "TypeError: Cannot read properties of undefined (reading 'id')". This indicates a problem in the user's code, likely related to accessing the `id` property of an undefined object.

**In summary:** The image depicts a coding problem where the user needs to fetch weather data from APIs and format it into a JSON object. The error message suggests that the user's code has a bug preventing it from correctly processing the API response. The provided JSON snippet in the coding challenge box is the answer.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/305](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/305)
---
same problem, could anyone help what is wrong.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/306](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/306)
---
@AnvithaV check this out

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/307](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/307)
---
No the city is same as before. But i think it fetches the latest data. As i saved it yesterday it was correct. But today when i clicked on save button again it got wrong.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/308](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/308)
---
What error are you getting ?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/309](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/309)
---
how to approach question 8 of ga4

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/310](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/310)
---
For question #8. Can I use the .github/workflows that I created for the previous assignments or i need to create a new workflow?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/311](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/311)
---
still the same {“id”:“tt24871974”,“title”:“12. Subservience”,“year”:“2024”,“rating”:“5.4”},  
Error: At [12].year: Values don’t match. Expected: "2024– ". Actual: “2024”

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/312](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/312)
---
Change the value manually

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/313](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/313)
---
I am still not sure why the github action question is not working for me. I have manually triggered the workflow multiple times but i keep getting the same ‘name’ error even though it has been specified in the code. Can somebody kindly help?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/314](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/314)
---
Have you given your email id in name ?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/315](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/315)
---
image1865×789 48 KB

  
Completed GA4 with 10/10.  
I have also use tweak that the some answer and question are check and generate on client side.
The image shows a dark-themed online quiz or assessment interface. 


Here's a breakdown of the visible elements:

* **Top Bar:** A green bar at the top displays "01:37:59 left," indicating a remaining time limit, "Score: 10/10" showing the current score, and buttons labeled "Check all" and "Save."  A small gear icon suggests settings or options.

* **Login Information:** Below the top bar, text shows the user is logged in as "23f2003807@ds.study.iitm.ac.in," and a "Logout" button is provided.

* **Recent Saves:** A section titled "Recent saves" displays a list of previous save attempts. Each entry shows a "Reload" button (presumably to restore that saved state), the date and time of the save, and the score achieved at that point.  Three entries are visible.

* **Questions:** A section labeled "Questions" appears at the bottom. Only the first question is visible: "1. Import HTML to Google Sheets (1 mark)."  This indicates a multiple-choice, potentially graded, online test.


The overall design is clean and functional, consistent with online learning platforms or quiz applications. The dark background and green accents are visually appealing. The prominent display of score and time remaining emphasizes the timed nature of the assessment.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/316](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/316)
---
See there is difference of hyphen . Correct it manually.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/317](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/317)
---
Just try re-running your code once and paste in the current response. Check if its working or not.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/318](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/318)
---
Change the slight differences manually accordingly with the expected values

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/319](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/319)
---
I haven’t done MLP and BDM so should I drop TDS now

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/320](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/320)
---
Hi,

I couldn’t able to create markdown from pdf, it showing missing links, but i couldn’t able to find the link in pdf either. I think i’m missing something.

anyone suggest some way how to do pdf to markdown correctly?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/321](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/321)
---
if it says something is missing, just add the same. refer to week-2 question 1 for markdown syntax if necessary

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/322](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/322)
---
yes  
But still doesnt work

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/323](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/323)
---
In q10 i am geeting …missing links- error  
Any idea how to correct this

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/324](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/324)
---
Beyond the specific tools mentioned (like `IMPORTHTML` in Google Sheets or `httpx` and `lxml` in Python), what are the broader *ethical considerations* when scraping data from websites, and how can developers ensure they are acting responsibly and respecting website owners’ rights and resources?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/326](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/326)
---
image1104×369 21.3 KB

  
is everything fine with the answer format?? i am trying this for so long anything i want to change ??
The image shows a programming challenge related to data retrieval and extraction using the Hacker News RSS API.  The task is to find the link to the most recent Hacker News post that mentions "WebAssembly" and has at least 86 points.

Here's a breakdown of the content:

* **Instructions:** The top section describes the task, outlining three steps:
    1. **Automate Data Retrieval:** Use the API to fetch the latest Hacker News posts, filtering by the number of points.
    2. **Extract and Present Data:** Extract the `<link>` tag from the most recent `<item>` element in the API response.
    3. **Share the result:** Submit only the URL of the post.

* **Input/Output:** There's a text box where the user should enter the URL.  Below it, the error message "Error: Incorrect link" indicates that the entered URL ("https://news.ycombinator.com/item?id=38790552") is wrong.

* **Contextual Information:**  The text provides hints about the API and what elements are relevant within the API response ( `<item>` and `<link>` tags).

In short, the image captures a failed attempt at solving a programming challenge that involves interacting with the Hacker News RSS API to retrieve specific information based on keywords and a point threshold.  The provided URL is incorrect, according to the challenge's assessment.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/327](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/327)
---
What is the error are you facing ?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/328](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/328)
---
can someone help through this error!!  

Capture1119×204 37.9 KB
Here's a description of the image:

The image shows a dark-themed code editor or similar interface displaying JSON data and an error message.

**JSON Data:** The main part of the image shows a snippet of JSON data, structured as an array of JSON objects. Each object represents a movie or show with the following keys:

* `"id"`: A unique identifier (appears to be an IMDb ID, prefixed with "tt").
* `"title"`: The title of the movie or show.
* `"year"`: The year or year range of release.
* `"rating"`: A numerical rating.

**Error Message:** Below the JSON data, an error message is displayed:  `Error: At [10]year: Values don't match. Expected: "2021-". Actual: "2021-`. This indicates a validation error in the JSON data at the tenth object (index 10), specifically concerning the `"year"` field. The expected value was apparently a year range starting with "2021-", but the actual value is also "2021-", which suggests a problem with data consistency or validation rules.  Note that the last entry of the JSON is truncated and incomplete.

**Interface Elements:** The JSON data is enclosed within a rectangular box, suggestive of a code editor or a debugging tool. There's a small circular icon with an exclamation mark inside, typically used to denote warnings or errors.  A small, barely visible scrollbar suggests there might be additional content outside the current view.


In summary, the image shows a common scenario in software development where JSON data is being validated, and an error is reported due to a discrepancy in the year field.  The incompleteness of the final JSON object is also a data issue.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/329](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/329)
---
Check if you have made the query proprly. also, check if you taken the correct link from the item

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/330](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/330)
---
in q10 i am getting error- missing links.  
can i get any explanation about this error so that i can figure out this ?  
@Saransh\_Saini as i left with this question only

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/331](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/331)
---
Pdf content one link, I think your converting method was unable to convert link into markdown format , add it manual from pdf.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/332](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/332)
---
I have done that also but still getting same error

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/333](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/333)
---
The one with blue line must be link here in the pdf.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/334](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/334)
---
After that it asking to add tables, i added the same but the issue ‘Missing Tables’ exists

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/335](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/335)
---
23f2000573:

> if it says something is missing, just add the same. refer to week-2 question 1 for markdown syntax if necessary

refer to this @21f3000745

22f3000804:

> can someone help through this error!!

if it is saying something has a mismatch, just spot the mismatch one by one and manually change it @22f3000804
That's an image of a letter "G" on a solid purple background. 


Here's a breakdown of the image:

* **Letter:** A capital letter "G" is centrally positioned.  The font is simple, sans-serif, and likely a common system font. The "G" is white or light-colored, providing high contrast against the purple background.

* **Background:** The background is a uniform, medium-toned purple.  There are no other elements, textures, or gradients present.

* **Overall:** The image is very minimalist and simple. It's likely a logo element, a profile icon, or part of a larger design.  The size and resolution are low, suitable for small-scale use.
 That's a blurry, low-resolution image that appears to be a digital painting or rendering of a fantastical landscape. 


Here's a breakdown of what can be discerned:

* **Foreground:** The immediate foreground is dominated by several tall, slender, rock-like formations or pillars. They are predominantly grayish-purple, with reddish-pink, almost coral-like, growths or textures clinging to their sides. These growths might be plants or some kind of organic material.

* **Background:** The background shows a hazy, indistinct landscape with muted greens and hints of a hilly or mountainous terrain. The background elements lack sharp definition, contributing to the dreamlike, ethereal quality of the piece. The green suggests vegetation, perhaps a forest or jungle.

* **Overall Style:** The style is painterly and impressionistic.  The colors are soft and somewhat muted, with a blend of greens, purples, and reds. The lack of sharp edges and details creates a sense of atmosphere and mystery. The low resolution significantly limits the detail that can be perceived.

There is no discernible text within the image.  The image's low resolution makes it difficult to determine the exact nature of the objects or the specific artistic intent.  It evokes a feeling of an otherworldly or fantastical setting.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/336](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/336)
---
Here for the bonus marks, it was great solving the GA4.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/338](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/338)
---
After you click the link, a page containing all the questions will appear. Attempt them and save it on that particular page using your IITM email ID. Through your ID, submissions will be taken.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/339](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/339)
---
Thankyou , but now i am getting missing code error. What it means? @23f2000573

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/340](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/340)
---
You just have to add a space after a hyphen

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/341](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/341)
---
Check if you are using table formating where there is a table, also there is perhaps a code block in the pdf where a small section of text is in different font than the rest.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/342](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/342)
---
No there is no code block in the pdf. Now i m getting missing code error. Why this error can arise @Saransh\_Saini

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/343](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/343)
---
I am also facing the same error in this question

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/344](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/344)
---
the answer format is correct the link is probably not the latest one, I had the same issue because my code was working only for the first 100 entries… you should try paginating your code so it can cover more entries

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/345](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/345)
---
just change the values as itis coming in the error

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/346](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/346)
---
change the name manually as the name is diiferent on imdb according to the region, I had the same issue…

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/347](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/347)
---
are you able do it now? Reload and check

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/348](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/348)
---
yes facing the same thing

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/349](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/349)
---
you are missing code block

Normal : print(123)  
Code Block : `print(123)`

you can refer to week 2 q1 for the syntax of code block

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/350](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/350)
---
Screenshot 2025-02-09 2340281910×314 56.7 KB

  
anyone have idea about this error?
The image shows a code editor or IDE with a question and a partially visible JSON data structure.  The question at the top asks "What is the JSON data?". The answer, a JSON array of movie objects, is displayed below.  Each object in the array has the following structure: `{"id":"<imdb_id>","title":"<movie_title>","year":"<year>","rating":"<rating>"}`. There are at least ten movie objects visible in the displayed JSON array. The movies have titles like "16. A Serbian Film," "17. Sugar Baby," and "25. Striptease," with corresponding years and ratings.  The bottom of the image displays a `TypeError` message indicating a problem reading the `textContent` property of a null value. This error message suggests a problem in how the JSON data is being accessed or parsed by the code.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/351](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/351)
---
image1757×367 48.3 KB

  
getting this error
The image shows a web page with a section titled "Impact," describing the benefits of using UrbanRide's bounding box data processing capabilities.  Below this, there's a question: "What is the maximum latitude of the bounding box of the city Riyadh in the country Saudi Arabia on the Nominatim API? Value of the maximum latitude". A text box is provided for the answer, where "27.7020999" has been entered.  However, there's an error message displayed underneath, stating, "Error: Incorrect latitude. Check OSM ID ending with 8390". This indicates the entered latitude is wrong, and the user needs to check OpenStreetMap data with an ID ending in 8390.  A small circle with a number "①" is also visible next to the error message, likely indicating a help or information button.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/352](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/352)
---
Yes thankyou i noticed that code block.  
But now getting missig heading @Saransh\_Saini

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/353](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/353)
---
@carlton sir what about this question.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/354](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/354)
---
You have to go to the Settings tab, select Actions from the left panel and choose General from the drop-down list. Then scroll down completely and choose “Read and Write Permission” under the Workflow Permission section

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/355](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/355)
---
Getting at root differnt number of properties for below

```

"2025-02-10": "Sunny intervals and a gentle breeze",
"2025-02-11": "Light rain showers and a gentle breeze",
"2025-02-12": "Thundery showers and a gentle breeze",
"2025-02-13": "Thundery showers and a moderate breeze",
"2025-02-14": "Sunny intervals and a gentle breeze",
"2025-02-15": "Drizzle and a gentle breeze",
"2025-02-16": "Sunny and a gentle breeze",
"2025-02-17": "Sunny intervals and a gentle breeze",
"2025-02-18": "Sunny intervals and a gentle breeze"}

```

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/356](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/356)
---
I’m assuming it’s occurring because the text formatting for the JSON is incorrect. Try and put it in the correct format

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/357](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/357)
---
I’ve reloaded a dozen time and even extracted the data again and again to account for any changes but it still doesn’t work.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/358](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/358)
---
22f3002723:

> ```
> {"2025-02-10": "Sunny intervals and a gentle breeze",
> "2025-02-11": "Light rain showers and a gentle breeze",
> "2025-02-12": "Thundery showers and a gentle breeze",
> "2025-02-13": "Thundery showers and a moderate breeze",
> "2025-02-14": "Sunny intervals and a gentle breeze",
> "2025-02-15": "Drizzle and a gentle breeze",
> "2025-02-16": "Sunny and a gentle breeze",
> "2025-02-17": "Sunny intervals and a gentle breeze",
> "2025-02-18": "Sunny intervals and a gentle breeze"}
>
> ```

{“2025-02-09”: “Partly cloudy and light winds”,  
“2025-02-10”: “Sunny intervals and a gentle breeze”,  
“2025-02-11”: “Light rain showers and a gentle breeze”,  
“2025-02-12”: “Thundery showers and a gentle breeze”,  
“2025-02-13”: “Thundery showers and a moderate breeze”,  
“2025-02-14”: “Sunny intervals and a gentle breeze”,  
“2025-02-15”: “Drizzle and a gentle breeze”,  
“2025-02-16”: “Sunny and a gentle breeze”,  
“2025-02-17”: “Sunny intervals and a gentle breeze”,  
“2025-02-18”: “Sunny intervals and a gentle breeze”}
That's a close-up shot of a simple, minimalist avatar or icon. 


Here's a description:

* **Background:** The background is a solid, muted grayish-blue color.

* **Letter:** A capital letter "S" is centered on the background. The "S" is white or very light-colored, making it stand out clearly against the background. The typeface is a clean, sans-serif font.

* **Overall Impression:** The image is very simple and uncluttered. It's likely used as a profile picture or placeholder image online, representing a user or account starting with the letter S.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/359](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/359)
---
There needs to be two weeks worth of data so if it’s starting from the 9th it should be till the 22nd

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/361](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/361)
---
make the edits clearly in the repository and then open it, the url that is then showed. Just copy and paste it into the box, it will work

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/362](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/362)
---
what problem is their in ques 2 and 3

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/363](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/363)
---
yeah same for me. seems we were unlucky
That's a digital depiction of a yellow emoticon, specifically a "sad face" emoji. 


Here's a breakdown of its features:

* **Shape:** It's a perfect or near-perfect circle.
* **Color:** The main body is a bright, golden yellow.
* **Facial Features:**  It has two small, dark brown or black dots representing eyes.  These are positioned relatively close together and near the center of the upper half of the circle. The mouth is a downward-curving, simple arc, suggesting sadness or disappointment. This arc is dark brown or black, like the eyes.

The overall style is consistent with commonly used emojis on digital platforms.  There is no text present.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/364](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/364)
---
What can I refer to for proper steps to solve Question 10?  
Thanks!

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/365](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/365)
---
Q10 is giving errors even after doing everything

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/367](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/367)
---
23ds3000241:

> o if it’s

getting values dont match for below now  
{“2025-02-09”: “Partly cloudy and light winds”,  
“2025-02-10”: “Sunny intervals and a gentle breeze”,  
“2025-02-11”: “Light rain showers and a gentle breeze”,  
“2025-02-12”: “Thundery showers and a gentle breeze”,  
“2025-02-13”: “Thundery showers and a moderate breeze”,  
“2025-02-14”: “Sunny intervals and a gentle breeze”,  
“2025-02-15”: “Drizzle and a gentle breeze”,  
“2025-02-16”: “Sunny and a gentle breeze”,  
“2025-02-17”: “Sunny intervals and a gentle breeze”,  
“2025-02-18”: “Sunny intervals and a gentle breeze”,  
“2025-02-19”: “Light cloud and a gentle breeze”,  
“2025-02-20”: “Sunny intervals and a moderate breeze”,  
“2025-02-21”: “Light rain showers and a moderate breeze”,  
“2025-02-22”: “Light cloud and a moderate breeze”}
That's a close-up shot of a digital avatar or icon. 


Here's a description:

* **Background:** The background is a solid, rich, pinkish-red or crimson color.

* **Foreground:** Centered on the background is a single, uppercase letter "K". The "K" is white and relatively large, taking up a significant portion of the image. The font is simple, sans-serif, and clean.

* **Overall:** The image is simple, uncluttered, and likely represents a user identifier or initial, perhaps for a profile on a website or app.  The color scheme is bold.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/368](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/368)
---
thanks for the help…

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/369](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/369)
---
@23f3002537, @21f3000745, @Jeleshiya

Anyone who received the Nur-Sultan parameter for this question and at least attempted it will get a mark.

Kind regards

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/371](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/371)
---
sir what about bonus marks cuz my score was 9/10 due to q4(Nur-sultan).

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/372](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/372)
---
The bonus mark will be processed afterwards. That is checked before the scores are pushed to portal.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/373](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/373)
---
Nominatim API gives me the bounding box of the location. How exactly the bounding box helps me to find the details of the location?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/374](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/374)
---
I am facing issues in Q9 , can you help me out?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/375](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/375)
---
const movies = ;

document.querySelectorAll(‘.sc-d5ea4b9d-0.ejavrk’).forEach((item, index) => {  
if (index >= 25) return; // Stop after collecting 25 movies

```
const titleElement = item.querySelector('.ipc-title__text');
const yearElement = item.querySelector('.sc-d5ea4b9d-7.URyjV.dli-title-metadata-item');
const ratingElement = item.querySelector('.ipc-rating-star--rating');

if (titleElement && yearElement) {
    const idMatch = item.querySelector('a[href*="/title/tt"]')?.href.match(/tt(\d+)/);
    const id = idMatch ? `tt${idMatch[1]}` : null;
    const title = titleElement.innerText.trim();
    //const yearText = yearElement.innerText.replace(/\D/g, "").trim(); // Remove non-numeric characters
    const yearText = yearElement.innerText.trim();
    const year = yearText ? yearText : null; // Keep year as a string
    const rating = ratingElement ? ratingElement.innerText.trim() : null; // Keep rating as a string

    if (id && title && year && rating && parseFloat(rating) >= 3 && parseFloat(rating) <= 5) {
        movies.push({ id, title, year, rating });
    }
}

```

});

// Output JSON data with no spaces after colon  
console.log(JSON.stringify(movies, (key, value) => typeof value === ‘string’ ? value.trim() : value, 0));

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/376](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/376)
---
image1903×808 62.7 KB

  
sir i have completed and saved the test but it shows score 0. and also  

image1735×772 124 KB

  
the graded assignment is showing like i didn’t submit it. please check on this.
The image shows a screenshot of a web page, likely an online grading system or assignment platform. 


Here's a breakdown of the content:

* **Top Bar:** A red bar at the top displays the time the page was accessed ("Ended at Sun, 9 Feb, 2025, 11:59 pm IST"), the current score (0), and buttons for "Check all" and "Save." There's also a small, possibly menu, icon in the top right corner.

* **Bonus Marks Section:** A dark gray box explains a bonus mark system for students.  IITM BS students who participate in a specific discussion thread ("GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]") on a platform called "Discourse" by asking relevant questions or replying will receive one bonus mark.

* **Login Information:** Below the bonus section, the user's login information is shown: "You are logged in as 23f3000975@ds.study.iitm.ac.in."  A "Logout" button is provided.

* **Recent Saves Section:** A dark gray box displays recent saves with timestamps, indicating the time each save was made and the score at that time.  Each entry includes a "Reload" button, implying the user can restore their assignment to a previous saved state.  The most recent save is stated to be the official score.


The overall design uses dark colors (dark gray and dark green) with a contrasting red top bar.  The text is clear and easy to read.  The screenshot suggests a system used for academic assignments, possibly involving online discussion forums and automatic grading or scoring.
 The image shows a screenshot of a web page, likely a learning management system (LMS) interface.  The main focus is on a section titled "Graded Assignment 3".

Here's a breakdown of the visible content:

**Left-hand Side Navigation:** This area displays a list of modules and assignments:

* **Development Tools** (header)
* **Module 2: Deployment Tools** (with a dropdown arrow)
* **Module 3: Large Language Models** (with a dropdown arrow)
* **Project 1** (with a dropdown arrow)
* **Module 4: Data Sourcing** (with an upward arrow)
* **Graded Assignment 4** (highlighted in a circle, indicating it's possibly the current focus)
* **Module 5: Data Preparation** (with a dropdown arrow)


**Right-hand Side: Graded Assignment 3 Information:**  This section contains crucial information about the assignment:

* **"Graded Assignment 3"** (title)
* **Due Date Passed:** Clearly states that the due date has passed, providing the past due date (2025-02-05, 23:59 IST).
* **Multiple Submissions:** Informs users they could submit multiple times before the deadline.  The final submission would be graded.
* **Troubleshooting:** Provides troubleshooting steps for common access problems such as:
    * Disabling ad blockers.
    * Enabling cookies and Javascript.
    * Using Chrome browser.
    * Disabling interfering browser extensions.
    * Deactivating overly aggressive antivirus software.
* **Student ID Requirement:**  Emphasizes the *mandatory* use of the student ID (example format provided) for submission. Failure to do so will result in a score of zero.
* **Assignment Link:** Provides a direct link to access the assignment: `https://exam.sanand.workers.dev/tds-2025-01-ga3`


**Overall:** The screenshot is likely from a student's view within an online course platform.  It shows that a graded assignment's deadline has passed, providing instructions on how to access and submit the assignment, along with troubleshooting guidance. The highlighted "Graded Assignment 4" on the left suggests the student might be navigating related materials or preparing for a subsequent assignment.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/377](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/377)
---
Your most recent score will be considered, as long as you saved it before the deadline

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/378](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/378)
---
Here are the Discourse IDs that replied to this post. @carlton could you please add 1 mark to them in the GA (not the overall score)?

* Please include only those are enrolled this term, obviously.
* If they didn’t attempt GA4, please include them anyway and give them 1/10.
* If they got 10/10 already, please add 1 mark anyway and give them 11/10.

```
21F1005510
21f2000296
21f2000588
21f2000709
21f2001369
21f3000745
21f3001379
21f3001797
21f3001993
21f3002277
22ds2000011
22ds3000157
22f1000120
22f1000535
22f2000008
22f2000113
22f2001590
22f2001640
22f3000079
22f3000519
22f3000586
22f3000639
22f3000657
22f3000804
22f3000910
22f3001011
22f3001315
22f3001754
22f3001840
22f3002034
22f3002175
22f3002184
22f3002723
22f3002771
23ds3000040
23ds3000149
23ds3000241
23f1000299
23f1000422
23f1000625
23f1001126
23f1001174
23f1001231
23f1001301
23f1001839
23f1002534
23f1002571
23f1003139
23f2000098
23f2000237
23f2000573
23f2000926
23f2001177
23f2001286
23f2001305
23f2001413
23f2001738
23f2002291
23f2003268
23f2003717
23f2003751
23f2003853
23f2004042
23f2004636
23f2004644
23f2004752
23f2004907
23f2004941
23f2005138
23f2005275
23f2005419
23f3001208
23f3001601
23f3001752
23f3002537
23F300327
23f3003594
23f3003871
23f3004024
23f3004114
23f3004162
24ds1000082_Vivek
24ds2000024
24ds2000108
24ds3000032
24ds3000090
24f2000695
24f2003130
Abhay222
ABHIJITH_VS
adeepu.here
Adityism
akashkunwar
anu2023
AnvithaV
AryanTikam
Atif01
carlton
daksh76
Deepanshutomar
GIRISH_VISHVESHVAR_B
gouthamnischay
H1Dd3n_xx
Haricharan
HARISH.S
iamsarthak
jashmevada
Jayeshbansal
Jeleshiya
JoelJeffrey
koustubhr
lakshaygarg654
Lokkiii
Megha
mohiit
Namannn28
namanshyamsukha
nayonika
Neelakandan
Nelson
nilaychugh
parthpatel
rabbaniIITB
Rehbar
Rohitb
rohitgarg
roy2003
Rrishit
Sagan
sandeepstele
Saransh_Saini
sarvan108
sha_512_av
ShahbaazSingh
sharma_abhay
ShivaniAdhiyaman
shivanshgupta0007
Siddhu3050
Suhani
swatikap
tanmaysahu295
tarundude02
Udipth
vaishnavi.k
Vedant22
vidushi
vidya19
yasharabhavi

```

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/379](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/379)
---
Hello sir, my name is mentioned here however I did not get the bonus mark.

Warm regards,  
Nayonika Arora  
24ds1000090

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/381](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/381)
---
ig, they have not updated.

not reflected on my portal too

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/382](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/382)
---
image1880×873 141 KB

  
As you can see in this screen shot i already tried this question and getting error so i posted it on discourse. But still i did not get any marks for attempting this question.  
i got only 9/10.
This image shows a discussion thread from a course, likely online, titled "GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]".  The thread is about a coding error.

Here's a breakdown of the visible content:

* **Top Bar:** Shows the course title, and sub-headers indicating the course's subject area ("Tools in Data Science"), and relevant metadata ("announcement term1-2025 graded-assignment week-4"). There are also icons for a menu, search, and notifications.

* **Left Sidebar:** Contains a navigation menu with sections for "Topics," "My Posts," "Docs," "More," "Categories" (listing courses, operational issues, a professionals' corner, and all categories), and "Tags" (showing "clarification").

* **Main Content Area:**  This is where the main discussion takes place.  

    * **Post:**  User "A" (22f2000008) describes a coding error encountered repeatedly while running code to obtain weather data for Nur-Sultan.

    * **Error Message:** A detailed Python error message is displayed, showing a `NameError` because the variable `location_id` is not defined.  The error originates from line 35 of the code, which attempts to construct a URL using this undefined variable.  A code snippet shows this line within a larger context.

    * **Replies & Interactions:**  There are reply buttons, reaction icons (heart, link, and three dots), and timestamps associated with the post and replies. Time stamps indicate that the original post was made on January 31, and there was another reply/interaction on February 8.

* **Right Sidebar:** Displays a thread progress indicator ("168/360"), indicating this post is part of a larger discussion.

The overall context suggests the user is seeking help debugging their Python code, which is designed to fetch weather data using a BBC Weather API (or a similar service). The core issue is the failure to correctly retrieve or define a location ID for Nur-Sultan before constructing the API request URL.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/383](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/383)
---
Hello @s.anand @carlton Sir,  
As can be seen, my roll number is present in this list (21f2000588) and in GA4 I have got 10/10 but unfortunately, that bonus mark hasn’t been added (as can be seen from the score displayed on the dashboard). So I request you to add that bonus mark to the total kindly.

Hoping for a positive response.  
Thanks & Regards  
Digvijaysinh Chudasama  
21f2000588

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/384](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/384)
---
@22f2000008 Your roll number is in the list shared by professor Anand.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/385](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/385)
---


Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/386](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/386)
---
image1900×860 118 KB

  
I am not saying anything regarding bonus marks. I am asking GA4 q4 about  
Nur-Sultan in this question everyone getting error after post in discourse ,sir say who attempt this question get a marks .But i am not recieved this question marks
This image is a screenshot of a discussion thread on a platform likely used for online learning or course management. 


Here's a breakdown of the content:

**Top Bar:**

* **GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]:** This is the title of the thread, indicating a discussion about data sourcing within a course called "GA4" ("Tools in Data Science" is also mentioned), specifically for the month of January 2025.  "TDS" might be an abbreviation for "Term Data Science" or a similar term.

* **Navigation elements:**  There are icons for courses, tools, and possibly a search bar.

**Left Sidebar:**

* **Navigation:** Sections for Topics, My Posts, Docs, More, Categories (with options like Courses, Operational Issues, Professionals Corner), and Tags (with "clarification" listed).  This suggests a well-organized platform.

**Main Content Area:**

* **Discussion Posts:** The main area shows two posts:
    * **rohitgarg's post:** This user complains that an update has not been reflected on their portal.
    * **carlton's post:** This post is from a user identified as a Course Teaching Assistant (TA).  Carlton explains that anyone who used a specific parameter ("Nur-Sultan") in answering a question will receive a mark.  They also include mentions of other users, possibly their usernames (@2313002537, @21f3000745, @Jeleshiya).

* **Post Metadata:** Each post shows timestamps (3h, 1h), and reaction counts (likes).  A reply button is also visible.


**Right Sidebar:**

* **Timeline:** A vertical timeline shows the dates and times of posts, indicating the activity over a couple of days. 


**Other Elements:**

* **User Avatars:** Small profile pictures appear next to user names.
* **Usernames:** Several usernames are shown.
* **IDs or Codes:** There's a string of alphanumeric characters ("22f2000008") near the bottom, possibly a reference number or internal ID.

**Overall:**

The screenshot captures a typical online learning forum discussion, highlighting a specific issue about grading criteria and the status of updates on student portals. The platform seems to be designed to facilitate communication and collaboration among students and teaching staff.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/387](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/387)
---
if a student has 10/10 and his name is in the bonus list, how would that look like in the dashboard?

I don’t think it is added in my case.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/388](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/388)
---
It will show up as 110 marks. Bonus marks are for all discourse posts on this thread that Anand has identified as valid. I have provided operations team with the update corrected scores. You will start seeing them in the dashboard soon.

Also these are the list of students that have been affected by Nur-Sultan in their questions. These will get an automatic mark for that question if they attempted it. Note that this is not a bonus mark. This is a free mark.

23f3002537@ds.study.iitm.ac.in  
23f3003875@ds.study.iitm.ac.in  
21f3002112@ds.study.iitm.ac.in  
23f2003437@ds.study.iitm.ac.in  
22f3002236@ds.study.iitm.ac.in  
22f3001705@ds.study.iitm.ac.in  
22f2000008@ds.study.iitm.ac.in  
21f1001892@ds.study.iitm.ac.in  
23f1002075@ds.study.iitm.ac.in  
23f1001126@ds.study.iitm.ac.in  
22f3002661@ds.study.iitm.ac.in  
22f2000506@ds.study.iitm.ac.in  
24f1002149@ds.study.iitm.ac.in  
23f2002473@ds.study.iitm.ac.in

Kind regards

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/389](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/389)
---
Please refer to this reply.

GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025] Tools in Data Science

> It will show up as 110 marks. Bonus marks are for all discourse posts on this thread that Anand has identified as valid. I have provided operations team with the update corrected scores. You will start seeing them in the dashboard soon.
> Also these are the list of students that have been affected by Nur-Sultan in their questions. These will get an automatic mark for that question if they attempted it. Note that this is not a bonus mark. This is a free mark.
> 23f3002537@ds.study.iitm.ac.in
> 23f3…

Kind regards
That's a close-up headshot of a man. 


Here's a description:

* **The Man:** He appears to be of South Asian descent, with dark hair, brown eyes, and tan skin. He's wearing rectangular, dark-framed glasses. His expression is neutral to slightly smiling. He has short, neatly styled hair. He's wearing a purple collared shirt.

* **The Background:** The background is a plain, light yellowish-beige or tan color, providing a simple, uncluttered backdrop that focuses attention on the man.

* **Image Quality:** The image quality is somewhat low-resolution; the details are a bit soft, and there's a slight blurring, particularly noticeable around the edges.  This suggests it might be a smaller, compressed version of a larger image.


There is no text visible in the image.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/390](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/390)
---
For those who didn’t submit but still need to practice the questions like to check if the answer is right, or cross-check the solutions for GA 4 and GA 5, is there a special link where the portal just checks the answer and says right or wrong. I wasn’t able to do GA4 or even try to attempt GA 5 before deadline, but i would like to go through the process of submitting etc. is there any link or solutions for GA 4 and GA5.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/391](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/391)
---
is there anyway to practice the assignments and check answers even though the deadline for the assignment passes? or is the answer given somewhere just for learning sake. I understand that each set of students get different questions. @Jivraj @carlton @s.anand

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/392](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/392)
---
