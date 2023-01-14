# Тренировка со словарями 
# Есть супер герои. На миссию требуются герои высокого ранга (уровень силы от 80)
# Требуется составить список таких героев.

dict = {
    'Piter Parker': 30, 
    'Spider man': 80,
    'Roman Makulin': 99,
    'Batman': 70,
    'Joker': 55,
    'Superman': 90
}

new_dict = {key:val for key,val in dict.items() if val >= 80}
print('All heroes: ', dict)
print('Starting heroes: ', sorted(new_dict.items(), key = lambda dict:dict[1]))

