CREATE table projects(
    id integer not null primary key,
    name text,
    version text,
    author text,
    author_email text,
    home_page text,
    license text,
    maintainer text,
    maintainer_email text,
    package_url text,
    platform text,
    project_url text,
    requires_python text,
    summary text,
    yanked int,
    yanked_reason text,
    classifiers text,
    requires_dist text,
    UNIQUE(name, version)
);

CREATE table urls(
    project_id int,
    url text,
    upload_time text,
    package_type text,
    python_version text,
    requires_python text,
    size int,
    yanked int,
    yanked_reason text,
    foreign key(project_id) REFERENCES projects(id)
);
