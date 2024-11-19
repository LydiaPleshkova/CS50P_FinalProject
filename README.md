# Baby Name Suggester
#### Video Demo:  <URL HERE>
#### Description:
TODO

## Overview

The **Baby Name Suggester** is an interactive Python program designed to help parents choose the perfect name for their baby. With over 258,000 name options sourced from a CSV file, the program offers tailored suggestions based on gender, first letter, or random selection. It’s a simple and fun tool for parents embarking on the journey of naming their child.

---

## Features

1. **Filter Names by Gender**:
   - Choose names specifically for boys or girls, sourced from the `baby_names.csv` file.

2. **Filter Names by First Letter**:
   - Specify a starting letter to narrow down name suggestions.

3. **Random Name Suggestions**:
   - Receive up to five random names if no specific preferences are given.

4. **Dual Suggestions**:
   - Get suggestions for both boys and girls when the gender is not specified.

---

## Prerequisites

1. **Python**: Version 3.6 or higher.
2. **CSV File**: Ensure a file named `baby_names.csv` is present in the same directory as the script. It must contain two columns:
   - `name`: The baby name.
   - `sex`: The gender associated with the name (`boy` or `girl`).

---

## How It Works

1. **Run the Program**:
   - Start the program, and you’ll be greeted with a welcome message.

2. **Select Gender**:
   - Answer whether you know the baby’s gender by typing "Yes" or "No".
   - If "Yes", specify the gender (`Boy` or `Girl`).

3. **Filter by First Letter**:
   - Decide whether you want to filter names by the first letter.
   - If "Yes", enter the preferred letter to receive suggestions.
   - If "No", get random name suggestions.

4. **Suggestions for Both Genders**:
   - If gender is not specified, the program suggests names for both boys and girls.

5. **Output**:

---

## Sample Interaction

### Input
   Do you already know if it’s a boy or a girl? Please type "Yes" or "No" and press Enter: Yes Please type "Boy" or "Girl" and press Enter: Boy Do you want to choose the first letter for a name? Please type "Yes" or "No" and press Enter: Yes Please type the first letter you prefer: A
   - Suggestions are displayed as a neatly formatted numbered list.
     
### Output
Here are five name suggestions for your sweet baby starting with "A":

Adam
Aiden
Aaron
Andrew
Alex


### Alternate Output (Random Suggestions)
That is okay! Here are five randomly chosen name suggestions for your sweet baby:

Liam
Noah
Ethan
Mason
Logan


---

## Error Handling

- **File Not Found**: If the `baby_names.csv` file is missing, the program notifies the user and exits.
- **Missing Columns**: If the CSV file does not contain the required `name` or `sex` columns, an error message is displayed.
- **Invalid Input**: The program prompts users to correct unsupported entries, such as unrecognized gender or letter inputs.

---

## Installation and Execution

1. Clone or download the repository.
2. Place the `baby_names.csv` file in the same directory as the script.
3. Run the script using:
   ```bash
   python baby_name_suggester.py
