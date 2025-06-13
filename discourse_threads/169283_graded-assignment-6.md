# Thread URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283)

Please post any questions related to Graded Assignment 6 - Data Analysis

Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.

Deadline 2025-03-15T18:30:00Z

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/1](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/1)
---


Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/2](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/2)
---
The answer choices for questions 1 and 2 in graded assignment 6 are quite confusing. Both questions are single-select, yet three out of the four options are correct in each case. I’m unsure whether to choose one of the correct options or if the question is actually asking for the incorrect one. Could someone please clarify?

@carlton

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/3](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/3)
---
@Jivraj @Saransh\_Saini  
I have similar concern  
For Q1, I used the following code:

```
print(f'Pearson correlation for Karnataka between price retention and column')
kk = df[df['State'] == 'Karnataka']
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = kk['price_retention'].corr(kk[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')

```

And got the following output:

```
Pearson correlation for Karnataka between price retention and column
	Mileage (km/l)            : 0.03
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.04

```

Whereas options are below where none of them are correct.  

image281×219 9.1 KB

Whereas for Q2 (Punjab and Yamaha) I used the following code:

```
print(f'Pearson correlation for Punjab and Yamaha between price retention and column')
pb = df[(df['State'] == 'Punjab') & (df['Brand'] == 'Yamaha')]
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = pb['price_retention'].corr(pb[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')

```

and got the following answers:

```
Pearson correlation for Punjab and Yamaha between price retention and column
	Mileage (km/l)            : 0.24
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.08

```

The options for Q2 are given below and 2 of them are correct (AvgDistance and Mileage).  

image278×216 9.19 KB
Here's a breakdown of the image's content:

**Layout and Elements:**

*   **Radio Buttons:** The image depicts a set of radio buttons. Radio buttons are form elements that allow a user to select only one option from a predefined list.
*   **Options:** There are four distinct options presented, each associated with a radio button.
*   **Selected Option:** The second radio button is selected (filled in with a blue circle), indicating that this option is currently chosen.

**Text Content:**

*   **'Mileage: 0.95'**: This represents an option related to "Mileage" with a value of "0.95".
*   **'AvgDistance: -0.05'**: This represents an option related to "AvgDistance" (average distance) with a value of "-0.05".
*   **'Mileage: 0.21'**: This represents an option related to "Mileage" with a value of "0.21".
*   **'EngineCapacity: 0.17'**: This represents an option related to "Engine Capacity" with a value of "0.17".

**Interpretation:**

This image likely represents a feature selection process or a configuration setting within a larger application or system. The user is being asked to choose which feature or parameter they want to focus on, and each option seems to represent a different property (Mileage, Average Distance, Engine Capacity) along with a corresponding value. The "AvgDistance" option is currently selected.
 Here's a detailed description of the image's content:

**Overall:**

The image shows a selection of radio button options. Each option consists of a radio button and a textual label. One of the radio buttons is selected (highlighted).

**Specific Elements:**

*   **Radio Buttons:** There are four radio buttons displayed. Radio buttons are small, circular buttons that allow a user to select one option from a set of choices. The third button from the top is highlighted, indicating that it's the selected option.
*   **Text Labels:** Each radio button has an associated text label. The labels are:
    *   'Mileage: 0.95'
    *   'AvgDistance: -0.06'
    *   'Mileage: 0.24'
    *   'EngineCapacity: -0.08'

**Observations:**

*   The labels appear to represent different vehicle characteristics or features (Mileage, Average Distance, Engine Capacity) along with their respective numerical values.
*   The values associated with each feature seem to be numerical values, some of which are negative.
*   The radio buttons provide a mechanism for the user to choose one of these options, perhaps for a sorting, filtering, or other type of selection process within a larger interface.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/4](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/4)
---
@24f2006061 We are looking into it. We will update based on our analysis. Thanks for letting us know.

Kind regards

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/5](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/5)
---
I used a python script to get the solution to quesiton 1 of week 6 graded assignment. It matches three options. Is this a bug or like we then need to analyze using the pearson coefficient to determine which option is the correct one  

image1383×263 25 KB
Here's a breakdown of the image content:

**Overall:**

*   The image is a screenshot of a multiple-choice question from what appears to be an online quiz or test.

**Text:**

*   **Question:** The question is related to analyzing factors that influence the resale value of motorcycles (Yamaha) in Delhi for a premium dealership. Specifically, it asks about the impact of mileage, average daily distance traveled, and engine capacity on price retention. Pearson Correlation Coefficient is used and price retention is (resale price / original price).

*   **Answer Choices:**
    *   'Mileage: 0.01'
    *   'AvgDistance: 0.00'
    *   'EngineCapacity: 0.13' (This one is selected)
    *   'EngineCapacity: 0.95'

*   **Other Text:**
    *   "1 point" indicating the point value of the question.

**Visual Elements:**

