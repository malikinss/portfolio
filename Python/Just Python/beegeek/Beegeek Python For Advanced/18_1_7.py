'''
TODO:   Transliteration is the transfer of signs of one writing system 
        by signs of another writing system, in which each sign (or 
        sequence of signs) of one writing system is transmitted by the 
        corresponding sign (or sequence of signs) of another writing 
        system.

        A text file is available to you cyrillic.txt containing the 
        text. 

        Write a program to transliterate this file, that is, replace 
        Cyrillic characters with Latin ones in accordance with the 
        proposed table. 

        All other symbols must be left unchanged. 

        The result of the transliteration must be written to a file transliteration.txt .

NOTE:   Consider that the executable program and the specified files are 
        in the same folder.


'''

transliteration_dict = {'а':'a', 'б':'b', 'в':'v', 'г':'g',
                        'д':'d', 'е':'e', 'ё':'jo', 'ж':'zh',
                        'з':'z', 'и':'i', 'й':'j', 'к':'k',
                        'л':'l', 'м':'m', 'н':'n', 'о':'o',
                        'п':'p', 'р':'r', 'с':'s', 'т':'t',
                        'у':'u', 'ф':'f', 'х':'h', 'ц':'c',
                        'ч':'ch', 'ш':'sh', 'щ':'shh', 'ъ':'*',
                        'ы':'y', 'ь':"'", 'э':'je', 'ю':'ju', 'я':'ya'}

def transliterate(file, result_file):
    for letter in file.read():
        if letter in transliteration_dict:
            result_file.write(transliteration_dict[letter])
        elif letter.lower() in transliteration_dict:
            result_file.write(transliteration_dict[letter.lower()].capitalize())
        else:
            result_file.write(letter)

def task():    
    with open('cyrillic.txt') as given_file, open('transliteration.txt', 'w') as result_file:
        transliterate(given_file, result_file)

task()

