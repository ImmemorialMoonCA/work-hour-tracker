import csv
from datetime import datetime

# Constants
WORKDAYS_PER_YEAR = 260

def parse_time(time_str):
    return datetime.strptime(time_str, "%H:%M")

def calculate_net_hours(start, end, took_lunch):
    total_hours = (end - start).seconds / 3600
    if took_lunch.lower() in ["y", "yes"]:
        total_hours -= 0.5
    return round(total_hours, 2)

def main():
    print("🔧 Work Hour Tracker (Salary-Based Edition)\n")
    yearly_salary = float(input("Yearly salary (e.g. 49500): "))
    daily_salary = round(yearly_salary / WORKDAYS_PER_YEAR, 2)
    print(f"Daily salary based on 260 days/year: ${daily_salary:.2f}")

    date = input("Date (YYYY-MM-DD): ")
    job = input("Job name: ")
    start_time = parse_time(input("Start time (HH:MM, 24h): "))
    end_time = parse_time(input("End time (HH:MM, 24h): "))
    took_lunch = input("Took lunch? (Y/N): ")

    net_hours = calculate_net_hours(start_time, end_time, took_lunch)
    effective_rate = round(daily_salary / net_hours, 2)

    print(f"\n✅ You worked {net_hours} hours. Effective hourly rate: ${effective_rate:.2f}")

    # Save to CSV
    with open("data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, job, start_time.strftime("%H:%M"), end_time.strftime("%H:%M"), took_lunch.upper(), net_hours, daily_salary, effective_rate])
        print("📁 Entry saved to data.csv")

if __name__ == "__main__":
    main()