*   Radio buttons indicate that it's a single-choice question.
*   One radio button is filled in, indicating the selected answer.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/6](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/6)
---
Dear Sirs, Can we have some response on these issues related particularly to the questions 1 and 2 of Graded Assignment 6. It looks like multiple options are correct in the given options. Any guidance or hint, on how to arrive at the right answer will be helpful. Thanks and regards. @carlton @Jivraj @Saransh\_Saini

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/7](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/7)
---
Yeah…Even I am facing the same issue. Out of the 4 options provided, 3 options are correct in my case both for Q1 & Q2, but both these questions are single-choice questions. Kindly look into it and help us out @carlton !

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/8](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/8)
---
I guess for both Q1 & Q2, we need to find the option that is having stronger correlation (positive/negative). Please correct me if I am wrong.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/9](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/9)
---
Any updates on these? I am too facing the same issue.

@carlton @Jivraj @Saransh\_Saini

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/10](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/10)
---
In GA6 for first 2 questions 3 out of 4 options are correct. Even the question is not clearly asking anything. Kindly suggest are we supposed to select the wrong one  

image2083×575 47.6 KB
Here's a breakdown of the image content:

**Content:**

The image presents a multiple-choice question related to motorcycle resale value analysis.

**Text:**

*   **Question Prompt:** It describes a scenario where the user is a strategic consultant for a premium motorcycle dealership chain. The objective is to analyze factors influencing motorcycle resale value in Maharashtra. Specifically, the task involves evaluating the impact of mileage (km/l), average daily distance traveled, and engine capacity on price retention (%) for Yamaha motorcycles. Pearson Correlation Coefficient is used, and price retention is defined as (resale price / original price).
*   **Answer Options:** The image provides four answer choices, each representing the Pearson correlation coefficient for a different factor:
    *   'AvgDistance: 0.09'
    *   'Mileage: 0.95'
    *   'EngineCapacity: -0.02'
    *   'Mileage: 0.12'
    
**Other Features:**

*   A checkbox is selected for the "Mileage: 0.95" option.
*   The question is worth 1 point.

**In essence, the image shows a question testing understanding of how different factors might correlate with motorcycle resale value.**
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/11](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/11)
---
Kindly update us regarding the status of Q1 & Q2 @carlton @Jivraj

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/12](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/12)
---
@Jivraj @carlton @Saransh\_Saini  
Dear TDS Team,

There are multiple issues in Graded Assignment 6 that require urgent attention:

1. Questions 1 and 2, along with their options, are ambiguous.
2. In Questions 3 and 4, I am unable to obtain an exact answer that matches any of the given options, despite trying multiple approaches, including the Excel regression method and other models in a Google Colab file.
3. The data for Question 10 is missing. I attempted to run the shapefile in QGIS, but it resulted in an error. Additionally, I searched for the shapefile of New York roads on official websites, but their servers are currently under maintenance.

The assignment deadline is approaching, but these issues remain unresolved. Kindly look into this matter at the earliest and provide a resolution as soon as possible.

Thank you for your support.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/13](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/13)
---
Yes, there are no specifics in Q1 to Q4 and are quite ambiguous.

For instance:

> forecast the 2027 resale value of the Hero - HF Deluxe in Gujarat, using historical data.

but is this talking about the average resale value as no input features are specified?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/14](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/14)
---
Let’s wait for their response.  
I submitted nearby option for Q3 and Q4

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/15](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/15)
---
@Jivraj @carlton @Saransh\_Saini  
Can you please provide any update ASAP as the deadline for this GA coincides with Quiz 2. With many ambiguities unresolved it’s hard to solve this and study for Quiz 2 (and do offline college work even though that’s not your problem).  
Thanks

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/16](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/16)
---
Hi @all

Question intends you to select most correlated one.  
Select option which is absolute highest.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/17](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/17)
---
@Jivraj - Can you please check answer choices for Q7 for GA6 where no choices are matching with the answer. The answer is coming to around 11.5 kms which is 11500 meters.  
Q.A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Pine Pines Junction : (26.5596,-99.5336) ;Maple Fields Station : (26.4212,-99.4597);South Glen Crossing : (26.5962,-99.5243);Cedar Creek Retreat : (26.56,-99.4519) & Central Command Post Location: (26.4644,-99.4771) Using the Haversine package, calculate the distance from the Central Command Post to Pine Pines Junction. Which of the following is the MOST ACCURATE distance

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/18](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/18)
---
image1318×377 34.2 KB

  
what to do if 3 options have same value -0.04 and all are correct?
Here's a detailed description of the image content:

The image presents a multiple-choice question related to analyzing factors influencing motorcycle resale value.

**Text:**

*   The question text states that the user is a strategic consultant for a premium motorcycle dealership chain in Maharashtra. The objective is to analyze key factors affecting motorcycle resale value.
*   The analysis specifically focuses on the impact of mileage (km/l), average daily distance traveled, and engine capacity on price retention (%) for Honda motorcycles.
*   The method to be used is the Pearson Correlation Coefficient. Price retention is defined as (resale price / original price).
*   Four answer options are provided, each presenting a different factor (AvgDistance, EngineCapacity, Mileage) and a correlation coefficient value:
    *   'AvgDistance: -0.04'
    *   'AvgDistance: 0.95'
    *   'EngineCapacity: -0.04'
    *   'Mileage: -0.04'

**Objects and Features:**

*   The image shows a typical multiple-choice question format with radio buttons next to each answer option.
*   The fourth option ('Mileage: -0.04') is currently selected, indicated by the filled radio button.
*   There's a label "1 point" next to the question number, suggesting this is part of a quiz or assessment.

