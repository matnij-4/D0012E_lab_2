# -*- coding: utf-8 -*-

import hashing
import key
import random
import time

""" Nedan är funktionerna som skriver mätdata till LaTEX grafer
"""


def test(v2_starttable, tablelength, keyrand, datarand, valueC, number_of_keys, rehashMultiplyer, number_of_tests):
    timeList = []
    loadList = []
    probesList = []
    chainList = []
    collList = []

    print("1")
    start = time.time()
    for number in range(number_of_tests):
        hashingFunction1 = hashing.hashing(v2_starttable)
        hashingFunction1.valueC = valueC
        hashingFunction1.rehashMultiplyer = rehashMultiplyer
        for ind in range(number_of_keys):
            keyObj = key.key(random.randint(1, keyrand), random.randint(1, datarand))
            hashingFunction1.setNumProbes(hashing.rehashProbing(keyObj, False))
    timeList.append(((time.time() - start) / number_of_tests))
    loadList.append(hashingFunction1.getLoadFactor())
    probesList.append(hashingFunction1.getNumProbes())
    chainList.append(hashingFunction1.getCollosionChain())
    collList.append(hashingFunction1.getCollisionCounter())


    print("2")
    start = time.time()
    for number in range(number_of_tests):
        hashingFunction2 = hashing.hashing(tablelength)
        for ind in range(number_of_keys):
            keyObj = key.key(random.randint(1, keyrand), random.randint(1, datarand))
            hashingFunction2.setNumProbes(hashingFunction2.closestProbing(keyObj))
    timeList.append(((time.time() - start) / number_of_tests))
    loadList.append(hashingFunction2.getLoadFactor())
    probesList.append(hashingFunction2.getNumProbes())
    chainList.append(hashingFunction2.getCollosionChain())
    collList.append(hashingFunction2.getCollisionCounter())

    print("3")
    start = time.time()
    for number in range(number_of_tests):
        hashingFunction3 = hashing.hashing(tablelength)
        for ind in range(number_of_keys):
            keyObj = key.key(random.randint(1, keyrand), random.randint(1, datarand))
            hashingFunction3.setNumProbes(hashingFunction3.defaultProbing(keyObj))
    timeList.append(((time.time() - start) / number_of_tests))
    loadList.append(hashingFunction3.getLoadFactor())
    probesList.append(hashingFunction3.getNumProbes())
    chainList.append(hashingFunction3.getCollosionChain())
    collList.append(hashingFunction3.getCollisionCounter())

    return [timeList, loadList, probesList, chainList, collList]


