# Syllabus-Analyzer
📘 Syllabus Tracker & Analyzer
A Streamlit web app that allows you to track, edit, and analyze syllabus progress interactively using a simple CSV file. Perfect for students, teachers, or course coordinators.

🔧 Features
✅ Upload a syllabus CSV file

✏️ Edit topic statuses (Pending, Completed, In Progress)

📉 Track syllabus progress by subject

📊 Visualize:

Topics per subject

Weekly topic distribution

Completion status (pie chart)

💾 Download the updated CSV file

📁 CSV Format
Make sure your CSV includes at least the following columns:

c
Copy
Edit
Subject,Topic,Week,Status
Math,Algebra,1,Completed
Math,Geometry,2,Pending
Physics,Motion,1,In Progress
Chemistry,Acids,1,Completed
Week column is optional but recommended.

🚀 How to Run
Install dependencies (if not already):

bash
Copy
Edit
pip install streamlit pandas matplotlib
Run the app:

bash
Copy
Edit
streamlit run syllabus_tracker_analyzer_app.py
Upload your .csv file through the sidebar and start tracking!

📸 Screenshots
🔹 Tracker Tab
Update the status of each topic quickly and save changes.

🔹 Analyzer Tab
Visual summary of subject progress, weekly topics, and completion status.

📦 File Structure
Copy
Edit
📁 syllabus-tracker/
├── syllabus_tracker_analyzer_app.py
└── README.md
🧠 To-Do / Future Enhancements
 Add new topics directly from the app

 Filter by subject or week

 Export progress report as PDF

💡 License
MIT License — feel free to use and modify it for personal or academic use.