In essence, the image depicts a question asking the user to evaluate the correlation between different motorcycle attributes and price retention, focusing on Honda models in Maharashtra. The user has selected 'Mileage: -0.04' as the answer.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/19](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/19)
---
@carlton @Jivraj  
My question 7 for GA6 is :  
A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Silver Springs Community : (42.1029,-85.665) ;Pleasant Harbor Community : (42.1238,-85.9043);Summit Shores Village : (42.0415,-85.8696);River Retreat Outpost : (42.0417,-85.6836) & Central Command Post Location: (42.0587,-85.7226) Using the Haversine package, calculate the distance from the Central Command Post to Silver Springs Community. Which of the following is the MOST ACCURATE distance  
Whose options provided are :  
10418 meters

12287 meters

10965 meters

11149 meters

However, after trying all methods out there my distance comes out to be 6873 meters, I selected 10418 as the answer (closest approximation to 6873 meters)

I assume that the question must have been central command post to summit shores village (whose answer turns out to be 12287 meters)  
Kindly look into the question, and let me know about the same (the destination from central command post)

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/20](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/20)
---
Please post any questions related to Graded Assignment 6 - Data Analysis

Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.

Deadline 2025-03-15T18:30:00Z

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/1](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/1)
---


Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/2](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/2)
---
The answer choices for questions 1 and 2 in graded assignment 6 are quite confusing. Both questions are single-select, yet three out of the four options are correct in each case. I’m unsure whether to choose one of the correct options or if the question is actually asking for the incorrect one. Could someone please clarify?

@carlton

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/3](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/3)
---
@Jivraj @Saransh\_Saini  
I have similar concern  
For Q1, I used the following code:

```
print(f'Pearson correlation for Karnataka between price retention and column')
kk = df[df['State'] == 'Karnataka']
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = kk['price_retention'].corr(kk[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')

```

And got the following output:

```
Pearson correlation for Karnataka between price retention and column
	Mileage (km/l)            : 0.03
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.04

```

Whereas options are below where none of them are correct.  

image281×219 9.1 KB

Whereas for Q2 (Punjab and Yamaha) I used the following code:

```
print(f'Pearson correlation for Punjab and Yamaha between price retention and column')
pb = df[(df['State'] == 'Punjab') & (df['Brand'] == 'Yamaha')]
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = pb['price_retention'].corr(pb[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')

```

and got the following answers:

```
Pearson correlation for Punjab and Yamaha between price retention and column
	Mileage (km/l)            : 0.24
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.08

```

The options for Q2 are given below and 2 of them are correct (AvgDistance and Mileage).  

image278×216 9.19 KB
Here's a detailed description of the image:

**Overall Structure:**

The image shows a multiple-choice style selection presented in a vertical list.  Each choice consists of a radio button and a text label.

**Content of Each Choice:**

1.  **Choice 1:**
    *   Radio Button: Unselected (empty circle).
    *   Text Label: 'Mileage: 0.95'

2.  **Choice 2:**
    *   Radio Button: Selected (filled blue circle).
    *   Text Label: 'AvgDistance: -0.05'

3.  **Choice 3:**
    *   Radio Button: Unselected (empty circle).
    *   Text Label: 'Mileage: 0.21'

4.  **Choice 4:**
    *   Radio Button: Unselected (empty circle).
    *   Text Label: 'EngineCapacity: 0.17'

**Key Observations:**

*   One choice ('AvgDistance: -0.05') is currently selected.
*   The labels appear to represent some kind of measurement or feature ('Mileage', 'AvgDistance', 'EngineCapacity') paired with a numerical value.
*   The labels are strings with single quotes surrounding them.
 Here's a detailed description of the image's content:

**Overall Layout:**

The image shows a snippet of a user interface, likely from a web page or application. It presents a list of radio button options, each associated with a string value.

**Text Content and Radio Buttons:**

*   **Radio Button 1:**
    *   The text label associated with the first radio button is `'Mileage: 0.95'`.
    *   The radio button itself is not selected.

*   **Radio Button 2:**
    *   The text label associated with the second radio button is `'AvgDistance: -0.06'`.
    *   The radio button itself is not selected.

*   **Radio Button 3:**
    *   The text label associated with the third radio button is `'Mileage: 0.24'`.
    *   The radio button is selected (filled with a blue circle).

*   **Radio Button 4:**
    *   The text label associated with the fourth radio button is `'EngineCapacity: -0.08'`.
    *   The radio button itself is not selected.

**Inference:**

Based on the text, it seems like the options represent different features or variables, possibly related to vehicle attributes or performance metrics. The user has selected the option associated with "Mileage: 0.24". The use of single quotes around the values suggests they are being treated as strings.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/4](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/4)
---
@24f2006061 We are looking into it. We will update based on our analysis. Thanks for letting us know.

Kind regards

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/5](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/5)
---
I used a python script to get the solution to quesiton 1 of week 6 graded assignment. It matches three options. Is this a bug or like we then need to analyze using the pearson coefficient to determine which option is the correct one  

image1383×263 25 KB
The image is a screenshot of a multiple-choice question. The question reads: "As a strategic consultant for a premium motorcycle dealership chain, your objective is to analyze the key factors influencing motorcycle resale value in Delhi. Specifically, you will evaluate the impact of mileage (km/l), average daily distance traveled, and engine capacity on price retention (%) for Yamaha. Use Pearson Correlation Coefficient and price retention is (resale price/original price)."

