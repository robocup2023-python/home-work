import argparse
import pandas as pd
parser=argparse.ArgumentParser(description="从CSV文件中删除特定列。")
parser.add_argument('--path',help="文件路径为：")
parser.add_argument('--number',help="删除哪一列？")
args=parser.parse_args()
file_path=args.path
column=args.number

drinks=pd.read_csv(file_path)
column_to_remove=column
drinks=drinks.drop(column_to_remove,axis=1)
drinks.to_csv(file_path,index=False)
