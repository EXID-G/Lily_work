#!/bin/bash

# 从2开始到35结束的for循环
for i in $(seq 2 35)
do
    # 使用echo命令将指定的文本写入文件，并在每两行之间添加一个空行
    echo "timeline;location;context" > "$i.txt"
    echo "" >> "$i.txt"  # 添加一个空行
    echo "timeline;dos;context" >> "$i.txt"
    echo "" >> "$i.txt"  # 添加一个空行
    echo "timeline;emosOrEvaluations;context" >> "$i.txt"
    echo "" >> "$i.txt"
done

echo "文件创建完成。"