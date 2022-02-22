def intro():
    print("Hello, welcome to your diary and mood tracker!")

    response = ""
    while(response!='Q'):
        response = input("Please pick an option to continue: Type D for diary, M for mood tracker\
            P for period tracker, Q for quitting, FLUSH for removing all entries\n")
        if(response=='D'):
            type_diary()
        elif(response=='M'):
            type_mood()
        elif(response=='P'):
            type_period()
        elif(response=='FLUSH'):
            flush_entries()
        else:
            if(response!='Q'):
                print("Please type either D, M or P")

def type_diary():
    print("You picked diary, here we go")
    print("I hope you are well cutie!")
    user_input = input("Start typing your diary and hit enter when you are ready!:\n")
    
    diary_entry={
        "date": date.today().strftime("%m/%d/%y"),
        "entry": user_input
    }

    collection_name = db["DiaryEntries"]
    collection_name.insert_one(diary_entry)
    print("Good to go girl! You are all set.")

def type_mood():
    print("You picked mood tracker, here we go. Please follow the instructions")
    user_ranking = input("Please rate how you are feeling out of ten.\n")
    user_summary = input("Please type how you are feeling\n")
    user_remedy = input("Please type the remedy you followed/or thinking of following\n")

    mood_entry={
        "date": date.today().strftime("%m/%d/%y"),
        "ranking": user_ranking,
        "summary": user_summary,
        "remedy": user_remedy
    }

    collection_name = db["MoodEntries"]
    collection_name.insert_one(mood_entry)
    print("Good to go girl! You are all set.")

def type_period():
    collection_name = db["PeriodEntries"]
    print("Period tracker!")

    if(collection_name.count_documents({"end_date": {"$exists": False}})!=0 and collection_name.estimated_document_count()!=0):
        collection_name.update_one({"end_date": {"$exists": False}}, {"$set": {"end_date": date.today().strftime("%m/%d/%y")}})
    else:
        new_period = {
            "start_date": date.today().strftime("%m/%d/%y"),
        }
        collection_name.insert_one(new_period)
    print("You are all set!")

def flush_entries():
    confirmation = input("Please type YES to continue flushing")
    if(confirmation=='YES'):
        db["PeriodEntries"].delete_many({})
        db['DiaryEntries'].delete_many({})
        db['PeriodEntries'].delete_many({})
        print('Flushed!')

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = ''
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)
    # Create the database for our example (we will use the same database throughout the tutorial
    return client['MoodTracker']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    

    from datetime import date

    # Get the database
    db = get_database()
    # collection_name = db["MoodTracker"]

    intro()
