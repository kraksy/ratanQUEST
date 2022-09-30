import time as tm
import os 
import random as rd

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clear()
    
    titleart()

    print("\n"*2)

    print("=== start(1) ===")
    print("=== nastavení(2) ===")
    print("=== quit(3) ===")

    print("\n"*1)

    main = input(">>>          ")

    if main == "1":

        tm.sleep(1.0)

        clear()

        prolog()

    elif main == "2":

        print("made in progress")
        
        tm.sleep(1.0)

        clear()

        menu()

    elif main == "3":

        uluse()

def titleart():
    print("""
          | |                                    | |  
 _ __ __ _| |_ __ _ _ __     __ _ _   _  ___  ___| |_ 
| '__/ _` | __/ _` | '_ \   / _` | | | |/ _ \/ __| __|
| | | (_| | || (_| | | | | | (_| | |_| |  __/\__ \ |_ 
|_|  \__,_|\__\__,_|_| |_|  \__, |\__,_|\___||___/\__|
                               | |                    
                               |_| 
    """)

def uluse():
    clear()
    print("""
                                    dP oo                dP 
                                    88                   88 
dP    dP .d8888b. dP    dP    .d888b88 dP .d8888b. .d888b88 
88    88 88'  `88 88    88    88'  `88 88 88ooood8 88'  `88 
88.  .88 88.  .88 88.  .88    88.  .88 88 88.  ... 88.  .88 
`8888P88 `88888P' `88888P'    `88888P8 dP `88888P' `88888P8 
o~~~~.88~ooooooooooooooooooooooooooooooooooooooooooooooooooo
 d8888P            
    """)
    tm.sleep(8.0)
    menu()

def pp():
    print("""
                (O)
                <M
     o          <M               rataň slayer
    /| ......  /:M\------------------------------------------------,,,,,,
  (O)[]XXXXXX[]I:K+}=====<{H}>================================------------>
    \| ^^^^^^  \:W/------------------------------------------------''''''
     o          <W  
                <W
                (O)
    """)

def ratan():
    print("""
                       ,  ♛  .
                       (\,;,/)
                        (o o)\//,    mighty rataň
                         \ /     \,
                         `+'(  (   \    )
                            //  \   |_./
                          '~' '~----'    
    """)

def d1():
    print("""
				..........
				.	 .
				.	 .
				.   X	 .
				.	 .
				 ...  ...
		           ....... '  ' .......
			   '	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '
		           ....... '  ' .......
			   '	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '		  ....
				   '  '	  ........'  '........	
				   '  '  '      ...  ...      ' 
				   '  '  '.....`  '  '  `.....'
			   	   '  '...........'  '................
                                   '			             ````.
				   .. ...........................    ....' 
				                                 '  '
								 '  '
			                                     .....  .....
				   			     .	        .
				                             .	        .
				                             .	        .
				                             .	        .
                                                             ............
    """)

def d2():
    print("""
    				..........
				.	 .
				.	 .
				.   	 .
				.	 .
				 ...  ...
		           ....... '  ' .......
			   '  X	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '
		           ....... '  ' .......
			   '	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '		  ....
				   '  '	  ........'  '........	
				   '  '  '      ...  ...      ' 
				   '  '  '.....`  '  '  `.....'
			   	   '  '...........'  '................
                                   '			             ````.
				   .. ...........................    ....' 
				                                 '  '
								 '  '
			                                     .....  .....
				   			     .	        .
				                             .	        .
				                             .	        .
				                             .	        .
                                                             ............
    """)

def d3():
    print("""
    				..........
				.	 .
				.	 .
				.   	 .
				.	 .
				 ...  ...
		           ....... '  ' .......
			   '  	 ..'  '..  X  '
			    '.....`'  '`.....' 
				   '  '
		           ....... '  ' .......
			   '	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '		  ....
				   '  '	  ........'  '........	
				   '  '  '      ...  ...      ' 
				   '  '  '.....`  '  '  `.....'
			   	   '  '...........'  '................
                                   '			             ````.
				   .. ...........................    ....' 
				                                 '  '
								 '  '
			                                     .....  .....
				   			     .	        .
				                             .	        .
				                             .	        .
				                             .	        .
                                                             ............
    """)

