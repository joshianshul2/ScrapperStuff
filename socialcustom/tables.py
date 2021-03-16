# tutorial/tables.py
import django_tables2 as tables
from .models import User,PropertyMaster

# ATTRIBUTES = {
#     "th" : {
#         "_ordering": {
#             "orderable": "sortable", # Instead of `orderable`
#             "ascending": "ascend",   # Instead of `asc`
#             "descending": "descend",  # Instead of `desc`
#             "border " : "3",
#         }
#     }
# }
#
# class PersonTable(tables.Table):
#     class Meta:
#         model = User
#         # template_name = "django_tables2/.html"
#         # fields = ("email", )
#         email = tables.Column(attrs=ATTRIBUTES)
#
# table = tables.Table(queryset, attrs=ATTRIBUTES)

# or

class simple_list(tables.Table):
    # name = tables.Column(attrs=ATTRIBUTES)

    class Meta:
        model = PropertyMaster
        template_name = "django_tables2/semantic.html"
        # email = tables.Column(attrs=ATTRIBUTES)
        fields = ("acres","rate" )


# class PersonTable(tables.Table):
#     class Meta:
#         model = User
#         template_name = "django_tables2/semantic.html"
#         fields = ("first_name","email" )
#
#

#
# class SimpleTable(tables.Table):
#     class Meta:
#         model = Simple
#
#
# class SimpleTable(tables.Table):
#      id = tables.Column(attrs={"td": {"class": "my-class"}})
#      age = tables.Column(attrs={"tf": {"bgcolor": "red"}})

# table = SimpleTable(data,template_name="django_tables2/bootstrap-responsive.html")
class SomeTable(tables.Table):

    class Meta:
        model= PropertyMaster
        attrs = {"class": "pinned-row","table" : "border"}
        fields = ("accountId","address","city","state","zip","country","netprice","area", "Rate","Url")

