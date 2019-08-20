import matplotlib.pyplot as plt
import csv


hour = []
users = []
commits_num = []

with open("/Users/dsivan/Brodmann/BIrodmann/test/report_output/result.csv",'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(plots)
    for row in plots:
        hour.append(int(row[0]))
        users.append(int(row[1]))
        commits_num.append(int(row[2]))

ax1 = plt.subplot(1,1,1)
pop=ax1.bar(hour,users,width=0.5,color='b',align='center')
ax2 = ax1.twinx()
users=ax2.bar(hour,commits_num,width=0.2,color='g',align='center')

# ax.bar(users, commits_num, width=1, color='g', align='center')




plt.title('Top N commited users per hour')
plt.legend()
plt.show()