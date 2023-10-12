import os

cesta_repo = "C:/Users/papay/Documents/git/"

def pridaj_subor(nazov, repozitar):
    os.chdir(repozitar)
    os.system("git add " + nazov)
    return

def git_commit(sprava, repozitar):
    os.chdir(repozitar)
    os.system("git commit -m \"" + sprava + "\"")
    return

def git_push(repozitar):
    os.chdir(repozitar)
    os.system("git push")
    return

file = open(cesta_repo+"novy.txt", "w")
file.write("Náhodný text")
file.close()

pridaj_subor("novy.txt", cesta_repo)
git_commit("Commit cez skript", cesta_repo)
git_push(cesta_repo)




