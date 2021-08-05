# PyBLS

The PyBLS module is a python module specifically designed to interact with the Bureau of Labor Statistics
API and transform the results into a Pandas Dataframe. 

## Prerequisites

The following python packages must be installed into your environment:

| Package | Version |
| ------- | ------- |
| Pandas | 1.2.3+ |
| requests | 2.25.1+ |

Any versions lower than this may work, but have not been tested. 

## Setup

This tool is designed to only interact with version 2 of the Bureau of Labor Statistics API, which *requires* the user to have an API key from the BLS. To obtain a key [follow this link](https://www.bls.gov/developers/home.htm) and select 'registration'. This will allow you to sign up for an API key.

PyBLS is designed to have your API key be set in an environment variable in the terminal that you are working in. Once the BLS has issued you your API key, set the following environment variable using one of the 2 processes below based on your machine-type:

Windows:
```psh
$Env:BLS_API_KEY='{YOUR_API_KEY}'
```

Mac/Linux:
```sh
export BLS_API_KEY='{YOUR_API_KEY}'
```

There are several advantages to using an API key and version 2 of the Bureau of Labor Statistics API, but the main one is that this will allow a user to query their API up to 500 times per day as opposed to only 25 times with version 1. Version 2 also allows for laregr timeframes per query, and more series IDs in a single query.

## Usage

Below is a simple example of how PyBLS could be called:

```python
from pybls.bls_data import BlsData

my_bls_data = BlsData(
    ['ENUUS00040010','ENU0400040010'],
    2015,
    2020
)
```

From here, follow the API guide to see what you are able to do with this BlsData object that has just been instantiated.

## API

### `BlsData.from_json`

Alternate constructor for BlsData that takes a json file of data returned from the BLS
API and uses it to create a BlsData object. Mainly used for testing to limit calls to the BLS api, and so
work can be done offline by just saving the api data locally.

```python
import json
from pybls.bls_data import BlsData

my_bls_data = BlsData.from_json('json_file_with_raw_bls_data.json')
```

### `BlsData.write_to_json`

Writes raw data from BLS API out to a json file to avoid having to re-query the API for testing.

Arguments:
- file_name = str; Name of the file that should be outputted.

```python
from pybls.bls_data import BlsData

my_bls_data = BlsData(
    ['ENUUS00040010','ENU0400040010'],
    2015,
    2020
)

my_bls_data.write_to_json('bls_json_data.json')
```

### `BlsData.create_graph`

Returns a graph-able plotly object from the given data and constructed dataframe. Renames columns based on the mapping of seriesIDs to locations from the BLS area codes.
Arguments:
- title = str; graph title
- graph_type = str; the style of graph to be used **(only accepts `line` and `bar`)**
- custom_column_names = dict; mapping of seriesID to custom defined column names. Default=`None`
- transpose = bool; transpose df to graph correctly. Default=False
- short_location_names = bool; removes the state from the coumn names to shorten the length. Default=`True`
- graph_labels = dict; a mapping of x and y axis labels to output a graph with custom labels Default=`None`

Returns a plotly express object.

from pybls.bls_data import BlsData

```python
my_bls_data = BlsData(
    ['ENUUS00040010','ENU0400040010'],
    2015,
    2020
)

fig = my_bls_data.create_graph('BLS API Test Graph', 'line', graph_labels = {'date': 'Date', 'value': 'Amount in USD'})

fig.show()
```

### `BlsData.create_table`

Creates an html table from the dataframe with cleaned columns.
Arguments:
- custom_column_names = dict; mapping of series ID to custom column name. Default=`None`
- short_location_names = bool; removes the state from the coumn names to shorten the length. Default=`True`
- index_color = str; the color to apply to the index column and header row. Default=`None`
- descending = bool; changes indexes to sort on descending if True. Default=`False`
- index_label = str; adds a custom index label to the index column in a table. Default=''
- lines = str: colors the borders between cells with a specified color.
- align = str: aligns the text inside of cells in either right, left, or center. Default=None
Returns plotly.graph_object.Figure() object.

```python
my_bls_data = BlsData(
    ['ENUUS00040010','ENU0400040010'],
    2015,
    2020
)

fig = my_bls_data.create_table(
    custom_column_names = {'ENUUS00040010' : 'Entire US', 'ENU0400040010' : 'Arizona'},
    index_color='orange',
    descending=True,
    line_color='black',
    align='left')

fig.show()
```

### `BlsData.clean_df`

Cleans the standard dataframe up by renaming columns with locations, or applying the custom column names.
Arguments:
- custom_column_names = dict; mapping of series ID to custom column name. `Default`=`None`
- short_location_names = bool; removes the state from the coumn names to shorten the length. Default=`True`
