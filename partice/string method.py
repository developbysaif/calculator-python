name = "saif kaleem "
print (name.upper()) # it will convert all the characters in upper case
print (name.lower()) # it will convert all the characters in lower case
print (name.title()) # it will convert the first character of each word in upper case and rest in lower case
print (name.strip()) # it will remove the extra spaces from the beginning and end of the
print (name.swapcase()) # it will convert the upper case characters to lower case and lower case characters to upper case
print (name.find("kal"))
print (name.rfind("kal")) # it will return the index of the last occurrence of the substring "kal" in the string "name". If the substring is not found, it will return -1. In this case, it will return 5 because "kal" starts at index 5 in the string "saif kaleem ".
print (name.count("a")) # it will return the number of occurrences of the substring "a" in the string "name". In this case, it will return 2 because there are two occurrences of "a" in the string "saif kaleem ".
print(name.startswith("saif")) # it will return True because the string "name" starts with the substring "saif". If the string did not start with "saif", it would return False.
print(name.endswith("kaleem")) # it will return False because the string "name"
# does not end with the substring "kaleem". If th
# e string ended with "kaleem", it would return True.
print(name.index("kal"))
#Validation returns True or Fals    e
# it will split the string "name" into a list of substrings based on whitespace. In this case, it will return ['saif', 'kaleem'].
print(name.isalpha())
# it will return False because the string "name" contains spaces, which are not alphabetic characters. If the string contained only alphabetic characters, it would return True.
print(name.isdigit())
# it will return False because the string "name" contains alphabetic characters and spaces, which are not digits. If the string contained only digits, it would return True.
print(name.isalnum())
# it will return False because the string "name" contains spaces, which are not alphanumeric
print(name.isupper())
# it will return False because the string "name" contains lowercase characters. If the string contained only uppercase characters, it would return True.
print(name.islower())
# it will return False because the string "name" contains uppercase characters. If the string contained
print(name.isspace())
# it will return False because the string "name" contains alphabetic characters and spaces, which are not whitespace. If the string contained only whitespace characters, it would return True.
print(name.istitle())
# it will return False because the string "name" is not in title case. If the string were in title case, it would return True.
#Modify&clean the string 
name1 = "   saif kaleem   "
print(name1.strip()) # it will remove the extra spaces from the beginning and end of the
print(name1.lstrip()) # it will remove the extra spaces from the beginning of the string
print(name1.rstrip()) # it will remove the extra spaces from the end of the string
# it will return the index of the first occurrence of the substring "kal" in the string "name". If the substring is not found, it will return -1. In this case, it will return 5 because "kal" starts at index 5 in the string "saif kaleem ".
print (name1.replace("saif", "kaleem"))


print(name1.removeprefix("   ")) # it will remove the prefix "   " from the string "name1". In this case, it will return "saif kaleem   ".
print(name1.removesuffix("   ")) # it will remove the suffix "   " from

#Split&join the string
name2 = "saif kaleem"
# it will replace all occurrences of the substring "saif" with "kaleem" in the string "name1". In this case, it will return "kaleem kaleem ".
print (name2.split())
print (name2.split("kaleem")) # it will split the string "name2" into a list of substrings based on the substring "kaleem". In this case, it will return ['saif ', ''].
# it will join the list of substrings ['saif', 'kaleem'] into   
# a single string, with a space character as the separator. In this case, it will return "saif kaleem".
print(" ".join(name2.split()))

print(name2.rsplit()) # it will split the string "name2" into a list of substrings based on whitespace, starting from the right. In this case, it will return ['saif', 'kaleem'].
print(name2.splitlines()) # it will split the string "name2" into a list of substrings based on line breaks. In this case, it will return ['saif kaleem'] because there are no line breaks in the string.
print(name2.join(["saif", "kaleem"])) # it will join the list of strings ["saif", "kaleem"] into a single string, with the string "name2" as the separator. In this case, it will return "saifkaleem".

#Formating&aligment
name3 = "saif"
print(name3.center(10)) # it will center the string "name3" within a
# field of width 10, padding it with spaces on both sides. In this case, it will return "   saif    ".
print(name3.ljust(10)) # it will left-justify the string "name3
# within a field of width 10, padding it with spaces on the right. In this case, it will return "saif      ".
print(name3.rjust(10)) # it will right-justify the string "name3" within a field of width 10, padding it with spaces on the left. In this case, it will return "      saif".
print(name3.zfill(10)) # it will pad the string "name3" with
# zeros on the left until it reaches a total width of 10 characters. In this case, it will return "000000saif".
print(name3.ljust(10, "*")) # it will left-justify the string "name3" within a field of width 10, padding it with asterisks on the right. In this case, it will return "saif******".
print(name3.rjust(10, "*")) # it will right-justify the string "

#Ecoding&decoding
name4 = "saif kaleem"
encoded_name = name4.encode("utf-8") # it will encode the string "name4" using the UTF-8 encoding scheme. The resulting encoded string will be a bytes object that represents the original string in a specific format. In this case, it will return b'saif kaleem'.
print(encoded_name)
decoded_name = encoded_name.decode("utf-8") # it will decode the bytes object "encoded_name" back into a string using the UTF-8 encoding scheme. The resulting decoded string will be the original string that was encoded. In this case, it will return "saif kaleem".
print(decoded_name)
