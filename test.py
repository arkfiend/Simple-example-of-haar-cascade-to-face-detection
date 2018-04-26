from functions import *

import os







def geraResp(dif):
    res = []
    path = []   # WINDOWS
    
    #   LINUX
    texto=""
    if dif==1:
        texto = "easy/easy.txt"
    if dif==2:
        texto = "med/med.txt"
    if dif==3:
        texto = "hard/hard.txt"
    
    #Ando no arquivo
    archive = open(texto, "r")
    string = 0 #Serve para saber se e uma string
    max_ = 0 #Seve para saber se o e o valor maximo agora
    coord = 0 #Serve para saber se e uma coordenada
    
    while 1:
        lines = archive.readlines()
        if not lines:
            break #Sai do loop 
        
        i=0
        while True:
            if i >=len(lines):
                break
            
            #Primeiro pego a string
            path = "C:/Joao Mari/Aprendizado/FACE RECOGNITION/git lab"
            path = path + "/"
            path = path + lines[i]
            if path[len(path)-1]=='\n':
                path = path[:-1] # tira o /n
            
            #print "Path=  i = ", i
            
            ###Agora pego o numero de itens
            i = i+1
            if i>=len(lines):
                break
            min_ = 0
            max_ = lines[i]
            if len(max_)>1: #######################################33 tem que ser igua a /n """"""" mais que 10 facs
                max_ = max_[:-1]
            max_ = int(max_)
            ###Agora pego o numero de itens
            
            #print "Num=  i = ", i
            
            ###Faco um FOR para percorrer e pegar as coords
            coord =[]
            
            for j in range(0, max_):
                
                i = i+1
                if i>=len(lines):
                    break
                
                lol = []
                lol = lines[i]
                
                if lol[len(lol)-1]=='\n':
                    lol=lol[:-1]
                
                lol = lol.split(' ')
                coord.append((int(lol[0]), int(lol[1]), int(lol[2]), int(lol[3])))
                
            ###Inserir as informacoes num vetor
            res.append((path, max_, coord))
            #print "Coord = ", i
            i = i+1
            if i >= len(lines):
                break
            
            #print "------"
        return res


def try_(resp, taxa_de_erro):
    total_imagens = len(resp)
    acertos = 0
    pontuacao = 0
    for i in range(0, total_imagens):
        path = resp[i][0]
        pic = misc.imread(path)
        faces_resposta = resp[i][1]
        
        ######################################################3
        vector_face = face_detect(pic)
        if len(vector_face)> 10:
            #Tratar esse caso, fazer algo pra filtrar somente as melhores.
            print "mais de 10"
        
        if len(vector_face)==0:
            '''print "----------------"
            print "Nao encontrada nenhuma face."
            print "path = ", path
            print "----------------"
            '''
            continue

        
        ###plt.figure()
        ###plt.imshow(pic)
        ###axis = plt.gca()
        
        
        #Comparar os lcoais dos retangulos e ver se acertou
        for vec in resp[i][2]:
                    x = vec[0] - taxa_de_erro
                    y = vec[1] - taxa_de_erro
                    w = vec[2] + taxa_de_erro
                    h = vec[3] + taxa_de_erro
                    
                    for (xf, yf, wf, hf) in vector_face:
                        ###axis.add_patch(Rectangle((xf,yf), wf, hf, facecolor='none', edgecolor='red'))
                        ##CADEIA DE IFs
                        distX = abs(x - xf)
                        distY = abs(y - yf)
                        '''print "\n\nx = ", x
                        print "y = ", y
                        print "w = ", w
                        print "h = ", h
                        print "distX = ", distX
                        print "distY = ", distY
                        '''
                        
                        if (distX < w or distX < wf) and (distY < h or distY < w):
                            ##print "ACERTOU"
                            acertos = acertos+1
                            ##print "acertos = ", acertos
                    #Ver se acertou todas as faces
                    ###axis.add_patch(Rectangle((x,y), w, h, facecolor='none', edgecolor='yellow'))
                    ###plt.show()
                    
                    if acertos >= faces_resposta:
                        pontuacao = pontuacao +1
                        acertos = 0
                    acertos = 0
    return pontuacao