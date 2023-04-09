from datetime import date, datetime
import inflect

def main():
    inf = inflect.engine()
    tday = datetime.strptime(str(date.today()),"%Y-%m-%d")
    try:
        user = input("Date of Birth: ").strip()
        user_Date = datetime.strptime(user,"%Y-%m-%d")
        delta = str((tday - user_Date) * 60 * 60).split(" ")
        print(f"{inf.number_to_words(delta[0])} minutes")
    except:
        print("Invalid Date")

if __name__ == "__main__":
    main()
