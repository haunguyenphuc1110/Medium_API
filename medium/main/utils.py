from .serializers import *
from django.db.models import Sum


def get_product_from_cate3_new(inputID):
    tempSet = CateProduct.objects.filter(cate3_id_new=inputID).all()
    return list(map(lambda x: x.product_id, tempSet))


def getAllProduct_fromListCate3(inputID_list):
    returnArr = []
    for i in inputID_list:
        returnArr += get_product_from_cate3_new(i)
    return returnArr


def getTotalValueCount_fromListCate3(inputID_list):
    totalValueCount = 0

    for i in inputID_list:
        prod_list = get_product_from_cate3_new(i)
        addValue = Products.objects.filter(pk__in=prod_list, status=200).aggregate(
            Sum("value_count")
        )["value_count__sum"]

        totalValueCount += addValue if addValue else 0
    return totalValueCount
