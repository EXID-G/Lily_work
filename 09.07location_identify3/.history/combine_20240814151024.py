import ast

def combine_list_todf(my_filename):
    result = get_one_hanlp_list(my_filename) + get_one_match_list(my_filename)
    # df = pd.DataFrame(result, columns=['location_name', 'value', 'method']).groupby("location_name").agg({"value": lambda x: list(x)}).reset_index()
    # df["count"] = df["value"].apply(lambda x: len(x))
    df = pd.DataFrame(result, columns=['location_name', 'value', 'method'])
    df["filename"] = my_filename
    df.to_csv(f"data/output_hanlp_match/csv/{my_filename}.csv", index=False,encoding="utf-16",sep="\t")
    return df

def get_one_hanlp_list(my_filename):
    # with open(f"data/output_hanlp/{my_filename}.txt", "r") as f:
    with open(f"data/output_hanlp+worldcloud/txt/{my_filename}.txt", "r") as f:
        content = f.read()
        tmp_ner_list = [ast.literal_eval(i.strip()) for i in content[1:-1].strip().split("\n")]
        result =[[item[0], (index, item[2],item[3]),"hanlp"] for index, sublist in enumerate(tmp_ner_list) for item in sublist if item[1] == 'ns']
    return result

def get_one_match_list(my_filename):
    with open(f"data/output_match/txt/{my_filename}.txt", "r") as f:
        content = f.read()
        tmp_ner_list = [ast.literal_eval(i.strip()) for i in content[1:-1].strip().split("\n")]
        result =[[item[0], (index, item[2],item[3]),"patch"] for index, sublist in enumerate(tmp_ner_list) for item in sublist if item[1] == 'ns']
    return result