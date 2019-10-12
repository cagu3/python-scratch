import shutil, os, datetime
from PIL import Image


# Find N newest files in a list of files!
def n_max_elements(list1, n):
    final_list = []

    for i in range(0, n):
        max1 = list1[0]
        for j in range(len(list1)):
            if os.path.getctime(list1[j]) > os.path.getctime(max1):
                max1 = list1[j]
        list1.remove(max1)
        final_list.append(max1)

    return final_list


# Find the newest pics! (Those are the spotlight pics)
def find_newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return n_max_elements(paths, 6)


# Copy pics to another folder!
def copy():
    files = find_newest(r'C:\Users\cguthrie\AppData\Local\Packages\Microsoft.Windows.'
                        r'ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets')
    for file in files:
        shutil.copy(file, r'C:\Users\cguthrie\Pictures\Background\test')
    print("Finished copying background pictures")


# Delete the vertical pics cause they look bad with landscape monitors!
def delete_vertical_pics():
    copy()
    path = r'C:\Users\cguthrie\Pictures\Background\test'

    files = os.listdir(path)
    for file in files:
        im = Image.open(path + '\\' + file)
        sizes = im.size
        im.close()
        if sizes[0] < sizes[1]:
            os.remove(path + '\\' + file)
            print("Removed " + file + '   X')


# Make nicer looking file names!
def create_file_name(i):
    now = datetime.datetime.now()
    path = r'C:\Users\cguthrie\Pictures\Background\test'
    return path + '\\' + now.strftime("%Y-%m-%d") + '_' + str(i) + '.jpg'


# Rename the files so they are more clear!
def rename():
    delete_vertical_pics()
    path = r'C:\Users\cguthrie\Pictures\Background\test'

    files = os.listdir(path)
    i = 1
    for file in files:
        old_name = path + '\\' + file
        new_name = create_file_name(i)
        os.rename(old_name, new_name)
        i += 1
    print("Renamed all files to date_i.jpg")


# Finally, move the files into the bg folder!
def move_to_bg():
    rename()
    path = r'C:\Users\cguthrie\Pictures\Background'

    files = os.listdir(path + '\\test')
    for file in files:
        src = path + '\\test\\' + file
        dst = path + '\\' + file
        shutil.move(src, dst)
        print("Moved " + file)


# This does everything!! kinda
move_to_bg()
