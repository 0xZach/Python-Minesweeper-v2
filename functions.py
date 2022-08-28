import tkinter as tk
import tkinter.font as font
import random as r


def toSettings(ws):
    ws.rootS = tk.Frame(ws.root, borderwidth=10, bg='DodgerBlue2', relief="solid")
    ws.rootS.pack()
    widthS = 350
    heightS = 500
    ws.rootS.place(x=(ws.current_x_size/2 - widthS/2),y=(ws.current_y_size/2 - heightS/2),width = widthS, height = heightS)

    ws.sizet = tk.Label(ws.root,bg="SkyBlue3",text="Resolution: ")
    ws.sizet.pack()
    ws.sizet.place(x=(ws.current_x_size/2 - widthS/2+50),y=(ws.current_y_size/2 - heightS/2 + 20))

    ws.sizel = tk.Listbox(ws.root, bg="SkyBlue3")
    ws.sizel.pack()
    ws.sizel.place(x=(ws.current_x_size/2 - widthS/2+50),y=(ws.current_y_size/2 - heightS/2 + 50),height=100)
    ws.sizel.insert(0,'Maximised')
    ws.sizel.insert(1,'fullscreen')

    ws.difft = tk.Label(ws.root,bg="SkyBlue3",text="Difficulty: ")
    ws.difft.pack()
    ws.difft.place(x=(ws.current_x_size/2 - widthS/2+50),y=(ws.current_y_size/2 - heightS/2 + 220))

    ws.difflist = tk.Listbox(ws.root, bg="SkyBlue3")
    ws.difflist.pack()
    ws.difflist.insert(0,'Easy')
    ws.difflist.insert(1,'Normal')
    ws.difflist.insert(2,'Hard')
    ws.difflist.place(x=(ws.current_x_size/2 - widthS/2+50),y=(ws.current_y_size/2 - heightS/2 + 250),height=100)

    ws.applyS = tk.Button(ws.root, text="Apply",bg="SkyBlue3",activebackground="SkyBlue3", command = lambda:applySettings(ws))
    ws.applyS.pack()
    ws.applyS.place( x=(ws.current_x_size/2 - widthS/2 +20) , y=(ws.current_y_size/2 -heightS/2 + heightS-heightS/10) )

    ws.quitS = tk.Button(ws.root, text="return",bg="SkyBlue3",activebackground="SkyBlue3", command = lambda:toMenu(ws))
    ws.quitS.pack()
    ws.quitS.place(x=(ws.current_x_size/2 - widthS/2 + widthS-widthS/5),y=(ws.current_y_size/2 -heightS/2 + heightS-heightS/10))

def applySettings(ws):
    selectionSize = ws.sizel.curselection() # renvoi l'index choisi sous forme de tableau
    if(selectionSize != ()):
        if(selectionSize[0] == 0):
            ws.newSize(0,0,1)
        elif(selectionSize[0] == 1):
            ws.newSize(0,0,2)
    
    selectionDiff = ws.difflist.curselection()
    if(ws.gameStart == True):
        if(selectionDiff != ()):
            ws.nbr_flags.destroy()
            ws.display_nbrbombs.destroy()
            if(selectionDiff[0] == 0):
                ws.diff.set(0)
                create_grid(ws,ws.diff)
            elif(selectionDiff[0] == 1):
                ws.diff.set(1)
                create_grid(ws,ws.diff)
            elif(selectionDiff[0] == 2):
                ws.diff.set(2)
                create_grid(ws,ws.diff)
            toMenu(ws)
            toSettings(ws)
    else:
        if(selectionDiff != ()):
            if(selectionDiff[0] == 0):
                ws.diff.set(0)
            elif(selectionDiff[0] == 1):
                ws.diff.set(1)
            elif(selectionDiff[0] == 2):
                ws.diff.set(2)

def toMenu(ws):

    ws.sizel.destroy()
    ws.sizet.destroy()

    ws.difflist.destroy()
    ws.difft.destroy()

    ws.applyS.destroy()
    ws.rootS.destroy()
    ws.quitS.destroy()


