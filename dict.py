a={
    'name':"hari",
    'age':22,
    'address':'Nepal'
    
}
print(a)
print(type(a))
print(len(a))

print(a["age"])

a['address']='ktm'
a['phone']=9746449474

data={
    'name':'Bidur',
    'role':'developer'
}

a.update(data)

print(a)

fifa_world_cup_2026 = {
    "tournament": "FIFA World Cup 2026",
    "edition": 23,
    "hosts": ["United States", "Canada", "Mexico"],
    "start_date": "2026-06-11",
    "final_date": "2026-07-19",
    "teams": 48,
    "groups": 12,
    "teams_per_group": 4,
    "total_matches": 104,
    "group_stage_matches_per_team": 3,
    "qualification_format": {
        "automatic_qualifiers": "Top 2 teams from each group",
        "additional_qualifiers": "8 best third-placed teams",
        "total_knockout_teams": 32
    }
}


fifa = fifa_world_cup_2026['qualification_format']['automatic_qualifiers']
print(fifa)

data = {
    "name": "Sudan",
    "phone": [
        {"type": "NTC", "number": 9844},
        {"type": "Ncell", "number": 9806}
    ],
}
# Sudan NTC number is 9844
# Sudan Ncell number is 9806
print(f' {data["name"]} {data['phone'][0]['type']} number is {data["phone"][0]['number']} ')
print(f' {data["name"]} {data['phone'][1]['type']} number is {data["phone"][1]['number']} ')

print(fifa_world_cup_2026.get('to','Key value is not found'))

#items
#keys
#values