# -*- coding: utf-8 -*-
import sys
import json


def parse_file(filename):
    ret = []
    with open(filename) as fd:
        for line in fd.readlines():
            code, level, name, pcode = line.split(',')
            item = {
                        'model':'district.district',
                        'pk':code,
                        'fields': {
                            'name':name,
                            'parent':pcode.strip(),
                            'level':level
                        }
                   }
            ret.append(item)
    return ret

def create_fixture(data, filename):
    with open(filename, 'wb') as fd:
        fd.write(json.dumps(data, ensure_ascii=False, indent=4).encode('utf-8'))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print ("Usage: %s <source> <target>" % sys.argv[0])
        sys.exit(1)
    data = parse_file(sys.argv[1])
    create_fixture(data, sys.argv[2])
