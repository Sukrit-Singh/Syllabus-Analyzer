# Syllabus Tracker & Analyzer 📘

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

A Streamlit web application to track and analyze your syllabus progress visually.

## Features ✨

- **CSV Upload**: Easily upload your syllabus data in CSV format
- **Status Tracking**: Update completion status (Pending/In Progress/Completed)
- **Visual Analytics**:
  - Topics distribution per subject
  - Weekly topic distribution
  - Completion status pie chart
  - Subject-wise progress tracking
- **Export**: Download updated syllabus with your progress

## Requirements 📋

- Python 3.7+
- Streamlit
- Pandas
- Matplotlib

## Installation 🛠️

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/syllabus-tracker.git
   cd syllabus-tracker
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
## Usage 🚀
1. Prepare your CSV file with at least these columns:
- Subject
- Topic
- Status (should contain "Pending", "In Progress", or "Completed")
- (Optional) Week for weekly distribution analysis

2. Run the app:
   ```bash
   streamlit run syllabus_streamlit_app.py

3. Upload your CSV file and start tracking!


## Contributing 🤝
Contributions are welcome! Please open an issue or submit a pull request.

## License 📜
This project is licensed under the MIT License
