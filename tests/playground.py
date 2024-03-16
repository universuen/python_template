# import context
#
#
# with open('dict.txt', 'r') as f:
#     raw_dict = f.read()
# dict_items = raw_dict.split(';')
#
# final_dict = dict()
# for item in dict_items:
#     if '=' not in item:
#         continue
#     print(item)
#     k, v = item.split('=')
#     v = v.replace("'", '')
#     final_dict[k] = v
#
# with open('msg.txt', 'r') as f:
#     encrypted_msg = f.read()
# encrypted_msg_items = encrypted_msg.split('$')
#
# final_msg_items = list()
# for item in encrypted_msg_items:
#     if item not in final_dict.keys():
#         continue
#     final_msg_items.append(final_dict[item])
#
# print(''.join(final_msg_items))

import base64
import re


text = r"""\
bash -c "$(base64 -d <<< "\
IyEvYmluL2Jhc2gKZXhwb3J0IExBTkc9ZW5fVVMuVVRGLTgKcmVkPSdcMDMzWzA7MzFtJwpncmVl
bj0nXDAzM1swOzMybScKeWVsbG93PSdcMDMzWzA7MzNtJwpibHVlPSdcMDMzWzA7MzZtJwpiYmx1
ZT0nXDAzM1swOzM0bScKcGxhaW49J1wwMzNbMG0nCnJlZCgpeyBlY2hvIC1lICJcMDMzWzMxbVww
MzNbMDFtJDFcMDMzWzBtIjt9CmdyZWVuKCl7IGVjaG8gLWUgIlwwMzNbMzJtXDAzM1swMW0kMVww
MzNbMG0iO30KeWVsbG93KCl7IGVjaG8gLWUgIlwwMzNbMzNtXDAzM1swMW0kMVwwMzNbMG0iO30K
Ymx1ZSgpeyBlY2hvIC1lICJcMDMzWzM2bVwwMzNbMDFtJDFcMDMzWzBtIjt9CndoaXRlKCl7IGVj
aG8gLWUgIlwwMzNbMzdtXDAzM1swMW0kMVwwMzNbMG0iO30KcmVhZHAoKXsgcmVhZCAtcCAiJCh5
ZWxsb3cgIiQxIikiICQyO30KW1sgJEVVSUQgLW5lIDAgXV0gJiYgeWVsbG93ICLor7fku6Vyb290
5qih5byP6L+Q6KGM6ISa5pysIiAmJiBleGl0CiNbWyAtZSAvZXRjL2hvc3RzIF1dICYmIGdyZXAg
LXFFICdeICoxNzIuNjUuMjUxLjc4IGdpdGxhYi5jb20nIC9ldGMvaG9zdHMgfHwgZWNobyAtZSAn
XG4xNzIuNjUuMjUxLjc4IGdpdGxhYi5jb20nID4+IC9ldGMvaG9zdHMKaWYgW1sgLWYgL2V0Yy9y
ZWRoYXQtcmVsZWFzZSBdXTsgdGhlbgpyZWxlYXNlPSJDZW50b3MiCmVsaWYgY2F0IC9ldGMvaXNz
dWUgfCBncmVwIC1xIC1FIC1pICJkZWJpYW4iOyB0aGVuCnJlbGVhc2U9IkRlYmlhbiIKZWxpZiBj
YXQgL2V0Yy9pc3N1ZSB8IGdyZXAgLXEgLUUgLWkgInVidW50dSI7IHRoZW4KcmVsZWFzZT0iVWJ1
bnR1IgplbGlmIGNhdCAvZXRjL2lzc3VlIHwgZ3JlcCAtcSAtRSAtaSAiY2VudG9zfHJlZCBoYXR8
cmVkaGF0IjsgdGhlbgpyZWxlYXNlPSJDZW50b3MiCmVsaWYgY2F0IC9wcm9jL3ZlcnNpb24gfCBn
cmVwIC1xIC1FIC1pICJkZWJpYW4iOyB0aGVuCnJlbGVhc2U9IkRlYmlhbiIKZWxpZiBjYXQgL3By
b2MvdmVyc2lvbiB8IGdyZXAgLXEgLUUgLWkgInVidW50dSI7IHRoZW4KcmVsZWFzZT0iVWJ1bnR1
IgplbGlmIGNhdCAvcHJvYy92ZXJzaW9uIHwgZ3JlcCAtcSAtRSAtaSAiY2VudG9zfHJlZCBoYXR8
cmVkaGF0IjsgdGhlbgpyZWxlYXNlPSJDZW50b3MiCmVsc2UgCnJlZCAi6ISa5pys5LiN5pSv5oyB
5b2T5YmN55qE57O757uf77yM6K+36YCJ5oup5L2/55SoVWJ1bnR1LERlYmlhbixDZW50b3Pns7vn
u5/jgIIiICYmIGV4aXQKZmkKdnNpZD0kKGdyZXAgLWkgdmVyc2lvbl9pZCAvZXRjL29zLXJlbGVh
c2UgMj4vZGV2L251bGwgfCBjdXQgLWQgXCIgLWYyIHwgY3V0IC1kIC4gLWYxKQpvcD0kKGNhdCAv
ZXRjL3JlZGhhdC1yZWxlYXNlIDI+L2Rldi9udWxsIHx8IGNhdCAvZXRjL29zLXJlbGVhc2UgMj4v
ZGV2L251bGwgfCBncmVwIC1pIHByZXR0eV9uYW1lIHwgY3V0IC1kIFwiIC1mMikKaWYgW1sgJChl
Y2hvICIkb3AiIHwgZ3JlcCAtaSAtRSAiYXJjaHxhbHBpbmUiKSBdXTsgdGhlbgpyZWQgIuiEmuac
rOS4jeaUr+aMgeW9k+WJjeeahCAkb3Ag57O757uf77yM6K+36YCJ5oup5L2/55SoVWJ1bnR1LERl
YmlhbixDZW50b3Pns7vnu5/jgIIiICYmIGV4aXQKZmkKY2FzZSAkKHVuYW1lIC1tKSBpbgphYXJj
aDY0KSBjcHU9YXJtNjQ7Owp4ODZfNjQpIGNwdT1hbWQ2NDs7CiopIHJlZCAi55uu5YmN6ISa5pys
5LiN5pSv5oyBJCh1bmFtZSAtbSnmnrbmnoQiICYmIGV4aXQ7Owplc2FjCmlmIFsgISAteCAiJChj
b21tYW5kIC12IGJ6aXAyKSIgXTsgdGhlbgp5ZWxsb3cgIuivt+eojeetieKApuKApiIKaWYgW1sg
JHJlbGVhc2UgPSBDZW50b3MgJiYgJHt2c2lkfSA9fiA4IF1dOyB0aGVuCmNkIC9ldGMveXVtLnJl
cG9zLmQvICYmIG1rZGlyIGJhY2t1cCAmJiBtdiAqcmVwbyBiYWNrdXAvIApjdXJsIC1vIC9ldGMv
eXVtLnJlcG9zLmQvQ2VudE9TLUJhc2UucmVwbyBodHRwOi8vbWlycm9ycy5hbGl5dW4uY29tL3Jl
cG8vQ2VudG9zLTgucmVwbwpzZWQgLWkgLWUgInN8bWlycm9ycy5jbG91ZC5hbGl5dW5jcy5jb218
bWlycm9ycy5hbGl5dW4uY29tfGcgIiAvZXRjL3l1bS5yZXBvcy5kL0NlbnRPUy0qCnNlZCAtaSAt
ZSAic3xyZWxlYXNldmVyfHJlbGVhc2V2ZXItc3RyZWFtfGciIC9ldGMveXVtLnJlcG9zLmQvQ2Vu
dE9TLSoKeXVtIGNsZWFuIGFsbCAmJiB5dW0gbWFrZWNhY2hlCmNkCmZpCmlmIFsgLXggIiQoY29t
bWFuZCAtdiBhcHQtZ2V0KSIgXTsgdGhlbgphcHQgdXBkYXRlIC15IAphcHQgaW5zdGFsbCBiemlw
MiAteSAKZWxpZiBbIC14ICIkKGNvbW1hbmQgLXYgeXVtKSIgXTsgdGhlbgp5dW0gdXBkYXRlIC15
IAp5dW0gaW5zdGFsbCBlcGVsLXJlbGVhc2UgLXkKeXVtIGluc3RhbGwgYnppcDIgLXkKZWxpZiBb
IC14ICIkKGNvbW1hbmQgLXYgZG5mKSIgXTsgdGhlbgpkbmYgdXBkYXRlIC15IApkbmYgaW5zdGFs
bCBiemlwMiAteSAKZmkKZmkKaWYgWyAteCAiJChjb21tYW5kIC12IGJ6aXAyKSIgXTsgdGhlbgpy
bSAtcmYgQ0Z3YXJwLnNoCndnZXQgLXFOIGh0dHBzOi8vZ2l0bGFiLmNvbS9yd2tneWcvQ0Z3YXJw
L3Jhdy9tYWluLzFDRndhcnAuc2ggIHx8IGN1cmwgLXNTZkxPIGh0dHBzOi8vZ2l0bGFiLmNvbS9y
d2tneWcvQ0Z3YXJwL3Jhdy9tYWluLzFDRndhcnAuc2gKY2htb2QgK3ggMUNGd2FycC5zaAptdiAx
Q0Z3YXJwLnNoIENGd2FycC5zaApiYXNoIENGd2FycC5zaAplbHNlCnJlZCAiVlBT5pu05paw5L6d
6LWW5pe25Ye66ZSZ77yM5bu66K6u6YeN5ZCvVlBT44CC5aaC5p6c5L6d5pen5aaC5q2k5bu66K6u
5pu05o2i57O757uf6YeN6KOFVlBTIgpmaQo=")" bash "$@" """

cnt = 0
# Loop until no more 'bash' commands are found within the text
while 'bash' in text:
    cnt += 1
    print(cnt)
    # Extract base64 code from text using a regular expression
    base64_pattern = re.compile(r'base64 -d <<< "([^"]+)"')
    matches = base64_pattern.findall(text)
    if not matches:
        break  # Exit loop if no base64 code is found

    # Decode base64 code
    base64_code = matches[0]
    decoded_text = base64.b64decode(base64_code).decode('utf-8')

    # Update text for the next iteration
    text = decoded_text

# Print the fully decoded content
print(text)


