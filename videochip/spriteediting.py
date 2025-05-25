# times=3: 30,30,30,20,20,20,10,10,10
import spritedrawer
from copy import deepcopy
def StrechSprite(SpriteEditing, Times):
    SpriteEdit = spritedrawer.GetrownumbersSpritedrawer(SpriteEditing)
    print("sprite edit:", SpriteEdit)
    tmp = len(SpriteEdit[0])
    print("tmp:", tmp)
    k = 1
    for row in SpriteEdit:
        tmp_list = deepcopy(row)
        for i in range(tmp):
            for j in range(Times):
                row.insert(k, tmp_list[i])
                k += 1
            k += 1
        k = 1
        # for j in range(Times):
        #     row.insert(i, row[k])
        #     i += 1
        # i += 1
        # k += 1
        # print(k)
        # print(j)
    print("sprite edit:", SpriteEdit)
    open(SpriteEditing, 'w').close()  # Clear the file before writing
    for row in SpriteEdit:
        with open(SpriteEditing, 'a') as file:
            file.write(','.join(row) + '\n')
def size(SpriteEditing, Times):
    StrechSprite("videochip/test.txt",Times)
    # SpriteEditing: 
    SpriteEdit = spritedrawer.GetrownumbersSpritedrawer(SpriteEditing)
    # Only duplicate lists (rows) inside SpriteEdit, not elements within rows
    new_SpriteEdit = []
    for row in SpriteEdit:
        for i in range(Times):
            new_SpriteEdit.append(deepcopy(row))
    SpriteEdit[:] = new_SpriteEdit  # Replace original with duplicated rows

    # Save the modified SpriteEdit back to the file
    open(SpriteEditing, 'w').close()  # Clear the file before writing
    for row in SpriteEdit:
        with open(SpriteEditing, 'a') as file:
            file.write(','.join(row) + '\n')

        

    # first we will take each row and take each item ex, 10,20, and add however many more times we want to add: ex: 10,10,10 becomes 10,10,10,10,10,10,10,10,10 if we were to size it by 3.
    #aftewards, we'll take each row and add a new item each time.

size("videochip/test.txt",10)
