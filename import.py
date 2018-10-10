import pymysql


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

# get latest cube detail (unfinished)
# get_latest_cube_detail(id)
