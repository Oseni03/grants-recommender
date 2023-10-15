from celery import shared_task

from .models import FundProfile, Fund
from .utils import get_summary

template = """
You are a professional grant writer with years of experience. 
Given the text below, generate a concise summary of the text which can be used to determine grant opportunity match for the specific user without leaving out any detail.

{text}

CONCISE SUMMARY:"""


@shared_task
def get_fund_summary(fund_id, texts):
    instance = Fund.objects.get(id=fund_id)
    output = get_summary(template, texts)
    
    print(output)
    
    instance.summary = output
    instance.save()


@shared_task
def get_profile_summary(profile_id, texts):
    instance = FundProfile.objects.get(id=profile_id)
    output = get_summary(template, texts)
    
    print(output)
    
    instance.summary = output
    instance.save()