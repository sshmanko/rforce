import pytest
from rforce import parse


def test_nodata():
    key = 'windows'
    data = {}
    assert parse(key, data) == []


def test_single_ok():
    key = 'windows'
    data = {
        "windows": {
            "name": "machine1",
            "location": "westeurope",
            "type": "windows",
            "storageProfile": {
                "osDisk": {
                    "managedDisk": {
                        "id": "f3779e61-9bc8-4d7c-a659-2dd91a8a6167"
                    }
                }
            }
        }
    }
    assert parse(key, data) == ['f3779e61-9bc8-4d7c-a659-2dd91a8a6167']


def test_list_ok():
    key = 'splunk'
    data = [
        {
            "windows": {
                "name": "machine1",
                "location": "westeurope",
                "type": "windows",
                "storageProfile": {
                    "osDisk": {
                    }
                }
            }
        },
        {
            "linux": {
                "name": "machine2",
                "location": "eastus",
                "type": "solaris",
                "storageProfile": {
                    "osDisk": {
                        "managedDisk": {
                            "id": "d352cb25-da51-4389-a7a9-44467454b07e"
                        }
                    }
                }
            }
        },
        {
            "splunk": {
                "name": "machine3",
                "location": "francecentral",
                "type": "linux",
                "storageProfile": {
                    "osDisk": {
                        "managedDisk": {
                            "id": "05470de3-393a-46b0-8f03-e323d2269e5e"
                        }
                    }
                }
            }
        },
        {
            "splunk": {
                "name": "machine7",
                "location": "francecentral",
                "type": "linux",
                "storageProfile": {
                    "osDisk": {
                        "managedDisk": {
                            "id": "05470de3-393a-46b0-8f03-e323d2269e5f"
                        }
                    }
                }
            }
        }
    ]
    assert parse(key, data) == ['05470de3-393a-46b0-8f03-e323d2269e5e', '05470de3-393a-46b0-8f03-e323d2269e5f']
