import os

import csv

def split_dob(dob):
    re_arrange = []

    x = dob.split("-")

    #arrange list by MM/DD/YYYY
    re_arrange.extend([x[1],x[2],x[0]])

    arranged = '/'.join(re_arrange)

    return(arranged)

def social_security(ssn):

    x = ssn.split("-")

    x[0]='***'
    x[1]='**'
    # for number_list in x[:2]:
    #     # for numbers in range(len(number_list)):
    #         # x[x.index(number_list)]=number_list.replace(number_list[numbers],'*')
    #     print(number_list)
        
    # print(number_list)

    # number_list.replace(number_list[numbers],'*') for number_list in x[:2] for numbers in range(len(number_list)))
    
    social = '-'.join(x)
    
    return(social)

us_state_abbrev = {

    'Alabama': 'AL',

    'Alaska': 'AK',

    'Arizona': 'AZ',

    'Arkansas': 'AR',

    'California': 'CA',

    'Colorado': 'CO',

    'Connecticut': 'CT',

    'Delaware': 'DE',

    'Florida': 'FL',

    'Georgia': 'GA',

    'Hawaii': 'HI',

    'Idaho': 'ID',

    'Illinois': 'IL',

    'Indiana': 'IN',

    'Iowa': 'IA',

    'Kansas': 'KS',

    'Kentucky': 'KY',

    'Louisiana': 'LA',

    'Maine': 'ME',

    'Maryland': 'MD',

    'Massachusetts': 'MA',

    'Michigan': 'MI',

    'Minnesota': 'MN',

    'Mississippi': 'MS',

    'Missouri': 'MO',

    'Montana': 'MT',

    'Nebraska': 'NE',

    'Nevada': 'NV',

    'New Hampshire': 'NH',

    'New Jersey': 'NJ',

    'New Mexico': 'NM',

    'New York': 'NY',

    'North Carolina': 'NC',

    'North Dakota': 'ND',

    'Ohio': 'OH',

    'Oklahoma': 'OK',

    'Oregon': 'OR',

    'Pennsylvania': 'PA',

    'Rhode Island': 'RI',

    'South Carolina': 'SC',

    'South Dakota': 'SD',

    'Tennessee': 'TN',

    'Texas': 'TX',

    'Utah': 'UT',

    'Vermont': 'VT',

    'Virginia': 'VA',

    'Washington': 'WA',

    'West Virginia': 'WV',

    'Wisconsin': 'WI',

    'Wyoming': 'WY',

}


csvpath = os.path.join('..', 'Resources', 'employee_data.csv')

with open(csvpath, newline='') as csvfile, open('converted_employee_data.csv','w',newline='') as csvfile1:

    csvreader = csv.reader(csvfile, delimiter=',')

    header=next(csvreader)

    employee_id=[]
    name_first=[]
    name_last=[]
    date_of_birth=[]
    ssn=[]
    state=[]

    for i in csvreader:
        employee_id.append(i[0])
        name_first.append(i[1].split(" ")[0])
        name_last.append(i[1].split(" ")[1])
        date_of_birth.append(split_dob(i[2]))
        ssn.append(social_security(i[3]))
        state.append(us_state_abbrev[i[4]])

    header[1]='First Name'
    header.insert(2,'Last Name')

    new_data=[]
    for i in range(len(employee_id)):
        new_data.append([employee_id[i],name_first[i],name_last[i],date_of_birth[i],ssn[i],state[i]])

    new_data.insert(0,header)

    csv.writer(csvfile1).writerows(new_data)