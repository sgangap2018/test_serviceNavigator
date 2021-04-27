import pandas as pd

#function to dump json file data into a pandas dataframe from which
#the project ID (for url) are extracted
def get_args():
	IDS = []
	#open json test data into dataframe
	read_file = open("test_data/data_file.json", "r")
	df = pd.read_json(read_file)
	for column_name, item in df.iteritems():
		project_id = item['projectId']
		IDS.append(project_id)
	return IDS




