# PyPi Data

The contents of the PyPi JSON API for all packages, updated every 12 hours

## Why?

Fetching bulk data from the PyPi API in bulk is non-trivial, and using the [BigQuery dataset](https://warehouse.pypa.io/api-reference/bigquery-datasets.html) requires using BigQuery. The entire package dataset is not large and easily fits into the memory of most developer machines, so it's much more fluid to explore the data with Pandas than the heavyweight (and sometimes expensive) BigQuery.

## Release data

### Via sqlite database

Every day the contents of this repository is bundled into a sqlite database and added as a [Github Release](https://github.com/pypi-data/pypi-json-data/releases). The schema can 
be found [in schema.sql](./scripts/schema.sql) and contains release + download data, without classifiers or readme information. An example:

```sql
select projects.name, sum(urls.size) as size
from projects
join urls on urls.project_id = projects.id
group by 1
order by size DESC
LIMIT 10
```

### Via git checkout

Each package has a unique directory within [release_data/](release_data/), prefixed with the first two
*lowercased* characters of the package name. Each package has a unique JSON file containing the full API response for *all package releases* within it. 

For example: [release_data/d/j/django.json](release_data/d/j/django.json) contains:

```json
{
    "1.0.1": {
        "info": {
            "author": "Django Software Foundation",
            "author_email": "foundation at djangoproject com",
            "bugtrack_url": null,
            "classifiers": [
                "Development Status :: 5 - Production/Stable",
                "Environment :: Web Environment",
                "Framework :: Django",
                "Intended Audience :: Developers",
                "License :: OSI Approved :: BSD License",
                "Operating System :: OS Independent",
                "Programming Language :: Python",
                "Topic :: Internet :: WWW/HTTP",
                "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
                "Topic :: Internet :: WWW/HTTP :: WSGI",
                "Topic :: Software Development :: Libraries :: Application Frameworks",
                "Topic :: Software Development :: Libraries :: Python Modules"
            ],
            "description": "UNKNOWN",
            "description_content_type": null,
            "docs_url": null,
            "download_url": "http://www.djangoproject.com/m/bad-installer.txt",
            "downloads": {
                "last_day": -1,
                "last_month": -1,
                "last_week": -1
            },
            "home_page": "http://www.djangoproject.com/",
            ... and other keys
```

