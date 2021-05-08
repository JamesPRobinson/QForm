import csv
from csv import DictReader

fieldnames = {'EN' : ['Question 1','Question 2','Question 3','Question 4','Question 5','Question 6','Question 7','Question 8','Question 9','Question 10'],
              'IT' : ['Domanda 1','Domanda 2','Domanda 3','Domanda 4','Domanda 5','Domanda 6','Domanda 7','Domanda 8','Domanda 9','Domanda 10']}
def get_encoding(filename):
    return 'utf-8'

def generate_questions(country_code):
    questions_dict = {}
    filename = f"data/questions_{country_code}.csv"
    line_num = 0
    with open(filename, encoding=get_encoding(filename), mode='r') as file:
        reader = DictReader(file, fieldnames=fieldnames[country_code])
        for row in reader:           
            questions_dict[line_num] =  [row[e] for e in fieldnames[country_code]]
            line_num += 1
    return questions_dict
        
