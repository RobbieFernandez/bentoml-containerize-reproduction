from bentoml.io import Text
import bentoml

svc = bentoml.Service(name="test", runners=[])


@svc.api(input=Text(), output=Text())
def inference(input_txt):
    return "Hello"
