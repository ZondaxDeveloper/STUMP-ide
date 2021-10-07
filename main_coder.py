from tkinter import *

def Root_raiz():
    raiz = Tk()
    gmy = "340x800"
    raiz.geometry(gmy)

    cod_sd1 = Label(raiz, text="""Import Modules:
    imp [module]
    frxm [module] imp [submodule or *(all)]
    """).pack()


    cod_sd2 = Label(raiz, text="""Vars:
    bool, integer, string, flt""").pack()


    cod_sd3 = Label(raiz, text="""Structures:
    if{

    }
    else{

    }
    tryStructure:
        try:
        exept:
        else:

    

    class [clasname](){

    }
    def [defname](){

    }
    """).pack()
    cod_sd4 = Label(raiz, text="""Operators:
    +, -, x, /,
    ConsoleLog(print):
    prt([text])""").pack()


    raiz.mainloop()