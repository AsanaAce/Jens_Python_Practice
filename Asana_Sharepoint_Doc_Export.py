'''
Created on Jun 24, 2024

@author: tcampbel
'''
from Task_Scripts.Get_Tasks_From_Project import get_ship_numbers
from Task_Scripts.GetAttachmentsFromObject import get_attachments_from_tasks

project_id = '1207554779947807'

ship_data = get_ship_numbers(project_id)

ship_data_list = [item for item in ship_data]


task_gid_list = []
ship_num_list = []

for i in range(len(ship_data_list)):
    task_gid_list.append(ship_data_list[i]['gid'])
    ship_num_list.append(ship_data_list[i]['custom_fields'][1]['text_value']) 

for task, ship in zip(task_gid_list, ship_num_list):
    get_attachments_from_tasks(task, ship)