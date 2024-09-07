import pandas as pd
import ast
from tqdm import tqdm
import os

def get_one_hanlp_list(my_filename,dir_hanlp):
    with open(f"{dir_hanlp}/{my_filename}.txt", "r") as f:
        content = f.read()
        tmp_ner_list = [ast.literal_eval(i.strip()) for i in content[1:-1].strip().split("\n")]
        result =[[item[0], (index, item[2],item[3]),"hanlp"] for index, sublist in enumerate(tmp_ner_list) for item in sublist if item[1] == 'ns']
    return result

def get_one_match_list(my_filename,dir_match):
    with open(f"{dir_match}/{my_filename}.txt", "r") as f:
        content = f.read()
        tmp_ner_list = [ast.literal_eval(i.strip()) for i in content[1:-1].strip().split("\n")]
        result =[[item[0], (index, item[2],item[3]),"patch"] for index, sublist in enumerate(tmp_ner_list) for item in sublist if item[1] == 'ns']
    return result

def combine_list_todf(my_fileName, outputFolder_hanlp,outputFolder_match,outputFolder_combine):
    result = get_one_hanlp_list(my_fileName,outputFolder_hanlp) + get_one_match_list(my_fileName,outputFolder_match)
    df = pd.DataFrame(result, columns=['location_name', 'value', 'method'])
    df["filename"] = my_fileName
    df.to_csv(f"{outputFolder_combine}/{my_fileName}.csv", index=False,encoding="utf-16",sep="\t")
    return df

def combine_runFiles(fileName_list, outputFolder_hanlp,outputFolder_match,outputFolder_combine):
    for i in tqdm(fileName_list):
        file
        combine_list_todf(filename, outputFolder_hanlp,outputFolder_match,outputFolder_combine)

