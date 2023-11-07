import Project5Start

game_data = Project5Start.get_project5_data()

menu_text = """
[1] Find largest total sales
[2] Find latest release
[3] Find oldest release
[4] Find highest price
[5] Add new Game
[6] Exit program
"""
while True:
    print(menu_text)
    choice = input("please enter the number of your selection:")
    if '1' in choice:
        largest_sales = 0
        for game in game_data:
            if largest_sales < game['total_sales']:
                largest_sales = game['total_sales']
        print(f"the highest money making 2d Game on steam made {largest_sales}")
    elif '2' in choice:
        latest_release = game_data[0]
        for game in game_data:
            if game['release']> latest_release['release']:
                latest_release = game
        print(f"{latest_release['name']} was released most recently")
    elif '3' in choice:
        pass
    elif '6' in choice:
        break
    else:
        print(f" {choice} not yet implemented, please choose something else")