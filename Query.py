#!/usr/bin/env python3
from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint
import re

try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:
        # NOTE: client will automatically disconnect at the end of the scope
        
        # == Simple RPC without argument
     
       
        # == RPC with arguments
        print("Query the Streming info:")
        
        object_get_args = {
            "from": {
                "ofType": ["Sound"]
            },
            "options": {
                "return": ["name", "@IsStreamingEnabled", "audioSource:maxDurationSource"]
            }
        }
        result = client.call("ak.wwise.core.object.get", object_get_args)
     
        #remove 1 level of dictionnary
        result = result["return"]
        for i in result:
            test = i.values()
            if False in test :
                print(test)
                

        #pprint(result)

            
               


        
except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")