from docx import Document
from tqdm import tqdm
imp

def get_one_hanlp_list(my_filename,outputFolderHanlp):
    with open(f"{outputFolderHanlp}/{my_filename}.txt", "r") as f:
        content = f.read()
        tmp_ner_list = [ast.literal_eval(i.strip()) for i in content[1:-1].strip().split("\n")]
        result =[[item[0], (index, item[2],item[3]),"hanlp"] for index, sublist in enumerate(tmp_ner_list) for item in sublist if item[1] == 'ns']
    return result

def get_one_match_list(my_filename,outputFolderMatch):
    with open(f"{outputFolderMatch}/{my_filename}.txt", "r") as f:
        content = f.read()
        tmp_ner_list = [ast.literal_eval(i.strip()) for i in content[1:-1].strip().split("\n")]
        result =[[item[0], (index, item[2],item[3]),"patch"] for index, sublist in enumerate(tmp_ner_list) for item in sublist if item[1] == 'ns']
    return result


def combine_list_todf(my_filename,outputFolderCombine):
    result = get_one_hanlp_list(my_filename) + get_one_match_list(my_filename)
    df = pd.DataFrame(result, columns=['location_name', 'value', 'method'])
    df["filename"] = my_filename
    df.to_csv(f"{outputFolderCombine}/{my_filename}.csv", index=False,encoding="utf-16",sep="\t")
    return df

