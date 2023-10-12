def path():
    import os
    os.mkdir("img")
    for i in range(1,101):
        file_name="X4G{}.png".format(i)
        file_path = os.path.join("img", file_name)