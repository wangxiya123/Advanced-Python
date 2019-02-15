import re 
 for k in range(1, 6): 
with open(str(k)+".txt", encoding = "gbk", errors = "ignore") as f: 
text = f.read(); 
it = re.finditer(r'\w+', text); 
dict = {}; 
for match in it: 
if (dict.__contains__(match.group())): 
dict[match.group()] += 1; 
else: 
dict[match.group()] = 1; 
sorted_dict = sorted(dict.items(), key = lambda e:e[1], reverse = True); 
i = 0; 
print("#"+str(k)+":"); 
print("freq*\tword"); 
print("-----\t-----"); 
for key in sorted_dict: 
print(str(key[1])+"\t"+key[0]); 
i += 1; 
if (i == 10): 
break; 
print("");
