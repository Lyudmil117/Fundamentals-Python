n = int(input())
music_dict = {}

for i in range(n):
    information = input().split("|")
    piece = information[0]
    composer = information[1]
    key = information[2]

    music_dict[piece] = []
    music_dict[piece].append(composer)
    music_dict[piece].append(key)

command = input()


while command != "Stop":

    command = command.split("|")

    current_command = command[0]
    piece = command[1]
    # composer = command[2]
    # key = command[3]

    if current_command == "Add":
        composer = command[2]
        key = command[3]
        if piece in music_dict:
            print(f"{piece} is already in the collection!")
        else:
            music_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif current_command == "Remove":
        if piece in music_dict:
            music_dict.pop(piece)
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    elif current_command == "ChangeKey":
        new_key = command[2]
        if piece in music_dict:
            music_dict[piece][1] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    command = input()

for misic in music_dict:
    print(f'{misic} -> Composer: {music_dict[misic][0]}, Key: {music_dict[misic][1]}')
#обърни внимание че тук използваме MUSIC а не music_dict[key] зариди това, че тук правим цикъла с MUSIC
