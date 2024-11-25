import json

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