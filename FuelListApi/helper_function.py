import requests
import json
import pandas as pd


def EVChargingStations(users_key, fuel_type, country, limit, users_status, evChargeType):
    '''
    To return the queried data based on the users input.
    Full docs can be found here: https://developer.nrel.gov/docs/transportation/alt-fuel-stations-v1/all/
    
    Arguments: api_key(str), fuel_type(str), country(str), limit(str)
    
    returns: DataFrame 

    '''
    #   Connection string should contain the required parameters found at docs. 
    #   Optional parameters exist to filter down the data. 
    connection_string = "https://developer.nrel.gov/api/alt-fuel-stations/v1.json?api_key={}&fuel_type={}&country={}&limit={}&status={}&ev_connector_type={}".format(users_key, fuel_type, country,limit, users_status,evChargeType)

    # API DOCS - ,https://developer.nrel.gov/docs/transportation/alt-fuel-stations-v1/all

    #   Call the API. A 200 code is a success. 
    response = requests.get(connection_string)

    #   The response object needs to be Parsed into JSON. 
    raw_data = json.loads(response.content)

    #   Error check (should happen at the .get level)
    if len(raw_data.keys()) == 1:
        print("Error in a parameter")
    else:

    #   Based on the keys available, we want to know about fuel_stations
    #   The [0:] allows us to access all datapoints and not a single selection. 
    #   Read into a DataFrame and return to the user. 
        raw_data =  raw_data["fuel_stations"][:]
        df_data = pd.DataFrame.from_dict(raw_data)
        return df_data

