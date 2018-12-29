from tkinter import *
from sys import exit

root = Tk()
root.title("BorkaConvert 0.1")


topframe = Frame(root)
topframe.pack(side=TOP)
middleframe = Frame(root)
middleframe.pack()
lowerframe = Frame(root)
lowerframe.pack(side=BOTTOM)


def stop():
    root.destroy()
    exit()



def retrive():
    inputverdi = inn1.get()
    enhetinput = inn2.get()
    enhetoutput = inn3.get()

    ########## tempratur ##########
    if enhetinput.lower() == "celsius" or enhetinput.lower() == "c" :
        enhetinputtype = 1
        konverteringstype = 1
        fancy = "Celsius °C"

    if enhetinput.lower() == "kelvin" or enhetinput.lower() == "k" :
        enhetinputtype = 2
        konverteringstype = 1
        fancy = "K (Kelvin)"

    if enhetinput.lower() == "fahrenheit" or enhetinput.lower() == "f" :
        enhetinputtype = 3
        konverteringstype = 1
        fancy = "Fahrenheit °F"

    if enhetoutput.lower() == "celsius" or enhetoutput.lower() == "c":
        enhetoutputtype = 1
        konverteringstypeout = 1
        fancyout = "Celsius °C"

    if enhetoutput.lower() == "kelvin" or enhetoutput.lower() == "k":
        enhetoutputtype = 2
        konverteringstypeout = 1
        fancyout = "K (Kelvin)"

    if enhetoutput.lower() == "fahrenheit" or enhetoutput.lower() == "f":
        enhetoutputtype = 3
        konverteringstypeout = 1
        fancyout = "Fahrenheit °F"

    ##konverteringstype mulig eller ikke
    if konverteringstype == konverteringstypeout and str(konverteringstype) == 1 :
        konversjon = "tempratur"


    ##konversjon
    if str(enhetinputtype) == "1":
        if str(enhetoutputtype) == "2":
            outputverdi = float(inputverdi) + 273.15
        if str(enhetoutputtype) == "3":
            outputverdi = (((float(inputverdi))*(9/5))+32)

    if str(enhetinputtype) == "2":
        if str(enhetoutputtype) == "1":
            outputverdi = float(inputverdi) - 273.15
        if str(enhetoutputtype) == "3":
            outputverdi = (((float(inputverdi))*(9/5))-459.67)

    if str(enhetinputtype) == "3":
        if str(enhetoutputtype) == "1":
            outputverdi = (float(inputverdi) - 32)*(5/9)
        if str(enhetoutputtype) == "2":
            outputverdi = ((float(inputverdi)+459.67)*(9/5))

    printfuver = (inputverdi + " " + fancy + " er "  + "%.2f" % float(outputverdi) + " " + fancyout)

    printfu = Label(lowerframe, text=printfuver)
    printfu.pack()


intro = Label(middleframe, text= "Jeg ønsker å konverte:")
intro.pack(side=LEFT)

inn1 = Entry(middleframe)
inn1.pack(side=LEFT)

inn2 = Entry(middleframe)
inn2.pack(side=LEFT)

intro2 = Label(middleframe, text= " til ")
intro2.pack(side=LEFT)

inn3 = Entry(middleframe)
inn3.pack(side=LEFT)

buttonenter = Button(lowerframe, text="kalkuler", fg="red", command=retrive)
buttonenter.pack(side=BOTTOM)

button1 = Button(topframe, text="exit", fg="red", command=stop)
button1.pack(side=LEFT)

navn = Label(topframe, text="Enhets konverterer")
navn.pack(side=LEFT)


root.mainloop()
