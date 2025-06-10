import cdsapi

dataset = "reanalysis-era5-pressure-levels"
request = {
    "product_type": ["reanalysis"],
    "variable": [
        "geopotential",
        "specific_humidity",
        "temperature",
        "u_component_of_wind",
        "v_component_of_wind"
    ],
    "year": ["YYYY"],
    "month": ["MM"],
    "day": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
    ],
    "time": [
        "00:00", "03:00", "06:00",
        "09:00", "12:00", "15:00",
        "18:00", "21:00"
    ],
    "pressure_level": [
        "1", "2", "3",
        "5", "7", "10",
        "20", "30", "50",
        "70", "100", "125",
        "150", "175", "200",
        "225", "250", "300",
        "350", "400", "450",
        "500", "550", "600",
        "650", "700", "750",
        "775", "800", "825",
        "850", "875", "900",
        "925", "950", "975",
        "1000"
    ],
    "data_format": "grib",
    "download_format": "unarchived",
    "area": [55, -140, 15, -50]
}

client = cdsapi.Client()
client.retrieve(dataset, request).download('ERA5_WRF_PLEV_YYYYMM.grib')

