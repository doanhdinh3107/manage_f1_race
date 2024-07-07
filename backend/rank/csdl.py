import sqlite3
#duong dan den csdl
path="C:\DRF\db.sqlite3"
#tao ket noi
connection=sqlite3.connect(path)
#tao con tro cursor thuc hien ket noi
cursor=connection.cursor()
#cau lenh muon thuc hien
sql="insert into rank_racer values(13,'https://media.formula1.com/image/upload/f_auto,c_limit,q_75,w_1320/content/dam/fom-website/drivers/2024Drivers/zhou','Dang Doanh','2003-7-31 02:21:45',1,5000,'sieu dep trai hoc gioi')"
#thuc thi cau lenh
cursor.execute(sql)
connection.commit()
cursor.close()
connection.close()
