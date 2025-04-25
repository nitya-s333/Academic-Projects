#Author: Nitya Rajender Arya 
#Student ID: 24155608
# CITS1401 Project 1

#Task-1: define main()
#We define the main function that takes 5 inputs
#Expected inputs-("csvfile_1","csvfile_2",int(age),"sa2_1","sa2_2")

def main(csvfile_1, csvfile_2, age, sa2_1, sa2_2):
    #Task 2: Reading the file content and extracting data from it 
    #Task 2.1: Validate if input is given as string or not
    if type(csvfile_1) is not str or type(csvfile_2) is not str:
        print("Error: Input file names must be strings.")
        return 0       
    #Task 2.2: Validate if the files given as csv or not
    if not (csvfile_1.lower().endswith('.csv') and csvfile_2.lower().endswith('.csv')):
        print("Error: One or both input files are not CSV.")
        return None
    try:
        #Task 2.3 : Read the files and extract its data
        #Step -1: Open the file in read mode and extract header and records from it.
        #Step 2: Since the file is in csv format, we remove any leading/trailing spaces using split()
        #Then convert the extracted data to lowercase to ensure case-insenstivity
        #Finally, extract the data using split()
        file = open(csvfile_1, 'r')
        area_lines = file.readlines()
        file.close()
        area_data = [line.strip().lower().split(',') for line in area_lines]
        area_records = area_data[1:]

        file = open(csvfile_2, 'r')
        pop_lines = file.readlines()
        file.close()
        pop_data = [line.strip().lower().split(',') for line in pop_lines]
        pop_header = pop_data[0]
        pop_records = pop_data[1:]
        
    #Task 2.4: Raise errors if something goes wrong while opening and reading the file in try block
    except FileNotFoundError:
        print("Error: One or both files not found.")
        return None, [], [], 0

    except PermissionError:
        print("Error: Cannot read area file (permission denied).")
        return None, [], [], 0

    except:
        print("Error: Unexpected error reading files.")
        return None, [] ,[], 0


    # Task 3: Calculate OP1
    # Step 3.1: Validate if age is int or not
    try:
        # Step 1.5: Validate that age is an integer
        age = int(age)
    except ValueError:
        print("Error: Age must be an integer.")
        return 0  # Since age is numeric we return 0 in case of anhy error
    
   # Step 3.2: Extract Relevant column from the data according to the input age
   # First we seperate the header from the rest of the data to get the column names which contain age range
   # Then we extract the ranges by checking for "-" or "over" in them 
    
    try:
        age_groups = []
        for header in pop_header[1:]:
            h = header.strip().replace("age", "").replace(" ", "")
            if '-' in h:
                parts = h.split('-')
                if parts[0].isdigit() and parts[1].isdigit():
                    age_groups.append((header, [int(parts[0]), int(parts[1])]))
            elif 'over' in h:
                num = ""
                for c in h:
                    if c.isdigit():
                        num += c  # Concatenate digits directly
                if num:
                    age_num = int(num)
                    age_groups.append((header, [age_num, None]))
    except ValueError:
        print("Error: Invalid numeric value encountered while processing age headers.")
        return 0  # Return 0 for numeric value errors
    except IndexError:
        print("Error: Index error while processing age headers.")
        return []  # Return an empty list for index errors
    except:
        print("Unexpected error occured while retreiving the relevant age groups")
        return None  # Return None for any other unexpected errors


    # Step 3.3: Match input age with the extracted column
    matched_col = None
    matched_range = []
    for name, groups in age_groups:
        lower = groups[0]
        upper = groups[1]
        if upper is None:
            if age >= lower:
                matched_col = name
                matched_range = [lower, age]
                break
        else:
            if lower <= age <= upper:
                matched_col = name
                matched_range = [lower, upper]
                break

    # Task 4: The matched range will be used to calculate OP2, OP3, OP4

    # Now we have to find the given sa_3 code for a given sa_2 code using area_records
    
    # Task 4.1: Find the SA3 code for a given SA2 code using area_records.
    # For this we look for the SA2 code in column 5 using row, since its csv and data is stored in lists of lists
    # To access a value in a column, we access a particular index inside a row.
    #When matched we return SA_3 col from column 3 (row[2])

    def process_statistics(area_records, pop_records, pop_header, age_groups, matched_col, sa2_code_one, sa2_code_two):
        def find_sa3(sa2_code):
            for row in area_records:
                if row[4] == sa2_code:
                    return row[2]
            return None
        #Task 4.2: Get the state name and SA3 name for a given SA3 code.
        #Step 1:Search for the SA3 code in column 3 (row[2]).
        #Step 2: Return the state name from column 2 (row[1]) and SA3 name from column 4 (row[3]).

        def get_state_and_sa3_name(sa3_code):
            for row in area_records:
                if row[2] == sa3_code:
                    return row[1], row[3]
            return None, None
        
        #Task 4.3: Get a list of SA2 codes that belong to a given SA3 code.
        # For this, use a list comprehension to collect row[4] (SA2 codes) for rows where row[2] matches the SA3 code.
        def sa2s_in_sa3(sa3_code):
            return [row[4] for row in area_records if row[2] == sa3_code]
        
        #Task 4.4: Fetch the population value for a specific SA2 code and age group column.
        #Step 1: Find the row in pop_records with the matching SA2 code (column 0).
        #Step 2: Then we look through the columns to find the one that matches the given age column.
        #Step 3: Convert it to int and return the population.
        #Step 4: If it's not an integer, return 0 to handle bad data safely.
        def get_pop_value(sa2_code, column):
            for row in pop_records:
                if row[0] == sa2_code:
                    for i in range(1, len(pop_header)):
                        if pop_header[i].strip() == column.strip():
                            try:
                                return int(row[i])
                            except:
                                return 0
            return 0
        
        #Task 4.5: Get a list of population values in a specific age group for all SA2s in an SA3.
        #Step 1: First we have to get all SA2s within the given SA3 (sa2s_in_sa3).
        #Step 2: For each SA2, we extract the population for the target column using get_pop_value.
        def get_pop_values_for_sa3(sa3_code, column):
            return [get_pop_value(sa2, column) for sa2 in sa2s_in_sa3(sa3_code)]

        # Task 5: Get OP2
        # OP2: We calculate mean and standard deviation of the selected age group population across all SA2s in the
        # corresponding SA3 of each input SA2 code.
        
        try:
            def compute_stats(sa2_code):
                sa3_code = find_sa3(sa2_code)
                if sa3_code is None:
                    return None
                values = get_pop_values_for_sa3(sa3_code, matched_col)
                if not values:
                    return 0
                mean = sum(values) / len(values)
                var = sum((x - mean) ** 2 for x in values) / (len(values) - 1) if len(values) > 1 else 0.0
                return [sa3_code, round(mean, 4), round(var ** 0.5, 4)]

            op2 = [compute_stats(sa2_code_one), compute_stats(sa2_code_two)]
        except ZeroDivisionError:
            # Handle division by zero errors
            print("Error: Division by zero while calculating statistics for SA2 code .")
            return 0  # Return 0 for division by zero errors

        except TypeError:
            # Handle type errors (e.g., invalid data types in the values list)
            print("Error: Type error while calculating statistics for SA2 code.")
            return 0  # Return 0 for type errors

        except:
            # Catch any other unexpected errors and print the error message
            print("Unexpected error while calculating statistics for SA2 code {sa2_code}")
            return 0  # Return 0 for any other unexpected errors

        # Task 6: Calculate OP3
        # OP3: Identifies the SA3 area with the highest total age group population in each state and computes its percentage share of total population.
        #Here for each state we have to find the following:
        #Task 6.1: The SA3 area with the largest population in the extracted age group.
        #Task 6.2:The percentage of that population with respect to the total population in the same SA3 area.
        #Task 6.3: If there's a tie, we choose the SA3 with the smaller area code that is sorted alphabetically by sa3_code.
        try:
            #Step -1 :We accumulate the data by sa_3
            sa3_stats = []
            for row in pop_records:
                sa2_code = row[0]
                sa3_code = find_sa3(sa2_code)
                if not sa3_code:
                    continue
                age_val = get_pop_value(sa2_code, matched_col)
                total = sum(int(x) if x.isdigit() else 0 for x in row[1:])
                found = False
                for stat in sa3_stats:
                    if stat[0] == sa3_code:
                        stat[2] += age_val
                        stat[3] += total
                        found = True
                        break
                if not found:
                    state, sa3_name = get_state_and_sa3_name(sa3_code)
                    sa3_stats.append([sa3_code, sa3_name, age_val, total, state])
                    
            #Step 2: Find best sa_2 area per state
            state_best = []
            for row in sa3_stats:
                sa3_code, sa3_name, age_total, grand_total, state = row
                if grand_total == 0:
                    continue
                percentage = age_total / grand_total
                found = False
                for entry in state_best:
                    if entry[0] == state:
                        if age_total > entry[3] or (age_total == entry[3] and sa3_code < entry[4]):
                            entry[1] = sa3_name
                            entry[2] = percentage
                            entry[3] = age_total
                            entry[4] = sa3_code
                        found = True
                        break
                if not found:
                    state_best.append([state, sa3_name, percentage, age_total, sa3_code])
                    
            #Format the final output
            op3 = []
            for entry in sorted(state_best, key=lambda x: x[0]):
                op3.append([entry[0], entry[1], round(entry[2], 4)])

        except:
            print("Unexpected error occurred while processing OP3. Details:")
            return None

        # Task 7: Calculate OP4
        # OP4: Here we have to compute the correlation coefficient between age group populations of two given SA2 areas across all age brackets.
        # 1. First we try get all age group population values for the given SA2 codes (sa2_code_one and sa2_code_two).
        # 2. Then we check if the lists of population values for both SA2 codes have the same length or are empty; if not, set correlation to 0
        # 3. Finally, we calclate the correlation coefficient using the formula.

        
        try:
            def extracted_age_values(sa2_code):
                return [get_pop_value(sa2_code, col_name) for col_name, _ in age_groups]

            x = extracted_age_values(sa2_code_one)
            y = extracted_age_values(sa2_code_two)

            if len(x) != len(y) or len(x) == 0:
                corr = 0.0
            else:
                xbar = sum(x) / len(x)
                ybar = sum(y) / len(y)
                num = sum((x[i] - xbar) * (y[i] - ybar) for i in range(len(x)))
                den = (sum((xi - xbar) ** 2 for xi in x) * sum((yi - ybar) ** 2 for yi in y)) ** 0.5
                corr = round(num / den, 4) if den != 0 else 0
        except ZeroDivisionError:
            print("Error: Division by zero occurred while calculating correlation.")
            return 0

        except TypeError:
            print("Error: Invalid data type encountered while calculating correlation.")
            return None

        except Exception:
            print("Unexpected error occurred while calculating correlation.")
            return None

        return op2, op3, corr

    op2, op3, op4 = process_statistics(area_records, pop_records, pop_header, age_groups, matched_col, sa2_1, sa2_2)
    return matched_range, op2, op3, op4


