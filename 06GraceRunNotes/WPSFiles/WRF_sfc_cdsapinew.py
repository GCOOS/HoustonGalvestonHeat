import cdsapi

dataset = "reanalysis-era5-single-levels"
request = {
    "product_type": ["reanalysis"],
    'variable':[
            '10m_u_component_of_wind','10m_v_component_of_wind','2m_dewpoint_temperature',
            '2m_temperature','land_sea_mask','mean_sea_level_pressure',
            'orography','sea_ice_cover','sea_surface_temperature','skin_temperature',
            'snow_density','snow_depth','soil_temperature_level_1',
            'soil_temperature_level_2','soil_temperature_level_3','soil_temperature_level_4',
            'surface_pressure','volumetric_soil_water_layer_1','volumetric_soil_water_layer_2',
            'volumetric_soil_water_layer_3','volumetric_soil_water_layer_4'
    ],
    "year": ["YYYY"],
    "month": ["MM"],
    "day": [
        "23", "24", "25",
        "26", "27", "28",
        "29", "30", "31",
    ],
    "time": [
        "00:00", "03:00", "06:00",
        "09:00", "12:00", "15:00",
        "18:00", "21:00"
    ],
    "data_format": "grib",
    "download_format": "unarchived",
    "area": [55, -140, 15, -50]
}

client = cdsapi.Client()
client.retrieve(dataset, request).download('ERA5_WRF_SFC_YYYYMM.grib')

