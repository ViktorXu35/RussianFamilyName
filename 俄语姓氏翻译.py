#  Авторские права (c) 2021.
#  Автор (Виктор Сюй) имеет все права на использование, адаптацию и распространение данной программы.
#  Почта для справки: viktor.p.xu@yandex.ru

def get_monosyl(lis):
    a = []
    for i in lis:
        c = str(i).split(' ')
        a.extend(c)
    return a

def sort_by_letters(lis):
    three=[]
    two=[]
    one=[]
    for i in lis:
        if len(i)==3:
            three.append(i)
        elif len(i)==2:
            two.append(i)
        elif len(i)==1:
            one.append(i)
    dic={'three':three,'two':two,'one':one}
    return dic

def get_index(example,num,ex=[]):
    leng=[i for i in range(len(example)-num+1)]
    index=[]
    all_index=[]
    for i in list(filter(lambda x:x not in ex,leng)):
        str1=example[i:i+num]
        alls=merger[list(merger.keys())[3-num]]
        if str1 in alls:
            for j in range(num):
                index.append((i,str1))
                all_index.append(i+j)
                j+=1
    return [index,all_index]

def get_ex(example,num):
    return [get_index(example,num)[1][i] for i in range(len(get_index(example,num)[1]))]

def check_and_replace(example):
    example = example.replace('его', 'ево')
    example = example.replace('ого', 'ово')
    example = example.replace('гк', 'хк')
    example = example.replace('чт', 'шт')
    #m在b，p前发n
    for i in range(len(example)-1):
        example=list(example)
        if example[i]=='м':
            if example[i+1]=='б':
                example[i]='н'
            if example[i+1]=='п':
                example[i] = 'н'
            else:pass
    example = ''.join(example)
    for i in range(len(example)-2):
        example=list(example)
        if example[i] in vowel:
            if example[i+1]=='н' and example[i+2] in vowel:
                example[i+1]='нн'
            else:pass
        else:pass
    example=''.join(example)
    return example

def concat_syl(dic):
    mergein=[]
    for i in range(1,len(dic.keys())):
        leng=len(list(dic.keys()))
        if dic[list(dic.keys())[leng-i]] in vowel:
            if dic[list(dic.keys())[leng-i-1]] in consonant:
                mergein.append((list(dic.keys())[leng-i-1],dic[list(dic.keys())[leng-i-1]]+dic[list(dic.keys())[leng-i]]))
            else:
                mergein.append((list(dic.keys())[leng-i],dic[list(dic.keys())[leng-i]]))
        else:
            mergein.append((list(dic.keys())[leng - i], dic[list(dic.keys())[leng - i]]))
    mergein.append((0,dic[0]))
    return dict(sorted(mergein))

