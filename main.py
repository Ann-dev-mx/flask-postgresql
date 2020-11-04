import matplotlib.pyplot as plt
import psycopg2


con = psycopg2.connect(
    host="localhost",
    port="5432",
    database="check",
    user="postgres",
    password="admin"
    )
cur = con.cursor()
cur.execute("SELECT numberofmatch, numberofgoal, creaditsobtained FROM checktable ")
values = cur.fetchall()
print(values)
con.commit()
cur.close()

figure = plt.figure()
axes = figure.add_subplot(1, 1, 1)
axes.bar(
    range(len(values)),
    [values[1] for values in values],
    tick_label = [values[0] for values in values]

)
plt.show()