def d4():
    print("""
    				..........
				.	 .
				.	 .
				.   	 .
				.	 .
				 ...  ...
		           ....... '  ' .......
			   '  	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '
		           ....... '  ' .......
			   '  X	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '		  ....
				   '  '	  ........'  '........	
				   '  '  '      ...  ...      ' 
				   '  '  '.....`  '  '  `.....'
			   	   '  '...........'  '................
                                   '			             ````.
				   .. ...........................    ....' 
				                                 '  '
								 '  '
			                                     .....  .....
				   			     .	        .
				                             .	        .
				                             .	        .
				                             .	        .
                                                             ............
    """)

def d5():
    print("""
    				..........
				.	 .
				.	 .
				.   	 .
				.	 .
				 ...  ...
		           ....... '  ' .......
			   '  	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '
		           ....... '  ' .......
			   '  	 ..'  '..  X  '
			    '.....`'  '`.....' 
				   '  '		  ....
				   '  '	  ........'  '........	
				   '  '  '      ...  ...      ' 
				   '  '  '.....`  '  '  `.....'
			   	   '  '...........'  '................
                                   '			             ````.
				   .. ...........................    ....' 
				                                 '  '
								 '  '
			                                     .....  .....
				   			     .	        .
				                             .	        .
				                             .	        .
				                             .	        .
                                                             ............
    """)

def d6():
    print("""
    				..........
				.	 .
				.	 .
				.   	 .
				.	 .
				 ...  ...
		           ....... '  ' .......
			   '  	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '
		           ....... '  ' .......
			   '  	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '		  ....
				   '  '	  ........'  '........	
				   '  '  '  X    ...  ...     ' 
				   '  '  '.....`  '  '  `.....'
			   	   '  '...........'  '................
                                   '			             ````.
				   .. ...........................    ....' 
				                                 '  '
								 '  '
			                                     .....  .....
				   			     .	        .
				                             .	        .
				                             .	        .
				                             .	        .
                                                             ............
    """)

def d7():
    print("""
    				..........
				.	 .
				.	 .
				.   	 .
				.	 .
				 ...  ...
		           ....... '  ' .......
			   '  	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '
		           ....... '  ' .......
			   '  	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '		  ....
				   '  '	  ........'  '........	
				   '  '  '      ...  ...   X  ' 
				   '  '  '.....`  '  '  `.....'
			   	   '  '...........'  '................
                                   '			             ````.
				   .. ...........................    ....' 
				                                 '  '
								 '  '
			                                     .....  .....
				   			     .	        .
				                             .	        .
				                             .	        .
				                             .	        .
                                                             ............
    """)

def d8():
    print("""
    				..........
				.	 .
				.	 .
				.   	 .
				.	 .
				 ...  ...
		           ....... '  ' .......
			   '  	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '
		           ....... '  ' .......
			   '  	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '		  ....
				   '  '	  ........'  '........	
				   '  '  '      ...  ...      ' 
				   '  '  '.....`  '  '  `.....'
			   	   '  '...........'  '................ 
                                   '			             ``X``.
				   .. ...........................    ....' 
				                                 '  '
								 '  '
			                                     .....  .....
				   			     .	        .
				                             .	        .
				                             .	        .
				                             .	        .
                                                             ............
    """)

def d9():
    print("""
    
				..........
				.	 .
				.	 .
				.   	 .
				.	 .
				 ...  ...
		           ....... '  ' .......
			   '  	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '
		           ....... '  ' .......
			   '  	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '		  ....
				   '  '	  ........'  '........	
				   '  '  '      ...  ...      ' 
				   '  '  '.....`  '  '  `.....'
			   	   '  '...........'  '................ 
                                   '			             ````.
				   .. ...........................    ....' 
				                                 '  '
								 '  '
			                                     .....  .....
				   			     .	        .
				                             .	        .
				                             .	   X    .
				                             .	        .
                                                             ............
    """)

def ch4():
    print("""
    				..........
				.	 .
				.	 .
				.   	 .
				.	 .
				 ...  ...
		           ....... '  ' .......
			   '  	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '
		           ....... '  ' .......
			   '  	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '		  ....
				   '  '	  ........'  '........	
				   '  '  '      ...  ...      ' 
				   '  '  '.....`  '  '  `.....'
			   	   '  '...........'  '................ 
                                   'X		   	             ````.
				   .. ...........................    ....' 
				                                 '  '
								 '  '
			                                     .....  .....
				   			     .	        .
				                             .	        .
				                             .	        .
				                             .	        .
                                                             ............
    """)

