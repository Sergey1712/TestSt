#  Copyright (c) 2019.
#  Created by Sergey Pinchuk
#  All right reserved
from fuzzywuzzy import fuzz
import fuzzywuzzy


def fsearch(stroka, sokr):
    if fuzz.partial_ratio(stroka, sokr) >= 75 or fuzz.ratio(stroka, sokr) >= 75 or \
            fuzz.token_set_ratio(stroka, sokr) >= 75 or fuzz.token_sort_ratio(stroka, sokr) >= 75:
        return True
    if len(sokr) > 15:
        if fuzz.partial_ratio(stroka, sokr) >= 60 or fuzz.ratio(stroka,
                                                                sokr) >= 60 or fuzz.token_set_ratio(
            stroka, sokr) >= 60 or fuzz.token_sort_ratio(stroka, sokr) >= 60:
            return True
    else:
        return False
