products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)
#print(products[0][0])

for p in products:
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,名稱\n')#寫入檔案會形成亂碼，於是要再寫入時跟他說要用utf-8這個編碼
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')#加法只能字串跟字串