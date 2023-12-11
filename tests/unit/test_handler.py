import json
import pytest

from ParameterStoreGetValue import app


@pytest.fixture()
def fixture_event():
    return {"Name": "/sam/vpcProd"}

class TestParameterStoreGetValue:
    def test_get_parameter_value(self, fixture_event):
        assert app.get_parameter_value(fixture_event) == "vpc-0d6712c4bd670aca6"

