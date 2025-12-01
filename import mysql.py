import mysql.connector

# Kết nối đến MySQL
conn = mysql.connector.connect(
    host="localhost",       # hoặc IP server MySQL
    user="root",            # user MySQL
    password="250906", # mật khẩu bạn tạo
    database="qlbenhnhan" # tên database bạn vừa tạo
)

# Tạo con trỏ (cursor)
cursor = conn.cursor()

# Kiểm tra kết nối
cursor.execute("SELECT DATABASE();")
db = cursor.fetchone()
print("Đang kết nối tới database:", db)

# Đóng kết nối
cursor.close()
conn.close()