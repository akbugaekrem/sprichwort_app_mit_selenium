from selenium import webdriver
import time

browser=webdriver.Firefox()
browser.get("https://de.wiktionary.org/wiki/Kategorie:Sprichwort_(Deutsch)")
time.sleep(2)


elements=browser.find_elements_by_css_selector("div.mw-category div.mw-category-group ul li a")
nummer=1
wörter=[w.text for w in elements]
links=[w.get_attribute('href') for w in elements]
zip=list(zip(wörter,links))
with open("Sprichwörter.txt","w",encoding="UTF-8") as file:
     
     for w,l in zip:
          file.write(str(nummer)+".Wort:\n")
          file.write("----------------------------------------------\n")
          file.write(w+"\n")
          file.write("**********************************************\n")
          file.write("Bedeutungen:\n")
          browser.get(l)
          time.sleep(1)
          text1=browser.find_elements_by_css_selector("div.mw-parser-output dl")
          lists=[j.text for j in text1]
          try:
               if  "IPA" in lists[2]:
                    file.write(lists[3]+"\n")
               else:
                    file.write(lists[2]+"\n")
          except:
               print("Error"+"..........."+str(nummer))
          file.write("**********************************************\n")
          nummer+=1
          #if nummer==3:
               #break

browser.close()
     

