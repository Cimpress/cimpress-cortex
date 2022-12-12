# cimpress-cortex
This project contains the gitlab-template which will add the cortex template in the repos, where the template is included.

[![image](https://user-images.githubusercontent.com/52998940/206983465-2f478591-4ab2-4fc4-b301-0474be80b56d.png)](https://www.cortex.io/)

## Add the template to pipeline.

To add the template, you need to include the template in your repository

```sh
include:
  remote: 'https://github.com/Cimpress/cimpress-cortex/raw/main/gitlab-ci-templates/replace-cortex.yml'
```

Add the stage to execute the template in your repository

```sh
copy_cortex:
  variables:
    DOMAIN: <YourDomain>
    SERVICE_NAME: <NAME_OF_THE_SERVICE>
    CI_JOB_TOKEN: <YOUR_GITLAB_TOKEN>
    SERVICE_REPO: <SERVICE_REPO>
    GITLAB_URL: <GITLAB_REPO>
    APPLICATION_ID: <NEWRELIC_APPLICATION_ID>
    DOCUMENT_URL: <CONFLUENCE_DOC_URL>
    SWAGGER_URL: <SWAGGER_URL>
    PAGERDUTY_ID: <PAGER_SERVICE_ID>
    NEWRELIC_URL: <NEWRELIC_DASHBOARD_URL>
    ORG_ID: <SNYK_ORG_ID>
    PROJECT_ID: <SNYK_PROJECT_ID>
  stage: replace_cortex
  extends: .cortex
```

This will add the cortex.yml in your repository with the variables passed as a ENV variables. Create an MR with master branch.
Voila! Once merged the changes, you should be able to see your service in cortex.