The multiple-choice options are:
*   'Mileage: 0.01'
*   'AvgDistance: 0.00'
*   'EngineCapacity: 0.13'
*   'EngineCapacity: 0.95'

The third option, 'EngineCapacity: 0.13', is selected. The question is worth 1 point.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/6](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/6)
---
Dear Sirs, Can we have some response on these issues related particularly to the questions 1 and 2 of Graded Assignment 6. It looks like multiple options are correct in the given options. Any guidance or hint, on how to arrive at the right answer will be helpful. Thanks and regards. @carlton @Jivraj @Saransh\_Saini

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/7](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/7)
---
Yeah…Even I am facing the same issue. Out of the 4 options provided, 3 options are correct in my case both for Q1 & Q2, but both these questions are single-choice questions. Kindly look into it and help us out @carlton !

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/8](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/8)
---
I guess for both Q1 & Q2, we need to find the option that is having stronger correlation (positive/negative). Please correct me if I am wrong.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/9](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/9)
---
Any updates on these? I am too facing the same issue.

@carlton @Jivraj @Saransh\_Saini

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/10](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/10)
---
In GA6 for first 2 questions 3 out of 4 options are correct. Even the question is not clearly asking anything. Kindly suggest are we supposed to select the wrong one  

image2083×575 47.6 KB
Here's a breakdown of the image content:

**Overall:**

The image shows a multiple-choice question related to data analysis and motorcycle resale value. It presents a scenario where you are a strategic consultant tasked with analyzing factors influencing motorcycle resale value in Maharashtra. The question focuses on the impact of mileage, average daily distance traveled, and engine capacity on price retention for Yamaha motorcycles. You are told to use Pearson Correlation Coefficient and price retention (resale price / original price).

**Key Text/Information:**

*   **Scenario:** Strategic consultant analyzing motorcycle resale value in Maharashtra.
*   **Factors to Evaluate:** Mileage (km/l), average daily distance traveled, and engine capacity.
*   **Target:** Price retention (%) for Yamaha.
*   **Method:** Pearson Correlation Coefficient.
*   **Price Retention Definition:** Resale price / original price.
*   **Answer Options:**
    *   'AvgDistance: 0.09'
    *   'Mileage: 0.95' (This option is currently selected)
    *   'EngineCapacity: -0.02'
    *   'Mileage: 0.12'

**Structure:**

*   The question is numbered "1)" and is worth "1 point".
*   The answer options are presented as bullet points, each preceded by a radio button.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/11](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/11)
---
Kindly update us regarding the status of Q1 & Q2 @carlton @Jivraj

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/12](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/12)
---
@Jivraj @carlton @Saransh\_Saini  
Dear TDS Team,

There are multiple issues in Graded Assignment 6 that require urgent attention:

1. Questions 1 and 2, along with their options, are ambiguous.
2. In Questions 3 and 4, I am unable to obtain an exact answer that matches any of the given options, despite trying multiple approaches, including the Excel regression method and other models in a Google Colab file.
3. The data for Question 10 is missing. I attempted to run the shapefile in QGIS, but it resulted in an error. Additionally, I searched for the shapefile of New York roads on official websites, but their servers are currently under maintenance.

The assignment deadline is approaching, but these issues remain unresolved. Kindly look into this matter at the earliest and provide a resolution as soon as possible.

Thank you for your support.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/13](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/13)
---
Yes, there are no specifics in Q1 to Q4 and are quite ambiguous.

For instance:

> forecast the 2027 resale value of the Hero - HF Deluxe in Gujarat, using historical data.

but is this talking about the average resale value as no input features are specified?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/14](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/14)
---
Let’s wait for their response.  
I submitted nearby option for Q3 and Q4

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/15](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/15)
---
@Jivraj @carlton @Saransh\_Saini  
Can you please provide any update ASAP as the deadline for this GA coincides with Quiz 2. With many ambiguities unresolved it’s hard to solve this and study for Quiz 2 (and do offline college work even though that’s not your problem).  
Thanks

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/16](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/16)
---
Hi @all

Question intends you to select most correlated one.  
Select option which is absolute highest.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/17](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/17)
---
@Jivraj - Can you please check answer choices for Q7 for GA6 where no choices are matching with the answer. The answer is coming to around 11.5 kms which is 11500 meters.  
Q.A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Pine Pines Junction : (26.5596,-99.5336) ;Maple Fields Station : (26.4212,-99.4597);South Glen Crossing : (26.5962,-99.5243);Cedar Creek Retreat : (26.56,-99.4519) & Central Command Post Location: (26.4644,-99.4771) Using the Haversine package, calculate the distance from the Central Command Post to Pine Pines Junction. Which of the following is the MOST ACCURATE distance

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/18](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/18)
---
image1318×377 34.2 KB

  
what to do if 3 options have same value -0.04 and all are correct?
Here's a detailed description of the image:

**Content:**

The image displays a multiple-choice question, likely from an online quiz or assessment. The question pertains to analyzing factors influencing motorcycle resale value, specifically for Honda motorcycles in Maharashtra, India.

