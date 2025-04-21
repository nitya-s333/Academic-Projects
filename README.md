# Australian Population Statistics – CITS1401 Project

This Python script analyzes age-based population statistics across Australian regions using census-style CSV data. It was developed as part of the **CITS1401 – Problem Solving & Programming** unit at the University of Western Australia.

---

## 📜 Description

This Python 3 program analyzes population data from two CSV files to calculate:

- **OP1**: Age group range for the given age.
- **OP2**: Mean and standard deviation of the selected age group’s population in the two corresponding SA3 areas.
- **OP3**: SA3 area with the highest age group population percentage in each state.
- **OP4**: Correlation coefficient between population distributions across all age groups in two SA2 areas.

### 📁 Input Files:
- `csvfile_1`: Contains **geographical area details** (SA2 and SA3 mappings).
- `csvfile_2`: Contains **population data** grouped by age and SA2 code.

---

## 🧠 Development Notes

- The script is designed with **robust error handling** to gracefully manage:
  - Missing or unreadable files
  - Invalid file types
  - Type mismatches and user input errors
  - Case sensitivity in area codes
- Key challenges addressed:
  - Resolving `TypeError` during file unpacking
  - Ensuring all code logic is **case-insensitive**
  - Fixing inconsistent variable naming and unpacking issues

---

## ⚙️ Installation

Python 3 is required to run this script.  
✅ No external libraries are needed — it runs on the standard Python library.

---

## 🧪 Function Signature

```python
main(csvfile_1, csvfile_2, age, sa2_1, sa2_2)
🚀 Usage
Call the main() function in a Python script or interpreter with the following arguments:

csvfile_1 (str): Path to the area details CSV file

csvfile_2 (str): Path to the population data CSV file

age (int): Age to determine the corresponding age group

sa2_1 (str): First SA2 code for analysis

sa2_2 (str): Second SA2 code for analysis

✅ Example:
python
Copy
Edit
main("SampleData_Areas.csv", "SampleData_Populations.csv", 25, "123456789", "987654321")
📋 Outputs
The function returns a tuple containing:

matched_range – Age range matched for the given age

op2 – List of [SA3 code, mean, std. deviation] for both SA2 inputs

op3 – List of [State, SA3 name, % population] for top SA3s in each state

op4 – Correlation coefficient between two SA2 age distributions

💡 Technical Concepts Used
File I/O and exception handling

List comprehensions and nested functions

Case-insensitive string processing

Data aggregation and conditional filtering

Statistics: Mean, Standard Deviation, Correlation Coefficient
