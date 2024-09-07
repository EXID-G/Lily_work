from operation import *
from  combine import *
import os
import pandas as pd


def get_fileList(root_dir, fileName_list):
    return [f"{root_dir}/{fileName}" for fileName in fileName_list]

def runFiles(root_dir,outputFolder_name):
    ############################################################################################
    raw_root = "raw_data/Interview transcripts-round 1"
    outputFolder_hanlp = f"data/{outputFolder_name}/hanlp"
    outputFolder_match = "data/output_round1/match"
    fileName_list = os.listdir(raw_root)
    file_list = get_fileList(raw_root,fileName_list)


    ############################################################################################


    hanlp_runFiles(file_list, outputFolder_hanlp)

    ############################################################################################
    df_match = pd.read_csv("raw_data/match_frame.csv",encoding='utf-16',sep='\t')

    remove_words = ["建设","新建","高峰","前进","公安","海湾","楼下","西边","中村"]
    df_match_remove = removeWords_fromMF(df_match,remove_words)
    match_runFiles(file_list,outputFolder_match,df_match_remove)

