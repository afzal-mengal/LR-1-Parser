def first(grammar,terminals,nonterminals):
    symbols=nonterminals+terminals
    firstsets={}
    for i in symbols:
        firstsets[i]=None
    while(True):
        newfirstsets=firstsets.copy()
        for i in symbols:
            if i in terminals:
                firstsets[i]=i 
            else:
                rhs=grammar[i].split('|')
                for j in rhs:
                    for k in terminals:
                        if j.startswith(k):
                            firstsets[i]=k
                            if firstsets[i]:
                                if k not in firstsets[i]:
                                    if firstsets[i]:
                                        firstsets[i]=firstsets[i]+','+k
                                
                    for k in nonterminals:
                        if j.startswith(k):
                            firstsets[i]=firstsets[k]
                            if firstsets[i]:
                                if firstsets[k] not in firstsets[i]:
                                    if firstsets[i]:
                                        firstsets[i]=firstsets[i]+','+firstsets[k]
        if(firstsets==newfirstsets):
            break
    return firstsets


grammar={
    'S':'E',
    'E':'T-E|T',
    'T':'FxT|F',
    'F':'id'
}

terminals=['id','-']
nonterminals=['S','E','T','F']
first_sets=first(grammar,terminals,nonterminals)

initial={
    'S':'.E,$'
}