def ch1():


    print("""
    				..........
				.	 .
				.	 .
				.   	 .
				.	 .
				 ...  ...
		           ....... 'X ' .......
			   '  	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '
		           ....... '  ' .......
			   '  	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '		  ....
				   '  '	  ........'  '........	
				   '  '  '      ...  ...      ' 
				   '  '  '.....`  '  '  `.....'
			   	   '  '...........'  '................ 
                                   '			             ````.
				   .. ...........................    ....' 
				                                 '  '
								 '  '
			                                     .....  .....
				   			     .	        .
				                             .	        .
				                             .	        .
				                             .	        .
                                                             ............
    """)

def ch2():
    print("""
    				..........
				.	 .
				.	 .
				.   	 .
				.	 .
				 ...  ...
		           ....... '  ' .......
			   '  	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '
		           ....... '  ' .......
			   '  	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '		  ....
				   '  '	  ........'  '........	
				   '  '  '      ...  ...      ' 
				   '  '  '.....`  '  '  `.....'
			   	   '  '...........'  '................ 
                                   'X			             ````.
				   .. ...........................    ....' 
				                                 '  '
								 '  '
			                                     .....  .....
				   			     .	        .
				                             .	        .
				                             .	        .
				                             .	        .
                                                             ............
    """)

def ch3():
    print("""
    
				..........
				.	 .
				.	 .
				.   	 .
				.	 .
				 ...  ...
		           ....... '  ' .......
			   '  	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '
		           ....... '  ' .......
			   '  	 ..'  '..     '
			    '.....`'  '`.....' 
				   '  '		  ....
				   '  '	  ........'  '........	
				   '  '  '      ...  ...      ' 
				   '  '  '.....`  '  '  `.....'
			   	   '  '...........'  '................ 
                                   '		   X	             ````.
				   .. ...........................    ....' 
				                                 '  '
								 '  '
			                                     .....  .....
				   			     .	        .
				                             .	        .
				                             .	        .
				                             .	        .
                                                             ............
    """)

def ratanattackanim():
    print("""
          ___
 _  _  .-'   '-.
(.)(.)/         \   
 /XX             ;
o_\\-mm-......-mm`~~~~~~~~~~~~~~~~`
    """)

def prolog():

    #start

    d1()

    print("======================================================================================================================================")
    print("\n"*1)
    print('probudíš se v neznámé místnosti s velkou bolestí hlavy')
    print("1.zvednout se")
    print("2.vzdát to jako pussy")
    print("\n"*1)
    print("======================================================================================================================================")
    print("\n"*1)
    fs1 = input(">>>>")
    clear()
    if fs1 == "1":

        print("======================================================================================================================================")
        print("poté co se zvedneš tak zjistíš že jsi ve vězení nevíš jak jsi se sem dostal ani proč ale víš že chceš utéct")
        print("======================================================================================================================================")

        tm.sleep(1.0)

        clear()

        cell()

    elif fs1 == "2":


        print("======================================================================================================================================")
        print("ležíš na zemi tak dlouho , dokuď tě nesní divocí rataňi")
        print("======================================================================================================================================")

        clear()

    else: 
        print("======================================================================================================================================")
        print("nevybral si validní možnost")
        print("nedělal si nic tak dlouho že ti ukousl prst divoký rataň a vykrvácel si")
        print("======================================================================================================================================")

        clear()

