from datetime import datetime
from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
from dateutil.tz import gettz
from django.apps import AppConfig as DjangoAppConfig

from edc_appointment.appointment_config import AppointmentConfig
from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
from edc_appointment.constants import COMPLETE_APPT
from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_constants.constants import FAILED_ELIGIBILITY
from edc_data_manager.apps import AppConfig as BaseEdcDataManagerAppConfig
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
from edc_locator.apps import AppConfig as BaseEdcLocatorAppConfig
from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig
from edc_timepoint.apps import AppConfig as BaseEdcTimepointAppConfig
from edc_timepoint.timepoint import Timepoint
from edc_timepoint.timepoint_collection import TimepointCollection
from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT, \
    COMPLETED_PROTOCOL_VISIT, MISSED_VISIT

from training_dashboard.patterns import subject_identifier


class AppConfig(DjangoAppConfig):
    name = 'training'


class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
    configurations = [
        AppointmentConfig(
            model='edc_appointment.appointment',
            related_visit_model='training_subject.subjectvisit',
            appt_type='clinic'),
    ]


class EdcDataManagerAppConfig(BaseEdcDataManagerAppConfig):
    identifier_pattern = subject_identifier
    extra_assignee_choices = {}


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'Training Project'
    institution = 'Botswana-Harvard AIDS Institute'


class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
    report_datetime_allowance = -1
    visit_models = {
        'training_subject': ('subject_visit', 'training_subject.subjectvisit'), }


class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
    country = 'botswana'
    definitions = {
        'Clinic 1': dict(days=[MO, TU, WE, TH, FR, SA, SU],
                         slots=[100, 100, 100, 100, 100, 100, 100]),
    }


class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
    protocol = 'Training'
    protocol_name = 'Training - 123'
    protocol_number = '12'
    protocol_title = ''
    study_open_datetime = datetime(
        2021, 1, 1, 0, 0, 0, tzinfo=gettz('UTC'))
    study_close_datetime = datetime(
        2025, 12, 1, 0, 0, 0, tzinfo=gettz('UTC'))


class EdcTimepointAppConfig(BaseEdcTimepointAppConfig):
    timepoints = TimepointCollection(
        timepoints=[
            Timepoint(
                model='edc_appointment.appointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status=COMPLETE_APPT),
            Timepoint(
                model='edc_appointment.historicalappointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status=COMPLETE_APPT), ])


class EdcLocatorAppConfig(BaseEdcLocatorAppConfig):
    name = 'edc_locator'
    reference_model = 'training_subject.personalcontactinfo'


class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
    reason_field = {
        'training_subject.subjectvisit': 'reason'}
    create_on_reasons = [SCHEDULED, UNSCHEDULED, COMPLETED_PROTOCOL_VISIT]
    delete_on_reasons = [LOST_VISIT, MISSED_VISIT, FAILED_ELIGIBILITY]
