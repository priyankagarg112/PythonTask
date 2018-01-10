import json

def convert(keys):
    if keys:
        key=keys.pop()
        info=content['data']['100gm'][key]
        for index in range(len(info)):
            for sub_key in info[index].keys():
                if sub_key!='sub_cat':
                    value = info[index][sub_key]['quantity']
                    print "{} converted to: {}; {}; {}".format(value,(value)*0.23,(value)*0.50,float(value)*2.60)
                else:
                    for inner_index in range(len(info[index][sub_key])):
                        for sub_sub_key in info[index][sub_key][inner_index].keys():
                            if type(info[index][sub_key][inner_index][sub_sub_key]) == list:
                                for inner_inner_index in range(len(info[index][sub_key][inner_index][sub_sub_key])):
                                    for sub_sub_sub_key in info[index][sub_key][inner_index][sub_sub_key][inner_inner_index].keys():
                                        value = info[index][sub_key][inner_index][sub_sub_key][inner_inner_index][sub_sub_sub_key]['quantity']
                                        print "{} converted to: {}; {}; {}".format(value,(value)*0.23,(value)*0.50,float(value)*2.60)
                                    
                            else:
                                value = info[index][sub_key][inner_index][sub_sub_key]['quantity']
                                print "{} converted to: {}; {}; {}".format(value,(value)*0.23,(value)*0.50,float(value)*2.60)
        convert(keys)
    else:
        return

with open('data.json') as file_data:
    content = json.load(file_data)
keys=content['data']["100gm"].keys()
convert(keys)