**Text:**

*   **Question:** "As a strategic consultant for a premium motorcycle dealership chain, your objective is to analyze the key factors influencing motorcycle resale value in Maharashtra. Specifically, you will evaluate the impact of mileage (km/l), average daily distance traveled, and engine capacity on price retention (%) for Honda. Use Pearson Correlation Coefficient and price retention is (resale price / original price)."
*   **Possible Answers:**
    *   'AvgDistance: -0.04'
    *   'AvgDistance: 0.95'
    *   'EngineCapacity: -0.04'
    *   'Mileage: -0.04'
*   **Additional Text:** "1 point" (likely indicates the point value of the question).

**Visual Features:**

*   The question and answer choices are presented in a typical multiple-choice format.
*   One of the answer choices ('Mileage: -0.04') is selected, indicated by a filled-in radio button.

**Inference:**

The question is testing the understanding of how different motorcycle attributes (mileage, average distance, engine capacity) correlate with price retention (resale value compared to original price), using the Pearson Correlation Coefficient. The student needs to choose the option that correctly reflects the correlation between the given attribute and price retention.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/19](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/19)
---
@carlton @Jivraj  
My question 7 for GA6 is :  
A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Silver Springs Community : (42.1029,-85.665) ;Pleasant Harbor Community : (42.1238,-85.9043);Summit Shores Village : (42.0415,-85.8696);River Retreat Outpost : (42.0417,-85.6836) & Central Command Post Location: (42.0587,-85.7226) Using the Haversine package, calculate the distance from the Central Command Post to Silver Springs Community. Which of the following is the MOST ACCURATE distance  
Whose options provided are :  
10418 meters

12287 meters

10965 meters

11149 meters

However, after trying all methods out there my distance comes out to be 6873 meters, I selected 10418 as the answer (closest approximation to 6873 meters)

I assume that the question must have been central command post to summit shores village (whose answer turns out to be 12287 meters)  
Kindly look into the question, and let me know about the same (the destination from central command post)

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/20](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/20)
---
Have you succeeded in running the shape file for Q10? It seems to have some error.

@lakshaygarg654

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/21](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/21)
---
No,  
I use google to get MTFCC code for given road segment and after that mtfcc pdf to classify that road segment.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/22](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/22)
---
I downloaded the complete shape file zip from the census.gov site.  
Here is the link: https://www2.census.gov/geo/tiger/TIGER2024/PRISECROADS/tl\_2024\_36\_prisecroads.zip

It works fine in QGIS.  
@lakshaygarg654

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/23](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/23)
---
they have not provide all the files needed to read that shp file in the question .  
but your link includes them. thanks…

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/24](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/24)
---
I tried to access shapefile from official website 4-5 days ago, but server was under maintenance. I will check again Q10 after quiz 2.  
Thanks for sharing.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/25](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/25)
---
My question 9 for GA6 is :  
@carlton @Jivraj @Saransh\_Saini  

Screenshot 2025-03-15 205444878×668 38.1 KB

  

Screenshot 2025-03-15 2054561333×366 45.8 KB

I solved it in colab but options are getting mismatched there…kindly clarify this issue..
Here's a detailed description of the image, focusing on the code, text, and overall content:

**Overall Structure:**

The image appears to be a screenshot of a Python code snippet along with its output. The code calculates the distances between several locations and a central command post, sorts these locations by distance, and then prints an evacuation sequence based on distance.

**Code Breakdown:**

1.  **Import:**

    ```python
    from haversine import haversine
    ```

    This line imports the `haversine` function, likely from a library of the same name. This function calculates the great-circle distance between two points on a sphere given their longitudes and latitudes.

2.  **Coordinate Definitions:**

    ```python
    OakParkTown = (27.0096, -72.3822)
    EastSpringsSettlement = (27.0769, -72.394)
    EastFieldsJunction = (27.0961, -72.4248)
    RedPointTown = (26.9874, -72.426)
    CentralCommandPostLocation = (27.0552, -72.4893)
    ```

    This section defines the latitude and longitude coordinates for several communities (OakParkTown, EastSpringsSettlement, EastFieldsJunction, RedPointTown) and a central command post. Each location is represented as a tuple of (latitude, longitude).

3.  **Distance Calculation:**

    ```python
    distances = {
        "OakParkTown": haversine(OakParkTown, CentralCommandPostLocation),
        "EastSpringsSettlement": haversine(EastSpringsSettlement, CentralCommandPostLocation),
        "EastFieldsJunction": haversine(EastFieldsJunction, CentralCommandPostLocation),
        "RedPointTown": haversine(RedPointTown, CentralCommandPostLocation)
    }
    ```

    This creates a dictionary called `distances`.  The keys of this dictionary are the names of the communities, and the values are the distances calculated using the `haversine` function between each community and the `CentralCommandPostLocation`.

4.  **Sorting:**

    ```python
    optimal_sequence = sorted(distances, key=distances.get)
    ```

    This line sorts the communities based on their distances to the central command post.  `sorted()` function is used on the keys of the distances dictionary. The `key=distances.get` argument specifies that the sorting should be based on the values (distances) in the `distances` dictionary. `optimal_sequence` becomes a list of community names, sorted by distance from the central command post.

