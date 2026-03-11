from pages.dashboard_page import DashboardPage
import pytest


@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_displaying(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    dashboard_page_with_state.navbar.check_visible('username')
    dashboard_page_with_state.check_dashboard_title_visible()
    dashboard_page_with_state.check_scores_chart_visible()
    dashboard_page_with_state.check_courses_chart_visible()
    dashboard_page_with_state.check_student_chart_visible()
    dashboard_page_with_state.check_activities_chart_visible()
