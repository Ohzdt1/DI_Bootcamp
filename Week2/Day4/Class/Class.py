with open("names.txt", encoding = 'utf-8') as f:
    content =f.read()
    # for line in lines:
    #     if "Luke" in line:
    #         "Luke".append(line.strip() + " SkyWalker\n")
    #     else:
    #         "Luke".append(line)

    print(content)

---------------------------------------------------------------------------------------------
    import os

# Get the path of the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to file.txt
file_path = os.path.join(script_dir, "file.txt")