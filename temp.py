
spread_risk = input("Is the risk of fire spread in the area small, medium or high?"
                            "\nIf you do not know, ask the responsible fire department. ")

while spread_risk != "small" and spread_risk != "medium" and spread_risk != "high":
        spread_risk = input("This is neather 'small', 'medium', or 'high'."
                            "\nPlease check the risk of fire spread and insert on of the three terms.")