from django.contrib import admin
# Register your models here.
from import_export.admin import ImportExportModelAdmin

from aspmissue.models import ModelName, IssueAnalysis, Supplier, Software, IssueSummary, SoftwareType, ModelType, \
    MajorIssue


class SoftwareAdmin(ImportExportModelAdmin):  # FOR ADMIN IMPORT EXPORT ONLY
    pass


class modelnameModel(ImportExportModelAdmin):
    list_display = ('modelname', 'modeldescription')
    search_fields = ('modelname', 'modeldescription')

    class Meta:
        Model = ModelName


class IssueAnalysisModel(ImportExportModelAdmin):
    list_display = ['model', 'issue_name', 'imei', 'qc_findings', 'root_cause', 'evidence', 'posted_on', ]
    search_fields = ('issue_name', 'imei', 'qc_findings', 'evidence', 'model__modelname')

    class Meta:
        Model = IssueAnalysis


class IssueSummaryModel(ImportExportModelAdmin):
    list_display = ['model', 'software', 'total_issue', 'expected_software_date',
                    'actual_software_date', 'feedback_expected_date', 'feedback_actual_date', 'new_issue',
                    'reopen_issue','issue_clsoed_by_pm' ,'is_mp','supplier_can_not_fixed' ,'delay', 'get_software_by_pm', 'delay_software_by_qc']

    # readonly_fields = ('get_software_by_pm',)

    def get_software_by_pm(self, obj):
        if obj.expected_software_date is not None:
            return obj.actual_software_date - obj.expected_software_date
        elif obj.expected_software_date is None:
            return obj.feedback_actual_date - obj.actual_software_date

    def delay_software_by_qc(self, obj):
        if obj.feedback_expected_date is not None:
            return obj.feedback_actual_date - obj.feedback_expected_date

    class Meta:
        Model = IssueSummary


admin.site.register(SoftwareType)
admin.site.register(ModelType)

admin.site.register(ModelName, modelnameModel)
admin.site.register(IssueAnalysis, IssueAnalysisModel)
admin.site.register(Supplier, SoftwareAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(MajorIssue)
admin.site.register(IssueSummary, IssueSummaryModel)
