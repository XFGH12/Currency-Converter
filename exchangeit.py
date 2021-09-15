"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Sidney G. Cole, Jr.
Date:   2 September 2021
"""

import currency

src=input('3-letter code for original currency: ')
#print(src)
dst=input('3-letter code for the new currency: ')
#print(dst)
amt=input('Amount of the original currency: ')
amt=(float(amt))
#print(amt)

conversion=(currency.exchange(src, dst, amt))
#print(conversion)

round_conversion=round(conversion,3)
#print(round_conversion)



message1='You can exchange '
message2=' for '
print(message1+str(amt)+' '+str(src)+message2+str(round_conversion)+' '+str(dst)+'.')




