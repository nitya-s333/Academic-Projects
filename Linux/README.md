
---

# Renewable and Coal Energy Production Analyzer

## Overview

This project provides a **Bash script** (`analyze_energy.sh`) that analyzes **energy production data** — specifically **solar, wind, and coal energy** — from a structured **CSV** file.  
It allows users to extract the **minimum** or **maximum** production values either by:
- Specified **year** (across countries), or
- Specified **country code** (across years).

This ensures dynamic, user-friendly, and robust querying of energy data without manual filtering.

---

## Purpose

The primary goal of the script is to:
- Automate searching, filtering, and sorting **energy production** data.
- Handle **missing data**, **file validation**, and **user input errors** gracefully.
- Find the **minimum** or **maximum** value for **solar and wind energy** or **coal energy** production based on user queries.
- Provide meaningful, structured outputs for further analysis or reporting.

It was designed with data science pipelines and renewable energy studies in mind.

---

## Input

The input must be a `.csv` file with the following mandatory columns in its header:

| Column        | Description                                    |
| -------------- | ------------------------------------------------ |
| `Country`     | Name of the country                            |
| `Code`        | Country's 2–3 letter abbreviation (e.g., "USA", "IND") |
| `Year`        | Year of record                                 |
| `SolarWindTWh`| Energy produced from solar and wind (in TWh)   |
| `CoalTWh`     | Energy produced from coal (in TWh)             |

Example header:
```
Country,Code,Year,SolarWindTWh,CoalTWh
```

---

## How the Script Works

The script performs extensive validation before proceeding:

| Step | Validation Task |
| :-- | :-- |
| 1 | Check number of arguments (must be exactly 4). |
| 2 | Verify that the input file exists, is non-empty, and has a `.csv` extension. |
| 3 | Ensure the input CSV contains required columns (`Country`, `Code`, `Year`, `SolarWindTWh`, `CoalTWh`). |
| 4 | Check if the second argument is a valid **year** (4 digits) or **country code** (2–3 letters). |
| 5 | Confirm third argument is valid: either `solar_wind` or `coal`. |
| 6 | Confirm fourth argument is valid: either `minimum` or `maximum`. |

After validation:
- If querying by year: finds the country with minimum or maximum energy production in that year.
- If querying by country code: finds the year when that country had minimum or maximum production.

---

## Usage

```
./analyze_energy.sh <csv_file> <year_or_country_code> <solar_wind|coal> <min|max>
```

Example Commands:

Find the maximum solar and wind energy producer in 2021:
```
./analyze_energy.sh OWID_Solar_wind_vs_Coal.csv 2021 solar_wind max
```

Find the minimum coal energy produced by India (IND) across all years:
```
./analyze_energy.sh OWID_Solar_wind_vs_Coal.csv IND coal min
```

---

## Features

- Automatic case-insensitivity for energy types (handles "Coal", "COAL", "coal").
- Automatic case-insensitivity for country codes ("ind", "Ind", "IND" → "IND").
- Flexible inputs — accepts "min", "minimum", "MAX", "Maximum", etc.
- Dynamic output based on type of query (year or country code).
- Temporary files cleaned up after each execution to avoid clutter and data leaks.
- Clear, human-readable final outputs.

---

## Example Output

When querying a year:
```
The maximum amount of electrical energy produced from solar and wind in 2021 was 500.5 TWh by China (CHN).
```

When querying a country code:
```
The minimum amount of electrical energy produced from coal by India (IND) was 120.3 TWh in 2003.
```

---

## Error Handling

The script provides clear error messages if:
- Wrong number of arguments are given.
- Input file is missing or not a `.csv`.
- Required columns are missing.
- Invalid year, country code, energy type, or operation is given.
- No matching data is found for the input query.

Example error message:
```
Error: File must have a .csv extension.
```

---

## Future Improvements

- Add support for other renewable sources like Hydro, Nuclear, and Geothermal.
- Include graphical summaries (e.g., top 5 countries by solar wind usage) using `gnuplot`.
- Improve performance for extremely large CSV files.

---

## Cleanup

After each execution, the script automatically deletes temporary files like `.data_temp.csv` to maintain a clean workspace.

---

## Summary

This bash script is a robust, validated, and user-friendly tool for analyzing energy production across countries and years.  
It can be easily extended or integrated into bigger data science and analytics pipelines dealing with global energy datasets.

---

## Files

- `analyze_energy.sh` — main bash script.
- `OWID_Solar_wind_vs_Coal.csv` — example CSV file (expected format).

---

## Quick Run

```
chmod +x analyze_energy.sh
./analyze_energy.sh your_data.csv 2020 solar_wind min
```

---
