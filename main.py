from ast import Raise, While
from hmac import digest
from pickle import TRUE



word = input('word: ')
Rword=word[::-1]
Lword=word.lower()
Uword=Lword[::-1]
list=[]
list2=[]

if  word.isdigit():
 raise Exception('number not allowed')
 
elif word==Rword:
     list.append(word)
     list2.append(Rword)
     print(f'that is right {word} equal reverse {Rword}')

elif word!=Rword:
     if Lword==Uword:
      print(f'ok that is right after handlling :) and  this is a base name {Lword} and this is a reversed {Uword}')
     elif Lword!=Uword:
          raise Exception('this word it will not be read on both sides')
