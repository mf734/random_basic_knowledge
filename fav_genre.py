'''
Example 1:

Input:
userSongs = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
},
songGenres = {  
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

Output: {  
   "David": ["Rock", "Techno"],
   "Emma":  ["Pop"]
}

Explanation:
David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre.
'''

def favorGenre(userMap, genreMap):
	if not userMap or not genreMap:
		d = {}
		# 将user中全部清空
		for u in userMap:
			d[u] = []
		return d
	
	# reverse the genremap
	# s_g store which song belongs to what genre
	s_g = {}
	for gen in genreMap:
		for song in genreMap[gen]:
			s_g[song] = gen

	from collections import defaultdict
	u_gens = defaultdict(list)
	for u in userMap:
		# s是一个user喜欢的每首歌
		# 查询这首歌的genre，加入进u_gens中
		# u_gens就是一个由“人”：“喜欢的genre”组成的dict
		for s in userMap[u]:
			gen = s_g[s]
			u_gens[u].append(gen)

	final = {}
	for u in u_gens:
		fav_gens = []
		temp = {}
		# 将user的gen取出
		for g in u_gens[u]:
			# temp记载这个user的喜欢gen的歌曲的个数
			if g in temp:
				temp[g] += 1
			else:
				temp[g] = 1
		# maxVal就是这个用户最喜欢的gen里的歌曲的个数
		maxVal = max(temp.values())
		# 遍历temp，找到是哪些gen有最高的计数，将gen赋值给fav_gens，最后进入dict
		for k in temp:
			if temp[k] == maxVal:
				fav_gens.append(k)
		final[u] = fav_gens
	return final

'''
判空处理
创造song_gen
创造user_gen
将每个user的gen取出计数
输出计数最高的gen
'''