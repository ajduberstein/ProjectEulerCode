chain_len = 0
longest_chain = 0;
largest_num = 0
while (i < 1000000):
	chain_num = i;
	chain_len = 1;
	while (chain_num > 1):
		if (chain_num % 2 == 0):
			chain_num = chain_num/2;
		else:
			chain_num = 3*chain_num+1;
		chain_len+=1;
	if (chain_len > longest_chain):
		longest_chain = chain_len;
		largest_num = i;
	i+=1
