from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
class FundCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class FundType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class FundEligibility(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class FundProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    matches = models.ManyToManyField("Fund", related_name="profiles", through="Recommendation")
    location = models.CharField(max_length=255, help_text=_("Your geographic scope"))
    objectives = models.TextField(help_text=_("Your mission and goals"))
    fund_type = models.ForeignKey(FundType, on_delete=models.PROTECT)
    fund_category = models.ForeignKey(FundCategory, on_delete=models.PROTECT)
    eligibility = models.ForeignKey(FundEligibility, on_delete=models.PROTECT)
    estimated_budget = models.DecimalField(max_digits=15, decimal_places=2)
    background = models.TextField(help_text=_("Little about your history"))
    project_summary = models.TextField(help_text=_("Describe the problem to be solved"))
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, unique=True)
    
    def __str__(self):
        return str(self.title)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Fund(models.Model):
    title = models.CharField(max_length=255)
    agency_name = models.CharField(max_length=255)
    opportunity_no = models.CharField(max_length=15, unique=True)
    fund_type = models.ForeignKey(FundType, on_delete=models.PROTECT)
    eligibility = models.ForeignKey(FundEligibility, on_delete=models.PROTECT, related_name="funds")
    fund_category = models.ForeignKey(FundCategory, on_delete=models.PROTECT)
    expected_award_no = models.IntegerField()
    eligibility_info = models.TextField()
    description = models.TextField()
    url = models.URLField()
    estimated_total_funding = models.DecimalField(max_digits=15, decimal_places=2)
    posted_date = models.DateField()
    last_updated_date = models.DateField()
    closing_date = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title)


class Recommendation(models.Model):
    profile = models.ForeignKey(FundProfile, on_delete=models.CASCADE)
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["profile", "fund"],
                name="unique_profile_fund",
            ),
        ]