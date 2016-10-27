
from __future__ import print_function

import sys
import emoji
emojiList = [
            ":grinning_face:",
            ":grimacing_face:",
            ":grinning_face_with_smiling_eyes:",
            ":face_with_tears_of_joy:",
            ":smiling_face_with_open_mouth:",
            ":smiling_face_with_open_mouth_and_smiling_eyes:",
            ":smiling_face_with_open_mouth_and_cold_sweat:",
            ":smiling_face_with_halo:",
            ":winking_face:",
            ":smiling_face_with_smiling_eyes:",
            ":slightly_smiling_face:",
            ":relaxed:",
            ":face_savouring_delicious_food:",
            ":relieved_face:",
            ":heart_eyes:",
            ":kissing_heart:"
            ]
def convert():
    inString = sys.argv[1]
    hexVals = [ord(inString[i:i+1]) for i in range(0,len(inString),1)]
    indivHexVals = [[i / 16,i % 16] for i in hexVals]
    
    tempList = [i for sublist in indivHexVals for i in sublist]
    finalList = [emoji.emojize(emojiList[i],use_aliases = True) for i in tempList]
    for i in finalList:
        print (i,end="")
    #print(":smiling_with_open_mouth_&_smiling_eyes:")





convert()


