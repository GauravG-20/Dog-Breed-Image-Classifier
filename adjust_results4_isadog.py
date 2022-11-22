def adjust_results4_isadog(results_dic, dogfile):   
    dognames_dic=dict()
    
    with open(dogfile,"r") as infile:
        
        line = infile.readline()
        
        while line != "":
            line=line.strip().split(',')
            line = [i.strip().lower() for i in line]
            
            for i in line:
                if dognames_dic.get(i) is None:
                    dognames_dic[i] = 1
            line = infile.readline()

    dognames_dic_list = dognames_dic.keys() # list of keys of dognames_dic
    dognames_dic_set = set([i.strip().lower() for i in dognames_dic_list]) # set of keys of dognames_dic in lower
    
    for key in results_dic:
        breeds = results_dic[key][1].split(',')
        breeds = set([i.strip().lower() for i in breeds]) 
        if dognames_dic.get(results_dic[key][0].lower().strip()) is not None:
            
            if breeds.intersection(dognames_dic_set):
                results_dic[key].extend([1,1])
            else:
                results_dic[key].extend([1,0])
        else:
            if breeds.intersection(dognames_dic_set):
                results_dic[key].extend([0,1])   
            else:
                results_dic[key].extend([0,0])
                
    return None
            
    
