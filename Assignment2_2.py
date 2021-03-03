def avg(data):
    total = 0
    for i in range(data["count"]):   
        total += data["employees"][i]["salary"]
    ans = total / data["count"]
    print(ans)




avg({"count":3, "employees":[{"name":"John", "salary":30000 },
                                {"name":"Bob", "salary":60000 },
                                {"name":"Jenny", "salary":50000 }]})

