

'''

Answer:

I have used core python for this solution , Although we can aslo approch it with pandas module

'''

import os
def main(log_file_name):
    try:
        with open(log_file_name,'r') as f:
            lines = f.readlines()

        eater_id_records = {}
        fooditem_record = {}

        for l in lines:
            single_record = l.split(",")

            eater_id = single_record[0].split(":")[1].strip()
            foodmenu_id = single_record[1].split(":")[1].strip()

            # print(eater_id,foodmenu_id)
            if eater_id not in eater_id_records:
                eater_id_records[eater_id] = [foodmenu_id]
            elif foodmenu_id in eater_id_records[eater_id]:
                print(f"Error : More than One Foodmenu id in single eater_id in {log_file_name}")
                return
            else:
                eater_id_records[eater_id].append(foodmenu_id)
            

            # print(fooditem_record)
            if fooditem_record.get(foodmenu_id):
                fooditem_record[foodmenu_id] +=1

            else:
                fooditem_record[foodmenu_id] = 1

            

        list_sorted = sorted(fooditem_record.items(),key=lambda x:x[1],reverse=True)
        print(f"Top 3 menu item consumed for {log_file_name}")
        for food_item in list_sorted[:3]:
            print(f"Food item {food_item[0]} consumed {food_item[1]} times")

    except Exception as e:
        print("Error while processing log file ",e)

    # print(eater_id_records)

# main('test_case_1.txt')

for file_ in os.listdir():
    if "txt" in file_:
        main(file_)
        print("-------------------------")

    


