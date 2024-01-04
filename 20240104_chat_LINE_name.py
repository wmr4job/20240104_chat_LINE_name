with open('3.txt', 'r', encoding='utf-8-sig') as f:
	text = [] # 儲存讀取的內容
	for line in f:
		text.append(line.strip().split(' ')) # 去除分行、依空格切割

	# 對話紀錄格式為 時間說話者 內容
	for word in text:
		name = word[0][5:] # 字串也可以透過清單分割的方式來取值
		print(name)