#Debugging:
"""
Issue 1
-Error Type: TypeError while unpacking None during handling the file errors
- Error Description:
    TypeError: cannot unpack non-iterable NoneType object
- Erroneous Code Snippet:
    except FileNotFoundError:
        print("Error: One or both files not found.")
        return None
- Test Case:
    OP1, OP2, OP3, OP4 = main('missing.csv', 'missing.csv', 18, '401011001', '401021003')
- Reflection:
    I was returning `None` on file errors, but the user always expected a 4‑tuple (OP1, OP2, OP3, OP4).Hence, returning a single `None` caused a TypeError when unpacking.
    To solve this, I updated all error cases in file handling part for OP1 to `return None, [], [], 0.0` so the output format is always correct and unpacking succeeds.

Issue 3:
- Error Type:
    Logic Error – Incorrect handling of case sensitivity for SA3 codes
- Error Description:
    The program compares SA3 codes directly, which can cause mismatches if the input is in a different case
    than what's present in the CSV file. While SA3 codes are usually numeric, if any string-based identifiers
    or inputs were used (e.g., area names), failing to use `.lower()` for case-insensitive comparison would cause errors.
- Erroneous Code Snippet:
    if entry[0] == input_code:
- Test Case:
    main('SampleData_Areas.csv', 'SampleData_Populations.csv', 18, '401011001', '401021003')
    # Input with extra whitespace or different case
- Reflection:
    While this did not crash the program, it caused valid entries to be skipped, leading to wrong OP values.
    I fixed this by normalizing all relevant string comparisons using `.strip().lower()` to make the logic robust.
    
Issue 3
- Eroror Type: NameError for age range variable
- Error Description:
    NameError: name 'matched_bounds' is not defined
- Erroneous Code Snippet:
    op3.append([entry[0], entry[1], round(matched_bounds, 4)])
- Test Case:
    OP1, OP2, OP3, OP4 = main('SampleData_Areas.csv','SampleData_Populations.csv', 18,'401011001','401021003')
- Reflection:
    I had originally used `matched_bounds` to get the age range but later renamed it to `matched_range`.I forgot to update this in OP3. This caused a Name Error.
    I solved this by replacing all occurrences of `matched_bounds` with `matched_range` and fixed the bug . This allowed OP3 calculations to be done correctly.
"""


