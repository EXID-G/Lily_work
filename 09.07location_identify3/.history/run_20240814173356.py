from operation import *

raw_root = "raw_data/Interview transcripts-round 1"
outputFolder_hanlp = "data/output_round1/hanlp"
outputFolder_match = "data/output_round1/match"

def get_fileList(root_dir, fileName_list):
    return [f"{root_dir}/{fileName}" for fileName in fileName_list]

fileName_list = os.listdir(raw_root)
file_list = get_fileList(raw_root,fileName_list)
hanlp_runFiles(file_list, outputFolder_hanlp)
