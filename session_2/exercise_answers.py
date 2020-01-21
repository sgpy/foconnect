# Exercise: Here is a list of currency pairs. Please find out how many pairs that
#           contain 'CNH' currency. 
# Hint: You can use keyword 'in' to check if one string is a substring of another.
#       e.g. 'CNH' in 'USDCNH'

ccy_pair_list = [
    'USDCNH', 'USDJPY', 'HKDCNH', 'USDCAD', 'AUDUSD', 'ZARJPY', 'USDRUR', 'EURUSD',
    'EURJPY', 'USDSEK', 'USDCNY', 'USDINR', 'USDINO', 'USDKRW', 'USDKRO', 'EURSEK',
    'USDSAR', 'ZARTWD', 'ZARRUB', 'USDBRL', 'USBONB', 'SGDHKD', 'AUDEUR', 'CNHHKD',
    'CHFSEK', 'JPYCNH', 'USDCNH', 'USDPHP', 'USDIDR', 'USDTHB', 'EURJPY', 'USDHUF',
    'USDMYR', 'EURINO', 'GBPUSD', 'GBPHKD', 'USDDKK', 'HKDMOP', 'NZDHKD', 'CNHSGD',
]

print('CNH' in 'USDCNH')

# Please start here

# Answer 1
count = 0
for pair in ccy_pair_list:
    if 'CNH' in pair:
        count = count + 1
print('Number of pairs that contain CNH: ', count)



# Answer 2 - How to remove the duplicate pairs
#
# Hint: use set(ccy_pair_list)
count = 0
for pair in set(ccy_pair_list):
    if 'CNH' in pair:
        count = count + 1
print('Number of unique pairs that contain CNH: ', count)


# Answer 3 - Simplified version - Python way
print('Simplified version: ', len([p for p in ccy_pair_list if 'CNH' in p]))


# Answer 4... There can be more answers. Feel free to use what you have learnt.