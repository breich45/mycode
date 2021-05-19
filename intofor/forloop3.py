#!/usr/bin/env python3


farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


for i in farms:
    x = i.get("name")
    y = i.get("agriculture")
    z = ", ".join(y)
    #print("In the", x, "you will find", z)
    print(f"In the {x} you will find {z}")