def cell():
    
    print("======================================================================================================================================")
    print("1.prohlédnout svojí celu")
    print("2.vejít do chodby")
    print("======================================================================================================================================")

    fs2 = input(">>>>")
    clear()

    if fs2 == "1":

        print("======================================================================================================================================")
        print("zkusil si prohledat svojí celu bohužel si nic nenašel ")
        print("======================================================================================================================================")

        tm.sleep(1.0)

        clear()

    elif fs2 == "2":
        
        print("======================================================================================================================================")
        print("vešel jsi do haly a vidíš zde 4 dveře")
        print("======================================================================================================================================")

        tm.sleep(1.0)

        clear()

    print("======================================================================================================================================")
    print("1.prohledat všechny cely")
    print("2.jít přímo do strážnické místnosti")
    print("======================================================================================================================================")

    fs3 = input(">>>>")
    clear()

    if fs3 == "1":

        print("======================================================================================================================================")
        print("vešel jsi do první místnosti")
        print("======================================================================================================================================")

        tm.sleep(1.0)

        clear()

        ye()

    elif fs3 == "2":

        print("======================================================================================================================================")
        print("vešel jsi do strážnické místnosti")
        print("======================================================================================================================================")

        tm.sleep(1.0)

        clear()

        thatskip()
  
def ye():

    d2()

    print("======================================================================================================================================")
    print("1.prohlédni místnost")
    print("2.jdi do další místnosti")
    print("======================================================================================================================================")

    fs4 = input(">>>>")
    clear()

    if fs4 == "1":

        clear()

        print("======================================================================================================================================")
        print("při prohledávání jsi měl neštěstí a dva menší rataňové tě zahnaly do rohu za tebou je nalomená trubka zkusíš si jí vzít ?")
        print("======================================================================================================================================")

        tm.sleep(3.0)

        clear()

        firstfight()

    elif fs4 == "2":

        tm.sleep(1.0)

        clear()

        print("======================================================================================================================================")
        print("vešel jsi do 2. místnosti")
        print("======================================================================================================================================")

        tm.sleep(1.0)


    d3()

    print("======================================================================================================================================")
    print("1.prohlédni místnost")
    print("2.jdi do další místnosti")
    print("======================================================================================================================================")

    fs6 = input(">>>>")
    clear()

    if fs6 == "1":

        print("======================================================================================================================================")
        print("ty máš ale štěstní našel jsi nůž a vězeňský jumpsuit. vezmeš si tyto věci ?")
        print("======================================================================================================================================")

        tm.sleep(1.0)

        clear()

        

        print("======================================================================================================================================")
        print("1.vezmu si obojí")
        print("2.vezmu si pouze nůž")
        print("======================================================================================================================================")

        fs9 = input(">>>>")
        clear()

        if fs9 == "1":

            print("======================================================================================================================================")
            print("nasadil jsi si jumpsuit a vzal sis nůž a šel jsi o místnost dál")
            print("======================================================================================================================================")

            tm.sleep(1.0)

            clear()

        elif fs9 == "2":

            print("======================================================================================================================================")
            print("vzal jsis pouze nůž a šel jsi o místnost dál")
            print("======================================================================================================================================")

            tm.sleep(1.0)

            clear()


    elif fs6 == "2":


        print("======================================================================================================================================")
        print("vešel jsi do 3. místnosti")
        print("======================================================================================================================================")

        clear()

    d4()

    print("======================================================================================================================================")
    print("1.prohlédni místnost")
    print("2.jdi do další místnosti")
    print("======================================================================================================================================")

    fs7 = input(">>>>")
    clear()

    if fs7 == "1":

        print("======================================================================================================================================")
        print("našel jsi jídlo boužel je prošlé, pach toho shnnilého jídla tě vyhnal do další místnosti")
        print("======================================================================================================================================")

        tm.sleep(1.0)

        clear()

        print("======================================================================================================================================")
        print("vešel jsi do strážnické místnosti")
        print("======================================================================================================================================")

        tm.sleep(1.0)

        clear()

        thatskip()


    elif fs7 == "2":

        print("======================================================================================================================================")
        print("vešel jsi do strážnické místnosti")
        print("======================================================================================================================================")

        tm.sleep(1.0)


        clear()

        thatskip()

