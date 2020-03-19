#coding=utf-8
import argparse
import easydldatasetdownload
parser = argparse.ArgumentParser()
parser.add_argument('-dataset_id', type=int,help='input dataset_id of Easydl object detection')
parser.add_argument('-xmlpath', help='LabelImg working directory')
parser.add_argument('-version', help='pro or lite')
parser.add_argument('-suffix', help='labels file format')
args = parser.parse_args()
if args.dataset_id is None or args.xmlpath is None:
	print("Run \"python main.py -h\" for help")
else:
	if args.version is None:
		args.version="lite"
	if args.suffix is None:
		args.suffix="xml"
	
	easydldatasetdownload.downloaddateset(args.dataset_id,args.xmlpath+"\\",args.version,args.suffix)