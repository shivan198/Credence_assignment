import pandas as pd
import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb=client['Movies']
movieinfo = mydb.movieinfo

df = pd.read_json("file.json")

for i in df.index:
    val = df.iloc[i]
    # print(val['name'],val['img'],val['summary'])
    movieinfo.insert_one({"name":val['name'],"img":val['img'],"summary":val['summary']})

while True:
    print(" '0' to quit")
    print(" '1' to create a record")
    print(" '2' to read the database")
    print(" '3' to update the database")
    print(" '4' to delete the database")
    val = input("Enter a value : ")
    if val=='0' or val=='1' or val=='2' or val=='3' or val=='4':
        if val=='0':
            break
        elif val=='1':
            name = input("Enter name of the movie = ")
            img = input("enter link of image = ")
            summary = input("enter summary of the movie = ")
            movieinfo.insert_one({"name":name,"img":img,"summary":summary})

        elif val=='2':
            key = input("Enter key of the database either name or img or summary = ")
            # value = input("Enter the respective value = ")
            # value = value.strip()
            # value = value.lower()
            key=key.strip()
            key = key.lower()
            query = {key:"Harry Potter and the Order of the Phoenix"}
            result = movieinfo.find({},{key:1})
            for i in result:
                print(i)
            # print(result)

        elif val=='3':
            key = input("Enter the key you want to update either name or img or summary = ")
            value = input("Enter the respective value = ")
            value = value.strip()
            key=key.strip()
            key = key.lower()
            query = {key:value}
            present_data = movieinfo.find_one(query)
            key1 = input("Enter new key = ")
            value1 = input("Enter the new value = ")
            value1 = value1.strip()
            value1 = value1.lower()
            key1=key1.strip()
            key1 = key1.lower()
            new_data = {key1:value1}
            try:
                result = movieinfo.update_one(present_data,{"$set":new_data},upsert=True)
                if result.matched_count > 0 :
                    print("one record updated succesfully.")
                else:
                    print("Enter corect values, query was unsuccesful.")
            except:
                print("Enter corect values, query was unsuccesful.")
            

        elif val=='4':
            key = input("Enter the key you want to delete either name or img or summary = ")
            value = input("Enter the respective value = ")
            value = value.strip()
            # value = value.lower()
            key=key.strip()
            key = key.lower()
            query = {key:value}
            try:
                result = movieinfo.find_one(query)
                if len(result)>0 :
                    movieinfo.delete_one(query)
                    print("one record deleted succesfully.")
                else:
                    print("Enter corect values, query was unsuccesful.")
            except:
                print("Enter corect values, query was unsuccesful.")

    else:
        print("Enter a correct value")

