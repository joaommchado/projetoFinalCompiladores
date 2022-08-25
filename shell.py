from logging import raiseExceptions
import isiLanguage
from first_parser import firstParser

my_file = open(r"C:\Users\joao_\OneDrive\Desktop\Nova pasta\py-myopl-code\ep13\entrada.txt")
data = my_file.read()
data_into_list = data.split("\n")
my_file.close()
i = 0
print(data_into_list)

verificao = firstParser(data_into_list)
data_into_list, index, validador = verificao.retornar_final()

print(data_into_list)

if validador:
	while i < len(data_into_list):
		text = data_into_list[i]

		if text.strip() == "": continue
		result, error = isiLanguage.run('<stdin>', text)

		if error:
			print(error.as_string())
		
		elif result:
			if len(result.elements) == 1:
				if i in index:
					print(repr(result.elements[0]))

			else:
				if i in index:
					print(repr(result))
				else:
					continue
		i = i + 1
	else:
		raise("DECLARE O INICIO E O FIM DO PROGRAMA")
