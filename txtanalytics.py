data = []
with open('review.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
print('檔案讀取完了, 總共有', len(data), '筆資料')
print(data)

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 5:
		new.append(d)
print(len(new))
print('一共有', len(new), "資料小於5")

good = []
for d in data:
	if 'ramen' in d:
		good.append(d)
print(good)
print('ramen' in good)