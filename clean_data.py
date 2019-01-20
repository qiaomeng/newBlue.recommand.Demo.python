import json
import pdb

def clean_mysql_log(log_path="./data/BlueTV-DB-mms.txt", 
                    clean_path="./data/article_info.json"):
# def clean_mysql_log(log_path,clean_path)
    pdb.set_trace()
    with open(log_path, "r") as fp:
        log_file = fp.readlines()
        log_file = log_file[4:-2]
    col_name = "ID,PID,NAME_CN,DESCRIPTION,STARRING,DIRECTORY,TAG,CREATOR_NAME"
    col_name = col_name.split(",")
    result_dict = dict()
    for line in log_file:
        line = line[1:-1]
        line = line.replace(" ", "").split("|")
        tmp = dict(zip(col_name, line))
        result_dict[tmp["ID"]] = tmp
    with open(clean_path, "w+") as fp:
        json.dump(result_dict, fp)

if __name__ == "__main__":
    clean_mysql_log()
    pass