5.  **Output:**

    ```python
    for i, community in enumerate(optimal_sequence, start=1):
        print(f"{i}. {community} - Distance: {distances[community]:.2f} km")
    ```

    This loop iterates through the sorted `optimal_sequence` list. `enumerate` provides both the index (`i`, starting from 1) and the community name. It then prints the index, community name, and the distance from the `distances` dictionary, formatted to two decimal places, along with "km".

**Output Interpretation:**

The output at the bottom shows the evacuation sequence:

1.  EastFieldsJunction - Distance: 7.84 km
2.  EastSpringsSettlement - Distance: 9.74 km
3.  RedPointTown - Distance: 9.81 km
4.  OakParkTown - Distance: 11.76 km

This indicates that EastFieldsJunction is closest to the central command post, followed by EastSpringsSettlement, then RedPointTown, and finally OakParkTown, which is the farthest.

**Overall Purpose:**

The code simulates a scenario where communities need to be evacuated to a central command post based on their distance. The code calculates these distances, sorts the communities, and presents the evacuation order.
 Here's a breakdown of the image content:

**Overall Image Content:**

The image shows a multiple-choice question from what appears to be a test or assignment, specifically related to emergency evacuation planning.  The question presents a scenario with four communities and a central command post, providing their geographic coordinates. The task is to determine the optimal evacuation sequence based on the "nearest community first" strategy.

**Key Text and Numerical Information:**

*   **Question Text:**  The question describes a scenario where four communities need to be evacuated, using the "nearest community first" strategy. The goal is to determine the optimal sequence.
*   **Community Names and Coordinates:**
    *   Oak Park Town: (27.0096, -72.3822)
    *   East Springs Settlement: (27.0769, -72.394)
    *   East Fields Junction: (27.0961, -72.4248)
    *   Red Point Town: (26.9874, -72.426)
    *   Central Command Post Location (Start/End): (27.0552, -72.4893)
*   **Multiple Choice Options:** The image presents four options for the evacuation sequence, starting and ending at the "Start/End" location (Central Command Post).

**Visual Elements**

*   **Selected Answer:** The first option is selected. This suggests someone has already attempted to answer the question.
*   **Code Snippet:** It contains code which looks like the definition of the communities coordinates. This indicates that Haversine distance is intended to be used to determine the distances

**In summary, the image is a problem regarding optimal evacuation using the closest point strategy, with four sequences as options.**
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/26](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/26)
---
for the above question the options are None of these are matching and answer is around 11.5 kms  
3848 meters  
6265 meters  
4110 meters  
5106 meters

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/28](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/28)
---
For 7th Question in GA6 I got the answer 14265.93 Meters but the option I have in 7th are  
6069 meters  
7687 meters  
6106 meters  
7035 meters  
@carlton @Jivraj

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/29](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/29)
---
@carlton @Jivraj @Saransh\_Saini

for question 4, i have tried `=forecast` and also `=forecast.ets`, both of them are not working. There are two columns for years. One is year of manufacturing, another is year of registration. which one to take.

for question 7, none of the options match. I am selecting the `MOST ACCURATE` among the given options. Hope, it is correct

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/30](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/30)
---
Can anyone help me out on how to approach and solve the 10th question please!?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/31](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/31)
---
Check the distances of other locations from the central location. One student found **Question 7** of the **GA6 Option Set** based on the distances of other points, which do not match the requirements of Question 7.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/32](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/32)
---
i have the same issue

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/33](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/33)
---
yes i have the same issue  
and i got the same answer and am give the same options  
@carlton sir what to do?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/34](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/34)
---
@Jivraj @Saransh\_Saini  
For 7th Question in GA6 I got the answer 14265.9275 Meters but the option I have in 7th are  
6069 meters  
7687 meters  
6106 meters  
7035 meters

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/35](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/35)
---
Hello Sir,

Can you please check if this is the right answer. As per email received from @carlton sir we should select the absolute maximum value.  

image978×393 23.3 KB

Example : If we get answers as -0.3 and 0.2 then -0.3 is the right answer as it’s absolut value is maximum.

For the first question the correlation matrix is as follows,  

image748×431 17.5 KB

So shouldn’t it be -0.13?
Here's a breakdown of the image content:

**Context:**

*   The image is a multiple-choice question from some kind of online quiz or assessment.
*   The question is geared towards a strategic consultant for a motorcycle dealership.
*   The core task is to identify key factors influencing the resale value of Royal Enfield motorcycles in Uttar Pradesh.

**Question Details:**

*   **Goal:** Analyze the impact of mileage, average daily distance, and engine capacity on price retention.
*   **Method:** Use Pearson Correlation Coefficient.
*   **Formula for price retention:** resale price / original price.

**Answer Choices:**

*   'Mileage: 0.01'
*   'EngineCapacity: 0.95'
*   'AvgDistance: -0.13'
*   'EngineCapacity: 0.09'

**Feedback:**

*   The attempted answer ('AvgDistance: -0.13') was incorrect.
*   The correct answer is 'EngineCapacity: 0.09'.

**In essence, the image presents a business-related question requiring knowledge of correlation analysis and factors influencing motorcycle resale value.**
 Here is a detailed description of the image:

The image displays a correlation matrix visualized as a heatmap. The rows and columns represent four variables: "Mileage (km/l)", "Avg Daily Distance (km)", "Engine Capacity (cc)", and "Price Retention (%)". The matrix elements display the correlation coefficients between each pair of variables.

*   **Mileage (km/l)** has a correlation of 0.01 with Engine Capacity (cc) and Price Retention (%).
*   **Avg Daily Distance (km)** has a correlation of 0.04 with Engine Capacity (cc) and -0.13 with Price Retention (%).
*   **Engine Capacity (cc)** has a correlation of 0.09 with Price Retention (%).

The diagonal elements, representing the correlation of each variable with itself, are filled with the value 1.00 and are shown in red, indicating a perfect positive correlation.

The color scheme of the heatmap uses a gradient from blue to white to red. Blue indicates negative correlation, white indicates no correlation, and red indicates positive correlation. The intensity of the color reflects the strength of the correlation.

The numerical values (correlation coefficients) are displayed within each cell of the matrix.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/36](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/36)
---
Thanks for the colour picture.  
If you read the aforementioned email…  

Screenshot 2025-03-17 at 9.09.55 am1760×632 65.4 KB

Kind regards (in colour )
Here is a detailed description of the image content:

**Overall:** The image is a screenshot of an email. The email is titled "[TDS Jan 25] GA 6 Clarification" and appears to be an announcement or clarification from an educational institution.

**Key Elements:**

*   **Email Header:** The header shows the title of the email "[TDS Jan 25] GA 6 Clarification". There is also an "Inbox" tag followed by an "x" suggesting it's an open email in an inbox.
*   **Sender Information:** The sender's email address is "donot\_reply@study.iitm.ac.in." The email is addressed to "25t1\_se2002-announce." There is a profile image of a "d" inside of a circle.
*   **Email Body:**
    *   Salutation: "Dear Learner,"
    *   Content: The email clarifies an issue with "GA6 Question 1 and 2," indicating that the questions were unclear. It emphasizes that the correct answer is based on the "Absolute Maximum Correlation Coefficient."
    *   Example: An example is given to illustrate this. If options are -0.3 and 0.2, then -0.3 is the correct answer.
    *   Important Note: The email includes a disclaimer: "Do not worry if the portal marks you as being incorrect. We will still push the right scores on the dashboard if you chose the correct option." This indicates that there might be an error in the automated grading system, but the correct scores will be manually applied.
    *   Closing: "Kind regards"

*   **Visual Annotations:** There's a red arrow pointing to the disclaimer regarding potential incorrect marking by the portal. This highlight emphasizes the importance of that statement. There is also yellow highlighting around the email title.

**Content interpretation**

The email serves as a clarification for students regarding a specific assignment (GA6). It addresses a possible issue with the grading system and assures students that their scores will be corrected manually if they chose the right option, despite any errors in the automated grading. It highlights the importance of understanding the "Absolute Maximum Correlation Coefficient" for this assignment.
 Here's a detailed description of the image:

**Content:**

The image is a digital representation of a winking face emoji.

**Features:**

*   **Shape:** The emoji has a round, circular shape representing a face.
*   **Color:** The face is yellow.
*   **Facial Features:**
    *   **Eyes:** One eye is open and round, with a dark brown or black pupil. The other eye is closed in a wink.
    *   **Eyebrow:** One eyebrow (above the open eye) is visible, slightly curved upward.
    *   **Mouth:** The mouth is curved upwards into a smile. The inside of the mouth is dark brown or black.

**Overall Impression:** The emoji conveys a sense of playfulness, teasing, or suggestion.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/37](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/37)
---
Thank you sir. i have got questions 1 and 2 both marked as 0.  

image962×459 29.1 KB

In my case Please note the above two questions are asked to calculate pearson correlation coefficient for KTM brand and for maharashtra and Karnataka states.  
I have used excel to calculate the pearson correlation coefficient. Below the values I got for each question. Please verify.

|pearson correlation coefficient between impact of Mileage and Price retention for kTM brand for Karnataka||  
-0.026685695

|pearson correlation coefficient between average distance travelled and Price retention for kTM for karnataka||  
0.003953219

|pearson correlation coefficient between average Engine capacity and Price retention for kTM for karnataka||  
-0.010839295

|pearson correlation coefficient between impact of Mileage and Price retention for kTM brand for maharashta||  
0.029128825

|pearson correlation coefficient between average distance travelled and Price retention for kTM for Maharashtra||  
0.013019585

|pearson correlation coefficient between average Engine capacity and Price retention for kTM for Maharashtra||  
-0.056866212
Here is a detailed description of the image content:

The image is a screenshot of a multiple-choice question from an online assessment. The question focuses on analyzing factors influencing motorcycle resale value in Maharashtra, specifically for KTM motorcycles. The question asks the user to evaluate the impact of mileage (km/l), average daily distance traveled, and engine capacity on price retention (resale price / original price) using the Pearson Correlation Coefficient.

The options provided are:

*   'AvgDistance: 0.01'
*   'Mileage: 0.03'
*   'EngineCapacity: -0.06'
*   'Mileage: 0.95'