def thatskip():

    d5()

    print("======================================================================================================================================")
    print("vešel jsi do strážnické místnosti a vidíš tam dva mrtvé strážníky jeden má u sebe klíč co uděláš ?")
    print("======================================================================================================================================")

    tm.sleep(3.0)

    clear()

    print("======================================================================================================================================")
    print("1.zkusím ten klíč získat pomalu můžou se každou chvíli probudit a kousnout mě do prdele")
    print("2.vytrhnu mu ten klíč a jestě si do něj kopnu")
    print("======================================================================================================================================")

    fs4 = input(">>>>")
    clear()

    if fs4 == "1":

        clear()

        print("======================================================================================================================================")
        print("mrtví strážník byl zombie a to samé jeho kolega,nemůžeš útect protože tě drží za ruku")
        print("======================================================================================================================================")

        tm.sleep(2.0)

        clear()

        scnfight()

    elif fs4 == "2":

        print("======================================================================================================================================")
        print("vzal jsi si klíč a prvnímu mrtvému strážci jsi ukopl hlavu, šokován tím že to bylo tak lehké si nevšimneš že ten druhý byl zombie, už je moc pozdě na útěk připrav se bojovat")
        print("======================================================================================================================================")

        tm.sleep(3.0)

        clear()

        scnfight2()

def firstfight():

    print("======================================================================================================================================")
    print("1.vzít si trubku")
    print("2.bojovat holíma rukama")
    print("======================================================================================================================================")

    fs5 = input("")
    clear()

    if fs5 == "1":

        clear()

        print("======================================================================================================================================")
        print("ovedlo se ti urvat trubku bohužel jsi si nevšiml že zeď ze které  trčí je nestabilní a byl jsi zasipán cihlama")
        print("======================================================================================================================================")

        tm.sleep(1.0)

        uluse()

    elif fs5 == "2":

        clear()

        ratanattackanim()

        print("======================================================================================================================================")
        print("poté co jsi zbil rataňe jsi se rozhodl jít do další místnosti")
        print("======================================================================================================================================")

        tm.sleep(3.0)

        clear()

def scnfight():

    tm.sleep(3.0)

    print("======================================================================================================================================")
    print("bojuješ s 2 zombie strážníky, máš šanci 1/3 aby si vyhrál v souboji nebo mužeš utéct")
    print("======================================================================================================================================")

    tm.sleep(1.0)
    clear()

    print("======================================================================================================================================")
    print("1.bojovat 2.utéct")
    print("======================================================================================================================================")

    fs04 = input(">>>>")

    if fs04 == "1":
        if rd.random() < 40:
            clear()
            print("======================================================================================================================================")
            print("poté co jsi porazil dva zombie strážníky,ses ohlédl a viděl jsi zamčené dveře , dveře jsi odemkl a vešel jsi do chodby")
            print("======================================================================================================================================")
            ye2()
            tm.sleep(.0)

            clear()
        else:
            print("======================================================================================================================================")
            print("oba tě čapnou a hodí tě přez dveře do hordy rataňů co tě sežerou za živa")
            print("======================================================================================================================================")
            tm.sleep(3.0)

            clear()
            uluse()
    elif fs04 == "2":

        print("při tom co si utíkal tak si upadl")

        uluse()

def scnfight2():

    tm.sleep(3.0)

    print("======================================================================================================================================")
    print("bojuješ s 1 zombie strážníkem, máš šanci 1/2 aby si vyhrál v souboji nebo mužeš utéct")
    print("======================================================================================================================================")

    tm.sleep(1.0)
    clear()

    print("======================================================================================================================================")
    print("1.bojovat 2.utéct")
    print("======================================================================================================================================")


    fs05 = input(">>>>")

    if fs05 == "1":
        if rd.random() < 50:
            clear()
            print("======================================================================================================================================")
            print("poté co jsi porazil dva zombie strážníky,ses ohlédl a viděl jsi zamčené dveře , dveře jsi odemkl a vešel jsi do chodby")
            print("======================================================================================================================================")
            ye2()
            tm.sleep(1.0)

            clear()
        else:
            print("======================================================================================================================================")
            print("sekl tě nehtem do paty, bolestí si se skulil na zem a zemřel")
            print("======================================================================================================================================")
            tm.sleep(3.0)

            clear()
            uluse()
    elif fs05 == "2":
        
        print("při tom co si utíkal tak si upadl")

        uluse()

sword = False

