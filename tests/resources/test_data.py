def otaps_valuestream_with_only_same_name_otap():
    return {"items": [
        {
            "apiVersion": "project.openshift.io/v1",
            "kind": "Project",
            "metadata": {
                "labels": {
                    "app.kubernetes.io/instance": "generic-all-cluster",
                    "heritage": "argo",
                    "name": "grootverbruik-ops",
                    "ops.alliander.com/schedule-down": "false",
                    "project": "grootverbruik",
                    "type": "project",
                    "valuestream": "grootverbruik"
                },
                "name": "grootverbruik-ops",
            }
        }
    ]}


def otaps_single_valuestream():
    return {"items": [
        {
            "apiVersion": "project.openshift.io/v1",
            "kind": "Project",
            "metadata": {
                "labels": {
                    "app.kubernetes.io/instance": "generic-all-cluster",
                    "heritage": "argo",
                    "name": "grootverbruik-ops",
                    "ops.alliander.com/schedule-down": "false",
                    "project": "grootverbruik",
                    "type": "project",
                    "valuestream": "grootverbruik"
                },
                "name": "grootverbruik-ops-tst",
                "resourceVersion": "45473378",
                "selfLink": "/apis/project.openshift.io/v1/projects/security-team-a-tst",
                "uid": "775020e4-81dd-11e9-a287-0050568ab8da"
            }
        },
        {
            "apiVersion": "project.openshift.io/v1",
            "kind": "Project",
            "metadata": {
                "labels": {
                    "app.kubernetes.io/instance": "generic-all-cluster",
                    "heritage": "argo",
                    "name": "grootverbruik-ops",
                    "ops.alliander.com/schedule-down": "false",
                    "project": "grootverbruik-team-a",
                    "type": "project",
                    "valuestream": "grootverbruik"
                },
                "name": "grootverbruik-team-a-tst",
                "resourceVersion": "45473378",
                "selfLink": "/apis/project.openshift.io/v1/projects/security-team-a-tst",
                "uid": "775020e4-81dd-11e9-a287-0050568ab8da"
            }
        },
        {
            "apiVersion": "project.openshift.io/v1",
            "kind": "Project",
            "metadata": {
                "labels": {
                    "app.kubernetes.io/instance": "generic-all-cluster",
                    "heritage": "argo",
                    "name": "grootverbruik-ops",
                    "ops.alliander.com/schedule-down": "false",
                    "project": "grootverbruik-team-b",
                    "type": "project",
                    "valuestream": "grootverbruik"
                },
                "name": "grootverbruik-team-b-tst",
                "resourceVersion": "45473378",
                "selfLink": "/apis/project.openshift.io/v1/projects/security-team-a-tst",
                "uid": "775020e4-81dd-11e9-a287-0050568ab8da"
            }
        }
    ]}


def otaps_with_multiple_valuestreams():
    return {"items": [
        {
            "apiVersion": "project.openshift.io/v1",
            "kind": "Project",
            "metadata": {
                "labels": {
                    "app.kubernetes.io/instance": "generic-all-cluster",
                    "heritage": "argo",
                    "name": "grootverbruik-ops",
                    "ops.alliander.com/schedule-down": "false",
                    "project": "grootverbruik-team-a",
                    "type": "project",
                    "valuestream": "grootverbruik"
                },
                "name": "grootverbruik-team-a-ops",
            }
        },
        {
            "apiVersion": "project.openshift.io/v1",
            "kind": "Project",
            "metadata": {
                "labels": {
                    "app.kubernetes.io/instance": "generic-all-cluster",
                    "heritage": "argo",
                    "name": "security-ops",
                    "ops.alliander.com/schedule-down": "false",
                    "project": "security-team-a",
                    "type": "project",
                    "valuestream": "security"
                },
                "name": "security-team-a-ops",
            }
        }
    ]}


def pipelines_empty_response():
    return {}


def pipelines_per_namespace():
    return {"certificate-mgmt": ["x509-api", "x509-web"],
            "default": ["squid-proxy"],
            "demo-ops": ["openshift-cicdservice-api",
                         "openshift-cicdservice-api-feature-fza-3395",
                         "openshift-cicdservice-api-master-pipeline",
                         "openshift-example",
                         "openshift-example-pipeline"],
            "dgn-sandbox-ops": ["kit", "kit-pipeline"],
            "dockerfile-template": ["dockerfile-template"],
            "egress-test": ["sjtest"],
            "grootverbruik-team-a-ops": ["postcode-location",
                                         "postcode-location-pipeline",
                                         "postcode-location-pipeline-nexus",
                                         "postcode-location-pipeline-test2"],
            "grootverbruik-team-b-ops": ["crud-example",
                                         "crud-example-pipeline",
                                         "postcode-location-pipeline"],
            "gtslink": ["gtslink"],
            "guido-donderdag-sessie": ["jenkins-with-forza-workflow",
                                       "openshift-jenkins-agent-python",
                                       "postcode-location-master-pipeline"],
            "haproxy-tooling-persistent": ["haproxy-api",
                                           "haproxy-tls-gui"],
            "haproxy-tooling": ["haproxy-tls-gui"],
            "jonastest": ["jonastestwebsite"],
            "kkc-it-dev": ["kkc-it-build"],
            "kkc-it-tst": ["kkc-it-build"],
            "koen-ops": ["jenkins-forza",
                         "postcode-location",
                         "postcode-location-pipeline"],
            "koen": ["crud-example",
                     "digital-twin-test",
                     "diva-backend",
                     "docker-openshift-client",
                     "hello-world-spring-rest",
                     "hello-world-spring-rest-pipeline",
                     "jenkins-with-forza-workflow",
                     "postcode-location",
                     "postcode-location-pipeline",
                     "simple-session-app",
                     "simple-session-app-bc",
                     "spring-base",
                     "test-workflow-libs"],
            "marcelj-test": ["nginx-example"],
            "openshift-jenkins": ["jenkins-forza",
                                  "nist-data-mirror",
                                  "openshift-jenkins-agent-general",
                                  "openshift-jenkins-agent-python",
                                  "sonarqube"],
            "ot-abr-ops": ["bar-webservice",
                           "bar-webservice-pipeline",
                           "python-webservice-pipeline-template",
                           "python-webservice-pipeline-template-pipeline"],
            "playground": ["alpine",
                           "dotnet",
                           "logstash",
                           "toonfrequent"],
            "python-webservice": ["python-webservice"],
            "testweb": ["httpd-example",
                        "testweb"]}