The response "No, the answer is incorrect" is displayed, along with a score of 0. The accepted answer is given as 'Mileage: 0.03'. This suggests that the question aims to test the user's understanding of the correlation between mileage and price retention, and the correct correlation coefficient value.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/38](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/38)
---
@Jivraj @carlton  
Dear sirs,  
I have question no 7 got marked as 0. Please check the question below and the haversine distance for the given post comes to around 11.5 kms which is not matccing with any of the options and I have selected the closest answer. please check and let me know.  

image935×529 40.1 KB
Here's a breakdown of the image's content to help answer questions:

**Overall Content:**

The image is a screenshot of a multiple-choice question related to emergency management and calculating distance.  It appears to be from an online quiz or test.

**Textual Elements:**

*   **Question Prompt:** A wildfire threatens a rural region. The question requires using the Haversine package to calculate the distance between a Central Command Post and Pine Pines Junction.
*   **Location Coordinates:** The coordinates (latitude and longitude) are provided for the Central Command Post, Pine Pines Junction, Maple Fields Station, South Glen Crossing, and Cedar Creek Retreat.
*   **Multiple Choice Options:** The image provides four possible distance values (in meters):
    *   3848 meters
    *   6265 meters
    *   4110 meters
    *   5106 meters
*   **Feedback:** Shows the user's previous answer was incorrect.
*   **Score:** The user has a score of 0.
*   **Accepted Answer:** The accepted answer is listed as 5106 meters.

**Numerical Elements (Coordinates):**

*   **Pine Pines Junction:** (26.5596, -99.5336)
*   **Maple Fields Station:** (26.4212, -99.4597)
*   **South Glen Crossing:** (26.5962, -99.5243)
*   **Cedar Creek Retreat:** (26.56, -99.4519)
*   **Central Command Post:** (26.4644, -99.4771)

**Key Features:**

*   The question specifically mentions using the "Haversine package" which is a method/library often used to calculate the distance between two points on a sphere (like the Earth) given their latitudes and longitudes.
*   The question is about finding the *most accurate* distance, implying that the Haversine calculation needs to be performed to find the correct answer.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/39](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/39)
---
@carlton @Jivraj  
I did raise the question 2 days before the GA6 Deadline and doing so again after being marked as incorrect

My question 7 was A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Silver Springs Community : (42.1029,-85.665) ;Pleasant Harbor Community : (42.1238,-85.9043);Summit Shores Village : (42.0415,-85.8696);River Retreat Outpost : (42.0417,-85.6836) & Central Command Post Location: (42.0587,-85.7226) Using the Haversine package, calculate the distance from the Central Command Post to Silver Springs Community. Which of the following is the MOST ACCURATE distance

10418 meters

12287 meters

10965 meters

11149 meters

Whose right answer turned out 6873, however the answer pushed is 12287 meters, which is nowhere near the closest options (it would’ve been correct if the destination was summit shores village which isn’t the case with this question)

Also, my question 4 was :  
As an investment analyst monitoring motorcycle resale values, develop a forecasting model to predict future resale prices by brand and segment, considering seasonality and long-term trends. Specifically, forecast the 2027 resale value of the Kawasaki - Ninja 300 in Tamil Nadu, using historical data.

134483

94774

150666

199711

Whose correct option (through different methods and algorithms) was approximately closest to 94774 and again answer pushed is 150666 which again turns out to be incorrect

So is the case with questions 1 and 2 (where answers aren’t pushed according to absolute values, but as conveyed earlier, I believe this shall be resolved)

Kindly look into it

Thanks and Regards

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/40](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/40)
---
@carlton @Jivraj @Saransh\_Saini  
In Q4 , neither which regression model to use is given nor the what random state to use is given. I tried linear regression, random forest regression but it is giving answer which vary each time I compute, also, the option values are quite close.

image1227×446 24 KB
Here's a breakdown of the image content, focusing on relevant details:

**Overall:**

*   The image is a multiple-choice question from a test or quiz.
*   The question focuses on forecasting motorcycle resale values.

**Text:**

*   **Question:** As an investment analyst monitoring motorcycle resale values, develop a forecasting model to predict future resale prices by brand and segment, considering seasonality and long-term trends. Specifically, forecast the 2027 resale value of the Hero - HF Deluxe in Punjab, using historical data.
*   **Answer Choices:** The answer choices are numerical values, representing possible forecasted resale prices:
    *   194515
    *   185108
    *   142646 (selected)
    *   152609
*   **Feedback:** "No, the answer is incorrect." This indicates the selected answer (142646) is wrong.
*   **Score:** "Score: 0" This shows the current score is 0.

**Relevant Features:**

*   The question explicitly mentions "Hero - HF Deluxe" as the motorcycle model and "Punjab" as the location, defining the specific scenario for the forecast.
*   The question emphasizes the need to consider "seasonality and long-term trends" when developing the forecasting model.

In essence, the image presents a forecasting problem related to motorcycle resale values, provides multiple answer choices, and indicates that a specific answer was selected but is incorrect.
Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/41](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/41)
---
@all  
we are looking into problems with question 4, 6 and 10.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/43](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/43)
---
Hi,

Have the corrections been done on GA6 marks?

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/44](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/44)
---
Yes, corrections have been done in Ga6 marks.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/45](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/45)
---
Just to confirm, were the answers shown on the portal correct because I’m getting the same score as shown in the portal.

Post URL: [https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/46](https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/46)
---
