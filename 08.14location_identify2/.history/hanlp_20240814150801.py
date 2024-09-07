from docx import Document
from hanlp_restful import HanLPClient
import os
from tqdm import tqdm

# HanLP = HanLPClient('https://www.hanlp.com/api', auth='你申请到的auth')  # auth需要申请


HanLP = HanLPClient('https://www.hanlp.com/api', auth="NTc3MkBiYnMuaGFubHAuY29tOnV6R0xMS05pblB3c29CZE4=", language='zh')

def read_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return ''.join(full_text)

def split_text(text, max_length=15000):
    # 使用\n分割文本为句子列表
    sentences = text.split('\n')
    # display(len(sentences))
    parts = []
    current_part = ""

    for sentence in sentences:
        # 检查加入当前句子是否会超过最大长度
        if len(current_part) + len(sentence) + 1 > max_length:  # +1 是为了计算加入的换行符
            # 如果会超过，当前部分结束，开始新的部分
            parts.append(current_part)
            current_part = sentence  # 开始新的部分，当前句子是新部分的第一句
        else:
            # 如果不会超过，将当前句子加入当前部分
            if current_part:  # 如果当前部分不为空，先加入换行符
                current_part += '\n'
            current_part += sentence

    # 循环结束后，将最后一部分（如果有）加入到部分列表中
    if current_part:
        parts.append(current_part)

    return parts

def hanlp_run_oneFile(my_filepath):
    text = read_docx(my_filepath)
    # print(text)

    # 检查文本长度并分割
    # display(len(text.split("\n")))
    texts = split_text(text) if len(text) > 15000 else [text]
    # 初始化空列表来存储所有部分的结果
    all_ner_lists = []
    # display(len(texts))
    # display(len(texts[0].split("\n")))

    # 对每个文本部分调用 API 并合并结果
    for part_text in texts:
        doc = HanLP(part_text, tasks='ner/pku', language='zh')
        
        # doc.pretty_print()
        
        my_ner_list = doc['ner/pku']
        # display(len(my_ner_list))
        all_ner_lists.extend(my_ner_list)

    my_filename = my_filepath.split("/")[-1].split(".")[0]
    # display(len(all_ner_lists))
    return all_ner_lists, my_filename

def hanlp_run_oneFolder(input_folder,output_folder):
    fileList=os.listdir(input_folder)
    for i in tqdm(fileList):
        my_filepath = f"{input_folder}/{i}"
        ner_list, filename = hanlp_run_oneFile(my_filepath)
        with open(f"{output_folder}/{filename}.txt","w") as f:
            f.write("[\n")
            for item in ner_list:
                f.write("%s\n" % item)
            f.write("]")

