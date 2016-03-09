#!/usr/bin/python

import re
import sys
import time

from broadview_collector.broadview_collector import main 

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
