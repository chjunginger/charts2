__author__ = 'christianjunginger'
#produces a matrix used in the shiny app. It contains word count for specific words over all top100 lyrics through the years

import numpy as np
import pandas as pd
import re


feature_list=["strong","touch","lovers","lover","die","apart","lady","moon","car","peace","war","dreaming","dream","dreams","high","school","the","world","friends","friend","soul","twist","rock","and","night","we","feel","home","goodbye","time","life","man","woman","girl","boy","love","baby","hope","lips","eyes","money","club","darling","kiss","dance","party","drugs","shoot","kill","yeah","drink","steal","sexy","sad","happy","body","heart","smile","hate"]
total = pd.DataFrame(0, index = np.arange(1956,2015), columns = feature_list)

for yr in range(1956,2015):
    print(yr)
    for item in feature_list:
        g = open('1_grms_%s.txt'%yr)
        data = g.read()
        if (re.findall(r',%s,(.*?)\n'%item,data)!=[]):
            total.at[yr,item]=(re.findall(r',%s,(.*?)\n'%item,data))[0]


print(total)

total.to_csv("matrix_of_1_grm_count.txt")



