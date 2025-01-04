import pandas as pd

# Load the Excel file
file_path = 'Copy of Developers Swaqny Cv.xlsx'  # Replace with the actual path to your file
form_responses = pd.read_excel(file_path, sheet_name='Form Responses 1')

# Print the column names to check their actual names
print("Available columns:", form_responses.columns.tolist())

# Normalize column names for easier handling
form_responses.columns = [col.strip().lower().replace(" ", "_").replace(":", "") for col in form_responses.columns]

# Define all cities and areas near Tanta
cities_near_tanta = [
    'tanta', 'طنطا', 'tanta (قسم اول)', 'zagazig&tanta', 
    'samannoud - gharbia', 'banha and tanta', 'zefta', 
    'kafr el zayat', 'el mahalla', 'kafre elshiekh', 
    'zagazig', 'zifta', 'kafr el zayat', 'المحلة الكبرى'
]

# Apply the filter for cities (convert to lowercase for case-insensitive matching)
city_filter = form_responses['city_of_residence'].str.lower().str.contains('|'.join(cities_near_tanta), na=False)

# Apply filters
filtered_data = form_responses[city_filter]

# Define the regex pattern for female names (include the extracted names)
female_name_pattern = r'\b(Alaa Fathalla|Alaa Tourkey|Aya Mohamed Slama|Amira Shinnawi El-Bltage|Menna Soliman Ali Eldakrory|' \
                      r'Salma Amer AbdelGhany|Eman Ashraf Shawky Elbhnasy|Shimaa Ragab Saad|Amina AbdelAzeez SayedAhmed Marey|' \
                      r'Nrmeen Mohamed Sadek Elaraby|Mayar Mohamed Youssef Khedeer|Reem Ramadan Ali|Esraa Hany kaf|' \
                      r'lamya eltatawy|Nadia khaled mohamed hassan|Nada Elgarf|Nouran kadri Aboyousef|' \
                      r'Rawda ashor abdelhady|نورا ابو اليزيد|Aml elsaid mohammed hadila|Shahd baher galal ammar|' \
                      r'Hanin Ashraf Abdullah|Tasneem Atif Soliman Omar|Wessam lasheen|Arwa Ahmad Fahmi|' \
                      r'sara yasser mahmoud abdo|Maryam Khaled Hassan Mohamed Ahmed Eissa)\b'

# Add a column to prioritize names matching the female pattern
filtered_data['is_female_name'] = filtered_data['full_name'].str.contains(female_name_pattern, na=False, regex=True)

# Sort the data: prioritize female names, then keep the rest
sorted_details = filtered_data.sort_values(by='is_female_name', ascending=False)


# Select relevant columns for output
output_columns = [
    'full_name',
    'phone_number',
    'city_of_residence',
    'linkedin_profile_url',
    'github_profile_url',
    'what_is_your_current_experience_level?',
    'select_the_position_you_are_applying_for'
]
sorted_output = sorted_details[output_columns]

# Save the updated filtered data to a new Excel file
new_output_path = 'sorted_sd.xlsx'
sorted_output.to_excel(new_output_path, index=False, sheet_name='Sorted Developers Near Tanta')

print(f"File saved to {new_output_path}")
