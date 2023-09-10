
passpw = 'a123456'
retry = 3
while True:
	pw = input('請輸入密碼:')
	if pw == passpw:
		print('登入成功！')
		break
	else:
		retry = retry - 1
		print('密碼錯誤！還有',retry ,'次機會！')
		if retry == 0:
			break;


'''
passpw = 'a123456'
retry = 3
while retry > 0:
	pw = input('請輸入密碼:')
	if pw == passpw:
		print('登入成功！')
		break
	else:
		retry = retry - 1
		print('密碼錯誤！還有',retry ,'次機會！')
'''