print("あたり1%ガチャシミュレーション")
atari = 0
kiroku = ''
count = 0

def gacha():
	r=Math.random()
	if r < 0.01:
		atari+=1
		document.getElementById('atari').innerHTML = atari
	count += 1
	document.getElementById('count').innerHTML = count

	kiroku = kiroku + ' ' + r
	document.getElementById('result').innerHTML = kiroku

gacha()
