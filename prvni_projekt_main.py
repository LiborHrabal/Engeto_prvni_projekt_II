# Prvni projekt analyza textu. Projekt k opakovani cviceni 1-4.
# Zadani

#Zadani textu
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
oddelovac = "-" * 40
uzivatele = {"bob":"123", "ann": "pass123", "mike": "password123", "liz":"pass123"}

jmeno = input("Zadej jmeno: ").lower()
heslo = input("Zadej heslo: ").lower()

print(oddelovac,
      "\n" + "Welcome to the app, " + jmeno.capitalize(),
      "\n" + "We have 3 texts to be analyzed.",
      "\n" + oddelovac
      if jmeno in uzivatele and heslo == uzivatele.get(jmeno)
      else print("Invalid username or password. End of the program!...".upper()) + exit())

text_k_analyze = input("Enter a number btw. 1 and 3 to select: ")
if not text_k_analyze.isnumeric():
      print("Input is not a number.")
      exit()
elif not  3 >= int(text_k_analyze) >= 1:
      print("Number is not btw. 1 and 3.")
      exit()
else:
      print(oddelovac)

ocisteny_text = TEXTS[int(text_k_analyze)-1].strip(",.:;").split()
pocet_slov = len(ocisteny_text)
pocet_slov_s_prvnim_pismenem_velkym = len([slovo for slovo in ocisteny_text if slovo.istitle()])
pocet_slov_vsechna_velka = len([slovo for slovo in ocisteny_text if slovo.isupper()])
pocet_slov_vsechna_mala  = len([slovo for slovo in ocisteny_text if slovo.islower()])
pocet_cisel = len([slovo for slovo in ocisteny_text if slovo.isnumeric()])
suma_cisel = sum([int(slovo) for slovo in ocisteny_text if slovo.isnumeric()])
delky_slov_pocet = {}
for slovo in ocisteny_text:
      if len(slovo) not in delky_slov_pocet:
            delky_slov_pocet[len(slovo)] = 1
      else:
            delky_slov_pocet[len(slovo)] += 1

print("There are", pocet_slov, "words in the selected text.")
print("There are", pocet_slov_s_prvnim_pismenem_velkym, "titlecase words.")
print("There are", pocet_slov_vsechna_velka, "uppercase words.")
print("There are", pocet_slov_vsechna_mala, "lowercase words.")
print("There are", pocet_cisel, "numeric strings.")
print("The sum of all the numbers is:", suma_cisel)

nejvyssi_hodnota_vyskytu = max(delky_slov_pocet.values())
hlavicka_vypis = "LEN|"+"OCCURENCES".center(nejvyssi_hodnota_vyskytu + 2) + "|NR."
oddelovac2 = "-" * len(hlavicka_vypis)
print(oddelovac, hlavicka_vypis,oddelovac2,sep="\n")
for index, key in enumerate(sorted(delky_slov_pocet, reverse=False)):
      delka_hvezdicky = "*" * delky_slov_pocet.get(key)
      print(
            f"{key:>3}| {delka_hvezdicky}{'|':>{(len(hlavicka_vypis)-8) - delky_slov_pocet.setdefault(key) }}{delky_slov_pocet.setdefault(key)}"
      )







