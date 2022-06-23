def serch():

	tablica = eval(input('Podaj tablice [ , ]\n'))
	liczba = int(input('Podaj sume liczb jaka chcesz otrzymac\n'))
	for x in range(0, len(tablica)):
		for y in range(0, len(tablica)):
			if tablica[x]+tablica[y] == liczba and x != y:
				print(f'{x},{y}')
				return 0
			#else:
				#print("nie ma takiej sumy")

if __name__ == '__main__':
	serch()