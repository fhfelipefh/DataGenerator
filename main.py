#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


def randomItems():
    controller = 0
    qtdItems = randint(1, 6)
    strItens = "["
    while (controller < qtdItems):
        itemID = str(randint(0, 999))
        quantity = str(randint(0, 999))
        price = str(randint(0, 999))
        controller = controller + 1
        strItens += itemID + "-" + quantity + "-" + price + ","
    strItens = strItens[:-1]
    strItens += "]"
    return strItens


def randomDataName():
    randomFilename = str(randint(0, 9999))
    return randomFilename


def generateSalesman(qtdSalesman):
    global rDataName
    rDataName = randomDataName()
    fileQ = open('data'+rDataName+'.dat', mode="a+", encoding="utf-8")
    controller = 0
    identifier = "001"
    text = list()

    while (controller < qtdSalesman):
        cpf = str(randint(1000000000000, 9999999999999))
        nome = "Felipe"+str(randint(0, 999))
        salario = str(randint(1000, 200000))
        controller = controller + 1
        text.append(identifier+"ç"+cpf+"ç"+nome+"ç"+salario+"\n")
        fileQ.writelines(text)
        text.clear()

    fileQ.close()


def generateCustomers(qtdCustumers):
    fileQ = open('data'+rDataName+'.dat', mode="a+", encoding="utf-8")
    controller = 0
    identifier = "002"
    text = list()

    while (controller < qtdCustumers):
        cnpj = str(randint(1000000000000, 9999999999999))
        nome = "Felipe"+str(randint(0, 999))
        bussinesArea = str(randint(1000, 200000))
        controller = controller + 1
        text.append(identifier+"ç"+cnpj+"ç"+nome+"ç"+bussinesArea+"\n")

    fileQ.writelines(text)
    fileQ.close()


def generateSales(qtdSales):
    fileQ = open('data'+rDataName+'.dat', mode="a+", encoding="utf-8")
    controller = 0
    identifier = "003"
    text = list()

    while (controller < qtdSales):
        saleID = str(randint(10, 99))
        itemID = str(randint(0, 999))
        quantity = str(randint(0, 999))
        price = str(randint(0, 999))
        name = "name"+str(randint(0, 999))
        bussinesArea = str(randint(1000, 200000))
        controller = controller + 1
        text.append(identifier+"ç"+saleID+"ç"+randomItems()+"ç"+name+"\n")

    fileQ.writelines(text)
    fileQ.close()


def main():

    qtdOfFiles = int(input("Quantity of files: "))
    controller = 0
    while (controller < qtdOfFiles):
        qtdSalesman = int(input("Quantity of Salesman: "))
        qtdCostumers = int(input("Quantity of costumers: "))
        qtdSales = int(input("Quantity of Sales: "))
        generateSalesman(qtdSalesman)
        generateCustomers(qtdCostumers)
        generateSales(qtdSales)
        controller = controller + 1


main()