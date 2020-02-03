import re


def get_sku_list(filename):
    output_str = ''
    with open('sku_ids.txt') as f:
        for row in f:
            res = re.findall(r"item.jd.com/(.+?)\.html", row)
            if res != []:
                print(res)
                output_str += res[0] + ':1,'
    return output_str[:-1]