def ye2():

    ch4()

    print("======================================================================================================================================")
    print("na pravo od sebe vidíš schody ale také jak pokračuje chodba co se rozhodneš udělat ?")
    print("======================================================================================================================================")

    tm.sleep(3.0)

    clear()

    print("======================================================================================================================================")
    print("1.jdi k schodům")
    print("2.jdi dál po chodbě")
    print("======================================================================================================================================")

    fs0 = input(">>>>")
    clear()

    if fs0 == "1":

        clear()

        print("======================================================================================================================================")
        print("došel jsi ke schodům, z ničeho nic se ukázal nápis (dál neprojdeš toto není část dema)")
        print("======================================================================================================================================")

        tm.sleep(3.0)
        clear()

    elif fs0 == "2":

        tm.sleep(1.0)
        clear()

        print("======================================================================================================================================")
        print("jdeš dál a narazil jsi na rozcestí kam se hodláš vydat")
        print("======================================================================================================================================")

        tm.sleep(1.0)

        ch4()

        print("======================================================================================================================================")
        print("1.nahoru")
        print("2.dolu")
        print("3.rovně")
        print("======================================================================================================================================")

        fs00 = input(">>>>")

        if fs00 == "1":
            up()
            tm.sleep(1.0)
            clear()
        elif fs00 == "2":
            down()
            tm.sleep(1.0)
            clear()
        elif fs00 == "3":
            right()
            tm.sleep(1.0)
            clear()

def up():

        d6()

        fs00 = input(">>>>")
        if fs00 == "1":

            clear()

            print("======================================================================================================================================")
            print("vešel jsi do podlouhlé místnosti máš pocit jakoby na tebe někdo zíral půjdeš to prozkoumat nebo ne?(ano - 1)(ne - 2)")
            print("======================================================================================================================================")

            tm.sleep(1.0)
            clear()

        fs01 = input(">>>>")

        if fs01 =="1":

            print("======================================================================================================================================")
            print("vešel jsi do místnosti jak jdeš dál tak je čím dál tím větší tma po chvíli kolem sebe vidíš červené oči. už víš co tě čeká a jsi smýřený s osudem")
            print("======================================================================================================================================")

            tm.sleep(1.0)
            clear()

            uluse()

        elif fs01 == "2":

            print("======================================================================================================================================")
            print("řekl sis že se ti to nevyplátí a radši jsi to otočil a vrátil se na rozcestí")
            print("======================================================================================================================================")

            tm.sleep(1.0)
            clear()

            ye2()

def right():

    print("======================================================================================================================================")
    print("došel jsi ke zdi můžeš si jí prohlédnout ale proč by jsi to dělal ?")
    print("======================================================================================================================================")

    tm.sleep(1.0)
    clear()

    print("======================================================================================================================================")
    print("1.prohlédneš si zeď")
    print("2.odejdeš")
    print("======================================================================================================================================")

    fs03 = input(">>>>")

    if fs03 == "1":

        pp()

        print("======================================================================================================================================")
        print("ale copak byla to falešná zeď! a za ní byl legendární rataň slayer a automaticky jdeš do spodní místnosti kde už víš co tě čeká a s úsměvem jsi připraven na legendární boj")
        print("======================================================================================================================================")

        tm.sleep(1.0)
        clear()

        sword = True

        print("======================================================================================================================================")
        print("po té co vzal meč tak hned si věděl co udělat, běžel si s mečem do místnosti kde byl hluk, vešel si do místnosti a vidíš mighty rataňě")
        print("======================================================================================================================================")

        tm.sleep(5.0)

        print("použil si sílu legendary rataň slayera a usekls každou končetinu rataňovi , tím vítežíš a to je vše pro tohle demo, zbytek hry je za pay wallou 30e")
        print("tvoje postava byla poté zabita hordou hladových rataňů")
        tm.sleep(5.0)
        uluse()

    elif fs03 == "2":

        print("======================================================================================================================================")
        print("vrátíš se nazpátek na rozcestí")
        print("======================================================================================================================================")

        tm.sleep(1.0)
        clear()

        ye2()

def down(s):

    ratan()

    tm.sleep(8.0)

    print("======================================================================================================================================")
    print("vešel jsi do velké místnosti, zavřeli se za tebou dveře, a před tebou je the mighty rataň s nejistotou se připravíš na nejhorší")
    print("======================================================================================================================================")

    tm.sleep(5.0)

    print("mighty rataň tě rožšlápl jako malinu, potřebuješ speciální reliku na poražení mighty rataňe")
    tm.sleep(5.0)
    uluse()

menu()