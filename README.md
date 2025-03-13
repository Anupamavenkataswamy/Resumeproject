Project Report: Automated Resume Screening System
1. Project Name: Automated Resume Screening System
2. Introduction: The Automated Resume Screening System is a web-based application that enables recruiters to efficiently screen multiple resumes and match them with a given job description (JD). It uses Natural Language Processing (NLP) techniques, particularly TF-IDF vectorization and cosine similarity, to compare resumes against job descriptions and rank them based on relevance. Additionally, the system extracts candidate details such as name, email, and contact number to provide structured and actionable insights for recruiters.
3. Objectives:
•	To automate the process of resume screening.
•	To rank resumes based on their match percentage with the job description.
•	To extract key candidate details (Name, Email, and Contact Number).
•	To provide a user-friendly web interface for easy file upload and results display.
•	To allow recruiters to view resumes directly without downloading.
4. Tools and Technologies Used:
•	Programming Language: Python
•	Web Framework: Flask
•	Frontend Technologies: HTML, CSS, JavaScript
•	Machine Learning Library: Scikit-learn (TF-IDF Vectorization, Cosine Similarity)
•	PDF and DOCX Processing: pdfminer, python-docx
•	Version Control: Git & GitHub
•	Development Environment: Visual Studio Code (VS Code)
5. System Architecture: The system follows a simple client-server architecture where:
•	Users (recruiters) upload resumes and enter the job description via the web interface.
•	The backend processes the resumes, extracts relevant text, and computes similarity scores using NLP techniques.
•	The results are then sorted based on match percentage and displayed in a structured format.
•	The recruiter can click to view a resume directly without downloading it.
6. Key Features:
•	Multiple Resume Uploads: Users can upload multiple resumes in PDF or DOCX format.
•	Text Extraction: Extracts text from resumes using pdfminer and python-docx.
•	Matching Algorithm: Uses TF-IDF vectorization and cosine similarity to compare resumes with job descriptions.
•	Candidate Information Extraction: Extracts name, email, and contact number using regex.
•	Ranked Results: Displays resumes in descending order of match percentage.
•	Resume Viewing: Allows recruiters to view resumes directly on the web interface without downloading.
•	User-Friendly Interface: Simple and interactive UI built using HTML, CSS, and JavaScript.
7. Implementation Details:
•	Frontend: The web interface is built using HTML, CSS, and JavaScript for form submission and displaying results.
•	Backend: Flask framework handles HTTP requests, processes resumes, and computes similarity scores.
•	Text Processing: Extracts text from PDF and DOCX files using pdfminer and python-docx.
•	Machine Learning Model: Uses TF-IDF and cosine similarity from scikit-learn to calculate match percentages.
•	Sorting Mechanism: The computed match scores are sorted in descending order to rank resumes.
•	Resume Viewing: Resumes are displayed within the web interface using an embedded viewer.
8. Workflow:
1.	The recruiter visits the web application.
2.	Uploads multiple resumes in PDF/DOCX format.
3.	Enters the job description in a text box.
4.	Clicks the "Upload & Match" button.
5.	The system extracts text from resumes and calculates similarity scores.
6.	Resumes are ranked and displayed along with candidate details.
7.	Recruiters can click to view resumes directly.
9. Advantages:
•	Saves time and effort in manual resume screening.
•	Provides structured and ranked results for better decision-making.
•	Eliminates bias by focusing on skill matching.
•	Enhances the recruitment process efficiency.
10. Future Enhancements:
•	Integrating with an Applicant Tracking System (ATS) for seamless workflow.
•	Adding support for additional file formats like TXT and RTF.
•	Implementing advanced NLP techniques such as Named Entity Recognition (NER) for better information extraction.
•	Introducing AI-powered suggestions for recruiters based on candidate profiles.
•	Deploying the application on cloud platforms like AWS or Heroku for scalability.

11. Conclusion: The Automated Resume Screening System provides an efficient and intelligent approach to resume screening. By leveraging NLP techniques and a user-friendly interface, the system significantly reduces the time taken for recruiters to find suitable candidates. Future enhancements will further improve its capabilities, making it a valuable tool in the recruitment process.
________________________________________
