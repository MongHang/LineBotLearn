from pymongo import MongoClient
import datetime

stockDB = "line_bot_usage"
collection = "stock"


def constructor_stock():
   client = MongoClient(
       "mongodb://av2288444:t0955787053S@ac-gbnruue-shard-00-00.kt0hhit.mongodb.net:27017,ac-gbnruue-shard-00-01.kt0hhit.mongodb.net:27017,ac-gbnruue-shard-00-02.kt0hhit.mongodb.net:27017/?ssl=true&replicaSet=atlas-r0k35s-shard-0&authSource=admin&retryWrites=true&w=majority")
   db = client[stockDB]
   return db


def update_my_stock(user_name, stockNumber, condition, target_price):
    """
    更新暫存的股票名稱
    """
    db = constructor_stock()
    collection = db[user_name]
    collection.update_many(
        {"favorite_stock": stockNumber},
        {"$set": {"condition": condition, "price": target_price}}
    )
    content = f"股票{stockNumber}更新成功"

    return content


def write_my_stock(userID, user_name, stockNumber, condition, target_price):
    """
    新增使用者的股票
    """
    db = constructor_stock()
    collect = db[user_name]
    is_exist = collect.find_one({"favorate_stock": stockNumber})
    if is_exist != None:
        content = update_my_stock(user_name, stockNumber, condition, target_price)
        return content
    else:
        collect.insert_one(
            {
                "userID": userID,
                "favorite_stock": stockNumber,
                "condition": condition,
                "price": target_price,
                "tag": "stock",
                "date_info": datetime.datetime.now()
            }
        )

        return f"{stockNumber}已新增至您的股票清單"

# 秀出使用者的股票條件
def show_stock_setting(user_name, userID):
    db = constructor_stock()
    collect = db[user_name]
    datalist = list(collect.find({"userID": userID}))
    if datalist == []: return "您的股票清單為空，請透過指令新增股票至清單中"
    content = "您清單中的選股條件為:\n"
    for i in range(len(datalist)):
        content += f"{datalist[i]['favorite_stock']} {datalist[i]['condition']} {datalist[i]['price']}\n"
    return content


# 刪除使用者特定的股票
def delete_my_stock(user_name, stockNimber):
    db = constructor_stock()
    collect = db[user_name]
    collect.delete_one({"favorite_stock": stockNimber})
    return stockNimber + "刪除成功"

# 刪除使用者(全部股票)
def delete_my_allstock(user_name, userID):
    db = constructor_stock()
    collect = db[user_name]
    collect.delete_many({"userID": userID})
    return "全部股票刪除成功"
