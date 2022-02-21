myhex = "ocip{FTC0l_I4_t5m_ll0m_y_y3n58a025e3ÿ�}"
mytext = ""
for i in range(0, len(myhex), 4):
    part = myhex[i:i+4]
    mytext += "".join(reversed([str(k) for k in part]))

print(mytext)