import csv
import random

def filter_names_by_first_letter(names_list, letter):
    """Filter names by the first letter."""
    return [name for name in names_list if name.lower().startswith(letter.lower())]

def suggest_random_names(names_list, count=5):
    """Propose five options of random names."""
    return random.sample(names_list, min(len(names_list), count))

def baby_names(filename):
    """Load baby names from a CSV file and return as separate lists for boys and girls."""
    boys_names = []
    girls_names = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['sex'].lower() == 'boy':
                    boys_names.append(row['name'])
                elif row['sex'].lower() == 'girl':
                    girls_names.append(row['name'])
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except KeyError:
        print("Error: CSV file is missing required columns ('name' and 'sex').")
    return boys_names, girls_names

def main():
    boys_names, girls_names = baby_names('baby_names.csv')
    
    if not boys_names or not girls_names:
        print("Unable to load names. Please check the file and try again.")
        return

    print("Congratulations!!!\nWe will help you choose a name for your baby. We have 258,000 options!")
    congratulations = input('\nDo you already know if it’s a boy or a girl? Please type "Yes" or "No" and press Enter: ').strip().lower()

    if congratulations == "yes":
        sex_question = input('\nPlease type "Boy" or "Girl" and press Enter: ').strip().lower()
        if sex_question == "boy":
            chosen_list = boys_names
        elif sex_question == "girl":
            chosen_list = girls_names
        else:
            print('Invalid input. Please restart and type "Boy" or "Girl".')
            return
        
        sex_letter_question = input('\nDo you want to choose the first letter for a name? Please type "Yes" or "No" and press Enter: ').strip().lower()
        if sex_letter_question == 'yes':
            letter = input('\nPlease type the first letter you prefer: ').strip().upper()
            filtered_names = filter_names_by_first_letter(chosen_list, letter)
            if filtered_names:
                print(f'\nHere are five name suggestions for your sweet baby starting with "{letter}":\n' + '\n'.join([f"{i + 1}. {name}" for i, name in enumerate(filtered_names[:5])]))
            else:
                print(f'\nSorry, no names found starting with "{letter}".')
        else:
            print(f'\nThat is okay! Here are five randomly chosen name suggestions for your sweet baby:\n' + '\n'.join([f"{i + 1}. {name}" for i, name in enumerate(suggest_random_names(chosen_list))]))
    
    else:
        print('\nNo worries! We will suggest options for both boys and girls.')
        letter_question = input('Do you want to choose the first letter for a name? Please type "Yes" or "No" and press Enter: ').strip().lower()
        if letter_question == 'yes':
            letter = input('\nPlease type the first letter you prefer: ').strip().upper()
            filtered_boys = filter_names_by_first_letter(boys_names, letter)
            filtered_girls = filter_names_by_first_letter(girls_names, letter)
            print('\nThat is okay! Here are five randomly chosen name suggestions for your sweet baby:')
            print(f'\n  for baby-boy:\n' + '\n'.join([f"{i + 1}. {name}" for i, name in enumerate(filtered_boys[:5])]))
            print(f'\n  for baby-girl:\n' + '\n'.join([f"{i + 1}. {name}" for i, name in enumerate(filtered_girls[:5])]))
        else:
            print('\nThat is okay! Here are five randomly chosen name suggestions for your sweet baby:')
            print(f'\n  for baby-boy:\n' + '\n'.join([f"{i + 1}. {name}" for i, name in enumerate(suggest_random_names(boys_names))]))
    
            print(f'\n  for baby-girl:\n' + '\n'.join([f"{i + 1}. {name}" for i, name in enumerate(suggest_random_names(girls_names))]))

                  
if __name__ == "__main__":
    main()
