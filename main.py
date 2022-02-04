import time
laiks=time.strftime("%d-%m-%y %H:%M")
atbilde=("jā")
jaut=("jā")
treneri_v=["Juris Ozols","x", "Tomas Liepa", "Edvards Kalniņš", "Linus Bruņinieks", "Santa Balode"]
paroles=["5629","l","0492","1452","0372","7436"]
treneris_apraksts=["jautrs tel. num.:11112222","spējīgs treneris tel. num.:31112222","labs čoms tel. num.:11692222","mīl runāt par traktoriem tel. num.:00112222","augstākā izglītība sportā tel. num.:11114522","Apdāvināts treneris tel. num.:1234567"]
treneris_pieejams=["pirmdienas-piekdienas(10:00-19:00)","pirmdienas-ceturdienas(10:00-20:00)","pirmdienas-sesdiendas(9:00-19:00)","otradienas-piekdienas(10:00-18:00)","pirmdienas-piekdienas(10:00-19:00)","pirmdienas-piekdienas(18:00-22:00)"]
zvaigznes=[" "," "," "," "," ",""]
telpas=["Valmiera, Kaktusa iela, 34","Cēsis, Poda iela, 12","Valmiera, desu iela, 1"]
darbalaiki=["8:30-20:00","9:00-21:00","8:00-22:00"]
bildes=["https://www.baseins.eu/wp-content/uploads/2013/04/6X4B8217.jpg","https://www.baseins.eu/wp-content/uploads/2013/04/6X4B8217.jpg","https://www.baseins.eu/wp-content/uploads/2013/04/6X4B8217.jpg"]
aprikojums=["divas 10 kg hanteles","25 kg svaru bumba","12 matrači, 2 skriešanas trenežieri"]
abonetaji=["vards: juris telefona numurs vai ēpasts: 98765432 aboments: 1 treniņš nedēļā: 5 eiro "]
reitingu_skaits=[2,2,2,2,2,2]
reitings=[9,10,8,6,9,2]
abonesanas_skaits=[3,4,5,2]
abomenti=["1 treniņš nedēļā: 5 eiro","2 treniņi nedēļā: 10 eiro","4 treniņi nedēļā: 20 eiro","7 treniņi nedēļā: 30 eiro"]
abonetaji=[]
run=True
while run==True:
  for i in range(len(reitings)):
    zvaigznes[i]=reitings[i]/reitingu_skaits[i]
  print("Sveiki")
  apmekletajs=str(input("Vai esi apmeklētājs, vai treneris? :"))
  if apmekletajs==("treneris"):
    while atbilde==("jā"):
      v_parbaud=str(input("Ievadat savu vārdu un uzvārdu: "))
      pin_parbaud=str(input("Ievadi savu paroli: "))
      for i in range(len(treneri_v)):
        if v_parbaud==treneri_v[i] and pin_parbaud==paroles[i]:
          print("Sveiki teneri/e!")
          atbilde=("nē")
          apraksts_jaut=str(input("Vai, vējaties pārmainīt savu   aprakstu?:"))
          if apraksts_jaut==("jā"):
            apraksts_main=str(input("Rakstat pilnu aprakstu ar jūsu gribētājām pārmaiņām:"))
            treneris_apraksts[i]=apraksts_main
          pieejams_jaut=str(input("Vai gribat pārmainīt savas   darbadienas un laikus?: "))
          if pieejams_jaut==("jā"):
            pieejams_main=str(input("Ievadiet savus pārmainītos   darba laikus, dienas: "))
            treneris_pieejams[i]=pieejams_main
          zvaigznes_jaut=str(input("Vai gribat redzēt savu reitingu?: "))
          if zvaigznes_jaut==("jā"):
            print(zvaigznes[i])
          trenins_jaut=("vai vēlaties pieteikt treniņu?")
          if trenins_jaut==("jā"):
            trenins_laiks=("uzrakstat laiku diena")
          treneris_pietekums_jaut=("vai gribat pieteikt treniņu?")
          if treneris_pietekums_jaut==("jā"):
            print(f"laiks un datums tagad {laiks}")
            pietekums.append(str(input("ievdi apaļu skaitli ,piemēram 15:00 vai 15:30, un datumu (diena , mēn ,gads) ar cipariem (tādā pašā secībā kā izprintēts laiks): ")))
          atbilde==str(input("vai vēlaties iziet no sava profila?"))
        elif i==len(paroles)-1:
          print("Nepareizs vārds, vai parole.")
          atbilde=str(input("vai mēģināsiet velreiz?: "))
          if atbilde==("jā"):
            continue     
  elif apmekletajs==("apmeklētājs"):      
    velme=str(input("vai gribi trenēties viens, vai ar treneri?: "))
    if velme=="treneri" or velme=="ar treneri":
      bridinajums=str(input("(lai pieteiktos pie trenera tev jabūt abonētājam)Vai tu esi abonetajs?:"))
      if bridinajums==("jā"):
        while jaut==("jā"):
          telefons=str(input("ierakstiet savu personas kodu un telefona numuru:"))
          print(abomenti)
          abonements_pieteikt=(int(input("ievadiet abomenta kārtas ciparu ,skatoties no kreisāspuses (ar cipariem): ")))
          for i in range(len(abonetaji)):
            if abonetaji[i]==(f"tel. num., personas kods:{telefons} aboments:{abomenti[abonements_pieteikt-1]}"):
              print("sveiki, ievadītie dati pareizi!")
              jaut=("nē")
              break
            if i==len(abonetaji)-1:
              print("Ievadīti nepareizi dati.")
              jaut=str(input("vai mēģināsiet velreiz?: "))
          for i in range (len(paroles)):
            print(f"treneris/e: {treneri_v[i]} apraksts:   {treneris_apraksts[i]} pieejams: {treneris_pieejams[i]} reitings:{zvaigznes[i]}")
          novertesasa=str(input("vai gribat novērtēt treneri?: "))
          if novertesasa==("jā"):
            karta=int(input(f"kuru pēckārtas skatoties no kreisās malas sarakstā {treneri_v} treneri jūs gribat novērtēt (rakstat ar skaitļiem bez punkta) "))
            reitings[karta-1]+=int(input("ievadi zvaigžņu skaitu 1-5 veselos skaitļos?: "))
            reitingu_skaits[karta-1]+=1
    else:
      telpas_izveles=str(input("vai gribi redzēt piedāvātās zāles un to darba laikus?: "))
      if telpas_izveles==("jā"):
        for i in range(len(telpas)):
          print(f"{telpas[i]} atvērta:{darbalaiki[i]}")
      bildes_izvele=str(input("vai gribat redzēt telpu bildes?: "))
      if bildes_izvele==("jā"):
        for i in range (len(bildes)):
          print(f"telpa:{telpas[i]} bildes links:{bildes[i]}")
      aprikojums_izvele=str(input("vai gribat redzēt aprīkojumu?: "))
      if aprikojums_izvele==("jā"):
        for i in range (len(aprikojums_izvele)):
          print(f"telpas:{telpas[i]} aprikojums: {aprikojums[i]}")
      aboments_jaut=str(input("vai gribat pieteikties uz treniņu?: "))
      if aboments_jaut==("jā"):
        print(abomenti)
        telefons=str(input("ierakstiet savu personas kodu un telefona numuru:"))
        abonements_pieteikt=(int(input("ievadiet abomenta kārtas ciparu ,skatoties no kreisāspuses (ar cipariem): ")))
        abonesanas_skaits[abonements_pieteikt-1]+=1
        abonetaji.append(f"tel. num., personas kods:{telefons} aboments:{abomenti[abonements_pieteikt-1]}")
      aboments_atcelt=str(input("vai gribat atcelt abomentu?: "))
      if aboments_atcelt==("jā"):
        telefons=str(input("ierakstiet savu personas kodu un telefona numuru:"))
        print(abomenti)
        abonements_pieteikt=(int(input("ievadiet abomenta kārtas ciparu ,skatoties no kreisāspuses (ar cipariem): ")))
        for i in range(len(abonetaji)):
          if abonetaji[i]==(f"tel. num., personas kods:{telefons} aboments:{abomenti[abonements_pieteikt-1]}"):
            abonesanas_skaits[abonements_pieteikt-1]-=1
            abonetaji.remove(f"tel. num., personas kods:{telefons} aboments:{abomenti[abonements_pieteikt-1]}")
  elif apmekletajs==("dunkey32"):
    aprakstu_parb=str(input("vai gribat pārbaudīt treneru aprakstus?: "))
    if aprakstu_parb==("jā"):
      for i in range (len(treneri_v)):
        print(f"vārds:{treneri_v[i]} apraksts:{treneris_apraksts[i]}")
    zvaigznes_parb=str(input("vai gribat redzēt treneru reitingus?:"))
    if zvaigznes_parb==("jā"):
      for i in range (len(treneri_v)):
        print(f"vārds:{treneri_v[i]} reitings:{zvaigznes[i]}")
    bildes_main=str(input("vai gribat mainīt bildes?: "))
    if bildes_main==("jā"):
      for i in range (len(bildes)):
        bildes[i]=str(input(f"iekopējiet bildes linu {telpas[i]} telpai: "))
    aprikojums_main=str(input("vai gribat mainīt aprīkojuma sarakstu?: "))
    if aprikojums_main==("jā"):
      for i in range (len(aprikojums)):
        aprikojums[i]=str(input(f"ierakstat pilnu aprīkojuma uzskaitījumu {telpas[i]} telpai: "))
    darbalaiki_main=str(input("Gribat mainīt darbalaiku?: "))
    if darbalaiki_main==("jā"):
      for i in range (len(darbalaiki)):
        darbalaiki[i]=str(input(f"ievadiet {telpas[i]} laikus: "))
    treneris_jaut=str(input("vai gribat pievienot jaunu treneri?: "))
    if treneris_jaut==("jā"):
      treneri_v.append(str(input("ievadiet trenera vārdu uzvārdu: ")))
      paroles=(str(input("ievadi trenera paroli: ")))
    abonetaji_skaits_jaut=str(input(" katra abomenta veida skaitu?"))
    if abonetaji_skaits_jaut==("jā"):
      for i in range (len(abomenti)):
        print(f"{abomenti[i]} cilvēki pieteikušies: {abonesanas_skaits[i]}")
    abonetaji_jaut=str(input(" Vai gribat redzēt abonējošos cilvēkus?"))
    if abonetaji_jaut==("jā"):
      print(abonetaji)