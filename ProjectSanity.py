#!/usr/bin/env python3
from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint
import re
import csv


try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:

        csv_result = []

#----------------------------UNSTREAMED SFX----------------------------------------------------
        def checkStreamedFiles():

            print("File > maxDurationUnstreamed and unstreamed:", "\n")

            #formatting rows in CSV - first line doesn't get a previous blank space to avoid line one being empty
            csv_result.append(["FILE > MAXDURATIONUNSTREAMED AND UNSTREAMED:"])
            csv_result.append([" "])

            #Core Query
            object_get_args = {
                "from": {
                    "ofType": ["Sound"]
                },
                "options": {
                    "return": ["name", "@IsStreamingEnabled", "audioSource:maxDurationSource"]
                }
            }
            result = client.call("ak.wwise.core.object.get", object_get_args)
            #Data managing and checking

            maxDurationUnstreamed = 8
            

            #remove 1 level of dictionary for simpler syntax
            result = (result['return'])
            
            #loop every file unstreamed with duration > maxDurationUnstreamed
            iterator = 0
            
            for i in (result):
            
                if(result[iterator]["audioSource:maxDurationSource"]["trimmedDuration"]) > maxDurationUnstreamed and result[iterator]["@IsStreamingEnabled"] == False : 
                    print(result[iterator]["name"], "is unstreamed but has a length of", "%.2f" % (result[iterator]["audioSource:maxDurationSource"]["trimmedDuration"]), "seconds (max accepted value : %s seconds)" % maxDurationUnstreamed )
                    csv_result.append([result[iterator]["name"], "is unstreamed but has a length of", "%.2f" % (result[iterator]["audioSource:maxDurationSource"]["trimmedDuration"]), "seconds (max accepted value : %s seconds)" % maxDurationUnstreamed])
                   
                       
    
                iterator+=1
            print("\n")

#----------------------------UNSTREAMED MUSIC----------------------------------------------------
        def checkStreamedFilesMusic():

            print("Music File > maxDurationUnstreamed and unstreamed:", "\n")

            #formatting rows in CSV - first line doesn't get a previous blank space to avoid line one being empty
            csv_result.append([" "])
            csv_result.append(["MUSIC FILE > MAXDURATIONUNSTREAMED AND UNSTREAMED:"])
            csv_result.append([" "])

            #Core Query
            object_get_args = {
                "from": {
                    "ofType": ["MusicTrack"]
                },
                "options": {
                    "return": ["name", "@IsStreamingEnabled", "audioSource:maxDurationSource"]
                }
            }
            result = client.call("ak.wwise.core.object.get", object_get_args)
            #Data managing and checking

            maxDurationUnstreamed = 8
            

            #remove 1 level of dictionary for simpler syntax
            result = (result['return'])
            
            #loop every file unstreamed with duration > maxDurationUnstreamed
            iterator = 0
            
            for i in (result):
            
                if(result[iterator]["audioSource:maxDurationSource"]["trimmedDuration"]) > maxDurationUnstreamed and result[iterator]["@IsStreamingEnabled"] == False : 
                    print(result[iterator]["name"], "is unstreamed but has a length of", "%.2f" % (result[iterator]["audioSource:maxDurationSource"]["trimmedDuration"]), "seconds (max accepted value : %s seconds)" % maxDurationUnstreamed )
                    csv_result.append([result[iterator]["name"],"is unstreamed but has a length of", "%.2f" % (result[iterator]["audioSource:maxDurationSource"]["trimmedDuration"]), "seconds (max accepted value : %s seconds)" % maxDurationUnstreamed])
                   
                       
    
                iterator+=1
            print("\n")

#----------------------------VIRTUAL VOICE BEHAVIOR FOR ONE SHOT SOUND------------------------
        def weirdVirtualVoiceBehaviour():
            print("One shot sounds with VVB not KILL:", "\n")

            #formatting rows in CSV
            csv_result.append([" "])
            csv_result.append(["ONE SHOT SOUNDS WITH VVB NOT KILL:"])
            csv_result.append([" "])

            #Core Query
            object_get_args = {
                "from": {
                    "ofType": ["Sound"]
                },
                "options": {
                    "return": ["name", "@BelowThresholdBehavior", "@IsLoopingEnabled", ]
                }
            }
            result = client.call("ak.wwise.core.object.get", object_get_args)
            #Data managing and checking

            #remove 1 level of dictionary for simpler syntax
            result = (result['return'])
            #loop every  one shot file with virtual voice behaviour not kill
            iterator = 0
            
            for i in (result):
            
                if(result[iterator]["@BelowThresholdBehavior"]) != 1 and result[iterator]["@IsLoopingEnabled"] == False :
                    if(result[iterator]["@BelowThresholdBehavior"]) == 0:
                        VVB = "Continue to play"
                    elif (result[iterator]["@BelowThresholdBehavior"]) == 2:
                        VVB = "Send to virtual voice"
                    elif (result[iterator]["@BelowThresholdBehavior"]) == 3:
                        VVB = "Kill if finite else virtual"
                    print(result[iterator]["name"], "is one shot but has a VVB set as", VVB )
                    csv_result.append([result[iterator]["name"],"is one shot but has a VVB set as",VVB])
                   
            
                iterator+=1
            print("\n")