def buildconfigs():
    return {
        "apiVersion": "v1",
        "items": [
            {
                "apiVersion": "build.openshift.io/v1",
                "kind": "BuildConfig",
                "metadata": {
                    "labels": {
                        "app": "postcode-location"
                    },
                    "name": "postcode-location",
                    "namespace": "grootverbruik-team-a-ops",
                },
                "spec": {
                    "failedBuildsHistoryLimit": 5,
                    "nodeSelector": "",
                    "output": {
                        "to": {
                            "kind": "ImageStreamTag",
                            "name": "postcode-location:master"
                        }
                    },
                    "postCommit": {},
                    "resources": {
                        "limits": {
                            "cpu": "1",
                            "memory": "4Gi"
                        },
                        "requests": {
                            "cpu": "100m",
                            "memory": "512Mi"
                        }
                    },
                    "runPolicy": "Serial",
                    "source": {
                        "git": {
                            "ref": "ssh-test",
                            "uri": "git@github.com:Alliander/postcode-location.git"
                        },
                        "sourceSecret": {
                            "name": "ssh-test"
                        },
                        "type": "Git"
                    },
                    "strategy": {
                        "dockerStrategy": {
                            "dockerfilePath": "Dockerfile"
                        },
                        "type": "Docker"
                    },
                    "successfulBuildsHistoryLimit": 5,
                    "triggers": []
                },
                "status": {
                    "lastVersion": 59
                }
            },
            {
                "apiVersion": "build.openshift.io/v1",
                "kind": "BuildConfig",
                "metadata": {
                    "labels": {
                        "app": "postcode-location-pipeline"
                    },
                    "name": "postcode-location-pipeline",
                    "namespace": "grootverbruik-team-a-ops",
                },
                "spec": {
                    "failedBuildsHistoryLimit": 5,
                    "nodeSelector": {},
                    "output": {
                        "to": {
                            "kind": "ImageStreamTag",
                            "name": "postcode-location:latest"
                        }
                    },
                    "postCommit": {},
                    "resources": {},
                    "runPolicy": "Serial",
                    "source": {
                        "git": {
                            "ref": "master",
                            "uri": "git@github.com:Alliander/postcode-location.git"
                        },
                        "sourceSecret": {
                            "name": "ssh-test"
                        },
                        "type": "Git"
                    },
                    "successfulBuildsHistoryLimit": 5,
                    "triggers": []
                },
                "status": {
                    "lastVersion": 101
                }
            },
            {
                "apiVersion": "build.openshift.io/v1",
                "kind": "BuildConfig",
                "metadata": {
                    "labels": {
                        "app": "postcode-location-pipeline-nexus"
                    },
                    "name": "postcode-location-pipeline-nexus",
                    "namespace": "grootverbruik-team-a-ops",
                },
                "spec": {
                    "failedBuildsHistoryLimit": 5,
                    "nodeSelector": {},
                    "output": {
                        "to": {
                            "kind": "ImageStreamTag",
                            "name": "postcode-location-test2:latest"
                        }
                    },
                    "postCommit": {},
                    "resources": {},
                    "runPolicy": "Serial",
                    "source": {
                        "git": {
                            "ref": "nexus",
                            "uri": "https://github.com/Alliander/postcode-location.git"
                        },
                        "sourceSecret": {
                            "name": "argo-cd-github"
                        },
                        "type": "Git"
                    },
                    "successfulBuildsHistoryLimit": 5,
                    "triggers": []
                },
                "status": {
                    "lastVersion": 92
                }
            },
            {
                "apiVersion": "build.openshift.io/v1",
                "kind": "BuildConfig",
                "metadata": {
                    "labels": {
                        "app": "postcode-location-pipeline-test2"
                    },
                    "name": "postcode-location-pipeline-test2",
                    "namespace": "grootverbruik-team-a-ops",
                },
                "spec": {
                    "failedBuildsHistoryLimit": 5,
                    "nodeSelector": {},
                    "output": {
                        "to": {
                            "kind": "ImageStreamTag",
                            "name": "postcode-location-test2:latest"
                        }
                    },
                    "postCommit": {},
                    "resources": {},
                    "runPolicy": "Serial",
                    "source": {
                        "git": {
                            "ref": "test2",
                            "uri": "https://github.com/Alliander/postcode-location.git"
                        },
                        "sourceSecret": {
                            "name": "argo-cd-github"
                        },
                        "type": "Git"
                    },
                    "successfulBuildsHistoryLimit": 5,
                    "triggers": []
                },
                "status": {
                    "lastVersion": 17
                }
            }
        ],
        "kind": "List",
        "metadata": {
            "resourceVersion": "",
            "selfLink": ""
        }
    }
