import subprocess
try:
    result = subprocess.run(["git","status","--porcelain"""], capture_output=True, text=True)
    if result.returncode == 0:
        list_output = result.stdout.strip().split("\n")
        new_list = ['']
        choices = int(input("Commit all? (1-y/2-n)"))
        if choices == 2:
            print("Choose which number to commit:")
            num = 1
            for i in range(len(list_output)):
                print([num],list_output[i].strip())
                new_list.append(list_output[i])
                num +=1
            u_i = int(input("Enter:"))
            try:
                if u_i:
                    choose = new_list[u_i].strip()
                    if choose.startswith("M"):
                        subprocess.run(["git", "add", choose[1:].strip()])
                        commit_name =input("Enter commit name:")
                        subprocess.run(["git", "commit", "-m",commit_name])
                    elif choose.startswith("?"):
                        subprocess.run(["git", "add", choose[2:].strip()])
                        commit_name =input("Enter commit name:")
                        subprocess.run(["git", "commit", "-m",commit_name])
            except Exception as e:
                print(e)
        else: 
            subprocess.run(["git", "add", "."])
            subprocess.run(["git", "commit", "-m", "Auto-commited all changes files"])
    else: 
        print("No files changes.")
except Exception as e:
    print(e)