def create_grid(ws,difficulty):    
    
    def afficherBombs(): # fonction d'affichage de toute les bombes
        
        for i in range(100): # pour chaque case, on vérifie s'il y a une bombe et on applique la couleur
            
            if(infos['is_'+str(i)+'_bombed'] == False and infos['case_'+str(i)]["background"] == "red4"):
                infos['case_'+str(i)].configure(background="SpringGreen4")
                
            if(infos['is_'+str(i)+'_bombed'] == True and infos['case_'+str(i)]["background"] != "gray26"):
                infos['case_'+str(i)].configure(background="gray26")
    
    
    def gagner(): # fonction qui renvois un booleen, True si le joueur à gagné, False si ce n'est pas le cas
        for i in range(100): # pour chaque case, on vérifie si elle ne contient pas de bombe ET a déjà été découverte
            
            if(infos['is_'+str(i)+'_bombed'] == False and infos['case_'+str(i)]["background"] != "OliveDrab1"):
                return False # si une case ne correspond pas, alors on return false
                
        return True

    
    def numberOfBombs(wbutton): # returns int, nombre de bombes autour de la case
        
        nbBomb = 0
        list_ligne=[-1,0,1]
        list_colon=[-10,0,10]
        
        for i in list_ligne:
            if(wbutton+i >= 0 and wbutton+i < 100): # on test si on est bien dans le nombre de boutons
                
                for j in list_colon:
                    if((wbutton+j >= 0 and wbutton+j < 100) and (wbutton+j+i >=0 and wbutton+j+i < 100)): # on test si on est bien dans le nombre de boutons
                        
                        if(infos['is_'+str(wbutton+i+j)+'_bombed']== True and (infos[str(wbutton)+"_X"]+i>=0 and infos[str(wbutton)+"_X"]+i<=9)):
                            
                            if(infos['is_'+str(wbutton+i+j)+'_bombed']== True and (infos[str(wbutton)+"_Y"]>=0 and infos[str(wbutton)+"_Y"]<=9)):
                                nbBomb+=1
        
                
        return nbBomb
    
    
    def checkButtons(wbutton,first):
        list_Ligne=[-1,0,1] #listes des changements de coordonnées en ligne
        list_Colon=[-10,0,10] #listes des changements de coordonnées en colonne
        
        for i in list_Ligne:
            
            if(wbutton+i >= 0 and wbutton+i < 100): # on test si on est bien dans le nombre de boutons
                    #on teste si il y a une bombe dans la case '+i' et on vérifie si les coordonnées sont entre 0 et 9 (de 0 à la taille de ligne)
                    for j in list_Colon:
                        #print(j)
                        if((wbutton+j >= 0 and wbutton+j < 100) and (wbutton+j+i >=0 and wbutton+j+i < 100)): # on test si on est bien dans le nombre de boutons
                             
                            if(first==False):
                                 if(infos['case_'+str(wbutton+i+j)]['background']=='SpringGreen4'): # on regarde si la case est toujours caché et on ne la teste que dans le cas où elle l'est
                                     
                                    if(infos['is_'+str(wbutton+i+j)+'_bombed']== False and (infos[str(wbutton)+"_X"]+i>=0 and infos[str(wbutton)+"_X"]+i<=9)):
                                        if(infos['is_'+str(wbutton+j+i)+'_bombed'] == False and (infos[str(wbutton)+"_Y"]>=0 and infos[str(wbutton)+"_Y"]<=9)):
                                        # on vérifie si les coordonnées sont entre 0 et 9 (de 0 à la taille de la colonne)
                                            infos['case_'+str(wbutton+i+j)].configure(background="OliveDrab1") # on configure la nouvelle couleur
                                            #print(wbutton+i+j,i,j)
                                            
                                            nb_Bombs = numberOfBombs(wbutton+i+j)
                                            if(nb_Bombs > 0):
                                                infos['case_'+str(wbutton+i+j)].configure(text=nb_Bombs)
                                            elif(nb_Bombs == 0):
                                                checkButtons(wbutton+i+j,False)
                            
                            else:
                                if(infos['is_'+str(wbutton+i+j)+'_bombed']== False and (infos[str(wbutton)+"_X"]+i>=0 and infos[str(wbutton)+"_X"]+i<=9)):
                                    if(infos['is_'+str(wbutton+j+i)+'_bombed'] == False and (infos[str(wbutton)+"_Y"]>=0 and infos[str(wbutton)+"_Y"]<=9)):
                                    # on vérifie si les coordonnées sont entre 0 et 9 (de 0 à la taille de la colonne)
                                        infos['case_'+str(wbutton+i+j)].configure(background="OliveDrab1") # on configure la nouvelle couleur
                                        #print(wbutton+i+j,i,j)
                                        
                                        nb_Bombs = numberOfBombs(wbutton+i+j)
                                        if(nb_Bombs > 0):
                                            infos['case_'+str(wbutton+i+j)].configure(text=nb_Bombs)
                                        elif(nb_Bombs == 0):
                                            checkButtons(wbutton+i+j,False)

           
    def onclick(wbutton,jouable,difficulty):
        if(jouable.get()==1):
            # couleurs cases bombe: red4 ; gray26
            if(infos['is_'+str(wbutton)+'_bombed'] == True and infos['case_'+str(wbutton)]['background']!="gray26"):
                # on donne la couleur à la case si elle contient une bombe est n'est pas déjà colorée
                infos['case_'+str(wbutton)].configure(relief='sunken')
                infos['case_'+str(wbutton)].configure(background="gray26")
                # on affiche les autres bombes
                afficherBombs()
                # on termine la partie
                jouable.set(2)
                
                # on créé la fenetre d'affichage du message de fin de partie
                #lose_frame = tk.Tk()
                #lose_frame.title('Minesweeper ZS 1.0')
                #lose_frame.geometry('180x120')
                #lose_frame.configure(bg='light goldenrod')

                losefont = font.Font(family='Helvetica', size=30, weight='bold')
                replayfont = font.Font(family='Helvetica', size=15, weight='bold')
                lose = tk.Label(ws.root, text="You lost!", font = losefont, background='light goldenrod', relief="solid")
                lose.pack()
                lose.place(x=ws.current_x_size-ws.current_x_size/2.5-150,y=ws.current_y_size/3, width=250, height=100)
                replay = tk.Button(ws.root, text="Replay?", font = replayfont, background='goldenrod', activebackground='goldenrod', borderwidth=4, command= lambda:rejouer(jouable,replay,lose))
                replay.pack()
                replay.place(x=ws.current_x_size-ws.current_x_size/2.5-100,y=ws.current_y_size/3+200, width=150)
                
            elif(infos['case_'+str(wbutton)]['background']!="OliveDrab1" and infos['case_'+str(wbutton)]['background']!="gray26"):
                # on donne la couleur bleu à la case si elle ne contient une bombe est n'est pas déjà bleu
                checkButtons(wbutton,False)
                #print(gagner())
                if(gagner() == True): # si on a gagné
                    # on affiche l'emplacement des bombes
                    afficherBombs()
                    
                    # on termine la partie
                    jouable.set(2)
                    
                    # on affiche le message de fin de partie.
                    winfont = font.Font(family='Helvetica', size=30, weight='bold')
                    replayfont = font.Font(family='Helvetica', size=15, weight='bold')
                    win = tk.Label(ws.root, text="You Won!", font = winfont, background='light goldenrod', relief="solid")
                    win.pack()
                    win.place(x=ws.current_x_size-ws.current_x_size/2.5-150,y=ws.current_y_size/3, width=250, height=100)
                    replay = tk.Button(ws.root, text="Replay?", font = replayfont, background='goldenrod', activebackground='goldenrod', borderwidth=4, command= lambda:rejouer(jouable,replay,win))
                    replay.pack()
                    replay.place(x=ws.current_x_size-ws.current_x_size/2.5-100,y=ws.current_y_size/3+200, width=150)
        
        elif(jouable.get() == 0):
            if(difficulty.get() == 0):
                nbr_bombs=15
            elif(difficulty.get() == 1):
                nbr_bombs=25
            elif(difficulty.get() == 2):
                nbr_bombs=40
            infos['case_'+str(wbutton)]['background']="OliveDrab1"
            bomb_list=[wbutton]
            while(len(bomb_list) < nbr_bombs +1):
                bomb = r.randrange(100)
                dispo = True
                j = 0
                while(j < len(bomb_list) and dispo == True):
                    if(bomb_list[j] == bomb):
                        dispo = False
                    j=j+1
                if(dispo == True):
                    bomb_list.append(bomb)
                    infos['is_'+str(bomb)+'_bombed']=True
            jouable.set(1)
            checkButtons(wbutton,True)
        
    
    def left_click_press(event,i):
        infos['case_'+str(i)].configure(relief='sunken')
        onclick(i,jouable,difficulty)
    def left_click_release(event):
        event.widget.configure(relief='raised')
    
    def right_click_press(event,ws):
        if(difficulty.get() == 0):
            nbr_bombs=15
        elif(difficulty.get() == 1):
            nbr_bombs=25
        elif(difficulty.get() == 2):
            nbr_bombs=40
        
        event.widget.configure(relief='sunken')
        if(event.widget['background']=="SpringGreen4" and infos['nbr_flags'] < nbr_bombs):
            event.widget.configure(background="red4")
            infos['nbr_flags'] = infos['nbr_flags'] + 1
            ws.nbr_flags['text']= "flags left: "+str(nbr_bombs - infos['nbr_flags'])
        elif(event.widget['background']=="red4" and infos['nbr_flags'] <= nbr_bombs):
            event.widget.configure(background="SpringGreen4")
            infos['nbr_flags'] = infos['nbr_flags'] - 1
            ws.nbr_flags['text']= "flags left: "+str(nbr_bombs - infos['nbr_flags'])
    def right_click_release(event):
        event.widget.configure(relief='raised')
    
    def rejouer(jouable,replay,end):
        ws.nbr_flags.destroy()
        ws.display_nbrbombs.destroy()
        create_grid(ws,ws.diff)
        replay.destroy()
        end.destroy()


    


    
    
    # //////////////////////////////////////////////////début de la fonction////////////////////////////////////////////////////////////// #
    




    #switch(difficulty)
    infos = {}
    
    offsetY = 0  # int qui s'incrémentera pour faire plusieurs lignes
    
    jouable = tk.IntVar()
    jouable.set(0) # intVar qui décide si cliquer sur les boutons fait une action ou non.
    
    GameFont = font.Font(family='Helvetica', size=10, weight='bold')
    
    infos['nbr_flags']=0
    
    if(difficulty.get() == 0):
        nbr_bombs=15
    elif(difficulty.get() == 1):
        nbr_bombs=25
    elif(difficulty.get() == 2):
        nbr_bombs=40

    ws.nbr_flags = tk.Label(ws.root, text="flags left: "+str(nbr_bombs), font=GameFont, relief='solid', background='goldenrod')
    ws.nbr_flags.pack
    ws.nbr_flags.place(x = 27, y = ws.current_y_size/8)
    
    ws.display_nbrBombs = tk.Label(ws.root, text="number of bombs:"+str(nbr_bombs), font=GameFont, relief='solid', background='goldenrod')
    ws.display_nbrBombs.pack
    ws.display_nbrBombs.place(x = 682.0, y = ws.current_y_size/8)
    
    for i in range(100):
        name="case_"+str(i)
        infos[name]= tk.Label(ws.root, text="", width=8, height=4, font=GameFont, relief='raised', anchor='center')
        
        infos[name].bind("<ButtonPress-1>", lambda event,i=i:left_click_press(event,i))
        infos[name].bind("<ButtonRelease-1>", left_click_release)
        
        infos[name].bind("<ButtonPress-3>", lambda event,ws=ws: right_click_press(event,ws))
        infos[name].bind("<ButtonRelease-3>", right_click_release)
        
        infos[name].configure(background="SpringGreen4")
        
        infos['is_'+str(i)+'_bombed']=False
        
        """
        if(randrange(4) == 3): # 25% de bombes
            infos['is_'+str(i)+'_bombed']=True
        else:
            infos['is_'+str(i)+'_bombed']=False
        """
        
        # en fonction dun random entre 0 et 1, on donne la propriété correspondante
        # si True alors il y aura une bombe
        # si False alors il n'y aura pas de bombe
        
        #print(infos)
            
        infos[name].place(x = 80 * (i%10) + 27) # calcul de la valeur de largeur de la case en fonction du reste de i%10

        infos[name].place(y = 80*offsetY + ws.current_y_size/8 + 25) # calcul de la valeur de hauteur de la case en fonction de offsetY
        

        infos[str(i)+'_X']= i%10 # on récupère la place X dans le tableau de taille [X][Y]
        
        infos[str(i)+'_Y']= offsetY # on récupère la place Y dans le tableau de taille [X][Y]


        if(80*(i%10) == 720):  # on teste si on est arrivé à la fin de la largeur du tableau
            offsetY = offsetY + 1
    #print((ws.current_y_size/12+25),(ws.current_y_size/20+25))
    

def start_game(ws):
    #ws.newSize(0,0,1)
    ws.gameStart = True
    ws.name.place(x=ws.current_x_size/2 - 150, y=ws.current_y_size/20, height=50, width=250)
    ws.start.destroy()
    #ws.prop.destroy()
    ws.settings.place(x=ws.current_x_size - 250, y=ws.current_y_size/20, width = 80, height = 50)
    create_grid(ws,ws.diff)
