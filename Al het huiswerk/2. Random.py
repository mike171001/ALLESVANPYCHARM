import random

def monopolyworp():
    dobbel1_1 = random.randrange(1, 7)
    dobbel1_2 = random.randrange(1, 7)
    dobbel2_1 = random.randrange(1, 7)
    dobbel2_2 = random.randrange(1, 7)
    dobbel3_1 = random.randrange(1, 7)
    dobbel3_2 = random.randrange(1, 7)

    if dobbel1_1 == dobbel1_2:
        if dobbel2_1 == dobbel2_2:
            if dobbel3_1 == dobbel3_2:
                print('{} + {} = {} (dubbel)'.format (dobbel1_1, dobbel1_2, (dobbel1_1 + dobbel1_2)))
                print('{} + {} = {} (dubbel)'.format (dobbel2_1, dobbel2_2, (dobbel2_1 + dobbel2_2)))
                print('{} + {} =  (direct naar gevangenis)\n'.format(dobbel3_1, dobbel3_2))
            else:
                print('{} + {} = {} (dubbel)'.format (dobbel1_1, dobbel1_2, (dobbel1_1 + dobbel1_2)))
                print('{} + {} = {} (dubbel)'.format (dobbel2_1, dobbel2_2, (dobbel2_1 + dobbel2_2)))
                print('{} + {} = {}''\n'.format (dobbel3_1, dobbel3_2, (dobbel3_1 + dobbel3_2)))
        else:
            print('{} + {} = {} (dubbel)'.format (dobbel1_1, dobbel1_2, (dobbel1_1 + dobbel1_2)))
            print('{} + {} = {}''\n'.format (dobbel2_1, dobbel2_2, (dobbel2_1 + dobbel2_2)))
    else:
        print('{} + {} = {}''\n'.format(dobbel1_1, dobbel1_2, (dobbel1_1 + dobbel1_2)))

monopolyworp()