def LatexGraphTest(v2_starttable, tablelength, keyrand, datarand, valueC, number_of_keys, rehashMultiplyer,
                   number_of_tests):
    return_file_1 = open("V1_time.tex", "w")
    return_file_1.write("    \\addplot[color=blue]\n    coordinates {\n")
    return_file_2 = open("V2_time.tex", "w")
    return_file_2.write("    \\addplot[color=red]\n    coordinates {\n")
    return_file_3 = open("V3_time.tex", "w")
    return_file_3.write("    \\addplot[color=green]\n    coordinates {\n")

    return_file_4 = open("V1_load.tex", "w")
    return_file_4.write("    \\addplot[color=blue]\n    coordinates {\n")
    return_file_5 = open("V2_load.tex", "w")
    return_file_5.write("    \\addplot[color=red]\n    coordinates {\n")
    return_file_6 = open("V3_load.tex", "w")
    return_file_6.write("    \\addplot[color=green]\n    coordinates {\n")

    return_file_7 = open("V1_probes.tex", "w")
    return_file_7.write("    \\addplot[color=blue]\n    coordinates {\n")
    return_file_8 = open("V2_probes.tex", "w")
    return_file_8.write("    \\addplot[color=red]\n    coordinates {\n")
    return_file_9 = open("V3_probes.tex", "w")
    return_file_9.write("    \\addplot[color=green]\n    coordinates {\n")

    return_file_10 = open("V1_chain.tex", "w")
    return_file_10.write("    \\addplot[color=blue]\n    coordinates {\n")
    return_file_11 = open("V2_chain.tex", "w")
    return_file_11.write("    \\addplot[color=red]\n    coordinates {\n")
    return_file_12 = open("V3_chain.tex", "w")
    return_file_12.write("    \\addplot[color=green]\n    coordinates {\n")

    return_file_13 = open("V1_collisions.tex", "w")
    return_file_13.write("    \\addplot[color=blue]\n    coordinates {\n")
    return_file_14 = open("V2_collisions.tex", "w")
    return_file_14.write("    \\addplot[color=red]\n    coordinates {\n")
    return_file_15 = open("V3_collisions.tex", "w")
    return_file_15.write("    \\addplot[color=green]\n    coordinates {\n")

    for ind in range(1, 101):
        lst = test(v2_starttable, tablelength, keyrand, datarand, valueC, number_of_keys * ind, rehashMultiplyer,
                   number_of_tests)

        return_file_1.write("        (" + str(number_of_keys * ind) + ", " + str(lst[0][0]) + ")\n")
        return_file_2.write("        (" + str(number_of_keys * ind) + ", " + str(lst[0][1]) + ")\n")
        return_file_3.write("        (" + str(number_of_keys * ind) + ", " + str(lst[0][2]) + ")\n")

        return_file_4.write("        (" + str(number_of_keys * ind) + ", " + str(lst[1][0]) + ")\n")
        return_file_5.write("        (" + str(number_of_keys * ind) + ", " + str(lst[1][1]) + ")\n")
        return_file_6.write("        (" + str(number_of_keys * ind) + ", " + str(lst[1][2]) + ")\n")

        return_file_7.write("        (" + str(number_of_keys * ind) + ", " + str(lst[2][0]) + ")\n")
        return_file_8.write("        (" + str(number_of_keys * ind) + ", " + str(lst[2][1]) + ")\n")
        return_file_9.write("        (" + str(number_of_keys * ind) + ", " + str(lst[2][2]) + ")\n")

        return_file_10.write("        (" + str(number_of_keys * ind) + ", " + str(lst[3][0]) + ")\n")
        return_file_11.write("        (" + str(number_of_keys * ind) + ", " + str(lst[3][1]) + ")\n")
        return_file_12.write("        (" + str(number_of_keys * ind) + ", " + str(lst[3][2]) + ")\n")

        return_file_13.write("        (" + str(number_of_keys * ind) + ", " + str(lst[4][0]) + ")\n")
        return_file_14.write("        (" + str(number_of_keys * ind) + ", " + str(lst[4][1]) + ")\n")
        return_file_15.write("        (" + str(number_of_keys * ind) + ", " + str(lst[4][2]) + ")\n")

        print(ind)

    return_file_1.write("    };\n\t\\addlegendentry{Version 1}\n")
    return_file_1.close()
    return_file_2.write("    };\n\t\\addlegendentry{Version 2}\n")
    return_file_2.close()
    return_file_3.write("    };\n\t\\addlegendentry{Version 3}\n")
    return_file_3.close()

    return_file_4.write("    };\n\t\\addlegendentry{Version 1}\n")
    return_file_4.close()
    return_file_5.write("    };\n\t\\addlegendentry{Version 2}\n")
    return_file_5.close()
    return_file_6.write("    };\n\t\\addlegendentry{Version 3}\n")
    return_file_6.close()

    return_file_7.write("    };\n\t\\addlegendentry{Version 1}\n")
    return_file_7.close()
    return_file_8.write("    };\n\t\\addlegendentry{Version 2}\n")
    return_file_8.close()
    return_file_9.write("    };\n\t\\addlegendentry{Version 3}\n")
    return_file_9.close()

    return_file_10.write("    };\n\t\\addlegendentry{Version 1}\n")
    return_file_10.close()
    return_file_11.write("    };\n\t\\addlegendentry{Version 2}\n")
    return_file_11.close()
    return_file_12.write("    };\n\t\\addlegendentry{Version 3}\n")
    return_file_12.close()

    return_file_13.write("    };\n\t\\addlegendentry{Version 1}\n")
    return_file_13.close()
    return_file_14.write("    };\n\t\\addlegendentry{Version 2}\n")
    return_file_14.close()
    return_file_15.write("    };\n\t\\addlegendentry{Version 3}\n")
    return_file_15.close()


def LatexGraphTest2(v2_starttable, tablelength, keyrand, datarand, valueC, number_of_keys, rehashMultiplyer,
                    number_of_tests):
    return_file_v1 = open("Version1constTablelength.tex", "w")
    return_file_v1.write("    \\addplot[color=blue]\n    coordinates {\n")
    return_file_v2 = open("Version2constTablelength.tex", "w")
    return_file_v2.write("    \\addplot[color=red]\n    coordinates {\n")
    return_file_v3 = open("Version3constTablelength.tex", "w")
    return_file_v3.write("    \\addplot[color=green]\n    coordinates {\n")

    for ind in range(1, 100):
        timeList = test(v2_starttable, tablelength, keyrand, datarand, valueC, number_of_keys * ind, rehashMultiplyer,
                        number_of_tests)[0]
        return_file_v1.write("        (" + str(timeList[0]) + ", " + str(number_of_keys) + ")\n")
        return_file_v2.write("        (" + str(timeList[1]) + ", " + str(number_of_keys) + ")\n")
        return_file_v3.write("        (" + str(timeList[2]) + ", " + str(number_of_keys) + ")\n")
        print(ind)

    return_file_v1.write("    };\n\t\\addlegendentry{Version 1}\n")
    return_file_v1.close()
    return_file_v2.write("    };\n\t\\addlegendentry{Version 2}\n")
    return_file_v2.close()
    return_file_v3.write("    };\n\t\\addlegendentry{Version 3}\n")
    return_file_v3.close()
