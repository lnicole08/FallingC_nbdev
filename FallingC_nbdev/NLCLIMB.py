# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 23:17:03 2022

@author: lnico
"""
def chambertracking(dataframe, transgenic):
    
    import math
    import matplotlib.pyplot as plt
    
    phasedark_XY = dataframe[(dataframe['ExperimentState'] == 'Assimilation time - Dark') | (dataframe['ExperimentState']== 'Dark')] 
    avg_dark = average_list(phasedark_XY, "Dark")
    avgdark_start_values = avg_dark.iloc[0].values.tolist() #gives me start
    if math.isnan(avgdark_start_values[0]) == True:
        avgdark_start_values = avg_dark.iloc[1].values.tolist()
    
    
    phaselight_XY = dataframe[(dataframe['ExperimentState'] == 'Assimilation time - Full') | (dataframe['ExperimentState']== 'Full')] 
    avg_light = average_list(phaselight_XY, "Light")
    avglight_start_values = avg_light.iloc[0].values.tolist() #gives me start
    if math.isnan(avglight_start_values[0]) == True:
        avglight_start_values = avg_light.iloc[1].values.tolist()
    
    plt.figure(figsize=(7,7))
    #fig, axes = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(7,7))

    ax1 = plt.subplot(1,2,1)
    avg_dark.iloc[0:3,:].plot(x='DarkAvg_X', y='DarkAvg_Y', legend=None, color = "black", ax=ax1)
    avg_dark.iloc[2:,:].plot(x='DarkAvg_X', y='DarkAvg_Y', legend=None, color = "grey", ax=ax1)
    plt.plot(avgdark_start_values[0],avgdark_start_values[1],  "o", color = "black")
    plt.title('Avg position of fly in dark phase:\n'+ transgenic, fontsize=12)
    plt.ylabel('Y Position(mm)', fontsize=16)
    ax1.set(xlabel=None)

    ax2 = plt.subplot(1,2,2, sharex = ax1)
    avg_light.iloc[0:3,:].plot(x='LightAvg_X', y='LightAvg_Y', legend=None, color = "darkgreen", ax=ax2)
    avg_light.iloc[2:,:].plot(x='LightAvg_X', y='LightAvg_Y', legend=None, color = "limegreen", ax=ax2)
    plt.plot(avglight_start_values[0],avglight_start_values[1],  "o", color = "darkgreen")
    plt.title('Avg position of fly in light phase:\n'+ transgenic, fontsize=12)
    ax2.set(xlabel=None)

    #final plots
    ax1.get_shared_y_axes().join(ax1, ax2)
    ax2.set_yticks([])
    #text(5.5, 5, 'X Position(mm)', va='center', ha='center', fontsize=16)
    nnumber = int((len(dataframe.columns)-2)*0.5)
    ax1.text(0.5, -0.1,'n='+ str(nnumber), horizontalalignment='center', verticalalignment='center', transform = ax1.transAxes)
    ax2.text(0.5, -0.1,'n='+ str(nnumber), horizontalalignment='center', verticalalignment='center', transform = ax2.transAxes)
    ax1.text(1.1, -0.15,'X position(mm)', horizontalalignment='center', verticalalignment='center', transform = ax1.transAxes, fontsize=16)


    #plt.rcParams['figure.figsize'] = [4, 4]
    
    return plt

def average_list(df, phase):  #position tracking
    
    import pandas as pd
    
    phase_X = df.filter(regex="X.*")
    phase_Y = df.filter(regex='Y.*')
    averagelist = []
    averagelist.append(phase_X.mean(axis=1))
    averagelist.append(phase_Y.mean(axis=1))
    averagephase = pd.concat(averagelist, axis=1)
    averagephase.columns = [phase+'Avg_X', phase+'Avg_Y'] #renaming    

    return averagephase

def removenans(df):
    perc = 50.0
    min_count =  int(((100-perc)/100)*df.shape[0] + 1)
    df = df.dropna(axis=1, thresh=min_count)
    
    return df

def onlycolsneeded(df):
    cols = [col for col in df if col.endswith('X') or col.endswith('Y')]
    df = df.loc[:,cols]
    
    return df

def reassembly(results, results3, fps):
    import pandas as pd

    results2 = pd.DataFrame() 

    df_dark = results[(results['ExperimentState'] == 'Assimilation time - Dark') | (results['ExperimentState']== 'Dark')] 
    df_dark = df_dark.tail(fps*23)
    df_lightassim = results[(results['ExperimentState']== 'Assimilation time - Full')].tail(fps*3)
    df_light = results[(results['ExperimentState']== 'Full')].tail(fps*20)        
    df_recovery = results[(results['ExperimentState']== 'DARK - RECOVERY PHASE')]

    results2 = pd.concat([df_dark, df_lightassim, df_light]).reset_index(drop = True)    
    results2 = removenans(results2)      
    results2 = onlycolsneeded(results2)
    results3 = pd.concat([results3, results2], axis = 1).reset_index(drop = True)

    return results3

def jonnysmagic(df):
    
    test = df.loc[:,'Time'].reset_index()    
    test['Time_before'] = test["Time"].shift(1)
    test["e4"] = test["Time"] != test["Time_before"]
    test["Change"] = test["e4"].cumsum()

    return test

def fivefps(dfs, fps):
    import pandas as pd
    import numpy as np
    
    results3 = pd.DataFrame()
    results4 = pd.DataFrame()
    df_time = pd.DataFrame() 
    df_time['Seconds'] = np.arange(0,46,1/5)    
    
    for df in dfs:
        results = pd.DataFrame() 
        results2 = pd.DataFrame()  
        test = jonnysmagic(df)
        for i in range(1,test['Change'].max()+1):
            chunk = df[test['Change'] == i].head(5)
            results = pd.concat([results, chunk])
            
        results3 = reassembly(results, results3, fps)
        
    results4 = pd.concat([df_time, results3], axis=1)

    return results4

def mixedfps(dfs, fps):
    import pandas as pd
    import numpy as np
    
    df_time = pd.DataFrame() 
    df_time['Seconds'] = np.arange(0,46,1/fps)        
    results5 = pd.DataFrame()
    
    if fps==1: 
        adj_dfs=pd.DataFrame()
        for df in dfs:
            results3 = pd.DataFrame()
            results4 = pd.DataFrame() 
            if df.Seconds.diff().mean() < 0.8:
                test = jonnysmagic(df)
                new_df = df[df.index.isin(test.groupby(['Change'])['index'].min().values)] 
                new_df = reassembly(new_df, results3, fps)
                adj_dfs = pd.concat([adj_dfs, new_df], axis = 1).reset_index(drop=True)
            else:                
                df = reassembly(df, results3, fps)
                adj_dfs = pd.concat([adj_dfs, df], axis = 1).reset_index(drop=True)
                
    results5 = pd.concat([df_time, adj_dfs], axis=1)     
    
    return results5

def cleanup(results4, fps, driver):

    
    ly = []
    ly.extend(['Assimilation time - Dark' for i in range(fps*3)])
    ly.extend(['Dark' for i in range(fps*20)])
    ly.extend(['Assimilation time - Full' for i in range(fps*3)])
    ly.extend(['Full' for i in range(fps*20)])
    #ly.extend(['Recovery phase' for i in range(fps*20)])


    newElements=[*range(1,1000,1)]
    results4.columns = [driver +' X' + '_' + str(newElements.pop(0)) if "X" in col else col for col in results4.columns] 

    newElements=[*range(1,1000,1)] #needs a second one
    results4.columns = [driver +' Y' + '_' + str(newElements.pop(0)) if "Y" in col else col for col in results4.columns]

    results4.insert(1, 'ExperimentState', ly)
    #pixel conversion
    results4.iloc[:,2:] = results4.iloc[:,2:]*0.14  

    #checking for dead flies
    #nnumber = int((len(results4.columns)-2)*0.5)

    #checkingfirstrow = results4.iloc[0,2:]
    #if (nnumber*0.7) <= checkingfirstrow.isnull().sum() <= nnumber*2:
    #    results4 = results4.iloc[1:,:]
    
    return results4

def trans(filename, driver):
    import pandas as pd
    import os

    
    lst=[]
    dfs=[]


    for file_no, k in zip(os.listdir(filename), range(0,200)): 
        if file_no.lower().endswith(".csv") and "w1118" not in file_no:   
            f = os.path.join(filename, file_no)
            df=pd.read_csv(f)
            lst.append(df.Seconds.diff().mean())
            dfs.append(df)


    if all(x<0.8 for x in lst) == True:
        fps = 5
    else:
        fps=1

    if fps ==5:
        df_t = fivefps(dfs, fps)

    if fps ==1:
        df_t = mixedfps(dfs, fps)

    df_t = cleanup(df_t, fps, driver)  
    
    return df_t, fps

def control(filename, wt):
    import os
    import pandas as pd
    lst=[]
    dfs=[]


    for file_no, k in zip(os.listdir(filename), range(0,200)): 
        if file_no.lower().endswith(".csv") and "w1118" in file_no:   
            f = os.path.join(filename, file_no)
            df=pd.read_csv(f)
            lst.append(df.Seconds.diff().mean())
            dfs.append(df)

    if all(x<0.8 for x in lst) == True:
        fps = 5
    else:
        fps=1

    if fps ==5:
        df_t = fivefps(dfs, fps)

    if fps ==1:
        df_t = mixedfps(dfs, fps)

    df_t = cleanup(df_t, fps, wt)  
    
    return df_t, fps

def frames(df):
   
    time = df['Seconds'].iloc[2] - df['Seconds'].iloc[1]
    if time == 1.0:
        fps =1
    if time <1.0:
        fps =5
    
    return fps

def separation (df, phase):
    
    phase_X_Y= df[(df['ExperimentState'] == 'Assimilation time - '+ phase) | (df['ExperimentState']== phase)].drop(df.columns[[1]],axis = 1)
    
    return phase_X_Y

def maxheight(df, genre):
    import pandas as pd
    
    yonly = pd.DataFrame()
    yonly = df.filter(regex="Y.*")
    yonly['Seconds'] = df.loc[:,'Seconds']
    tacalc = pd.DataFrame()

    maxilst=[]
    timelst=[]

    for b in yonly.columns[0:-1]:
        maxi = yonly[b].max(axis=0)
        indx = yonly[b].idxmax()
        time = yonly.loc[indx,"Seconds"]
        maxilst.append(maxi)
        timelst.append(time)

    tacalc['Max height '+ genre] = maxilst
    tacalc["Time to reach max height " + genre]=timelst

    return tacalc

def heightso(dfexpt, avgmaxheight):
    import pandas as pd
    
    expt = pd.DataFrame()
    expt = dfexpt.filter(regex = "Y.*")
    expt = expt.reset_index(drop=True)

    ho2=pd.DataFrame()

    for n in expt.columns:
        nno = pd.DataFrame()
        nno[n] = expt[n]
        nno[n+' Top'] = 0
        nno.loc[(nno[n]>=avgmaxheight),[n+' Top']] = 1
        nno[n+' Quarter'] = 0
        nno.loc[(nno[n]>=0.75*avgmaxheight),[n+' Quarter']] = 1

        ho2 = pd.concat([ho2, nno], axis = 1)
    ce = pd.DataFrame()
    ce["max height hangout"] = ho2.filter(regex="Top.*").sum(axis=0).reset_index(drop=True)
    ce["three quarter height hangout"] = ho2.filter(regex="Quarter.*").sum(axis=0).reset_index(drop=True)
    ce.iloc[:,:] = ce.iloc[:,:]*1/frames(dfexpt)

    return ce

def speedcalc(df, fps):
    import pandas as pd
    import numpy as np
    
    indices = list(range(1,len(df.columns),2))
    rows = list(range(0,len(df)-1))
    df_dist = pd.DataFrame()
    
    for i,kk in zip(indices, range(1,len(indices))):  #parsing through each object
       # naming = df.iloc[:,i].name #series name
        distance_list =[]
        temp = pd.DataFrame()
        k = str(kk)
        
        for ii in rows: #parsing through each line in column
            x1_D = df.iloc[ii,i] #0,1
            y1_D = df.iloc[ii,i+1] #0,2
            x2_D = df.iloc[ii+1,i] #1,1
            y2_D = df.iloc[ii+1,i+1] #1,2
            distance = (((x2_D-x1_D)**2) + ((y2_D-y1_D)**2))**0.5
            distance_list.append(distance)
        temp["Velocity_"+k]= distance_list
        df_dist = pd.concat([df_dist, temp], axis=1).reset_index(drop=True)
        
    ca = 1/fps
    
    df_dist.iloc[:,:] = df_dist.iloc[:,:]/ca      
    
    df3 = pd.DataFrame([[np.nan] * len(df_dist.columns)], columns=df_dist.columns)
    df2 = pd.concat([df3, df_dist], ignore_index=True)
    #df2 = df3.concat(df_dist, ignore_index=True)
    
    df2['Seconds'] = df['Seconds'].reset_index(drop=True)
    return df2

def avgmean(df, phase, fps):
    import pandas as pd
    df9 = pd.DataFrame()
    dfd = pd.DataFrame()
    
    Dark_phase_X_Y= df[(df['ExperimentState']== phase)].drop(df.columns[[1]],axis = 1)
    df_speed_D = speedcalc(Dark_phase_X_Y, fps)    
    df9 = df_speed_D.iloc[:,0:-1]
    dfd["Mean"]= df9.mean(axis=1)

    return dfd       
         
def fallso(df, fps):
    import pandas as pd
    
    df0 = df.filter(regex="Y.*")
    fall2=pd.DataFrame()
    frontrow = df.iloc[:,0:2]
    
    for n,k in zip(df0.columns, range(1,len(df0.columns))):
        kk = str(k)
        fallo = pd.DataFrame()
        fallo['Diff_' + kk] = df0[n] - df0[n].shift(1)
        fallo['Fall_'+ kk ] = 0
        fallo.loc[(fallo['Diff_'+ kk ]<-15),['Fall_'+ kk]] = 1
        fallo['Distance_'+ kk]=0
        fallo.loc[(fallo['Diff_'+ kk]<-15),['Distance_'+ kk]] = fallo['Diff_'+kk]
        fall2 = pd.concat([fall2, fallo], axis = 1)
    
    fall2 = pd.concat([frontrow, fall2], axis=1)
    fall2['Total falls per sec']=fall2.filter(regex = "Fall.*").sum(axis=1)    
    fall2['Overall falls']=fall2['Total falls per sec'].cumsum()

    return fall2

def generation(df, driver):
    import pandas as pd
    import numpy as np
    import re
    from natsort import index_natsorted
    
    Dark_phase_X_Y = separation(df, "Dark")
    Light_phase_X_Y = separation(df, "Full")
    fps = frames(df)
    
    #falling occurence
    dff_dark = df[(df['ExperimentState'] == 'Assimilation time - Dark') | (df['ExperimentState']== 'Dark')] 
    dff_light = df[(df['ExperimentState'] == 'Assimilation time - Full') | (df['ExperimentState']== 'Full')] 
    dff_d=fallso(dff_dark, fps)
    dff_l=fallso(dff_light, fps)
    dfftot2 = pd.DataFrame()
    dfftot2 = pd.concat([dff_d, dff_l])
    dfftot2.iloc[:,2:] = dfftot2.iloc[:,2:]
    #dfftot4 = dfftot2.replace(0.0, "", regex=True)
    dfftot3 = dfftot2.filter(regex = "Fall.*")
    
    #speed
    df_speed_D = speedcalc(Dark_phase_X_Y, fps)
    df_speed_L = speedcalc(Light_phase_X_Y, fps)
    df_speedtot = pd.DataFrame()
    df_speedtot = pd.concat([df_speed_D, df_speed_L]).reset_index(drop=True) 
    dfst3 = df_speedtot
    dfst3.columns = dfst3.columns.str.replace(driver, 'Velocity '+ driver)
    
    dfst4 = dfst3.drop(["Seconds"], axis =1)
    dfst5 = pd.concat([dfftot2.filter(regex = "Diff.*"), dfst4],axis = 1)
    heading = dfst5.columns
    lstp = []
    pdf = pd.DataFrame()
    for n in range(0,len(heading)):
        lstp.append(int(re.search(r'(?<=_)\d+', heading[n]).group()))
    pdf['Headings']=heading
    pdf['num'] = lstp
    pdff= pdf.sort_values(by='num', key=lambda x: np.argsort(index_natsorted(pdf["num"]))).reset_index(drop=True)
    dfst6 = dfst5.reindex(columns = pdff['Headings'])
    for u2 in range(0,len(dfst6.columns),2):
        for u1 in range(0,len(dfst6)):
            if dfst6.iloc[u1,u2]<0.0:
                nval = dfst6.iloc[u1,u2+1]
                dfst6.iloc[u1,u2+1] = -abs(nval)
    dfst6 = dfst6.filter(regex="Velocity.*")
    
    #total
    dffnew = pd.DataFrame()
    dffnew = pd.concat([dffnew, df], axis=1)
    dffnew = pd.concat([dffnew, dfftot3], axis=1)
    dffnew = pd.concat([dffnew, dfst6], axis=1)

    heading2 = dffnew.iloc[:,2:].columns
    lstp2 = []
    pdf2 = pd.DataFrame()
    for n2 in range(0,len(heading2)):
        lstp2.append(int(re.search(r'(?<=_)\d+', heading2[n2]).group()))
    pdf2['Headings']=heading2
    pdf2['num'] = lstp2
    pdff2= pdf2.sort_values(by='num', key=lambda x: np.argsort(index_natsorted(pdf2["num"]))).reset_index(drop=True)
    dffn = dffnew.iloc[:,2:]
    dfr = dffn.reindex(columns = pdff2['Headings'])
    for v2 in range(2,len(dfr.columns),4):
        for v1 in range(0,len(dfr)):
            if dfr.iloc[v1,v2]>= 1:
                dfr.iloc[v1,v2+1] = np.nan
    first2 = dffnew.iloc[:,0:2]
    dftotalexpt = pd.concat([first2, dfr],axis=1)
    
    #removing tracking errors
    chunk = len(dftotalexpt.iloc[:,2:].columns)/4
    np.hsplit(dftotalexpt.iloc[:,2:],chunk)
    dfowo = pd.DataFrame()
    for n in np.hsplit(dftotalexpt.iloc[:,2:],chunk):
        #if velocity exceeds 100
        dfstp = n.filter(regex="Velocity.*")
        output = np.sum(dfstp > 100)
        
        #if acceleration exceeds 100
        temp = pd.DataFrame()
        temp['Acc'] = abs(dfstp.diff())/(1/fps)
        output2 = np.sum(temp > 100)
        
        #if there are dead flies
        half = int(len(n)/2)  #only checking dark half
        dfstp2 = n.iloc[0:half,1]
        output3 = np.sum(dfstp2 < 1)  #if y pos less than 1 (if y poss less than 1 for 110 times = dead fly)

        if int(output) < 3.0 and int(output2) < 8.0 and int(output3) < 100:
            dfowo=pd.concat([dfowo,n], axis=1)
                
    dfowo = pd.concat([dftotalexpt.iloc[:,0:2], dfowo], axis = 1)

    return dfowo

def calcgraph(df, filterword):
    import pandas as pd
  
    phase = ["Dark", "Full"]
    df4 = pd.DataFrame()
    for n in phase:        
        df_sd = df[(df["ExperimentState"] == "Assimilation time - "+n)|(df["ExperimentState"] == n)].reset_index(drop=True)
        df_time = pd.DataFrame()
        if n == "Full":
            df_time['Seconds'] = df_sd['Seconds']-23
        else:
            df_time['Seconds'] = df_sd['Seconds']
        df_sd2 = df_sd.filter(regex=filterword)
        df_time["ExperimentState"] = n
        df_sd2 = abs(df_sd2)
        df_sd3 = pd.concat([df_time, df_sd2], axis=1)
        df4 = pd.concat([df4, df_sd3])
        
    return df4

def meangraph(df):
    import pandas as pd
    phase = ['Dark','Full']
    dft = pd.DataFrame()
    for n in phase:
        df1 = df[(df["ExperimentState"] == "Assimilation time - "+n)|(df["ExperimentState"] == n)].reset_index(drop=True)
        df_meand = pd.DataFrame()
        df_meand['Seconds']=df1['Seconds']
        df_meand['ExperimentState'] = n
        df_meand['mean']= df1.iloc[:,2:].mean(axis=1)
        df_meand['CI']= df1.iloc[:,2:].sem(axis=1)*1.96        
        dft = pd.concat([dft, df_meand])
    return dft

def fallcalc(df, phase):
    import pandas as pd
    
    dff = df.filter(regex="Fall.*")
    dff = pd.concat([df.iloc[:,0:2], dff], axis=1)
    dff2 = dff[(dff["ExperimentState"] == "Assimilation time - "+phase)|(dff["ExperimentState"] == phase)].reset_index(drop=True)
    nnumber = len(dff2.iloc[:,2:].columns)
    dff2["Total falls per sec"] = (dff2.iloc[:,2:].sum(axis=1))/nnumber
    
    return dff2

def violinfall(df, phase):
    import pandas as pd
    import numpy as np
    
    dffall = df.filter(regex="Fall.*")
    dffall = pd.concat([df.iloc[:,0:2], dffall], axis=1)
    dffall = dffall[(dffall["ExperimentState"] == phase)].reset_index(drop=True)
    if phase == "Full":
        dffall['Seconds']-=26
    if phase == "Dark":
        dffall['Seconds']-=3
    df_test = dffall.copy()
    for r in dffall.iloc[:,2:].columns:
        df_temp = pd.DataFrame()
        df_temp['Time ' + r] = [0]*len(dffall)
        df_test = pd.concat([df_test,df_temp], axis = 1)
        df_test.loc[(dffall[r]>0), ['Time ' +r]] = df_test['Seconds']
    df_test= df_test.filter(regex="Time .*")
    df_test2 = pd.concat([dffall['ExperimentState'],df_test], axis = 1)
    dfuu = pd.melt(df_test2, id_vars=['ExperimentState'])
    dfuu= dfuu.replace(0.0, np.nan, regex=True)
    
    return dfuu

def rastergraph(dfexpt):
    import pandas as pd
    
    dffall = dfexpt[(dfexpt['ExperimentState'] == 'Dark') | (dfexpt['ExperimentState']== 'Full')].filter(regex="Fall.*")
    dffall = pd.concat([dfexpt.iloc[:,0:2], dffall], axis=1)
    df_test = dffall.copy()
    for r in dffall.iloc[:,2:].columns:
        df_temp = pd.DataFrame()
        df_temp['Time ' + r] = [0]*len(dffall)
        df_test = pd.concat([df_test,df_temp], axis = 1)
        df_test.loc[(dffall[r]>0), ['Time ' +r]] = df_test['Seconds']
    df_test= df_test.filter(regex="Time .*")
    dfuu = pd.melt(df_test)
    dfu2 = dfuu[dfuu['value'] > 0].reset_index(drop=True)  
    
    return dfu2

def velodabest(df, typeo, keyword):
    import pandas as pd
    #typeo is either WT or EXPT
    
    phase = ["Dark", "Full"]
    fgt2b = pd.DataFrame()
    for n in phase:
        df_sed = calcgraph(df, n, keyword)
        fgt = pd.DataFrame()
        fgt["Velocity"]= df_sed.iloc[:,2:].mean(axis=0)
        fgt["ExperimentState"] = n
        fgt2b = pd.concat([fgt2b, fgt])
        
    fgt2b["Type"] = typeo
    fgt2b
    
    return fgt2b