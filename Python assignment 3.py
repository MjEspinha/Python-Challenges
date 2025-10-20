import datetime

# Step 2: Get birth date from user
birth_year = int(input("Enter your birth year (e.g., 2000): "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

# Step 3: Create a date object
birth_date = datetime.date(birth_year, birth_month, birth_day)

# Step 4: Get today's date
today = datetime.date.today()

# Step 5: Calculate years and months
years = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    years -= 1

months = today.month - birth_date.month
if today.day < birth_date.day:
    months -= 1
if months < 0:
    months += 12

# Step 6: Display the result
print(f"You have been alive for {years} years and {months} months.")
