grade_max = float(input("What is your test max points?\nAnswer here: "))

def max_grade(max_points):
	oitenta_cinco = max_points * 0.85
	oitenta_quarto = max_points * 0.84
	setenta = max_points * 0.7
	sessenta_nove = max_points * 0.69
	cinquenta = max_points * 0.5
	quarenta_nove = max_points * 0.49
	vinte_oito = max_points * 0.28
	vinte_sete = max_points * 0.27

	all_grades = [oitenta_cinco, oitenta_quarto, setenta, sessenta_nove, cinquenta, quarenta_nove, vinte_oito, vinte_sete]

	def format_grades(grade):
		if grade % 1 == 0.5:
			return grade
		else:
			return round(grade)

	formatted_grades = [format_grades(grade) for grade in all_grades]

	if formatted_grades[0] == formatted_grades[1]:
		formatted_grades[0] += 0.5
   
	if formatted_grades[3] == formatted_grades[2]:
		formatted_grades[2] += 0.5

	if formatted_grades[4] == formatted_grades[5]:
		formatted_grades[4] += 0.5

	if formatted_grades[6] == formatted_grades[7]:
		formatted_grades[6] += 0.5

	print(f'''
	Your grades should be:
	   1 - {int(max_points)} - {formatted_grades[0]}
	   2 - {formatted_grades[1]} - {formatted_grades[2]}
	   3 - {formatted_grades[3]} - {formatted_grades[4]}
	   4 - {formatted_grades[5]} - {formatted_grades[6]}
	   5 - {formatted_grades[7]} - 0
    ''')

max_grade(grade_max)