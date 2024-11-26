def find_data_field_id(fieldName: str, dataFieldsList: list[dict]):
    for field in dataFieldsList:
        if field["datacellar:fieldName"] == fieldName:
            return field["datacellar:datasetFieldID"]

def find_timeseries(fieldId: int, timeSeriesList: list[dict]):
    for timeSeries in timeSeriesList:
        if timeSeries["datacellar:datasetFieldID"] == fieldId:
            return timeSeries

def extract_data_points(timeSeries: list[dict]):
    return timeSeries["datacellar:dataPoints"]

def extract_values_and_timestamps(datapoints: list[dict]):
    values, timestamps = [], []
    for datapoint in datapoints:
        values.append(datapoint["datacellar:value"])
        timestamps.append(datapoint["datacellar:timeStamp"])
    return {"values": values, "timestamps": timestamps}

def parse_datapoints(fieldName:str, data: dict) -> dict:
    """
    Extracts the values and timestamps for a specific field name from a JSON datacellar dataset.

    Parameters:
    ----------
    fieldName : str
        The name of the field to search for in the dataset (e.g., "outdoorTemperature").
    data : dict
        The full datacellar dataset loaded from a JSON file. This must follow the expected structure,
        containing keys like 'datacellar:datasetSelfDescription' and 'datacellar:timeSeriesList'.

    Returns:
    -------
    Dict[str, Union[List[float], List[str]]]: A dictionary containing two keys:
            - "values" (List[float]): A list of numerical values for the specified field.
            - "timestamps" (List[str]): A list of corresponding timestamps for the values.
    """
    dataFieldsList = data["datacellar:datasetSelfDescription"]["datacellar:datasetFields"]
    timeSeriesList = data["datacellar:timeSeriesList"]
    fieldId = find_data_field_id(fieldName, dataFieldsList)
    timeSeries = find_timeseries(fieldId, timeSeriesList)
    datapoints = extract_data_points(timeSeries)
    return extract_values_and_timestamps(datapoints)