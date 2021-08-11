"""
pybls module is designed to interact with the Bureau of Labor Statistics
API and translate returned json data into pandas dataframes.

In this init file, some code exists to initialize the dataframes for the
area codes that the BLS data uses to identify the region that a seriesID
pertains to.
"""
import pandas as pd
import pkg_resources

#Construct QCEW area codes DataFrame from area code csv
qcew_stream = pkg_resources.resource_stream(__name__, 'data/area_titles.csv')
qcew_area_codes_df = pd.read_csv(qcew_stream)
qcew_area_codes_df = qcew_area_codes_df.set_index('area_fips')

#Construct OES area codes DataFrame from area code csv
stream = pkg_resources.resource_stream(__name__, 'data/oes_areas.csv')
oes_area_codes_df = pd.read_csv(stream, dtype={'area_code':str})
oes_area_codes_df = oes_area_codes_df.set_index('area_code')

#Construct LA area codes for Local Area Employment Statistics locations
stream = pkg_resources.resource_stream(__name__, 'data/la_area.csv')
la_area_codes_df = pd.read_csv(stream)
la_area_codes_df = la_area_codes_df.set_index('area_code')
