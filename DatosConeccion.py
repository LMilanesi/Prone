import pymysql

timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db="defaultdb",
  host="prone-2024-prone-2024.k.aivencloud.com",
  password= DB_PASSWORD,
  read_timeout=timeout,
  port=11108,
  user="avnadmin",
  write_timeout=timeout,
)
