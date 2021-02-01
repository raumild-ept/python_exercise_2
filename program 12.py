#required dictionary database created.
#attandance_list and working hours list defined
emp_dict =  {
            101:{   'name': 'Anupriya Roy',
                    'depart_id':1,
                    'attendances':[{'date':1, 'hours':[3.5,4.5]},{'date':2, 'hours':[3.2,4.5]},{'date':3, 'hours':[3.2,4.6]},
                                 {'date':4, 'hours':[3.0,4.5]},{'date':5, 'hours':[2.5,4.5]},{'date':6, 'hours':[1.5,4.5]},
                                 {'date':7, 'hours':[2,3]},{'date':8, 'hours':[0,4.5]},{'date':9, 'hours':[2,3.5]},
                                 {'date':10, 'hours':[4,3.5]}],
                    'leaves':[{'date':7, 'no_of_hours':1.5},{'date':7, 'no_of_hours':1.5},{'date':8, 'no_of_hours':3}]
                },
            102:
             {   'name': 'Kadambari Sharma',
                 'depart_id':1,
                 'attendances':[{'date':1, 'hours': [0,4.5]},{'date':2, 'hours':[3.2,0]},{'date':3, 'hours':[3.2,4.6]},
                                {'date':4, 'hours':[1,4.5]},{'date':5, 'hours':[2.5,2]},{'date':6, 'hours':[1.5,1]},
                                {'date':7, 'hours':[2,4]},{'date':8, 'hours':[1,4.5]},{'date':9, 'hours':[2,2]},
                                {'date':10, 'hours':[2,3.5]}],
                 'leaves':[{'date':1, 'no_of_hours':3.5},{'date':2, 'no_of_hours':2},{'date':2, 'no_of_hours':2}]
             },
            103:
            {   'name': 'Abhishek Verma',
                'depart_id':1,
                'attendances':[{'date':3, 'hours':[3.2,4.6]},{'date':4, 'hours':[1,4.5]},{'date':5, 'hours':[2.5,2]},
                            {'date':6, 'hours':[1.5,1]},{'date':7, 'hours':[2,4]},{'date':8, 'hours':[1,4.5]},
                            {'date':9, 'hours':[2,2]},{'date':10, 'hours':[2,3.5]}
                ],
                'leaves':[{'date':1, 'no_of_hours':3},{'date':2, 'no_of_hours':2},{'date':2, 'no_of_hours':3}]
            }
}
emp_attendance_data_list = list()
emp_working_hours_list = list()
#to count attandance hours.
def count_attendance(emp_code):
    return sum(map(lambda a:sum(a['hours']),emp_dict[emp_code]['attendances']))

#to count leave hours
def count_leaves(emp_code):
    return sum(list(map(lambda a:a['no_of_hours'],emp_dict[emp_code]['leaves'])))

def less_than_seven(emp_code):
    #return list(map(lambda a:a['date'] if (sum(a['hours'])<7) else False,emp_dict[emp_code]['attendances']))
    new_list= list(filter(lambda a:a['date'] if sum(a['hours'])<7 else False ,emp_dict[emp_code]['attendances']))
    dates = list(map(lambda a:a['date'],new_list ))
    dates_hours = list(map(lambda a:sum(a['hours']),new_list))
    return dates,dates_hours
#list creator.
def do_things():
    for employee_code, employee_data in emp_dict.items():
        emp_attendance_hours = count_attendance(employee_code)
        emp_leave_hours = count_leaves(employee_code)
        date_list_less_then_seven_hours,hour_list = less_than_seven(employee_code)
        remaining_hours_list_by_date = list(map(lambda a: 8 - a, hour_list))

        emp_attendance_data_list.append({'employee_id':employee_code,
                                     'employee_name':employee_data['name'],
                                     'employee_attendance_hours':emp_attendance_hours,
                                     'emp_leave_hours':emp_leave_hours})
        emp_working_hours_list.append({employee_code:
                                       {
                                        'date':date_list_less_then_seven_hours,
                                        'total_hours': hour_list,
                                        'remaining_hours': remaining_hours_list_by_date
                                       }})
do_things()
# #printing the lists.
print(emp_attendance_data_list)
print(emp_working_hours_list)