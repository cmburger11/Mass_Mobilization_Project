import os

demands_display_dict = {
    'demand_labor_wage_dispute':
        [1, 'Labor or wage dispute', '[Labor or wage dispute]  SELECTED'], 
        
    'demand_land_farm_issue':
        [2, 'Land or farm issue', '[Land or farm issue]  SELECTED'],
        
    'demand_police_brutality':
        [3, 'Police brutality', '[Police brutality]  SELECTED'], 
        
    'demand_political_behavior_or_process':
        [4, 'Political behavior or process', '[Political behavior or process]  SELECTED'],
        
    'demand_price_hike_or_tax_policy':
        [5, 'Price hike or tax policy', '[Price hike or tax policy]  SELECTED'], 
        
    'demand_removal_of_politician':
        [6, 'Removal of politician', '[Removal of politician]  SELECTED'],
        
    'demand_social_restrictions':
        [7, 'Social restrictions', '[Social restrictions]  SELECTED']
}

demands_comp_dict = {
    'demand_labor_wage_dispute':0,
    'demand_land_farm_issue':1,
    'demand_police_brutality':0, 
    'demand_political_behavior_or_process':0,
    'demand_price_hike_or_tax_policy':0, 
    'demand_removal_of_politician':0,
    'demand_social_restrictions':1
}

demands_input = "Enter here:  "
demands_valids = ["1", "2", "3", "4", "5", "6", "7", ""]


def display_demand_set():
    os.system("clear")
    for key in demands_display_dict.keys():
        if demands_comp_dict[key] == 1:
            print(f"{demands_display_dict[key][0]}. {demands_display_dict[key][2]}")
        else:
            print(f"{demands_display_dict[key][0]}. {demands_display_dict[key][1]}")

def swap_demand_truth(entry):
    for key in demands_display_dict.keys():
        if int(entry) == demands_display_dict[key][0]:
            if demands_comp_dict[key] == 0:
                demands_comp_dict[key] = 1
            else:
                demands_comp_dict[key] = 0


def validate_input(input_str, valids):
    while True:
        entry = input(input_str)
        if entry not in valids:
            print("That is not an acceptable input.")
            continue
        else:
            break
    return entry


while True:
    display_demand_set()
    entry = validate_input(demands_input, demands_valids)
    if entry == "":
        break
    else:
        swap_demand_truth(entry)
        continue



























