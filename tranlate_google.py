
import urllib2
def translate(to_translate, to_langage="auto", langage="auto"):
	agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
	before_trans = 'class="t0">'
	link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_langage, langage, to_translate.replace(" ", "+"))
	#print link
	request = urllib2.Request(link, headers=agents)
	page = urllib2.urlopen(request).read()
	result = page[page.find(before_trans)+len(before_trans):]
	result = result.split("<")[0]
	return result

if __name__ == '__main__':
	file_name = raw_input('Enter csv file name:')
	row_name = raw_input('Enter row name:')
	with open(file_name, 'r') as f, open('out.csv', 'w') as out:
		first_line = f.readline()
		first_line = out.write(first_line.replace('\n', ','+ row_name +"\n"))
		for i in f:
			name_ru = i.split(',')[4]
			name_uk = translate(name_ru, 'uk', 'ru')
			if '&#39;' in name_uk:
				name_uk = name_uk.replace('&#39;', '\'')	
			print name_uk	
			out.write(i.replace('\n', ','+ name_uk.title() +"\n"))
