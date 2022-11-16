file = input().split("\\")
text = file[-1]

file_name = text.split(".")[0] # така мога да взема първото от сплита
extension = text.split(".")[1] # а така второто


print(f"File name: {file_name}")
print(f"File extension: {extension}")