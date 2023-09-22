import pandas as pd
#
docxl = pd.read_excel("lab_pi_101.xlsx")
count = docxl.shape[0]
group = docxl['Группа'].str.contains('ПИ101').sum()
namegroup = docxl[docxl['Группа'] == "ПИ101"]
countest = len(docxl[docxl['Группа'] == 'ПИ101']['Личный номер студента'].unique())
numstud = len(namegroup['Личный номер студента'].unique())
uniqpi101 = docxl.loc[docxl["Группа"] == "ПИ101", "Личный номер студента"].unique()
control = docxl['Уровень контроля'].unique()
year =sorted(docxl['Год'].unique())
print('В исходном датасете содержалось', count, 'оценок, из них', group, 'оценок относятся к группе ПИ101.', "\n" , 
"В датасете находятся оценки", countest, "студентов ПИ101 с следующими личными номерами:", ', '.join(map(str, uniqpi101)), "\n",
"Используемые формы контроля:" , ', '.join(map(str, control)), "\n",
"Данные представлены по следующим учебным годам:", ', '.join(map(str, year)))