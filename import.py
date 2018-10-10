import pymysql
from xml.dom import minidom


# sudo apt-get install python3-pymysql
# sudo apt-get install python-pip
# pip install PyMySQL

db = pymysql.connect("localhost","homestead","secret" ,"testing")
def insert_cube_header(time):
	try:
		cursor = db.cursor()
		sql = "INSERT INTO cube_header(time) VALUES ('%s')" % (time)
		cursor.execute(sql)
		db.commit()
		return cursor.lastrowid
	except Exception as e:
		db.rollback()


def insert_cube_detail(cube_header_id, currency, rate):
	try:
		cursor = db.cursor()
		sql = "INSERT INTO cube_detail(cube_header_id, currency, rate) VALUES ('%s', '%s', '%s')" % (cube_header_id, currency, rate)
		cursor.execute(sql)
		db.commit()
	except Exception as e:
		db.rollback()

def get_latest_cube_detail(max_id):
	try:
		cursor = db.cursor()
		sql = "select a.time, b.currency,b.rate from cube_header a join cube_detail b on a.id = b.cube_header_id where year(a.time) = 2018 and month(a.time) = 10 and day(a.time) = 9 order by b.rate;"
		cursor.execute(sql)
		rows = cursor.fetchall()
		for row in rows:
			print(row)
	except Exception as e:
		db.rollback()


# TO DOWNLOAD XML DATA AND INSERT IT TO DATABASE
# xmldoc = minidom.parse('eurofxref-hist-90d.xml')
# cubelist = xmldoc.getElementsByTagName('Cube')
# for cube in cubelist:
# 	cube_time_childs = cube.childNodes
# 	if len(cube_time_childs) > 0:
# 		for cube_time in cube_time_childs:
# 			cube_time_childs = cube_time.childNodes
# 			if len(cube_time_childs) > 0:
# 				time = cube_time.attributes['time'].value
# 				cube_header_id = insert_cube_header(time)
# 				for cube in cube_time_childs:
# 					insert_cube_detail(cube_header_id, cube.attributes['currency'].value, cube.attributes['rate'].value)

# get latest cube detail (unfinished)
# get_latest_cube_detail(id)
