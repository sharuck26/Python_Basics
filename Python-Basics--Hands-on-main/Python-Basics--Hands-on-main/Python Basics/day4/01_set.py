websites={"google", "yahoo", "orkut", "youtube", "apex"}
games = {"csgo", "valorant", "apex", "gta", "six seige"} 


#print(websites)

##websites.add("instagram")
##print(websites)

#websites.update(games)
#print(websites)

#websites.remove("orkut")
#print(websites)

#websites.discard("ok")
#print(websites)

#websites.pop()
#print(websites)

#new =websites.union(games)
#print(new)

#websites.intersection_update(games)
#print(websites)

temp=websites.intersection(games)
print(temp)

websites.symetric_difference_update(games)
print(websites)





























