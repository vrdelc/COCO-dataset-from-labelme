import sys
import argparse
import os
import random
import shutil

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True, help="images folder")
ap.add_argument("-f", "--folder", required=True, help="final folder name")
ap.add_argument("-l", "--labels", required=True, help="labels file")
#ap.add_argument("-p", "--labelme", required=True, help="path to labelme")
ap.add_argument("-y", "--year", required=False, default=2019, help="year (default:2019)",type=int)
ap.add_argument("-t", "--train", required=False, default=70, help="train % (default:70)",type=int)

args = vars(ap.parse_args())
print(args)

folder = args['folder']
train = args['train']
year = args['year']
json_files = []
for file in os.listdir(args['images']):
    if(file.endswith('.json') and os.path.isfile(args['images']+'/'+file[:-5]+".jpeg")):
        json_files.append(file[:-5])
random.shuffle(json_files)
print(str(len(json_files))+" images with annotations find in the directory")
train_number = int(len(json_files)*70/100)
json_train = json_files[:train_number]
print(str(len(json_train))+" images with annotations (train)")
json_val = json_files[train_number:]
print(str(len(json_val))+" images with annotations (val)")
if(not os.path.exists(folder)):
    os.mkdir(folder)
    print("Created folder: "+folder)
    os.mkdir(folder+"/train")
    os.mkdir(folder+"/val")
    os.mkdir(folder+"/annotations")
else:
    print("Folder exists, please give other name")
    sys.exit()

def generate_dataset(method="train", json_train = []):
    for file in json_train:
        json_shutil = shutil.copyfile(args['images']+"/"+file+".json", folder+"/"+method+"/"+file+".json")
        jpeg_shutil = shutil.copyfile(args['images']+"/"+file+".jpeg", folder+"/"+method+"/"+file+".jpeg")
        print(json_shutil,jpeg_shutil)
    count_train = 0
    for file in os.listdir(folder+"/"+method):
        if(file.endswith('.json') and os.path.isfile(folder+"/"+method+"/"+file[:-5]+".jpeg")):
            count_train+=1
    print(str(count_train)+" images with annotations: " + method)
    output_train = os.system("python "+"labelme2coco.py "+folder+"/"+method+" "+folder+"/"+method+str(year)+" --labels " + args['labels'])
    if output_train != 0:
        print("Problem generating: "+method)
        exit()
    shutil.copyfile(folder+"/"+method+str(year)+"/annotations.json",folder+"/annotations/instances_"+method+str(year)+".json")
    shutil.rmtree(folder+"/"+method)

generate_dataset("train", json_train)
generate_dataset("val", json_val)
