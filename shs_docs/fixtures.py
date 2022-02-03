#  Si Hay Sistema and Contributors 2021

from __future__ import unicode_literals
from . import __version__ as app_version


def fill_fixtures():
    # We declare fixtures as an empty list.
    fixtures_fillup = []

    wiki_page = {
        "dt": "Wiki Page"
    }

    wiki_settings = {
        "dt": "Wiki Sidebar"
    }

    wiki_sidebar = {
        "dt": "Wiki Settings"
    }

    wiki_revision = {
        "dt": "Wiki Page Revision"
    }

    fixtures_fillup.append(wiki_page)
    fixtures_fillup.append(wiki_settings)
    fixtures_fillup.append(wiki_sidebar)
    fixtures_fillup.append(wiki_revision)

    return fixtures_fillup

