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
    return values, timestamps

def parse_datapoints(fieldName:str, data: dict):
    """
    Extracts the values and timestamps for a specific field name from a JSON data structure.

    Parameters:
    ----------
    fieldName : str
        The name of the field to search for in the dataset (e.g., "outdoorTemperature").
    data : dict
        The full dataset loaded from a JSON file. This must follow the expected structure,
        containing keys like 'datacellar:datasetSelfDescription' and 'datacellar:timeSeriesList'.

    Returns:
    -------
    tuple[list[float], list[str]]
        A tuple containing two lists:
        - A list of values (floats) corresponding to the data points.
        - A list of timestamps (strings) associated with each value.
    """
    dataFieldsList = data["datacellar:datasetSelfDescription"]["datacellar:datasetFields"]
    timeSeriesList = data["datacellar:timeSeriesList"]
    fieldId = find_data_field_id(fieldName, dataFieldsList)
    timeSeries = find_timeseries(fieldId, timeSeriesList)
    datapoints = extract_data_points(timeSeries)
    return extract_values_and_timestamps(datapoints)