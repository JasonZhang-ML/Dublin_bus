from scrapy.exporters import CsvItemExporter
from scrapy.utils.project import get_project_settings
 

class WeatherCsvExporter(CsvItemExporter):
 
    def __init__(self, *args, **kwargs):
        # delimiter = get_project_settings().get('CSV_DELIMITER', ',')
        # kwargs['delimiter'] = delimiter
 
        fields_to_export = get_project_settings().get('FIELDS_TO_EXPORT', [])
        if fields_to_export:
            kwargs['fields_to_export'] = fields_to_export
 
        super(WeatherCsvExporter, self).__init__(*args, **kwargs)