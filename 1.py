with open("saved_calendars.txt", "r") as f:
    w = csv.DictReader(f, ["author_id", "name", "description", "ets", "eta", "users", "period"])

    for i in w:
        if i["author_id"] == "author_id":
            continue
        author_id = i["author_id"]
        name = i["name"]
        description = i["description"]
        data_1 = i["ets"]
        data_list1 = re.findall("\d+", data_1)
        yy1 = int(data_list1[0])
        mm1 = int(data_list1[1])
        dd1 = int(data_list1[2])
        hh1 = int(data_list1[3])
        mm1 = int(data_list1[4])
        ss1 = int(data_list1[5])
        ets = datetime.datetime(yy1, mm1, dd1, hh1, mm1, ss1)
        data_2 = i["eta"]
        data_list2 = re.findall("\d+", data_2)
        yy2 = int(data_list2[0])
        mm2 = int(data_list2[1])
        dd2 = int(data_list2[2])
        hh2 = int(data_list2[3])
        mm2 = int(data_list2[4])
        ss2 = int(data_list2[5])
        eta = datetime.datetime(yy2, mm2, dd2, hh2, mm2, ss2)
        users = ast.literal_eval(i["users"])
        period = int(i["period"])
        event = Event.Event(author_id, name, description, ets, eta, users, period)
        events.append(event)