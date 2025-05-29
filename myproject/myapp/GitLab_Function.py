
import gitlab
import requests
import certifi
import csv
import time
import os

import urllib3

# connect to gitlab


def create_gitlab_epic_hierarchy(group_path, TopLevel):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    TOKEN = "glpat-AXK_YZpDUWDY2g-t3FQw"

    # connection with GitLab
    # TOKEN = 'TWÓJ_TOKEN'
    gl = gitlab.Gitlab('https://gitlab.com/', private_token=TOKEN, ssl_verify=False)

    # get the group

    group = gl.groups.get(group_path)

    ################################### MAIN EPIC
    main_epic = group.epics.create({
        'title': f'PROJECT {TopLevel}',
        'description': 'Top-level epic for the project',
        'labels': ['Initiative Level::Top Level'],
    })

    ################################### LEVEL 1

    level1_epics_Titles = [
        '01. F2B Analysis',
        '02. IT Delivery'
    ]

    level1_epics_Descriptions = [
        '1. Epic related to the requirements creation by F2B Product Managers ',
        '2. Epic created for IT delivery for purpose of tracking development of the project by IT PODs'
    ]

    level1_epics = []

    for idx in reversed(range(len(level1_epics_Titles))):
        epic = group.epics.create({
            'title': f'{TopLevel} {level1_epics_Titles[idx]}',
            'parent_id': main_epic.id,
            'description': f'{level1_epics_Descriptions[idx]}',
            'labels': ['Initiative Level::Theme'],
        })
        level1_epics.append(epic)
    ################################### LEVEL 2

    level2_1_epics_Titles = [
        '01. Standard Scope',
        '02. CRs'
    ]

    level2_1_epics_Descriptions = [
        '1. Scope defined at the beginning of the project ',
        '2. Scope which increased due to new requirements'
    ]

    level2_2_epics_Titles = [
        '01. Analysis',
        '02. Development'
    ]

    level2_2_epics_Descriptions = [
        '1. Analysis',
        '2. Development'
    ]

    level2_epics = []

    # 3. Dla każdego Level 1 epica, stwórz po 2 dzieci (Level 2)
    for parent in level1_epics:
        if '1. F2B Analysis' in parent.title:
            for idx in reversed(range(len(level2_1_epics_Titles))):
                epic = group.epics.create({
                    'title': f'{TopLevel} {level2_1_epics_Titles[idx]}',
                    'parent_id': parent.id,
                    'description': f'{level2_1_epics_Descriptions[idx]}',
                    'labels': ['Initiative Level::Stream'],
                })
                level2_epics.append(epic)
        if '2. IT Delivery' in parent.title:
            for idx in reversed(range(len(level2_2_epics_Titles))):
                epic = group.epics.create({
                    'title': f'{TopLevel} {level2_2_epics_Titles[idx]}',
                    'parent_id': parent.id,
                    'description': f'{level2_2_epics_Descriptions[idx]}',
                    'labels': ['Initiative Level::Stream'],
                })
                level2_epics.append(epic)

    print(f"Hierarchy of the epics have been created for the project {TopLevel}")

    print('ok')