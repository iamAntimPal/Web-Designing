import pandas as pd
from ace_tools import display_dataframe_to_user

# Original sample data
data = {
    "Company Name": ["DataCorp", "Insight Analytics", "TechNova", "AI Solutions", "DeepMindX", "Quantum Data", "Visionary Labs"],
    "Job Title": ["Data Scientist", "Machine Learning Engineer", "Data Analyst", "AI Researcher", "Senior Data Scientist", "Data Engineer", "BI Developer"],
    "Location": ["Bangalore, India", "Mumbai, India", "Hyderabad, India", "Pune, India", "Chennai, India", "Delhi, India", "Kolkata, India"],
    "Date Applied": ["2025-05-01", "2025-04-28", "2025-05-03", "2025-04-30", "2025-05-05", "2025-04-25", "2025-05-07"],
    "Source": ["LinkedIn", "Referral", "Company Site", "Indeed", "GitHub", "Company Site", "AngelList"],
    "Referral": ["", "Rohit Kumar", "", "Priya Singh", "", "", "Anita Desai"],
    "Contact Name": ["N/A", "Sanjay Mehta", "N/A", "Deepa Rao", "N/A", "Vikram Patel", "N/A"],
    "Contact Email": ["", "smehta@insight.com", "", "drao@aisolutions.com", "", "vpatel@quantumdata.com", ""],
    "Phone Screen Date": ["2025-05-05", "2025-05-02", "2025-05-07", "2025-05-04", "", "2025-05-01", ""],
    "Technical Round Date": ["2025-05-10", "2025-05-06", "", "2025-05-08", "", "2025-05-03", ""],
    "Assessment Status": ["Completed", "Pending", "Completed", "Completed", "Pending", "Completed", "Pending"],
    "Round 1 Outcome": ["Passed", "N/A", "Passed", "Passed", "N/A", "Passed", "N/A"],
    "Round 2 Outcome": ["Pending", "N/A", "N/A", "Pending", "N/A", "Pending", "N/A"],
    "Offer Date": ["", "", "", "", "", "", ""],
    "Offered Salary": ["", "", "", "", "", "", ""],
    "Next Follow-Up": ["2025-05-12", "2025-05-08", "2025-05-12", "2025-05-11", "2025-05-10", "2025-05-07", "2025-05-13"],
    "Application Status": ["Interviewing", "Applied", "Interviewing", "Interviewing", "Applied", "Interviewing", "Applied"],
    "Notes": [
        "Strong resume fit; prep ML whiteboard questions",
        "Waiting for referral call",
        "Sent portfolio link",
        "Research AI projects before interview",
        "Referred by ex-colleague",
        "Practice SQL queries",
        "Follow up about test instructions"
    ]
}

df = pd.DataFrame(data)

# Filter for companies with a Round 1 Outcome (not 'N/A')
filtered_df = df[df["Round 1 Outcome"] != "N/A"].reset_index(drop=True)

display_dataframe_to_user(name="First-Round Interviewed Companies", dataframe=filtered_df)
