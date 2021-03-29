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
