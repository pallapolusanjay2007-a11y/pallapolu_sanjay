def count_vowels(text):
    return sum(1 for letter in text if letter.lower() in "aeiou")
def count_consentes(text):
    return sum(1 for letter in text if letter.isalpha() and letter.lower() not in "aeiou")
def count_words(text):
    return len(text.split())
def reveres_text(text):
    return text[::-1]


print("🫦 "*50)

print("welcome to the string operater ...")

print("🫦 "*50)

message = input("enter the your message : ")
while True:

   print("1.count vowels")
   print("2. count consentes")
   print("3.count words in the text")
   print("4.reverse the text")
   print("5.exit the string ")

   choice = input("enter your choice : ")


   if choice =="1":
       print(count_vowels(message))
   elif choice=="2":
       print(count_consentes(message))
   elif choice =="3":
       print(count_words(message))
   elif choice =="4":
       print(reveres_text(message))
   elif choice =="5":
       print("exiting the string..")
       print("see you later 🫦 🫦 🫦 🫦 🫦 🫦 ")
       break
   else:
       print("invalide choice....")