IN_FILENAME = "attendees.csv"

NUM_COPIES = 3

LOGO1 = "\includegraphics[trim=20 0 20 90, height=0.5cm]{pics/RiSE_LogoRGB_100323.eps}"
LOGO2 = "\includegraphics[trim=0 10 0 10, height=0.5cm]{pics/vcla_below_1_CMYK.pdf}"
LOGO3 = "\includegraphics[trim=275 275 275 275, height=0.5cm]{pics/logics}"

# Adjust to accomodate for input format
# e.g. change to identity function, if each line contains the wanted tag
def BEAUTIFY_NAMES(x):
  a,b = str.split(x.strip(), ",")
  return a.title(), b.title()

# Adjust to accomodate for input format
# e.g. do nothing, if each line contains the wanted tag
def PREPROCESS(f):
  #get rid of head
  f.readline()

################################################################################

HEADER = """\documentclass[a4paper,12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{tikz}
\usepackage[left=0cm,top=0cm,right=0cm,bottom=0cm,verbose,nohead,nofoot]{geometry}

\\begin{document}
\\thispagestyle{empty}


\\begin{tikzpicture}[remember picture,overlay, anchor = west,
font=\sffamily\huge]
"""

FOOTER = """
\end{tikzpicture}

\end{document}
"""

def make_labels(names, start, end):
  label_height = 3.52
  out = open("tex_files/labels_"+ str(start) + "_" + str(end) + ".tex", 'w')
  out.write(HEADER)
  k = 0
  for i in range(0,len(names),2):
    top_offset = -k * label_height - 0.3
    name = names[i][0] + " " + names[i][1]
    out.write("""\\node[anchor=north,minimum height="""+ str(label_height) +"""cm, minimum width=9.2cm, text width=7.5cm, align=left] (names) at (4.7cm, """ + str(top_offset) + """cm) {};""")
    out.write("\\node[below right=0.5cm] at (names.north west) {" +name+ "};")
    out.write("\\node[above right=0.5cm] (logo1) at (names.south west) {" + LOGO1 + "};")
    out.write("\\node[right=0.9cm] (logo2) at (logo1.east) {" + LOGO2 + "};")
    out.write("\\node[right=0.9cm] (logo3) at (logo2.east) {" + LOGO3 + "};\n\n")

    if i+1 < len(names):
      name = names[i+1][0] + " " + names[i+1][1]
      out.write("""\\node[anchor=north,minimum height="""+ str(label_height) +"""cm, minimum width=9.2cm, text width=7.5cm, align=left] (names) at (14.8cm, """ + str(top_offset) + """cm) {};""")
      out.write("\\node[below right=0.5cm] at (names.north west) {" +name+ "};")
      out.write("\\node[above right=0.5cm] (logo1) at (names.south west) {" + LOGO1 + "};")
      out.write("\\node[right=0.9cm] (logo2) at (logo1.east) {" + LOGO2 + "};")
      out.write("\\node[right=0.9cm] (logo3) at (logo2.east) {" + LOGO3 +
      "};\n\n")

    k = k + 1
  out.write(FOOTER)
  out.close()

f = open(IN_FILENAME)
PREPROCESS(f)

names = f.readlines()

corr_names = sorted(map(lambda x: BEAUTIFY_NAMES(x), names), key=lambda name: name[1])

all_names = NUM_COPIES*corr_names

for n in range(0,len(all_names), 16):
    start = 1*n
    end = 1*n+16
    make_labels(all_names[start:end], start, end)
