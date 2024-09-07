from extract_locationName_toTXT import *
from  combine import *
import os
import pandas as pd


def get_fileList(root_dir, fileName_list):
    return [f"{root_dir}/{fileName}" for fileName in fileName_list]

def runFiles(    rawData_dir,    outputFolder_name,    remove_words=["建设","新建","高峰","前进","公安","海湾","楼下","西边","中村"]    ):

    #######################################################
    outputFolder_hanlp = f"data/output_locationName/{outputFolder_name}/hanlp"
    outputFolder_match = f"data/output_locationName/{outputFolder_name}/match"
    outputFolder_combine = f"data/output_locationName/{outputFolder_name}/combine"

    if not os.path.exists(f"data/output_locationName/{outputFolder_name}"):
        os.mkdir(f"data/{outputFolder_name}")
    os.mkdir(outputFolder_hanlp)
    os.mkdir(outputFolder_match)
    os.mkdir(outputFolder_combine)

    print(f"Your raw files are from `{rawData_dir}`.")
    print(f"Your final `.csv` files will be saved in `{outputFolder_combine}`.")
    print("="*100)

    fileName_list = os.listdir(rawData_dir)
    file_list = get_fileList(rawData_dir,fileName_list)

    #######################################################
    ##* get ner_list
    hanlp_runFiles(file_list, outputFolder_hanlp)

    df_match = pd.read_csv("raw_data/match_frame.csv",encoding='utf-16',sep='\t')
    df_match_remove = removeWords_fromMF(df_match,remove_words)
    match_runFiles(file_list,outputFolder_match,df_match_remove)

    ##* combine two lists and convert to csv
    combine_runFiles(fileName_list,outputFolder_hanlp,outputFolder_match,outputFolder_combine)
    print("="*100)
    print("Completed!\n")

