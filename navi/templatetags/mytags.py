from django import template
from navi.models import Samples, Client, elementsName, Corms

register = template.Library()


@register.filter(name='validDate')
def validDate(text):
    if int(text) < 10:
        text = '0' + str(text)
        return text
    else:
        return text


@register.filter(name='percent')
def percent(count, arg):
    if arg != 0:
        return str(round((count / arg) * 100, 1)) + '%'
    else:
        return 0


@register.filter(name='count')
def percent(forloop, arg):
    return int(forloop) + 20 * (int(arg) - 1)

@register.filter(name='ostatok')
def ostatok(count, pk):
    c = Client.objects.get(pk=pk)
    s = Samples.objects.filter(client = c)
    for i in s:
        count -= i.count
    return count

@register.filter(name='elName')
def ostatok(elements):
    return len(elements)


@register.filter(name='stSample')
def stSample(model,id):
    s = model.filter(samples__id=id).filter(status="Готово")
    zero = []
    counter = 0
    for i in s:
        counter+=i.countSamples
    return counter


@register.filter(name='stSample')
def stSample(model,id):
    s = model.filter(samples__id=id).filter(status="Готово")
    counter = 0
    for i in s:
        counter+=i.countSamples
    return counter

@register.filter(name="stSamples")
def stSamples(model,id):
    s = model.filter(samples__id=id).filter(status="Готово")
    zero = []
    for i in s:
        zero.append(i)
    return zero

def jsn(data):
    b = 0
    if type(data) != int:
        for element in data:
            print(element)
            if type(data[element]) == list:
                if len(data) == 0:
                    b += 1
                else:
                    b += len(data)
            elif type(data) == dict and data[element] == {}:
                b += 1
            print(" ------ ", data)
            try:
                b += jsn(data[element])
            except:
                pass
    return b
@register.filter(name="jsonFormat")
def jsonFormat(data):
    return jsn(data)

@register.filter(name='retDic')
def retDic(dic, arg):
    return dic[arg]

@register.filter(name="minus")
def minus(n1,n2):
    return int(n1)-int(n2)


@register.filter(name="retList")
def retList(list):
    return list[1]

@register.filter(name="retTime")
def retList(list):
    return list[2]

@register.filter(name="isZero")
def isZero(number):
    if number == 0:
        return '---'
    return number
@register.filter(name="childElements")
def childElements(list, number):
    for i in list:
        print(i)
    return None

@register.filter(name="limitMax")
def limitMax(number,ids):
    for i in ids:
        number-=i.countSamples
    return number


@register.filter(name="limitSel")
def limitSel(number,ids):
    for i in ids:
        number-=i.countSamples
    return number


@register.filter(name="sampleSelection")
def sampleSelection(sample):
    number = sample.count
    for i in sample.selection.filter(status="Готово"):
        number-=i.countSamples
    return number

@register.filter(name="sampleAgrohym")
def sampleAgrohym(sample):
    number = sample.count
    for i in sample.agrohym.filter(status="Готово"):
        number-=i.countSamples
    return number


@register.filter(name="childDate")
def childDate(pk):
    corm = Corms.objects.get(pk=pk)
    try:
        c = corm.children
        return c.date
    except:
        return "<span style='color:gray;'>В процессе</span>"

@register.filter(name="childNot")
def childNot(j):
    try:
        c = j.children
        return False
    except:
        return True