if __name__ == '__main__':
    print('copyright @ Viktor Xu','\n'
          '请输入俄语姓氏','\n'
          '女性姓氏一般以а或я结尾')
    vowel=['а', 'я', 'э', 'эй', 'е', 'ы', 'ый', 'и', 'ий', 'ьи', 'ь', 'о', 'ё', 'йо', 'у', 'ю', 'ью', 'ай', 'аи', 'ау',
           'ао', 'уй', 'ан', 'ань', 'ян', 'янь', 'ен', 'ень', 'эн', 'энь', 'ын', 'ынь', 'ин', 'инь', 'он', 'онь', 'ун',
           'унь', 'юн', 'юнь', 'ей', 'ой']
    consonant=['б', 'п', 'д', 'т', 'г', 'к', 'в', 'ф', 'з', 'дз', 'с', 'ж', 'ш', 'дж', 'ч', 'тч', 'дч', 'щ', 'сч', 'ц',
               'дц', 'тц', 'дс', 'тс', 'цс', 'х', 'м', 'н', 'л', 'р']
    merger=sort_by_letters(vowel+consonant)
    male={'а': '阿', 'я': '亚', 'э': '埃', 'эй': '埃', 'е': '耶', 'ы': '厄', 'ый': '厄', 'и': '伊', 'ий': '伊', 'ьи': '伊', 'ь': '伊',
     'о': '奥', 'ё': '约', 'йо': '约', 'у': '乌', 'ю': '尤', 'ью': '尤', 'ай': '艾', 'аи': '艾', 'ау': '奥', 'ао': '奥',
     'уй': '维', 'ан': '安', 'ань': '安', 'ян': '扬', 'янь': '扬', 'ен': '延', 'ень': '延', 'эн': '恩', 'энь': '恩', 'ын': '恩',
     'ынь': '恩', 'ин': '因', 'инь': '因', 'он': '翁', 'онь': '翁', 'ун': '温', 'унь': '温', 'юн': '云', 'юнь': '云', 'ей': '耶伊',
     'ой': '奥伊', 'б': '布', 'ба': '巴', 'бя': '比亚', 'бэ': '贝', 'бэй': '贝', 'бе': '别', 'бы': '贝', 'бый': '贝', 'би': '比',
     'бий': '比', 'бьи': '比', 'бь': '比', 'бо': '博', 'бё': '比奥', 'бйо': '比奥', 'бу': '布', 'бю': '比尤', 'бью': '比尤',
     'бай': '拜', 'баи': '拜', 'бау': '包', 'бао': '包', 'буй': '布伊', 'бан': '班', 'бань': '班', 'бян': '比扬', 'бянь': '比扬',
     'бен': '边', 'бень': '边', 'бэн': '本', 'бэнь': '本', 'бын': '本', 'бынь': '本', 'бин': '宾', 'бинь': '宾', 'бон': '邦',
     'бонь': '邦', 'бун': '本', 'бунь': '本', 'бей': '别伊', 'бой': '博伊', 'п': '普', 'па': '帕', 'пя': '皮亚', 'пэ': '佩',
     'пэй': '佩', 'пе': '佩', 'пы': '佩', 'пый': '佩', 'пи': '皮', 'пий': '皮', 'пьи': '皮', 'пь': '皮', 'по': '波', 'пё': '皮奥',
     'пйо': '皮奥', 'пу': '普', 'пю': '皮尤', 'пью': '皮尤', 'пай': '派', 'паи': '派', 'пау': '保', 'пао': '保', 'пуй': '普伊',
     'пан': '潘', 'пань': '潘', 'пян': '皮扬', 'пянь': '皮扬', 'пен': '片', 'пень': '片', 'пэн': '彭', 'пэнь': '彭', 'пын': '彭',
     'пынь': '彭', 'пин': '平', 'пинь': '平', 'пон': '蓬', 'понь': '蓬', 'пун': '蓬', 'пунь': '蓬', 'пей': '佩伊', 'пой': '波伊',
     'д': '德', 'да': '达', 'дя': '佳', 'дэ': '代', 'дэй': '代', 'де': '杰', 'ды': '德', 'дый': '德', 'ди': '季', 'дий': '季',
     'дьи': '季', 'дь': '季', 'до': '多', 'дё': '焦', 'дйо': '焦', 'ду': '杜', 'дю': '久', 'дью': '久', 'дай': '代', 'даи': '代',
     'дау': '道', 'дао': '道', 'дуй': '杜伊', 'дан': '丹', 'дань': '丹', 'дян': '江', 'дянь': '江', 'ден': '坚', 'день': '坚',
     'дэн': '登', 'дэнь': '登', 'дын': '登', 'дынь': '登', 'дин': '金', 'динь': '金', 'дон': '东', 'донь': '东', 'дун': '敦',
     'дунь': '敦', 'дей': '杰伊', 'дой': '多伊', 'т': '特', 'та': '塔', 'тя': '佳', 'тэ': '泰', 'тэй': '泰', 'те': '捷', 'ты': '特',
     'тый': '特', 'ти': '季', 'тий': '季', 'тьи': '季', 'ть': '季', 'то': '托', 'тё': '乔', 'тйо': '乔', 'ту': '图', 'тю': '秋',
     'тью': '秋', 'тай': '泰', 'таи': '泰', 'тау': '陶', 'тао': '陶', 'туй': '图伊', 'тан': '坦', 'тань': '坦', 'тян': '强',
     'тянь': '强', 'тен': '坚', 'тень': '坚', 'тэн': '滕', 'тэнь': '滕', 'тын': '滕', 'тынь': '滕', 'тин': '京', 'тинь': '京',
     'тон': '通', 'тонь': '通', 'тун': '通', 'тунь': '通', 'тюн': '琼', 'тюнь': '琼', 'тей': '捷伊', 'той': '托伊', 'г': '格',
     'га': '加', 'гя': '吉亚', 'гэ': '盖', 'гэй': '盖', 'ге': '格', 'гы': '格', 'гый': '格', 'ги': '吉', 'гий': '吉', 'гьи': '吉',
     'гь': '吉', 'го': '戈', 'гё': '吉奥', 'гйо': '吉奥', 'гу': '古', 'гю': '久', 'гью': '久', 'гай': '盖', 'гаи': '盖',
     'гау': '高', 'гао': '高', 'гуй': '圭', 'ган': '甘', 'гань': '甘', 'гян': '吉扬', 'гянь': '吉扬', 'ген': '根', 'гень': '根',
     'гэн': '根', 'гэнь': '根', 'гын': '根', 'гынь': '根', 'гин': '金', 'гинь': '金', 'гон': '贡', 'гонь': '贡', 'гун': '贡',
     'гунь': '贡', 'гей': '格伊', 'гой': '戈伊', 'к': '克', 'ка': '卡', 'кя': '基亚', 'кэ': '凯', 'кэй': '凯', 'ке': '克',
     'кы': '克', 'кый': '克', 'ки': '基', 'кий': '基', 'кьи': '基', 'кь': '基', 'ко': '科', 'кё': '基奥', 'кйо': '基奥', 'ку': '库',
     'кю': '丘', 'кью': '丘', 'кай': '凯', 'каи': '凯', 'кау': '考', 'као': '考', 'куй': '奎', 'кан': '坎', 'кань': '坎',
     'кян': '基扬', 'кянь': '基扬', 'кен': '肯', 'кень': '肯', 'кэн': '肯', 'кэнь': '肯', 'кын': '肯', 'кынь': '肯', 'кин': '金',
     'кинь': '金', 'кон': '孔', 'конь': '孔', 'кун': '昆', 'кунь': '昆', 'кей': '克伊', 'кой': '科伊', 'в': '夫', 'ва': '瓦',
     'вя': '维亚', 'вэ': '韦', 'вэй': '韦', 'ве': '韦', 'вы': '维', 'вый': '维', 'ви': '维', 'вий': '维', 'вьи': '维', 'вь': '维',
     'во': '沃', 'вё': '维奥', 'вйо': '维奥', 'ву': '武', 'вю': '维尤', 'вью': '维尤', 'вай': '瓦伊', 'ваи': '瓦伊', 'вау': '沃',
     'вао': '沃', 'вуй': '维', 'ван': '万', 'вань': '万', 'вян': '维扬', 'вянь': '维扬', 'вен': '文', 'вень': '文', 'вэн': '文',
     'вэнь': '文', 'вын': '文', 'вынь': '文', 'вин': '温', 'винь': '温', 'вон': '翁', 'вонь': '翁', 'вун': '文', 'вунь': '文',
     'вей': '韦伊', 'вой': '沃伊', 'ф': '夫', 'фа': '法', 'фя': '菲亚', 'фэ': '费', 'фэй': '费', 'фе': '费', 'фы': '菲', 'фый': '菲',
     'фи': '菲', 'фий': '菲', 'фьи': '菲', 'фь': '菲', 'фо': '福', 'фё': '菲奥', 'фйо': '菲奥', 'фу': '富', 'фю': '菲尤',
     'фью': '菲尤', 'фай': '法伊', 'фаи': '法伊', 'фау': '福', 'фао': '福', 'фуй': '富伊', 'фан': '凡', 'фань': '凡', 'фен': '芬',
     'фень': '芬', 'фэн': '芬', 'фэнь': '芬', 'фын': '芬', 'фынь': '芬', 'фин': '芬', 'финь': '芬', 'фон': '丰', 'фонь': '丰',
     'фун': '丰', 'фунь': '丰', 'фей': '费伊', 'фой': '福伊', 'з': '兹', 'дз': '兹', 'за': '扎', 'дза': '扎', 'зя': '贾',
     'дзя': '贾', 'зэ': '泽', 'зэй': '泽', 'дзэ': '泽', 'дзэй': '泽', 'зе': '泽', 'дзе': '泽', 'зы': '济', 'зый': '济',
     'дзы': '济', 'дзый': '济', 'зи': '济', 'зий': '济', 'зьи': '济', 'зь': '济', 'дзи': '济', 'дзий': '济', 'дзьи': '济',
     'дзь': '济', 'зо': '佐', 'дзо': '佐', 'зё': '焦', 'зйо': '焦', 'дзё': '焦', 'дзйо': '焦', 'зу': '祖', 'дзу': '祖',
     'зю': '久', 'зью': '久', 'дзю': '久', 'дзью': '久', 'зай': '宰', 'заи': '宰', 'дзай': '宰', 'дзаи': '宰', 'зау': '藻',
     'зао': '藻', 'дзау': '藻', 'дзао': '藻', 'зуй': '祖伊', 'дзуй': '祖伊', 'зан': '赞', 'зань': '赞', 'дзан': '赞',
     'дзань': '赞', 'зян': '江', 'зянь': '江', 'дзян': '江', 'дзянь': '江', 'зен': '津', 'зень': '津', 'дзен': '津',
     'дзень': '津', 'зэн': '曾', 'зэнь': '曾', 'зын': '曾', 'зынь': '曾', 'дзэн': '曾', 'дзэнь': '曾', 'дзын': '曾',
     'дзынь': '曾', 'зин': '津', 'зинь': '津', 'дзин': '津', 'дзинь': '津', 'зон': '宗', 'зонь': '宗', 'дзон': '宗',
     'дзонь': '宗', 'зун': '尊', 'зунь': '尊', 'дзун': '尊', 'дзунь': '尊', 'зей': '泽伊', 'дзей': '泽伊', 'зой': '佐伊',
     'дзой': '佐伊', 'с': '斯', 'са': '萨', 'ся': '夏', 'сэ': '塞', 'сэй': '塞', 'се': '谢', 'сы': '瑟', 'сый': '瑟', 'си': '西',
     'сий': '西', 'сьи': '西', 'сь': '西', 'со': '索', 'сё': '肖', 'сйо': '肖', 'су': '苏', 'сю': '休', 'сью': '休', 'сай': '赛',
     'саи': '赛', 'сау': '绍', 'сао': '绍', 'суй': '绥', 'сан': '桑', 'сань': '桑', 'сян': '相', 'сянь': '相', 'сен': '先',
     'сень': '先', 'сэн': '森', 'сэнь': '森', 'сын': '森', 'сынь': '森', 'син': '辛', 'синь': '辛', 'сон': '松', 'сонь': '松',
     'сун': '孙', 'сунь': '孙', 'сюн': '雄', 'сюнь': '雄', 'сей': '谢伊', 'сой': '索伊', 'ж': '日', 'жа': '扎', 'жя': '扎',
     'жэ': '热', 'жэй': '热', 'же': '热', 'жы': '日', 'жый': '日', 'жи': '日', 'жий': '日', 'жьи': '日', 'жь': '日', 'жо': '若',
     'жё': '若', 'жйо': '若', 'жу': '茹', 'жю': '茹', 'жью': '茹', 'жай': '扎伊', 'жаи': '扎伊', 'жау': '饶', 'жао': '饶',
     'жуй': '瑞', 'жан': '然', 'жань': '然', 'жян': '让', 'жянь': '让', 'жен': '任', 'жень': '任', 'жэн': '任', 'жэнь': '任',
     'жын': '任', 'жынь': '任', 'жин': '任', 'жинь': '任', 'жон': '容', 'жонь': '容', 'жун': '容', 'жунь': '容', 'жей': '热伊',
     'жой': '若伊', 'ш': '什', 'ша': '沙', 'шя': '沙', 'шэ': '舍', 'шэй': '舍', 'ше': '舍', 'шы': '希', 'шый': '希', 'ши': '希',
     'ший': '希', 'шьи': '希', 'шь': '希', 'шо': '绍', 'шё': '绍', 'шйо': '绍', 'шу': '舒', 'шю': '舒', 'шью': '舒', 'шай': '沙伊',
     'шаи': '沙伊', 'шау': '绍', 'шао': '绍', 'шуй': '舒伊', 'шан': '尚', 'шань': '尚', 'шян': '尚', 'шянь': '尚', 'шен': '申',
     'шень': '申', 'шэн': '申', 'шэнь': '申', 'шын': '申', 'шынь': '申', 'шин': '申', 'шинь': '申', 'шон': '雄', 'шонь': '雄',
     'шун': '顺', 'шунь': '顺', 'шей': '舍伊', 'шой': '绍伊', 'дж': '季', 'джа': '贾', 'джэ': '杰', 'джэй': '杰', 'дже': '杰',
     'джы': '吉', 'джый': '吉', 'джи': '吉', 'джий': '吉', 'джьи': '吉', 'джь': '吉', 'джо': '焦', 'джё': '焦', 'джйо': '焦',
     'джу': '朱', 'джю': '久', 'джью': '久', 'джай': '贾伊', 'джаи': '贾伊', 'джау': '焦', 'джао': '焦', 'джуй': '朱伊',
     'джан': '占', 'джань': '占', 'джян': '江', 'джянь': '江', 'джен': '真', 'джень': '真', 'джэн': '真', 'джэнь': '真',
     'джын': '真', 'джынь': '真', 'джин': '金', 'джинь': '金', 'джон': '忠', 'джонь': '忠', 'джун': '准', 'джунь': '准',
     'джей': '杰伊', 'джой': '焦伊', 'ч': '奇', 'тч': '奇', 'дч': '奇', 'ча': '恰', 'тча': '恰', 'дча': '恰', 'чэ': '切',
     'чэй': '切', 'тчэ': '切', 'тчэй': '切', 'дчэ': '切', 'дчэй': '切', 'че': '切', 'тче': '切', 'дче': '切', 'чи': '奇',
     'чий': '奇', 'чьи': '奇', 'чь': '奇', 'тчи': '奇', 'тчий': '奇', 'тчьи': '奇', 'тчь': '奇', 'дчи': '奇', 'дчий': '奇',
     'дчьи': '奇', 'дчь': '奇', 'чо': '乔', 'тчо': '乔', 'дчо': '乔', 'чё': '乔', 'чйо': '乔', 'тчё': '乔', 'тчйо': '乔',
     'дчё': '乔', 'дчйо': '乔', 'чу': '丘', 'тчу': '丘', 'дчу': '丘', 'чай': '柴', 'чаи': '柴', 'тчай': '柴', 'тчаи': '柴',
     'дчай': '柴', 'дчаи': '柴', 'чау': '乔', 'чао': '乔', 'тчау': '乔', 'тчао': '乔', 'дчау': '乔', 'дчао': '乔', 'чуй': '崔',
     'тчуй': '崔', 'дчуй': '崔', 'чан': '昌', 'чань': '昌', 'тчан': '昌', 'тчань': '昌', 'дчан': '昌', 'дчань': '昌',
     'чян': '强', 'чянь': '强', 'тчян': '强', 'тчянь': '强', 'дчян': '强', 'дчянь': '强', 'чен': '琴', 'чень': '琴',
     'тчен': '琴', 'тчень': '琴', 'дчен': '琴', 'дчень': '琴', 'чэн': '琴', 'чэнь': '琴', 'чын': '琴', 'чынь': '琴',
     'тчэн': '琴', 'тчэнь': '琴', 'тчын': '琴', 'тчынь': '琴', 'дчэн': '琴', 'дчэнь': '琴', 'дчын': '琴', 'дчынь': '琴',
     'чин': '钦', 'чинь': '钦', 'тчин': '钦', 'тчинь': '钦', 'дчин': '钦', 'дчинь': '钦', 'чон': '琼', 'чонь': '琼',
     'тчон': '琼', 'тчонь': '琼', 'дчон': '琼', 'дчонь': '琼', 'чун': '春', 'чунь': '春', 'тчун': '春', 'тчунь': '春',
     'дчун': '春', 'дчунь': '春', 'чей': '切伊', 'тчей': '切伊', 'дчей': '切伊', 'чой': '乔伊', 'тчой': '乔伊', 'дчой': '乔伊',
     'щ': '希', 'сч': '希', 'ща': '夏', 'сча': '夏', 'ще': '谢', 'сче': '谢', 'щи': '希', 'щий': '希', 'щьи': '希', 'щь': '希',
     'счи': '希', 'счий': '希', 'счьи': '希', 'счь': '希', 'що': '晓', 'счо': '晓', 'щё': '晓', 'щйо': '晓', 'счё': '晓',
     'счйо': '晓', 'щу': '休', 'счу': '休', 'щю': '休', 'щью': '休', 'счю': '休', 'счью': '休', 'щай': '夏伊', 'щаи': '夏伊',
     'счай': '夏伊', 'счаи': '夏伊', 'щау': '肖', 'щао': '肖', 'счау': '肖', 'счао': '肖', 'щуй': '休伊', 'счуй': '休伊',
     'щан': '先', 'щань': '先', 'счан': '先', 'счань': '先', 'щен': '先', 'щень': '先', 'счен': '先', 'счень': '先', 'щэн': '欣',
     'щэнь': '欣', 'щын': '欣', 'щынь': '欣', 'счэн': '欣', 'счэнь': '欣', 'счын': '欣', 'счынь': '欣', 'щин': '辛',
     'щинь': '辛', 'счин': '辛', 'счинь': '辛', 'щон': '雄', 'щонь': '雄', 'счон': '雄', 'счонь': '雄', 'щун': '逊',
     'щунь': '逊', 'счун': '逊', 'счунь': '逊', 'щей': '谢伊', 'счей': '谢伊', 'щой': '晓伊', 'счой': '晓伊', 'ц': '茨', 'дц': '茨',
     'тц': '茨', 'дс': '茨', 'тс': '茨', 'цс': '茨', 'ца': '察', 'дца': '察', 'тца': '察', 'дса': '察', 'тса': '察', 'цса': '察',
     'ця': '齐亚', 'дця': '齐亚', 'тця': '齐亚', 'дся': '齐亚', 'тся': '齐亚', 'цся': '齐亚', 'цэ': '采', 'цэй': '采', 'дцэ': '采',
     'дцэй': '采', 'тцэ': '采', 'тцэй': '采', 'дсэ': '采', 'дсэй': '采', 'тсэ': '采', 'тсэй': '采', 'цсэ': '采', 'цсэй': '采',
     'це': '采', 'дце': '采', 'тце': '采', 'дсе': '采', 'тсе': '采', 'цсе': '采', 'цы': '齐', 'цый': '齐', 'дцы': '齐',
     'дцый': '齐', 'тцы': '齐', 'тцый': '齐', 'дсы': '齐', 'дсый': '齐', 'тсы': '齐', 'тсый': '齐', 'цсы': '齐', 'цсый': '齐',
     'ци': '齐', 'ций': '齐', 'цьи': '齐', 'ць': '齐', 'дци': '齐', 'дций': '齐', 'дцьи': '齐', 'дць': '齐', 'тци': '齐',
     'тций': '齐', 'тцьи': '齐', 'тць': '齐', 'дси': '齐', 'дсий': '齐', 'дсьи': '齐', 'дсь': '齐', 'тси': '齐', 'тсий': '齐',
     'тсьи': '齐', 'тсь': '齐', 'цси': '齐', 'цсий': '齐', 'цсьи': '齐', 'цсь': '齐', 'цо': '措', 'дцо': '措', 'тцо': '措',
     'дсо': '措', 'тсо': '措', 'цсо': '措', 'цу': '楚', 'дцу': '楚', 'тцу': '楚', 'дсу': '楚', 'тсу': '楚', 'цсу': '楚',
     'цю': '秋', 'цью': '秋', 'дцю': '秋', 'дцью': '秋', 'тцю': '秋', 'тцью': '秋', 'дсю': '秋', 'дсью': '秋', 'тсю': '秋',
     'тсью': '秋', 'цсю': '秋', 'цсью': '秋', 'цай': '采', 'цаи': '采', 'дцай': '采', 'дцаи': '采', 'тцай': '采', 'тцаи': '采',
     'дсай': '采', 'дсаи': '采', 'тсай': '采', 'тсаи': '采', 'цсай': '采', 'цсаи': '采', 'цау': '曹', 'цао': '曹', 'дцау': '曹',
     'дцао': '曹', 'тцау': '曹', 'тцао': '曹', 'дсау': '曹', 'дсао': '曹', 'тсау': '曹', 'тсао': '曹', 'цсау': '曹',
     'цсао': '曹', 'цуй': '崔', 'дцуй': '崔', 'тцуй': '崔', 'дсуй': '崔', 'тсуй': '崔', 'цсуй': '崔', 'цан': '灿', 'цань': '灿',
     'дцан': '灿', 'дцань': '灿', 'тцан': '灿', 'тцань': '灿', 'дсан': '灿', 'дсань': '灿', 'тсан': '灿', 'тсань': '灿',
     'цсан': '灿', 'цсань': '灿', 'цен': '岑', 'цень': '岑', 'дцен': '岑', 'дцень': '岑', 'тцен': '岑', 'тцень': '岑',
     'дсен': '岑', 'дсень': '岑', 'тсен': '岑', 'тсень': '岑', 'цсен': '岑', 'цсень': '岑', 'цэн': '岑', 'цэнь': '岑',
     'цын': '岑', 'цынь': '岑', 'дцэн': '岑', 'дцэнь': '岑', 'дцын': '岑', 'дцынь': '岑', 'тцэн': '岑', 'тцэнь': '岑',
     'тцын': '岑', 'тцынь': '岑', 'дсэн': '岑', 'дсэнь': '岑', 'дсын': '岑', 'дсынь': '岑', 'тсэн': '岑', 'тсэнь': '岑',
     'тсын': '岑', 'тсынь': '岑', 'цсэн': '岑', 'цсэнь': '岑', 'цсын': '岑', 'цсынь': '岑', 'цин': '钦', 'цинь': '钦',
     'дцин': '钦', 'дцинь': '钦', 'тцин': '钦', 'тцинь': '钦', 'дсин': '钦', 'дсинь': '钦', 'тсин': '钦', 'тсинь': '钦',
     'цсин': '钦', 'цсинь': '钦', 'цон': '聪', 'цонь': '聪', 'дцон': '聪', 'дцонь': '聪', 'тцон': '聪', 'тцонь': '聪',
     'дсон': '聪', 'дсонь': '聪', 'тсон': '聪', 'тсонь': '聪', 'цсон': '聪', 'цсонь': '聪', 'цун': '聪', 'цунь': '聪',
     'дцун': '聪', 'дцунь': '聪', 'тцун': '聪', 'тцунь': '聪', 'дсун': '聪', 'дсунь': '聪', 'тсун': '聪', 'тсунь': '聪',
     'цсун': '聪', 'цсунь': '聪', 'цей': '采伊', 'дцей': '采伊', 'тцей': '采伊', 'дсей': '采伊', 'тсей': '采伊', 'цсей': '采伊',
     'цой': '措伊', 'дцой': '措伊', 'тцой': '措伊', 'дсой': '措伊', 'тсой': '措伊', 'цсой': '措伊', 'х': '赫', 'ха': '哈', 'хя': '希亚',
     'хэ': '海/黑', 'хэй': '海/黑', 'хе': '赫', 'хы': '黑', 'хый': '黑', 'хи': '希', 'хий': '希', 'хьи': '希', 'хь': '希',
     'хо': '霍', 'ху': '胡', 'хю': '休', 'хью': '休', 'хай': '海', 'хаи': '海', 'хау': '豪', 'хао': '豪', 'хуй': '惠',
     'хан': '汉', 'хань': '汉', 'хян': '希扬', 'хянь': '希扬', 'хен': '亨', 'хень': '亨', 'хэн': '亨', 'хэнь': '亨', 'хын': '亨',
     'хынь': '亨', 'хин': '欣', 'хинь': '欣', 'хон': '洪', 'хонь': '洪', 'хун': '洪', 'хунь': '洪', 'хей': '赫伊', 'хой': '霍伊',
     'м': '姆', 'ма': '马', 'мя': '米亚', 'мэ': '梅', 'мэй': '梅', 'ме': '梅', 'мы': '梅', 'мый': '梅', 'ми': '米', 'мий': '米',
     'мьи': '米', 'мь': '米', 'мо': '莫', 'мё': '苗', 'мйо': '苗', 'му': '穆', 'мю': '缪', 'мью': '缪', 'май': '迈', 'маи': '迈',
     'мау': '毛', 'мао': '毛', 'муй': '穆伊', 'ман': '曼', 'мань': '曼', 'мян': '米扬', 'мянь': '米扬', 'мен': '缅', 'мень': '缅',
     'мэн': '门', 'мэнь': '门', 'мын': '门', 'мынь': '门', 'мин': '明', 'минь': '明', 'мон': '蒙', 'монь': '蒙', 'мун': '蒙',
     'мунь': '蒙', 'мей': '梅伊', 'мой': '莫伊', 'н': '恩', 'на': '纳', 'ня': '尼亚', 'нэ': '内', 'нэй': '内', 'не': '涅',
     'ны': '内', 'ный': '内', 'ни': '尼', 'ний': '尼', 'ньи': '尼', 'нь': '尼', 'но': '诺', 'нё': '尼奥', 'нйо': '尼奥', 'ну': '努',
     'ню': '纽', 'нью': '纽', 'най': '奈', 'наи': '奈', 'нау': '瑙', 'нао': '瑙', 'нуй': '努伊', 'нан': '南', 'нань': '南',
     'нян': '尼扬', 'нянь': '尼扬', 'нен': '年', 'нень': '年', 'нэн': '嫩', 'нэнь': '嫩', 'нын': '嫩', 'нынь': '嫩', 'нин': '宁',
     'нинь': '宁', 'нон': '农', 'нонь': '农', 'нун': '农', 'нунь': '农', 'нюн': '纽恩', 'нюнь': '纽恩', 'ней': '涅伊', 'ной': '诺伊',
     'л': '尔', 'ла': '拉', 'ля': '利亚', 'лэ': '莱', 'лэй': '莱', 'ле': '列', 'лы': '雷', 'лый': '雷', 'ли': '利', 'лий': '利',
     'льи': '利', 'ль': '利', 'ло': '洛', 'лё': '廖', 'лйо': '廖', 'лу': '卢', 'лю': '柳', 'лью': '柳', 'лай': '莱', 'лаи': '莱',
     'лау': '劳', 'лао': '劳', 'луй': '卢伊', 'лан': '兰', 'лань': '兰', 'лян': '良', 'лянь': '良', 'лен': '连', 'лень': '连',
     'лэн': '伦', 'лэнь': '伦', 'лын': '伦', 'лынь': '伦', 'лин': '林', 'линь': '林', 'лон': '隆', 'лонь': '隆', 'лун': '伦',
     'лунь': '伦', 'лей': '列伊', 'лой': '洛伊', 'р': '尔', 'ра': '拉', 'ря': '里亚', 'рэ': '雷', 'рэй': '雷', 'ре': '列',
     'ры': '雷', 'рый': '雷', 'ри': '里', 'рий': '里', 'рьи': '里', 'рь': '里', 'ро': '罗', 'рё': '廖', 'рйо': '廖', 'ру': '鲁',
     'рю': '留', 'рью': '留', 'рай': '赖', 'раи': '赖', 'рау': '劳', 'рао': '劳', 'руй': '鲁伊', 'ран': '兰', 'рань': '兰',
     'рян': '良', 'рянь': '良', 'рен': '连', 'рень': '连', 'рэн': '伦', 'рэнь': '伦', 'рын': '伦', 'рынь': '伦', 'рин': '林',
     'ринь': '林', 'рон': '龙', 'ронь': '龙', 'рун': '伦', 'рунь': '伦', 'рей': '列伊', 'рой': '罗伊'}
    female={'а': '阿', 'я': '娅', 'э': '埃', 'эй': '埃', 'е': '耶', 'ы': '厄', 'ый': '厄', 'и': '伊', 'ий': '伊', 'ьи': '伊', 'ь': '伊',
     'о': '奥', 'ё': '约', 'йо': '约', 'у': '乌', 'ю': '尤', 'ью': '尤', 'ай': '艾', 'аи': '艾', 'ау': '奥', 'ао': '奥',
     'уй': '维', 'ан': '安', 'ань': '安', 'ян': '扬', 'янь': '扬', 'ен': '延', 'ень': '延', 'эн': '恩', 'энь': '恩', 'ын': '恩',
     'ынь': '恩', 'ин': '因', 'инь': '因', 'он': '翁', 'онь': '翁', 'ун': '温', 'унь': '温', 'юн': '云', 'юнь': '云', 'ей': '耶伊',
     'ой': '奥伊', 'б': '布', 'ба': '巴', 'бя': '比亚', 'бэ': '贝', 'бэй': '贝', 'бе': '别', 'бы': '贝', 'бый': '贝', 'би': '比',
     'бий': '比', 'бьи': '比', 'бь': '比', 'бо': '博', 'бё': '比奥', 'бйо': '比奥', 'бу': '布', 'бю': '比尤', 'бью': '比尤',
     'бай': '拜', 'баи': '拜', 'бау': '包', 'бао': '包', 'буй': '布伊', 'бан': '班', 'бань': '班', 'бян': '比扬', 'бянь': '比扬',
     'бен': '边', 'бень': '边', 'бэн': '本', 'бэнь': '本', 'бын': '本', 'бынь': '本', 'бин': '宾', 'бинь': '宾', 'бон': '邦',
     'бонь': '邦', 'бун': '本', 'бунь': '本', 'бей': '别伊', 'бой': '博伊', 'п': '普', 'па': '帕', 'пя': '皮亚', 'пэ': '佩',
     'пэй': '佩', 'пе': '佩', 'пы': '佩', 'пый': '佩', 'пи': '皮', 'пий': '皮', 'пьи': '皮', 'пь': '皮', 'по': '波', 'пё': '皮奥',
     'пйо': '皮奥', 'пу': '普', 'пю': '皮尤', 'пью': '皮尤', 'пай': '派', 'паи': '派', 'пау': '保', 'пао': '保', 'пуй': '普伊',
     'пан': '潘', 'пань': '潘', 'пян': '皮扬', 'пянь': '皮扬', 'пен': '片', 'пень': '片', 'пэн': '彭', 'пэнь': '彭', 'пын': '彭',
     'пынь': '彭', 'пин': '平', 'пинь': '平', 'пон': '蓬', 'понь': '蓬', 'пун': '蓬', 'пунь': '蓬', 'пей': '佩伊', 'пой': '波伊',
     'д': '德', 'да': '达', 'дя': '佳', 'дэ': '黛', 'дэй': '黛', 'де': '杰', 'ды': '德', 'дый': '德', 'ди': '季', 'дий': '季',
     'дьи': '季', 'дь': '季', 'до': '多', 'дё': '焦', 'дйо': '焦', 'ду': '杜', 'дю': '久', 'дью': '久', 'дай': '黛', 'даи': '黛',
     'дау': '道', 'дао': '道', 'дуй': '杜伊', 'дан': '丹', 'дань': '丹', 'дян': '姜', 'дянь': '姜', 'ден': '坚', 'день': '坚',
     'дэн': '登', 'дэнь': '登', 'дын': '登', 'дынь': '登', 'дин': '金', 'динь': '金', 'дон': '栋', 'донь': '栋', 'дун': '敦',
     'дунь': '敦', 'дей': '杰伊', 'дой': '多伊', 'т': '特', 'та': '塔', 'тя': '佳', 'тэ': '泰', 'тэй': '泰', 'те': '捷', 'ты': '特',
     'тый': '特', 'ти': '季', 'тий': '季', 'тьи': '季', 'ть': '季', 'то': '托', 'тё': '乔', 'тйо': '乔', 'ту': '图', 'тю': '秋',
     'тью': '秋', 'тай': '泰', 'таи': '泰', 'тау': '陶', 'тао': '陶', 'туй': '图伊', 'тан': '坦', 'тань': '坦', 'тян': '强',
     'тянь': '强', 'тен': '坚', 'тень': '坚', 'тэн': '滕', 'тэнь': '滕', 'тын': '滕', 'тынь': '滕', 'тин': '京', 'тинь': '京',
     'тон': '通', 'тонь': '通', 'тун': '通', 'тунь': '通', 'тюн': '琼', 'тюнь': '琼', 'тей': '捷伊', 'той': '托伊', 'г': '格',
     'га': '加', 'гя': '吉亚', 'гэ': '盖', 'гэй': '盖', 'ге': '格', 'гы': '格', 'гый': '格', 'ги': '吉', 'гий': '吉', 'гьи': '吉',
     'гь': '吉', 'го': '戈', 'гё': '吉奥', 'гйо': '吉奥', 'гу': '古', 'гю': '久', 'гью': '久', 'гай': '盖', 'гаи': '盖',
     'гау': '高', 'гао': '高', 'гуй': '圭', 'ган': '甘', 'гань': '甘', 'гян': '吉扬', 'гянь': '吉扬', 'ген': '根', 'гень': '根',
     'гэн': '根', 'гэнь': '根', 'гын': '根', 'гынь': '根', 'гин': '金', 'гинь': '金', 'гон': '贡', 'гонь': '贡', 'гун': '贡',
     'гунь': '贡', 'гей': '格伊', 'гой': '戈伊', 'к': '克', 'ка': '卡', 'кя': '基亚', 'кэ': '凯', 'кэй': '凯', 'ке': '克',
     'кы': '克', 'кый': '克', 'ки': '基', 'кий': '基', 'кьи': '基', 'кь': '基', 'ко': '科', 'кё': '基奥', 'кйо': '基奥', 'ку': '库',
     'кю': '丘', 'кью': '丘', 'кай': '凯', 'каи': '凯', 'кау': '考', 'као': '考', 'куй': '奎', 'кан': '坎', 'кань': '坎',
     'кян': '基扬', 'кянь': '基扬', 'кен': '肯', 'кень': '肯', 'кэн': '肯', 'кэнь': '肯', 'кын': '肯', 'кынь': '肯', 'кин': '金',
     'кинь': '金', 'кон': '孔', 'конь': '孔', 'кун': '昆', 'кунь': '昆', 'кей': '克伊', 'кой': '科伊', 'в': '夫', 'ва': '娃',
     'вя': '维亚', 'вэ': '韦', 'вэй': '韦', 'ве': '韦', 'вы': '维', 'вый': '维', 'ви': '维', 'вий': '维', 'вьи': '维', 'вь': '维',
     'во': '沃', 'вё': '维奥', 'вйо': '维奥', 'ву': '武', 'вю': '维尤', 'вью': '维尤', 'вай': '瓦伊', 'ваи': '瓦伊', 'вау': '沃',
     'вао': '沃', 'вуй': '维', 'ван': '万', 'вань': '万', 'вян': '维扬', 'вянь': '维扬', 'вен': '文', 'вень': '文', 'вэн': '文',
     'вэнь': '文', 'вын': '文', 'вынь': '文', 'вин': '温', 'винь': '温', 'вон': '翁', 'вонь': '翁', 'вун': '文', 'вунь': '文',
     'вей': '韦伊', 'вой': '沃伊', 'ф': '夫', 'фа': '法', 'фя': '菲亚', 'фэ': '费', 'фэй': '费', 'фе': '费', 'фы': '菲', 'фый': '菲',
     'фи': '菲', 'фий': '菲', 'фьи': '菲', 'фь': '菲', 'фо': '福', 'фё': '菲奥', 'фйо': '菲奥', 'фу': '富', 'фю': '菲尤',
     'фью': '菲尤', 'фай': '法伊', 'фаи': '法伊', 'фау': '福', 'фао': '福', 'фуй': '富伊', 'фан': '凡', 'фань': '凡', 'фен': '芬',
     'фень': '芬', 'фэн': '芬', 'фэнь': '芬', 'фын': '芬', 'фынь': '芬', 'фин': '芬', 'финь': '芬', 'фон': '丰', 'фонь': '丰',
     'фун': '丰', 'фунь': '丰', 'фей': '费伊', 'фой': '福伊', 'з': '兹', 'дз': '兹', 'за': '扎', 'дза': '扎', 'зя': '贾',
     'дзя': '贾', 'зэ': '泽', 'зэй': '泽', 'дзэ': '泽', 'дзэй': '泽', 'зе': '泽', 'дзе': '泽', 'зы': '济', 'зый': '济',
     'дзы': '济', 'дзый': '济', 'зи': '济', 'зий': '济', 'зьи': '济', 'зь': '济', 'дзи': '济', 'дзий': '济', 'дзьи': '济',
     'дзь': '济', 'зо': '佐', 'дзо': '佐', 'зё': '焦', 'зйо': '焦', 'дзё': '焦', 'дзйо': '焦', 'зу': '祖', 'дзу': '祖',
     'зю': '久', 'зью': '久', 'дзю': '久', 'дзью': '久', 'зай': '宰', 'заи': '宰', 'дзай': '宰', 'дзаи': '宰', 'зау': '藻',
     'зао': '藻', 'дзау': '藻', 'дзао': '藻', 'зуй': '祖伊', 'дзуй': '祖伊', 'зан': '赞', 'зань': '赞', 'дзан': '赞',
     'дзань': '赞', 'зян': '姜', 'зянь': '姜', 'дзян': '姜', 'дзянь': '姜', 'зен': '津', 'зень': '津', 'дзен': '津',
     'дзень': '津', 'зэн': '曾', 'зэнь': '曾', 'зын': '曾', 'зынь': '曾', 'дзэн': '曾', 'дзэнь': '曾', 'дзын': '曾',
     'дзынь': '曾', 'зин': '津', 'зинь': '津', 'дзин': '津', 'дзинь': '津', 'зон': '宗', 'зонь': '宗', 'дзон': '宗',
     'дзонь': '宗', 'зун': '尊', 'зунь': '尊', 'дзун': '尊', 'дзунь': '尊', 'зей': '泽伊', 'дзей': '泽伊', 'зой': '佐伊',
     'дзой': '佐伊', 'с': '斯', 'са': '萨', 'ся': '夏', 'сэ': '塞', 'сэй': '塞', 'се': '谢', 'сы': '瑟', 'сый': '瑟', 'си': '锡',
     'сий': '锡', 'сьи': '锡', 'сь': '锡', 'со': '索', 'сё': '肖', 'сйо': '肖', 'су': '苏', 'сю': '秀', 'сью': '秀', 'сай': '赛',
     'саи': '赛', 'сау': '绍', 'сао': '绍', 'суй': '绥', 'сан': '桑', 'сань': '桑', 'сян': '相', 'сянь': '相', 'сен': '先',
     'сень': '先', 'сэн': '森', 'сэнь': '森', 'сын': '森', 'сынь': '森', 'син': '辛', 'синь': '辛', 'сон': '松', 'сонь': '松',
     'сун': '孙', 'сунь': '孙', 'сюн': '雄', 'сюнь': '雄', 'сей': '谢伊', 'сой': '索伊', 'ж': '日', 'жа': '扎', 'жя': '扎',
     'жэ': '热', 'жэй': '热', 'же': '热', 'жы': '日', 'жый': '日', 'жи': '日', 'жий': '日', 'жьи': '日', 'жь': '日', 'жо': '若',
     'жё': '若', 'жйо': '若', 'жу': '茹', 'жю': '茹', 'жью': '茹', 'жай': '扎伊', 'жаи': '扎伊', 'жау': '饶', 'жао': '饶',
     'жуй': '瑞', 'жан': '然', 'жань': '然', 'жян': '让', 'жянь': '让', 'жен': '任', 'жень': '任', 'жэн': '任', 'жэнь': '任',
     'жын': '任', 'жынь': '任', 'жин': '任', 'жинь': '任', 'жон': '容', 'жонь': '容', 'жун': '容', 'жунь': '容', 'жей': '热伊',
     'жой': '若伊', 'ш': '什', 'ша': '莎', 'шя': '莎', 'шэ': '舍', 'шэй': '舍', 'ше': '舍', 'шы': '希', 'шый': '希', 'ши': '希',
     'ший': '希', 'шьи': '希', 'шь': '希', 'шо': '绍', 'шё': '绍', 'шйо': '绍', 'шу': '舒', 'шю': '舒', 'шью': '舒', 'шай': '沙伊',
     'шаи': '沙伊', 'шау': '绍', 'шао': '绍', 'шуй': '舒伊', 'шан': '尚', 'шань': '尚', 'шян': '尚', 'шянь': '尚', 'шен': '申',
     'шень': '申', 'шэн': '申', 'шэнь': '申', 'шын': '申', 'шынь': '申', 'шин': '申', 'шинь': '申', 'шон': '雄', 'шонь': '雄',
     'шун': '顺', 'шунь': '顺', 'шей': '舍伊', 'шой': '绍伊', 'дж': '季', 'джа': '贾', 'джэ': '杰', 'джэй': '杰', 'дже': '杰',
     'джы': '吉', 'джый': '吉', 'джи': '吉', 'джий': '吉', 'джьи': '吉', 'джь': '吉', 'джо': '焦', 'джё': '焦', 'джйо': '焦',
     'джу': '朱', 'джю': '久', 'джью': '久', 'джай': '贾伊', 'джаи': '贾伊', 'джау': '焦', 'джао': '焦', 'джуй': '朱伊',
     'джан': '占', 'джань': '占', 'джян': '姜', 'джянь': '姜', 'джен': '珍', 'джень': '珍', 'джэн': '珍', 'джэнь': '珍',
     'джын': '珍', 'джынь': '珍', 'джин': '金', 'джинь': '金', 'джон': '忠', 'джонь': '忠', 'джун': '准', 'джунь': '准',
     'джей': '杰伊', 'джой': '焦伊', 'ч': '奇', 'тч': '奇', 'дч': '奇', 'ча': '恰', 'тча': '恰', 'дча': '恰', 'чэ': '切',
     'чэй': '切', 'тчэ': '切', 'тчэй': '切', 'дчэ': '切', 'дчэй': '切', 'че': '切', 'тче': '切', 'дче': '切', 'чи': '奇',
     'чий': '奇', 'чьи': '奇', 'чь': '奇', 'тчи': '奇', 'тчий': '奇', 'тчьи': '奇', 'тчь': '奇', 'дчи': '奇', 'дчий': '奇',
     'дчьи': '奇', 'дчь': '奇', 'чо': '乔', 'тчо': '乔', 'дчо': '乔', 'чё': '乔', 'чйо': '乔', 'тчё': '乔', 'тчйо': '乔',
     'дчё': '乔', 'дчйо': '乔', 'чу': '丘', 'тчу': '丘', 'дчу': '丘', 'чай': '柴', 'чаи': '柴', 'тчай': '柴', 'тчаи': '柴',
     'дчай': '柴', 'дчаи': '柴', 'чау': '乔', 'чао': '乔', 'тчау': '乔', 'тчао': '乔', 'дчау': '乔', 'дчао': '乔', 'чуй': '崔',
     'тчуй': '崔', 'дчуй': '崔', 'чан': '昌', 'чань': '昌', 'тчан': '昌', 'тчань': '昌', 'дчан': '昌', 'дчань': '昌',
     'чян': '强', 'чянь': '强', 'тчян': '强', 'тчянь': '强', 'дчян': '强', 'дчянь': '强', 'чен': '琴', 'чень': '琴',
     'тчен': '琴', 'тчень': '琴', 'дчен': '琴', 'дчень': '琴', 'чэн': '琴', 'чэнь': '琴', 'чын': '琴', 'чынь': '琴',
     'тчэн': '琴', 'тчэнь': '琴', 'тчын': '琴', 'тчынь': '琴', 'дчэн': '琴', 'дчэнь': '琴', 'дчын': '琴', 'дчынь': '琴',
     'чин': '钦', 'чинь': '钦', 'тчин': '钦', 'тчинь': '钦', 'дчин': '钦', 'дчинь': '钦', 'чон': '琼', 'чонь': '琼',
     'тчон': '琼', 'тчонь': '琼', 'дчон': '琼', 'дчонь': '琼', 'чун': '春', 'чунь': '春', 'тчун': '春', 'тчунь': '春',
     'дчун': '春', 'дчунь': '春', 'чей': '切伊', 'тчей': '切伊', 'дчей': '切伊', 'чой': '乔伊', 'тчой': '乔伊', 'дчой': '乔伊',
     'щ': '希', 'сч': '希', 'ща': '夏', 'сча': '夏', 'ще': '谢', 'сче': '谢', 'щи': '希', 'щий': '希', 'щьи': '希', 'щь': '希',
     'счи': '希', 'счий': '希', 'счьи': '希', 'счь': '希', 'що': '晓', 'счо': '晓', 'щё': '晓', 'щйо': '晓', 'счё': '晓',
     'счйо': '晓', 'щу': '休', 'счу': '休', 'щю': '休', 'щью': '休', 'счю': '休', 'счью': '休', 'щай': '夏伊', 'щаи': '夏伊',
     'счай': '夏伊', 'счаи': '夏伊', 'щау': '肖', 'щао': '肖', 'счау': '肖', 'счао': '肖', 'щуй': '休伊', 'счуй': '休伊',
     'щан': '先', 'щань': '先', 'счан': '先', 'счань': '先', 'щен': '先', 'щень': '先', 'счен': '先', 'счень': '先', 'щэн': '欣',
     'щэнь': '欣', 'щын': '欣', 'щынь': '欣', 'счэн': '欣', 'счэнь': '欣', 'счын': '欣', 'счынь': '欣', 'щин': '辛',
     'щинь': '辛', 'счин': '辛', 'счинь': '辛', 'щон': '雄', 'щонь': '雄', 'счон': '雄', 'счонь': '雄', 'щун': '逊',
     'щунь': '逊', 'счун': '逊', 'счунь': '逊', 'щей': '谢伊', 'счей': '谢伊', 'щой': '晓伊', 'счой': '晓伊', 'ц': '茨', 'дц': '茨',
     'тц': '茨', 'дс': '茨', 'тс': '茨', 'цс': '茨', 'ца': '察', 'дца': '察', 'тца': '察', 'дса': '察', 'тса': '察', 'цса': '察',
     'ця': '齐亚', 'дця': '齐亚', 'тця': '齐亚', 'дся': '齐亚', 'тся': '齐亚', 'цся': '齐亚', 'цэ': '采', 'цэй': '采', 'дцэ': '采',
     'дцэй': '采', 'тцэ': '采', 'тцэй': '采', 'дсэ': '采', 'дсэй': '采', 'тсэ': '采', 'тсэй': '采', 'цсэ': '采', 'цсэй': '采',
     'це': '采', 'дце': '采', 'тце': '采', 'дсе': '采', 'тсе': '采', 'цсе': '采', 'цы': '齐', 'цый': '齐', 'дцы': '齐',
     'дцый': '齐', 'тцы': '齐', 'тцый': '齐', 'дсы': '齐', 'дсый': '齐', 'тсы': '齐', 'тсый': '齐', 'цсы': '齐', 'цсый': '齐',
     'ци': '齐', 'ций': '齐', 'цьи': '齐', 'ць': '齐', 'дци': '齐', 'дций': '齐', 'дцьи': '齐', 'дць': '齐', 'тци': '齐',
     'тций': '齐', 'тцьи': '齐', 'тць': '齐', 'дси': '齐', 'дсий': '齐', 'дсьи': '齐', 'дсь': '齐', 'тси': '齐', 'тсий': '齐',
     'тсьи': '齐', 'тсь': '齐', 'цси': '齐', 'цсий': '齐', 'цсьи': '齐', 'цсь': '齐', 'цо': '措', 'дцо': '措', 'тцо': '措',
     'дсо': '措', 'тсо': '措', 'цсо': '措', 'цу': '楚', 'дцу': '楚', 'тцу': '楚', 'дсу': '楚', 'тсу': '楚', 'цсу': '楚',
     'цю': '秋', 'цью': '秋', 'дцю': '秋', 'дцью': '秋', 'тцю': '秋', 'тцью': '秋', 'дсю': '秋', 'дсью': '秋', 'тсю': '秋',
     'тсью': '秋', 'цсю': '秋', 'цсью': '秋', 'цай': '采', 'цаи': '采', 'дцай': '采', 'дцаи': '采', 'тцай': '采', 'тцаи': '采',
     'дсай': '采', 'дсаи': '采', 'тсай': '采', 'тсаи': '采', 'цсай': '采', 'цсаи': '采', 'цау': '曹', 'цао': '曹', 'дцау': '曹',
     'дцао': '曹', 'тцау': '曹', 'тцао': '曹', 'дсау': '曹', 'дсао': '曹', 'тсау': '曹', 'тсао': '曹', 'цсау': '曹',
     'цсао': '曹', 'цуй': '崔', 'дцуй': '崔', 'тцуй': '崔', 'дсуй': '崔', 'тсуй': '崔', 'цсуй': '崔', 'цан': '灿', 'цань': '灿',
     'дцан': '灿', 'дцань': '灿', 'тцан': '灿', 'тцань': '灿', 'дсан': '灿', 'дсань': '灿', 'тсан': '灿', 'тсань': '灿',
     'цсан': '灿', 'цсань': '灿', 'цен': '岑', 'цень': '岑', 'дцен': '岑', 'дцень': '岑', 'тцен': '岑', 'тцень': '岑',
     'дсен': '岑', 'дсень': '岑', 'тсен': '岑', 'тсень': '岑', 'цсен': '岑', 'цсень': '岑', 'цэн': '岑', 'цэнь': '岑',
     'цын': '岑', 'цынь': '岑', 'дцэн': '岑', 'дцэнь': '岑', 'дцын': '岑', 'дцынь': '岑', 'тцэн': '岑', 'тцэнь': '岑',
     'тцын': '岑', 'тцынь': '岑', 'дсэн': '岑', 'дсэнь': '岑', 'дсын': '岑', 'дсынь': '岑', 'тсэн': '岑', 'тсэнь': '岑',
     'тсын': '岑', 'тсынь': '岑', 'цсэн': '岑', 'цсэнь': '岑', 'цсын': '岑', 'цсынь': '岑', 'цин': '钦', 'цинь': '钦',
     'дцин': '钦', 'дцинь': '钦', 'тцин': '钦', 'тцинь': '钦', 'дсин': '钦', 'дсинь': '钦', 'тсин': '钦', 'тсинь': '钦',
     'цсин': '钦', 'цсинь': '钦', 'цон': '聪', 'цонь': '聪', 'дцон': '聪', 'дцонь': '聪', 'тцон': '聪', 'тцонь': '聪',
     'дсон': '聪', 'дсонь': '聪', 'тсон': '聪', 'тсонь': '聪', 'цсон': '聪', 'цсонь': '聪', 'цун': '聪', 'цунь': '聪',
     'дцун': '聪', 'дцунь': '聪', 'тцун': '聪', 'тцунь': '聪', 'дсун': '聪', 'дсунь': '聪', 'тсун': '聪', 'тсунь': '聪',
     'цсун': '聪', 'цсунь': '聪', 'цей': '采伊', 'дцей': '采伊', 'тцей': '采伊', 'дсей': '采伊', 'тсей': '采伊', 'цсей': '采伊',
     'цой': '措伊', 'дцой': '措伊', 'тцой': '措伊', 'дсой': '措伊', 'тсой': '措伊', 'цсой': '措伊', 'х': '赫', 'ха': '哈', 'хя': '希亚',
     'хэ': '海/黑', 'хэй': '海/黑', 'хе': '赫', 'хы': '黑', 'хый': '黑', 'хи': '希', 'хий': '希', 'хьи': '希', 'хь': '希',
     'хо': '霍', 'ху': '胡', 'хю': '休', 'хью': '休', 'хай': '亥', 'хаи': '亥', 'хау': '豪', 'хао': '豪', 'хуй': '惠',
     'хан': '汉', 'хань': '汉', 'хян': '希扬', 'хянь': '希扬', 'хен': '亨', 'хень': '亨', 'хэн': '亨', 'хэнь': '亨', 'хын': '亨',
     'хынь': '亨', 'хин': '欣', 'хинь': '欣', 'хон': '洪', 'хонь': '洪', 'хун': '洪', 'хунь': '洪', 'хей': '赫伊', 'хой': '霍伊',
     'м': '姆', 'ма': '玛', 'мя': '米亚', 'мэ': '梅', 'мэй': '梅', 'ме': '梅', 'мы': '梅', 'мый': '梅', 'ми': '米', 'мий': '米',
     'мьи': '米', 'мь': '米', 'мо': '莫', 'мё': '苗', 'мйо': '苗', 'му': '穆', 'мю': '缪', 'мью': '缪', 'май': '迈', 'маи': '迈',
     'мау': '毛', 'мао': '毛', 'муй': '穆伊', 'ман': '曼', 'мань': '曼', 'мян': '米扬', 'мянь': '米扬', 'мен': '缅', 'мень': '缅',
     'мэн': '门', 'мэнь': '门', 'мын': '门', 'мынь': '门', 'мин': '明', 'минь': '明', 'мон': '蒙', 'монь': '蒙', 'мун': '蒙',
     'мунь': '蒙', 'мей': '梅伊', 'мой': '莫伊', 'н': '恩', 'на': '娜', 'ня': '尼亚', 'нэ': '内', 'нэй': '内', 'не': '涅',
     'ны': '内', 'ный': '内', 'ни': '妮', 'ний': '妮', 'ньи': '妮', 'нь': '妮', 'но': '诺', 'нё': '尼奥', 'нйо': '尼奥', 'ну': '努',
     'ню': '纽', 'нью': '纽', 'най': '奈', 'наи': '奈', 'нау': '瑙', 'нао': '瑙', 'нуй': '努伊', 'нан': '楠', 'нань': '楠',
     'нян': '尼扬', 'нянь': '尼扬', 'нен': '年', 'нень': '年', 'нэн': '嫩', 'нэнь': '嫩', 'нын': '嫩', 'нынь': '嫩', 'нин': '宁',
     'нинь': '宁', 'нон': '农', 'нонь': '农', 'нун': '农', 'нунь': '农', 'нюн': '纽恩', 'нюнь': '纽恩', 'ней': '涅伊', 'ной': '诺伊',
     'л': '尔', 'ла': '拉', 'ля': '利亚', 'лэ': '莱', 'лэй': '莱', 'ле': '列', 'лы': '蕾', 'лый': '蕾', 'ли': '莉', 'лий': '莉',
     'льи': '莉', 'ль': '莉', 'ло': '洛', 'лё': '廖', 'лйо': '廖', 'лу': '卢', 'лю': '柳', 'лью': '柳', 'лай': '莱', 'лаи': '莱',
     'лау': '劳', 'лао': '劳', 'луй': '卢伊', 'лан': '兰', 'лань': '兰', 'лян': '良', 'лянь': '良', 'лен': '连', 'лень': '连',
     'лэн': '伦', 'лэнь': '伦', 'лын': '伦', 'лынь': '伦', 'лин': '琳', 'линь': '琳', 'лон': '隆', 'лонь': '隆', 'лун': '伦',
     'лунь': '伦', 'лей': '列伊', 'лой': '洛伊', 'р': '尔', 'ра': '拉', 'ря': '里亚', 'рэ': '蕾', 'рэй': '蕾', 'ре': '列',
     'ры': '蕾', 'рый': '蕾', 'ри': '丽', 'рий': '丽', 'рьи': '丽', 'рь': '丽', 'ро': '萝', 'рё': '廖', 'рйо': '廖', 'ру': '鲁',
     'рю': '留', 'рью': '留', 'рай': '赖', 'раи': '赖', 'рау': '劳', 'рао': '劳', 'руй': '鲁伊', 'ран': '兰', 'рань': '兰',
     'рян': '良', 'рянь': '良', 'рен': '连', 'рень': '连', 'рэн': '伦', 'рэнь': '伦', 'рын': '伦', 'рынь': '伦', 'рин': '琳',
     'ринь': '琳', 'рон': '龙', 'ронь': '龙', 'рун': '伦', 'рунь': '伦', 'рей': '列伊', 'рой': '萝伊'}
    first={'е':'叶','ей':'叶伊','в':'弗','ф':'弗','л':'勒','р':'勒'}
    #
    while True:
        try:
            example=check_and_replace(input('输入俄语姓氏：').lower())
            ex2=get_ex(example,3)
            ex1=list(set(get_ex(example,3)+get_ex(example,2)))
            index=dict(sorted(list(set(get_index(example,3)[0]+get_index(example,2,ex2)[0]+get_index(example,1,ex1)[0]))))
            seg=concat_syl(index)

            result=[]
            for k,v in seg.items():
                if k==0 and v in first.keys():
                    v=first[v]
                    result.append((k,v))
                else:
                    if example[len(example)-1] == 'а':
                        v=female[v]
                        result.append((k,v))
                    elif example[len(example)-1] == 'я':
                        v=female[v]
                        result.append((k,v))
                    else:
                        v = male[v]
                        result.append((k, v))
            end=''.join(dict(result).values())
            print(end)
        except Exception as e:
            print('Error:',e)


