import sqlite3

conn = sqlite3.connect('myquotes.db')
curr = conn.cursor()

# curr.execute("""create table quotes_tb(
#     title text,
#     author text,
#     tags text
# )
# """)

curr.execute("""
insert into quotes_tb values('hellooooooo','mama', '["sdjhf","sdfsdf"]')
""")



conn.commit()
conn.close()