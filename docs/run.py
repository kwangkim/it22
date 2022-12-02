
import subprocess
import sys
section="demo"
name=sys.argv[1]
versions=[0,1,2,3]
if len(sys.argv)>2:
    versions=sys.arg[2:]
def make_pdf(name,showanswer,ver,papersize,filename):
    subprocess.run(["quarto","render", f"{name}.qmd", "-P", f"showanswer:{showanswer}","-P", f"ver:{ver}","-M",f"papersize:{papersize}","-o", f"{filename}.pdf"])
for ver in versions:
    for showanswer in [True,False]:
        ans="_ANS" if showanswer else ""
        papersize="letter" if showanswer else "legal"
        vletter=chr(65+ver) 
        filename=f"{section}_{name}{vletter}{ans}"
        make_pdf(name,showanswer,ver,papersize,filename)


