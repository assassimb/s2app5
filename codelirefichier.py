import os
import argparse

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(prog="testargument parser")
    parser.add_argument('-d', required=True, help='ok')
    args = parser.parse_args()

    cwd = os.getcwd()
    rep_aut = os.path.join(cwd, "TextesPourEtudiants")
    
    print(rep_aut)
    if os.path.isabs(args.d):
        rep_aut = args.d
    else:
        rep_aut = os.path.join(rep_aut, args.d)
        
    rep_aut = os.path.normpath(rep_aut)
    
    authors = os.listdir(rep_aut)
    print(authors, len(authors))
    
    i = 0
    for i in range(len(authors)):
        print("aaa")
        