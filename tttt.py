import emoji
str='æ–¹æ–¹åœˆå­�ğŸ˜€ğŸ˜€ğŸ˜€'

a = "ç ç ¾SunShineð»"
print(a)
b = emoji.demojize(a.encode('iso-8859-1').decode('utf-8'))
print(b)
print(emoji.emojize(b))
