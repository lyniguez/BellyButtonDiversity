# import necessary libraries
from sqlalchemy import func
import datetime as dt
import numpy as np
import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

@app.route("/")
def index():
    
    return render_template("index.html")


@app.route('/names')
def names():
    DF = pd.read_csv("Instructions\DataSets\Belly_Button_Biodiversity_samples.csv")
    DF_index = DF.set_index('otu_id')
    results = list(DF_index)
    
    DF_list = list(np.ravel(results))
    return jsonify(DF_list)


@app.route('/otu')
def otu():
    DF = pd.read_csv("Instructions\DataSets\Belly_Button_Biodiversity_otu_id.csv")
    DF_index = DF.set_index('otu_id')
    results = DF_index['lowest_taxonomic_unit_found']
    
    DF_list = list(np.ravel(results))
    return jsonify(DF_list)


@app.route('/metadata', defaults={'sample':'BB_940'})
@app.route('/metadata/<sample>')
def metadata(sample):
    DF = pd.read_csv("Instructions\DataSets\Belly_Button_Biodiversity_Metadata.csv")
    DF_md_index = DF.set_index('SAMPLEID')
    sampleID = int(sample.replace("BB_",""))
    DF_sample = DF_md_index.loc[sampleID]
    DF_sample["SAMPLEID"] = sampleID
    results = DF_sample[["AGE","BBTYPE","ETHNICITY","GENDER","LOCATION","SAMPLEID"]]
    
    DF_list = results.to_dict()
    return jsonify(DF_list)

@app.route('/wfreq', defaults={'samplewf':'BB_940'})
@app.route('/wfreq/<samplewf>')
def wfreq(samplewf):
    DF = pd.read_csv("Instructions\DataSets\Belly_Button_Biodiversity_Metadata.csv")
    DF_wf_index = DF.set_index('SAMPLEID')
    samplewfID = int(samplewf.replace("BB_",""))
    DF_wf = DF_wf_index.loc[[samplewfID],['WFREQ']]
    results = DF_wf["WFREQ"].item()
    
    
    return jsonify(results)

@app.route('/samples', defaults={'sample':'BB_943'})
@app.route('/samples/<sample>')
def sample(sample = 'BB_943'):
    DF = pd.read_csv("Instructions\DataSets\Belly_Button_Biodiversity_Samples.csv")
    DF_sample_filter = DF.filter(items = [sample,'otu_id'])
    DF_sample_sort = DF_sample_filter.sort_values(by=sample, ascending=False)
    DF_sample_nonzero_nan = DF_sample_sort[DF_sample_sort > 0]
    DF_sample_nonzero = DF_sample_nonzero_nan.dropna()
    sample_values = DF_sample_nonzero[sample].tolist()
    otu_ids = DF_sample_nonzero['otu_id'].tolist()
    results = [{'otu_ids':otu_ids,'sample_values':sample_values}]

    return jsonify(results)


# this last bit of code allows you to run the python script through the terminal
if __name__ == '__main__':
    app.run()