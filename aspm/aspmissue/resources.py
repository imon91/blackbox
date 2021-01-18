from import_export import resources
from aspmissue.models import ModelName, IssueAnalysis, Supplier, Software, IssueSummary


class PhoneResource(resources.ModelResources):
    class Meta:
        model = ModelName


class IssueAnalysisModelResource(resources.ModelResources):
    class Meta:
        model = IssueAnalysis
        fields = ('model_modelname', 'issue_name', 'imei', 'qc_findings', 'root_cause', 'evidence', 'posted_on', )