# calculator.py
# مشروع آلة حاسبة
# الطالبة: امنية

def add(a, b):
    """
    دالة الجمع
    ترجع مجموع رقمين
    """
    return a + b


def subtract(a, b):
    """
    دالة الطرح
    ترجع الفرق بين رقمين
    """
    return a - b


def multiply(a, b):
    """
    دالة الضرب
    ترجع حاصل ضرب رقمين
    """
    return a * b


def divide(a, b):
    """
    دالة القسمة
    ترجع ناتج القسمة
    مع التحقق من القسمة على صفر
    """
    if b == 0:
        return "خطأ: لا يمكن القسمة على صفر"
    return a / b