#----------------------------POSITIVE VOICE VOLUME--------------------------------------------
        def positiveVoiceVolume():

            print("Positive voice volume:", "\n")
            
            #formatting rows in CSV
            csv_result.append([" "])
            csv_result.append(["POSITIVE VOICE VOLUME:"])
            csv_result.append([" "])
            #Core Query
            object_get_args = {
                "from": {
                    "ofType": ["Sound"]
                },
                "options": {
                    "return": ["name", "@Volume"]
                }
            }
            result = client.call("ak.wwise.core.object.get", object_get_args)
            #Data managing and checking

            maxPositiveVoiceVolume = 3

            #remove 1 level of dictionary for simpler syntax
            result = (result['return'])
            
            #loop every file unstreamed with voice volume > maxPositiveVoiceVolume
            iterator = 0
            for i in (result):
            
                if(result[iterator]["@Volume"]) > maxPositiveVoiceVolume:
                    print(result[iterator]["name"], "has a voice volume of", result[iterator]["@Volume"], "please set it as make up gain instead")
                    csv_result.append([result[iterator]["name"], "has a voice volume of",result[iterator]["@Volume"],"please set it as make up gain instead"])
                    
            
                iterator+=1
            print("\n")

#----------------------------UNREFERENCED FILES SFX-----------------------------------------------
        def unreferencedFiles():

            print("Unreferenced files:", "\n")
            
            #formatting rows in CSV
            csv_result.append([" "])
            csv_result.append(["UNREFERENCED FILES:"])
            csv_result.append([" "])
            #Core Query
            object_get_args = {
                "from": {
                    "ofType": ["Sound"]
                },
                "options": {
                    "return": ["name", "@Inclusion"]
                }

            }
            result = client.call("ak.wwise.core.object.get", object_get_args)
            #Data managing and checking


            #remove 1 level of dictionary for simpler syntax
            result = (result['return'])
            
            #loop every file Inclusion
            iterator = 0
            for i in (result):
                if(result[iterator]["@Inclusion"]) == False:
                        print(result[iterator]["name"], "is not included in the project")
                        csv_result.append([result[iterator]["name"], "is not included in the project"])
                    
            
                iterator+=1
            print("\n")

#----------------------------UNREFERENCED FILES MUSIC-----------------------------------------------
        def unreferencedFilesMusic():

            print("Music Unreferenced files:", "\n")
            
            #formatting rows in CSV
            csv_result.append([" "])
            csv_result.append(["MUSIC UNREFERENCED FILES:"])
            csv_result.append([" "])
            #Core Query
            object_get_args = {
                "from": {
                    "ofType": ["MusicTrack"]
                },
                "options": {
                    "return": ["name", "@Inclusion"]
                }

            }
            result = client.call("ak.wwise.core.object.get", object_get_args)
            #Data managing and checking


            #remove 1 level of dictionary for simpler syntax
            result = (result['return'])
            
            #loop every file Inclusion
            iterator = 0
            for i in (result):
                if(result[iterator]["@Inclusion"]) == False:
                        print(result[iterator]["name"], "is not included in the project")
                        csv_result.append([result[iterator]["name"], "is not included in the project"])
                    
            
                iterator+=1
            print("\n")

#----------------------------MASTER AUDIO BUS ROUTED SFX-----------------------------------------------
        def masterAudioBusRouted():

            print("Master audio bus routed sounds:", "\n")
            
            #formatting rows in CSV
            csv_result.append([" "])
            csv_result.append(["MASTER AUDIO BUS ROUTED SOUND:"])
            csv_result.append([" "])
            #Core Query
            object_get_args = {
                "from": {
                    "ofType": ["Sound"]
                },
                "options": {
                    "return": ["name", "@OutputBus"]
                }
            }
            result = client.call("ak.wwise.core.object.get", object_get_args)
            #Data managing and checking

            

            #remove 1 level of dictionary for simpler syntax
            result = (result['return'])
            
            #loop every file outpus bus being master audio bus
            iterator = 0
            for i in (result):
            
                if(result[iterator]["@OutputBus"]["name"]) == "Master Audio Bus" :
                    print(result[iterator]["name"], "is routed to the master audio bus")
                    csv_result.append([result[iterator]["name"], "is routed to the master audio bus"])
                    
            
                iterator+=1
            print("\n")

#----------------------------MASTER AUDIO BUS ROUTED MUSIC-----------------------------------------------
        def masterAudioBusRoutedMusic():

            print("Master audio bus routed music:", "\n")
            
            #formatting rows in CSV
            csv_result.append([" "])
            csv_result.append(["MASTER AUDIO BUS ROUTED MUSIC:"])
            csv_result.append([" "])
            #Core Query
            object_get_args = {
                "from": {
                    "ofType": ["MusicTrack"]
                },
                "options": {
                    "return": ["name", "@OutputBus"]
                }
            }
            result = client.call("ak.wwise.core.object.get", object_get_args)
            #Data managing and checking

            #remove 1 level of dictionary for simpler syntax
            result = (result['return'])
            
            #loop every file outpus bus being master audio bus
            iterator = 0
            for i in (result):
            
                if(result[iterator]["@OutputBus"]["name"]) == "Master Audio Bus" :
                    print(result[iterator]["name"], "is routed to the master audio bus")
                    csv_result.append([result[iterator]["name"], "is routed to the master audio bus"])
                    
            
                iterator+=1
            print("\n")

#----------------------------WRITING INTO CSV FILE--------------------------------------------
        def csvWriting():
            print ("-------------Writing results to CSV------------------")
            with open('QueryResult.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(csv_result)

            
        #Core Function execution 
        checkStreamedFiles()
        checkStreamedFilesMusic()
        weirdVirtualVoiceBehaviour()
        positiveVoiceVolume()
        unreferencedFiles()
        unreferencedFilesMusic()
        masterAudioBusRouted()
        masterAudioBusRoutedMusic()
        csvWriting()



#error if can't connect to waapi
except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")