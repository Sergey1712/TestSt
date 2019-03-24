def main():
    dict = {
        'плавкасаргона': (r"плавкасаргона", r"Плавка получена с установки продувки аргоном \n"),
        'тликв': (r"тликв=(\d{4})", r"Температура ликвидуса = \1 \n"),
        'трубокиспользовалидляпрожиганиястальковша': (
            r"("r"\d+)трубокиспользовалидляпрожиганиястальковша",
            r"\1 трубок использовали для прожигания стальковша \n"),
        'разлитаполностью': (r"разлитаполностью", r"Сталь разлита полностью \n"),
        'плавкасобработкойнаупк': (
            r"плавкасобработкойнаупк",
            r"Плавка обработана на установке «печь-ковш» с возможностью подогрева стали \n"),
        '1м1мзаменаворонки': (r"(\d+)м(\d+)мзаменаворонки", r"\1 машина \2 метр замена воронки \n"),
        'м15на5мзаменаворонки': (
            r"м(\d+)на(\d+)мзаменаворонки", r"\1 машина на \2 метре замена воронки \n"),
        '11*50ми12*11мзаменаворонок': (r"(\d+)м(\d+)ми(\d+)м(\d+)мзаменаворонок",
                                       r"\1 машина \2 метр и \3 машина \4 метр замена воронок \n"),
        'плавкасобработкойнаацв': (r"плавкасобработкойнаацв", r"Плавка на агрегате циркуляционного "
                                                              r"вакуумирования \n"),
        'напереходеперековшовка': (r"напереходеперековшовка", r"Перековшовка на переходе \n"),
        'м12-7слзамвор': (r"м(\d+)-(\d+)слзамвор", r"Машина \1 сляб \2 замена воронки \n"),
        'напереходенапл№1111прожигание': (
            r"напереходенапл№(\d+)прожигание", r"На переходе на плавку №\1 прожигание \n"),
        'сазотированием': (r"сазотированием", r"Плавка с азотрованием \n"),
        'расходазота-4мкуб/час': (
            r"расходазота-(\d+)мкуб/час", r"Расход азота = \1 кубометров/час \n"),
        'вполостьзащитнойтрубы': (r"вполостьзащитнойтрубы", r"В полость защитной трубы \n"),
        'расходаргона-2мкуб/час': (
            r"расходаргона-(\d+)мкуб/час", r"Расход аргона = \1 кубометров/час \n"),
        'vр-05м/мин1сл': (r"vр-(\d+)м/мин(\d+)сл", r"Скорость разливки на \2 слябе = \1 м/мин \n"),
        'vр-05м/мин': (r"vр-(\d+)м/мин", r"Скорость разливки = \1 м/мин \n"),
        'низкийурвп/к': (r"низкийурвп/к", r"Низкий уровень в п/к \n"),
        'унрсвывелиизработыпотинапереподготовку': (r"унрсвывелиизработыпотинапереподготовку",
                                                   r"Установку непрерывной разливки стали вывели из работы по ТИ на переподготовку \n"),

    }
    return dict
