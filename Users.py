import csv
import sign_in

header = ['Username', 'Password', 'Points']
data = []


# checking if the username is taken, and return False if not.
def user_name_taken(username):
    check_user_name = False
    for i in range(len(data)):
        if data[i][0] == username:
            check_user_name = True
            break
    return check_user_name


# if the username is not taken, add a new user to the data list
def add_new_user(username, password):
    points = 0
    data.append([username, password, points])
    # return username


# checking if the username and password match
def check_user_and_password(user_name, password):
    correct_password = False
    for i in range(len(data)):
        if data[i][0] == user_name:
            if data[i][1] == password:
                correct_password = True
                break
    return correct_password


# updating the csv file
def update_users_csv():
    with open('Users.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)


# return a list of usernames sorted by biggest number of points to the smallest number
def winner(users_list):
    points_list = []
    users_sort_by_points_list = []
    for i in range(len(data)):
        points_list.append(data[i][2])
    points_list.sort()
    points_list.reverse()
    for i in range(len(points_list)):
        for j in range(len(points_list)):
            if points_list[i] == data[j][2]:
                users_sort_by_points_list.append(users_list[j])
    return users_sort_by_points_list


users_list = []
run = True
while run:
    # username, password, point = sign_in.log_in()
    username = input("name")
    password = input("password")
    if not user_name_taken(username):
        add_new_user(username, password)
        update_users_csv()
    # if username == "done":
    #     for i in range(len(data)):
    #         users_list.append(data[i][0])
    #     print(winner(users_list))
