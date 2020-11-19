from django.db import models
from django.conf import settings
# Create your models here.

class funddetails:
    s : int
    IHHL_fund_id : int
    Sanctioned_IHHL : int
    Estimated_Cost : int
    Funds_from_ngo : int
class revenuedetails:
    s : int
    billid : int
    amount : int

class villages:
    villageid : int
    villagename : str
    districtname : str
    

